"""
Tia Clara v2 — três paletas em verde-sálvia médio (opções para a Clara escolher).

Mede cada paleta contra o brief v2 e gera a prancha de comparação:
  - o sálvia (cor principal) precisa estar na faixa "médio": saturação 12–30 %, luminosidade 50–65 % (HSL);
  - o verde de texto precisa ser legível sem virar quase preto: luminosidade HSL >= 25 % (o pinho da v1 tem ~17 %);
  - todo par de texto previsto passa no WCAG AA (4,5:1; 3:1 só onde o uso é texto grande).

    python3 tia-clara/_fonte/v2_paletas.py

Sai com código 1 se alguma regra falhar. Saída em 12-identidade-v2/02-paletas/ (paletas.json + paletas.html);
renderize o HTML com _fonte/render.js.
"""
import colorsys, json, os, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
SAIDA = os.path.join(RAIZ, '12-identidade-v2', '02-paletas')

# Papéis iguais nas três paletas; muda a temperatura do sálvia.
PALETAS = [
    {'id': 1, 'nome': 'Sálvia da serra', 'ideia': 'O verde da Mata Atlântica depois da chuva: neutro, calmo, o mais versátil.',
     'cores': {'salvia': '#86A38A', 'salvia_claro': '#DDE7DB', 'texto': '#37543F', 'fundo': '#F7F3EA',
               'superficie': '#FFFDF8', 'sol': '#E9A13B', 'mar': '#7FA7A8'}},
    {'id': 2, 'nome': 'Sálvia oliva', 'ideia': 'Puxado para o amarelo: mais quente e mais "casa", combina com areia.',
     'cores': {'salvia': '#9AAB82', 'salvia_claro': '#E5EAD7', 'texto': '#45552F', 'fundo': '#F8F2E6',
               'superficie': '#FFFCF5', 'sol': '#E58B3A', 'mar': '#8FAEA2'}},
    {'id': 3, 'nome': 'Sálvia do mar', 'ideia': 'Puxado para o azul: fresco, litorâneo, o mais "Ubatuba".',
     'cores': {'salvia': '#7FA59C', 'salvia_claro': '#D9E8E3', 'texto': '#2E5550', 'fundo': '#F6F3EC',
               'superficie': '#FFFFFB', 'sol': '#EFAE45', 'mar': '#5F9AA8'}},
]

NOMES = {'salvia': 'Sálvia (principal)', 'salvia_claro': 'Sálvia claro', 'texto': 'Verde de texto',
         'fundo': 'Fundo creme', 'superficie': 'Superfície', 'sol': 'Sol (acento)', 'mar': 'Mar (apoio)'}

# (primeiro plano, fundo, mínimo, uso)
PARES = [
    ('texto', 'fundo', 4.5, 'texto corrido'),
    ('texto', 'superficie', 4.5, 'texto em cartões'),
    ('texto', 'salvia_claro', 4.5, 'texto em blocos de apoio'),
    ('fundo', 'texto', 4.5, 'botão e faixa: creme sobre verde de texto'),
    ('texto', 'salvia', 3.0, 'só título grande sobre sálvia'),
]
# O sol é acento gráfico (o sol da logo, um ponto, um sublinhado): nunca fica atrás de texto.
# Verde de texto sobre sol dá 3,1–4,3:1 nas três paletas, abaixo do AA para texto comum.


def hsl(hexa):
    r, g, b = (int(hexa[i:i + 2], 16) / 255 for i in (1, 3, 5))
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return round(h * 360), round(s * 100, 1), round(l * 100, 1)


