"""
Tia Clara v2 — pranchas para a Clara escolher a direção (marco 1), no formato do WhatsApp (1080 x 1350).

  1-paletas.html            "Qual verde?"                      (paletas de 02-paletas/paletas.json)
  2-rotas.html              "Qual caminho de logo?"            (SVGs de 03-rotas/)
  3-aplicacoes-rota-X.html  cada rota no perfil do Instagram, no WhatsApp, no relatório e no site

Regras de produção da v1 mantidas (07-producao/producao.md): nada abaixo de 28 px em 1080 de largura.

    python3 tia-clara/_fonte/v2_paletas.py && python3 tia-clara/_fonte/v2_rotas.py
    python3 tia-clara/_fonte/v2_apresentacao.py
    NODE_PATH=$(npm root -g) node tia-clara/_fonte/v2_renderizar.js
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2_rotas import PALETAS, PALETA_DA_ROTA

AQUI = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.join(os.path.dirname(AQUI), '12-identidade-v2')
SAIDA = os.path.join(V2, '04-apresentacao')
PALETAS_INFO = {p['id']: p for p in json.load(open(os.path.join(V2, '02-paletas', 'paletas.json'), encoding='utf-8'))}

DESCRITOR = 'Auxiliar de veterinário · Pet sitter &amp; dog walker'
CREDENCIAL = 'Experiência em cuidados de enfermagem veterinária (auxiliar de veterinário)'
FRASE = 'Mais qualidade de tempo para quem mais importa.'
ROTAS = {
    'a': ('Com eles', 'Você de costas com o cão e o gato, olhando a serra e o mar.'),
    'b': ('Assinatura', 'Seu nome escrito à mão: o pingo do "i" é o sol, a onda é o mar.'),
    'c': ('As ilhas', 'No horizonte de Ubatuba, as ilhas são um gato e um cão. O sol nasce entre eles.'),
}
RODAPE = 'Proposta de direção · ainda não é a versão final'

BASE_CSS = '''
@font-face{font-family:Fig;src:url("../fontes/Figtree[wght].ttf");font-weight:300 900}
@font-face{font-family:Nor;src:url("../fontes/Norican-Regular.ttf")}
@font-face{font-family:Cou;src:url("../fontes/Courgette-Regular.ttf")}
*{box-sizing:border-box;margin:0}
body{width:1080px;height:1350px;overflow:hidden;background:#FBF9F4;color:#2F3B33;font:28px/1.35 Fig;padding:72px 72px 0;position:relative}
h1{font:800 60px/1.05 Fig;letter-spacing:-.015em} .sub{font-size:32px;color:#56615A;margin-top:12px}
.rod{position:absolute;left:72px;right:72px;bottom:36px;font-size:28px;color:#6B756D;display:flex;justify-content:space-between}
.letra{font:800 64px/1 Fig;color:#9AA59C;width:64px;flex:none}
'''


def pagina(titulo, corpo, css=''):
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{titulo}</title>'
            f'<style>{BASE_CSS}{css}</style></head><body>{corpo}</body></html>')


def prancha_paletas():
    linhas = []
    for pid in (1, 2, 3):
        p = PALETAS_INFO[pid]; c = p['cores']
        sw = ''.join(f'<span style="background:{c[k]}"></span>' for k in ('salvia', 'salvia_claro', 'fundo', 'texto', 'sol', 'mar'))
        linhas.append(f'''<div class="pl">
  <div class="letra">{pid}</div>
  <div class="info"><h2>{p["nome"]}</h2><p>{p["ideia"]}</p>
    <div class="sw">{sw}</div>
    <div class="prop"><span style="flex:55;background:{c["fundo"]}"></span><span style="flex:25;background:{c["salvia"]}"></span><span style="flex:10;background:{c["salvia_claro"]}"></span><span style="flex:7;background:{c["texto"]}"></span><span style="flex:3;background:{c["sol"]}"></span></div>
  </div>
  <div class="amostra" style="background:{c["salvia"]};color:{c["texto"]}"><i style="background:{c["sol"]}"></i><b>Tia Clara</b></div>
</div>''')
    css = '''.pl{display:flex;gap:28px;align-items:center;margin-top:44px;padding-top:40px;border-top:2px solid #E6E2D8}
.pl:first-of-type{margin-top:48px}
.info{flex:1} h2{font:800 40px Fig} .info p{color:#56615A;margin-top:4px}
.sw{display:flex;gap:10px;margin-top:18px} .sw span{width:62px;height:62px;border-radius:50%;border:2px solid #0000000d}
.prop{display:flex;height:22px;border-radius:11px;overflow:hidden;margin-top:16px;border:2px solid #0000000d}
.amostra{position:relative;width:210px;height:210px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none}
.amostra i{position:absolute;right:26px;top:26px;width:44px;height:44px;border-radius:50%}
.amostra b{font:400 50px Nor}'''
    corpo = (f'<h1>Qual verde?</h1><p class="sub">Todas mais claras que a versão anterior. Escolha 1, 2 ou 3.</p>'
             f'{"".join(linhas)}<div class="rod"><span>{RODAPE}</span><span>1/5</span></div>')
    return pagina('Qual verde?', corpo, css)


def prancha_rotas():
    linhas = []
    for r in 'abc':
        nome, ideia = ROTAS[r]
        linhas.append(f'''<div class="rt">
  <div class="letra">{r.upper()}</div>
  <div class="img"><img src="../03-rotas/rota-{r}/tc-{r}-assinatura.svg"></div>
  <div class="info"><h2>{nome}</h2><p>{ideia}</p>
    <div class="av"><img src="../03-rotas/rota-{r}/tc-{r}-reduzida.svg"><span>no WhatsApp</span></div></div>
</div>''')
    css = '''.rt{display:flex;gap:28px;align-items:center;margin-top:20px;padding-top:20px;border-top:2px solid #E6E2D8;height:276px}
.rt:first-of-type{margin-top:36px}
.img{width:330px;height:256px;display:flex;align-items:center;justify-content:center;flex:none;background:#fff;border-radius:22px;border:2px solid #EEEAE1;padding:14px}
.img img{max-width:100%;max-height:100%}
.info{flex:1} h2{font:800 40px Fig} .info p{color:#56615A;margin-top:4px}
.av{display:flex;align-items:center;gap:14px;margin-top:16px;color:#6B756D} .av img{width:64px;height:64px;border-radius:50%}
.pend{margin-top:22px;font-size:28px;color:#56615A;background:#F1EEE6;border-radius:16px;padding:16px 22px}'''
    corpo = (f'<h1>Qual caminho de logo?</h1><p class="sub">Escolha A, B ou C. Qualquer um funciona com qualquer verde.</p>'
             f'{"".join(linhas)}'
             f'<p class="pend">Antes de fechar, vamos comparar com a logo da sua colega para garantir que fique diferente.</p>'
             f'<div class="rod"><span>{RODAPE}</span><span>2/5</span></div>')
    return pagina('Qual caminho de logo?', corpo, css)


def prancha_aplicacoes(r, n):
    nome, _ = ROTAS[r]
    pid = PALETA_DA_ROTA[r]; p = PALETAS_INFO[pid]; c = p['cores']
    red = f'../03-rotas/rota-{r}/tc-{r}-reduzida.svg'
    fonte_nome = {'a': '800 34px Fig', 'b': '400 40px Nor', 'c': '400 36px Cou'}[r]
    css = f'''body{{background:{c["fundo"]};color:{c["texto"]}}}
.sub{{color:{c["texto"]};opacity:.85}}
.bloco{{background:{c["superficie"]};border-radius:24px;padding:18px 26px;margin-top:16px;border:2px solid {c["salvia_claro"]}}}
.rotulo{{font:700 28px Fig;letter-spacing:.06em;text-transform:uppercase;color:{c["texto"]};opacity:.75;margin-bottom:10px}}
.ig{{display:flex;gap:24px;align-items:center}} .ig img{{width:116px;height:116px;border-radius:50%;flex:none}}
.ig .n{{font:{fonte_nome}}} .ig .bio{{font-size:28px;line-height:1.3;margin-top:4px}}
.wa{{display:flex;gap:20px;align-items:center;margin-top:10px;padding-top:10px;border-top:2px solid {c["salvia_claro"]}}}
.wa img{{width:56px;height:56px;border-radius:50%}} .wa b{{font:700 30px Fig}} .wa span{{display:block;color:{c["texto"]};opacity:.8}}
.rel{{display:grid;grid-template-columns:auto 1fr;gap:10px 24px;align-items:center}}
.rel .lg{{width:80px;height:80px;border-radius:50%;grid-row:span 2}} .rel .t{{font:800 32px Fig}} .rel .m{{opacity:.85}}
.lin{{display:flex;gap:22px;padding:4px 0;border-top:2px solid {c["salvia_claro"]};font-variant-numeric:tabular-nums}} .lin b{{width:90px}}
.site{{background:{c["salvia"]};border-radius:24px;margin-top:16px;overflow:hidden}}
.barra{{display:flex;align-items:center;gap:14px;background:{c["superficie"]};padding:10px 26px}} .barra img{{width:52px;height:52px;border-radius:50%}}
.barra b{{font:{fonte_nome};font-size:30px}}
.dobra{{padding:18px 26px 22px;color:{c["texto"]}}} .dobra h3{{font:800 36px/1.1 Fig;max-width:820px}}
.dobra p{{margin-top:8px;max-width:860px}} .bt{{display:inline-block;margin-top:12px;background:{c["texto"]};color:{c["fundo"]};font:800 30px Fig;padding:10px 28px;border-radius:999px}}'''
    corpo = f'''<h1>Rota {r.upper()} · {nome}</h1><p class="sub">Na paleta {pid} · {p["nome"]}</p>
<div class="bloco"><div class="rotulo">Instagram e WhatsApp</div>
  <div class="ig"><img src="{red}"><div><div class="n">Tia Clara</div>
    <div class="bio">{DESCRITOR}<br>Ubatuba · região central<br>{FRASE}</div></div></div>
  <div class="wa"><img src="{red}"><div><b>Tia Clara</b><span>Relatório de visita · Thor</span></div></div>
</div>
<div class="bloco"><div class="rotulo">Relatório de visita</div>
  <div class="rel"><img class="lg" src="{red}"><div class="t">Thor · sábado, 14 set</div><div class="m">exemplo ilustrativo</div></div>
  <div style="margin-top:8px"><div class="lin"><b>08:02</b>Entrada</div><div class="lin"><b>08:12</b>Passeio · 40 min</div></div>
</div>
<div class="site"><div class="barra"><img src="{red}"><b>Tia Clara</b></div>
  <div class="dobra"><h3>{FRASE}</h3><p>{CREDENCIAL}.</p><span class="bt">Agendar visita</span></div></div>
<div class="rod"><span>{RODAPE}</span><span>{n}/5</span></div>'''
    return pagina(f'Rota {r.upper()} aplicada', corpo, css)


def gerar():
    os.makedirs(SAIDA, exist_ok=True)
    lista = []

    def salva(nome, html):
        with open(os.path.join(SAIDA, nome + '.html'), 'w', encoding='utf-8') as fh:
            fh.write(html)
        lista.append([nome, 1080, 1350])
        print('ok', nome)

    salva('1-paletas', prancha_paletas())
    salva('2-rotas', prancha_rotas())
    for i, r in enumerate('abc'):
        salva(f'3-aplicacoes-rota-{r}', prancha_aplicacoes(r, 3 + i))
    with open(os.path.join(SAIDA, 'lista.json'), 'w', encoding='utf-8') as fh:
        json.dump(lista, fh)


if __name__ == '__main__':
    gerar()
