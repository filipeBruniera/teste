#!/usr/bin/env python3
"""Gera as fontes web (WOFF2, subconjunto) de 10-site/assets/fontes a partir das fontes de
origem (fonte da verdade) em 05-design-system/fontes. Não altera as origens.

O que faz, por arquivo:
  1. Restringe os eixos variáveis que o CSS do site não varia (fontTools.varLib.instancer),
     mantendo os que são realmente usados (peso onde há mais de um valor; `opsz` da Literata,
     que o navegador ajusta sozinho por tamanho via font-optical-sizing: auto).
  2. Recorta o glyph set para Latin básico + Latin-1 Supplement + a pontuação tipográfica
     usada/prevista na página, preservando os recursos OpenType relevantes (kern, liga, ccmp,
     locl, calt, mark, mkmk, rvrn + tnum/onum/lnum/pnum para os algarismos tabulares dos
     horários e números de protocolo).
  3. Compila direto em WOFF2 (usa o pacote `brotli`).

Requer: pip install fonttools brotli
Uso:    python3 tia-clara/_fonte/fontes-web.py
"""
import os
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools import subset as ftsubset

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEM = os.path.join(RAIZ, "05-design-system", "fontes")
DESTINO = os.path.join(RAIZ, "10-site", "assets", "fontes")

# Latin básico (0x20–0x7E) + Latin-1 Supplement inteiro (0x A0–0xFF: acentos do português,
# ©, º, ª, ·, «», × etc.) + pontuação tipográfica usada no texto (– — " " ' ') ou prevista
# para futuras edições de conteúdo (bullet, reticências) — todas conferidas contra o cmap
# das fontes de origem antes de entrar aqui.
UNICODES = (
    set(range(0x20, 0x7F))
    | set(range(0xA0, 0x100))
    | {
        0x2013,  # – en dash
        0x2014,  # — em dash (usado: "espaço reservado para um depoimento —")
        0x2018,  # ' aspas simples de abertura
        0x2019,  # ' aspas simples de fechamento
        0x201C,  # " aspas duplas de abertura (usado nos depoimentos)
        0x201D,  # " aspas duplas de fechamento (usado nos depoimentos)
        0x2022,  # • bullet (não usado hoje, mantido por robustez de conteúdo)
        0x2026,  # … reticências (não usado hoje, mantido por robustez de conteúdo)
    }
)

# Recursos OpenType além do conjunto padrão do pyftsubset (que já preserva kern, liga, ccmp,
# locl, calt, mark, mkmk, rvrn, clig, rclt, rlig, dnom, numr, frac): tnum é o que os horários
# (`.tc-dado`, `font-variant-numeric: tabular-nums`) e os números do protocolo
# (`.tc-protocolo__numero`, mesma propriedade, mas em Literata) realmente acionam; onum/lnum/
# pnum entram junto para não perder as variantes de algarismo se o navegador pedir outra.
FEATURES_EXTRA = ["tnum", "onum", "lnum", "pnum"]


def subconjunto(font: TTFont, flavor: str = "woff2") -> ftsubset.Options:
    options = ftsubset.Options()
    options.flavor = flavor
    options.layout_features = list(set(options.layout_features) | set(FEATURES_EXTRA))
    options.name_IDs = [0, 1, 2, 3, 4, 5, 6]  # copyright, família, subfamília, id, nome completo, versão, postscript
    options.name_legacy = False
    options.recalc_bounds = True
    options.recalc_timestamp = False
    options.canonical_order = True
    subsetter = ftsubset.Subsetter(options=options)
    subsetter.populate(unicodes=UNICODES)
    subsetter.subset(font)
    return options


def gerar(nome_origem: str, nome_destino: str, limites_eixo: dict | None):
    caminho_in = os.path.join(ORIGEM, nome_origem)
    caminho_out = os.path.join(DESTINO, nome_destino)
    font = TTFont(caminho_in)

    if limites_eixo:
        font = instancer.instantiateVariableFont(
            font, limites_eixo, inplace=True, updateFontNames=True
        )
        # O passo de otimização do instancer pode remover do gvar a entrada de glifos cuja
        # variação ficou vazia dentro do novo intervalo do eixo (ex.: hífen mole, uni00AD) —
        # sem recriar a entrada (mesmo vazia), o subsetter quebra ao tentar reindexá-la a
        # seguir. Repõe uma lista vazia para todo glifo que ficou sem entrada.
        if "gvar" in font:
            gvar = font["gvar"]
            variacoes = dict(gvar.variations)
            for nome_glifo in font.getGlyphOrder():
                variacoes.setdefault(nome_glifo, [])
            gvar.variations = variacoes

    options = subconjunto(font)
    ftsubset.save_font(font, caminho_out, options)

    antes = os.path.getsize(caminho_in)
    depois = os.path.getsize(caminho_out)
    print(f"{nome_origem} -> {nome_destino}: {antes/1024:8.1f} KB -> {depois/1024:6.1f} KB")


def main():
    os.makedirs(DESTINO, exist_ok=True)

    # Literata normal: usada em 400 (corpo de depoimento) e 600 (títulos, display) — o CSS
    # nunca pede outro peso, então o eixo `wght` fica restrito a 400–600 (continua variável).
    # `opsz` fica intocado (7–72): o navegador aplica automaticamente por tamanho renderizado
    # (font-optical-sizing: auto, o padrão do CSS), do afeto pequeno (~19px) ao display (~56px).
    gerar(
        "Literata[opsz,wght].ttf",
        "Literata[opsz,wght].woff2",
        {"wght": (400, 600)},
    )

    # Literata itálico: o CSS só usa itálico em --tc-afeto, sempre no peso 400 — o eixo `wght`
    # é fixado (não varia mais no arquivo), `opsz` continua variável pelo mesmo motivo acima.
    gerar(
        "Literata-Italic[opsz,wght].ttf",
        "Literata-Italic[opsz].woff2",
        {"wght": 400},
    )

    # Instrument Sans normal: usada em 400/500/600/700 (corpo, dado, rótulo, botão, números do
    # passo) — o eixo `wght` fica como está (400–700, todo ele usado). `wdth` nunca é acionado
    # pelo CSS (sem font-stretch nem font-variation-settings com 'wdth'), então é fixado em 100
    # (largura normal, o valor padrão) para não carregar interpolação de largura que não serve.
    gerar(
        "InstrumentSans[wdth,wght].ttf",
        "InstrumentSans[wght].woff2",
        {"wdth": 100},
    )

    # Instrument Sans itálico: nenhum elemento do site pede itálico nesta família (o único
    # itálico do site é a voz, Literata) — arquivo não é gerado. Ver README para o motivo.
    print("InstrumentSans-Italic[wdth,wght].ttf: não gerado (itálico da Instrument Sans não é usado no site)")


if __name__ == "__main__":
    main()