def luminancia(hexa):
    def canal(v):
        v = int(v, 16) / 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (canal(hexa[i:i + 2]) for i in (1, 3, 5))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a, b):
    la, lb = sorted((luminancia(a), luminancia(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def avaliar(p):
    c, erros, pares = p['cores'], [], []
    _, s, l = hsl(c['salvia'])
    if not (12 <= s <= 30 and 50 <= l <= 65):
        erros.append(f"sálvia {c['salvia']} fora da faixa médio (S {s} %, L {l} %)")
    _, _, lt = hsl(c['texto'])
    if lt < 25:
        erros.append(f"verde de texto {c['texto']} escuro demais (L {lt} % < 25 %)")
    for fg, bg, minimo, uso in PARES:
        r = contraste(c[fg], c[bg])
        pares.append({'frente': fg, 'fundo': bg, 'razao': round(r, 2), 'minimo': minimo, 'uso': uso, 'ok': r >= minimo})
        if r < minimo:
            erros.append(f'{fg} sobre {bg}: {r:.2f}:1 < {minimo}:1 ({uso})')
    return {'sálvia_hsl': hsl(c['salvia']), 'texto_hsl': hsl(c['texto']), 'pares': pares, 'erros': erros}


def fmt_razao(v):
    return f'{v:.1f}'.replace('.', ',')


def prancha(resultados):
    fontes = '../fontes/'
    blocos = []
    for p, r in resultados:
        c = p['cores']
        amostras = ''.join(
            f'<div class="am"><div class="sw" style="background:{c[k]}"></div>'
            f'<div class="rot">{NOMES[k]}</div><div class="hex">{c[k]}</div></div>' for k in NOMES)
        pares = ''.join(
            f'<tr><td><span class="par" style="background:{c[x["fundo"]]};color:{c[x["frente"]]}">Aa</span></td>'
            f'<td>{x["uso"]}</td><td class="n">{fmt_razao(x["razao"])}:1 {"✓" if x["ok"] else "✗"}</td></tr>' for x in r['pares'])
        blocos.append(f'''
<section class="p">
  <div class="cab"><span class="num">{p["id"]}</span><div><h2>{p["nome"]}</h2><p>{p["ideia"]}</p></div></div>
  <div class="amostras">{amostras}</div>
  <div class="prop" title="proporção de uso">
    <span style="flex:55;background:{c["fundo"]}">creme 55</span><span style="flex:25;background:{c["salvia"]}">sálvia 25</span>
    <span style="flex:10;background:{c["salvia_claro"]}">10</span><span style="flex:7;background:{c["texto"]};color:{c["fundo"]}">7</span>
    <span style="flex:3;background:{c["sol"]}"></span></div>
  <div class="mini" style="background:{c["fundo"]};color:{c["texto"]}">
    <div class="topo" style="background:{c["salvia"]}">
      <div class="sol" style="background:{c["sol"]}"></div>
      <div class="nome">Tia Clara</div>
      <div class="desc">Pet sitter &amp; dog walker · Ubatuba</div>
    </div>
    <div class="cartao" style="background:{c["superficie"]}">
      <div class="lin"><b>08:02</b> Entrada</div><div class="lin"><b>08:12</b> Passeio · 40 min</div>
      <div class="fecho">Tudo certo por aqui.</div>
    </div>
    <div class="bt" style="background:{c["texto"]};color:{c["fundo"]}">Agendar visita</div>
  </div>
  <table>{pares}</table>
  <div class="medida">Sálvia: saturação {fmt_razao(r["sálvia_hsl"][1])} %, luminosidade {fmt_razao(r["sálvia_hsl"][2])} % ·
    verde de texto: luminosidade {fmt_razao(r["texto_hsl"][2])} % (v1: 17 %)</div>
</section>''')
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<style>
@font-face{{font-family:Fig;src:url("{fontes}Figtree[wght].ttf");font-weight:300 900}}
@font-face{{font-family:Nor;src:url("{fontes}Norican-Regular.ttf")}}
*{{box-sizing:border-box;margin:0}}
body{{width:1600px;background:#FBF9F4;color:#2F3B33;font:16px/1.45 Fig;padding:48px 48px 56px}}
h1{{font:700 34px Fig;letter-spacing:-.01em}} .sub{{margin-top:6px;color:#5B665E;font-size:18px}}
.grade{{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:32px}}
.p{{background:#fff;border:1px solid #E6E2D8;border-radius:18px;padding:26px}}
.cab{{display:flex;gap:16px;align-items:flex-start}} .num{{font:800 40px/1 Fig;color:#9AA59C}}
h2{{font:700 24px Fig}} .cab p{{color:#5B665E;font-size:15px;margin-top:2px}}
.amostras{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:20px}}
.sw{{height:58px;border-radius:10px;border:1px solid #0000000f}} .rot{{font:600 12px Fig;margin-top:6px}} .hex{{font:500 12px Fig;color:#6B756D}}
.prop{{display:flex;height:26px;margin-top:18px;border-radius:8px;overflow:hidden;border:1px solid #0000000f;font:600 11px/26px Fig;color:#2F3B33}}
.prop span{{padding-left:8px;white-space:nowrap;overflow:hidden}}
.mini{{position:relative;margin-top:14px;border-radius:14px;padding:0 0 20px;overflow:hidden;min-height:250px}}
.topo{{position:relative;padding:24px 24px 22px}}
.mini .sol{{position:absolute;right:24px;top:22px;width:54px;height:54px;border-radius:50%}}
.mini .cartao,.mini .bt{{margin-left:24px;margin-right:24px}}
.nome{{font:44px/1.1 Nor}} .desc{{font:600 12px Fig;letter-spacing:.14em;text-transform:uppercase;margin-top:4px}}
.cartao{{margin-top:16px;border-radius:12px;padding:12px 14px;font-size:14px}} .lin{{padding:3px 0}} .lin b{{display:inline-block;width:48px;font-variant-numeric:tabular-nums}}
.fecho{{font:22px Nor;margin-top:4px}}
.bt{{display:inline-block;margin-top:14px;padding:10px 18px;border-radius:999px;font:700 14px Fig}}
table{{width:100%;border-collapse:collapse;margin-top:18px;font-size:13px}} td{{padding:5px 4px;border-top:1px solid #EEEAE1}}
.par{{display:inline-block;width:40px;text-align:center;border-radius:6px;padding:2px 0;font-weight:700}} .n{{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}}
.medida{{margin-top:12px;font-size:13px;color:#5B665E}}
</style></head><body>
<h1>Três paletas em verde-sálvia médio</h1>
<p class="sub">Mesmos papéis nas três; muda a temperatura do verde. Todas mais claras que a v1 e com contraste de leitura aprovado. O sol é só acento gráfico, nunca fundo de texto.</p>
<div class="grade">{"".join(blocos)}</div>
</body></html>'''


def gerar():
    os.makedirs(SAIDA, exist_ok=True)
    resultados, falhou = [], False
    for p in PALETAS:
        r = avaliar(p)
        resultados.append((p, r))
        print(f'Paleta {p["id"]} · {p["nome"]}: sálvia HSL {r["sálvia_hsl"]}, texto HSL {r["texto_hsl"]}')
        for x in r['pares']:
            print(f'   {x["frente"]:>12} sobre {x["fundo"]:<12} {x["razao"]:5.2f}:1 (mín {x["minimo"]}) {"ok" if x["ok"] else "FALHA"}')
        for e in r['erros']:
            print('   ERRO:', e)
        falhou |= bool(r['erros'])
    with open(os.path.join(SAIDA, 'paletas.json'), 'w', encoding='utf-8') as f:
        json.dump([dict(p, medidas=r) for p, r in resultados], f, ensure_ascii=False, indent=2)
    with open(os.path.join(SAIDA, 'paletas.html'), 'w', encoding='utf-8') as f:
        f.write(prancha(resultados))
    print('ok paletas.json, paletas.html')
    if falhou:
        sys.exit('Alguma paleta não passou nas regras do brief v2.')


if __name__ == '__main__':
    gerar()
