"""
Tia Clara v2 — rotas de logo para a Clara escolher (marco 1). Não é a logo final.

Três lógicas diferentes, cada uma com símbolo, assinatura, versão reduzida (avatar) e versão em 1 cor:
  A · Com eles   — o selo da referência: a Clara de costas com o cão e o gato, diante da serra e do mar.
  B · Assinatura — "Tia Clara" em cursiva (Norican); o pingo do i é o sol, uma onda sublinha o nome.
  C · As ilhas   — no horizonte de Ubatuba, as ilhas são a cabeça de um gato e a de um cão; o sol nasce entre elas.

Mesmo método da v1 (marca.py): todo texto vira curva, nenhum SVG depende de fonte instalada.
Cores lidas de 12-identidade-v2/02-paletas/paletas.json (rode v2_paletas.py antes).

    python3 tia-clara/_fonte/v2_rotas.py
"""
import json, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import marca as mc

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
V2 = os.path.join(RAIZ, '12-identidade-v2')
FONTES = os.path.join(V2, 'fontes')
SAIDA = os.path.join(V2, '03-rotas')
NORICAN = os.path.join(FONTES, 'Norican-Regular.ttf')
COURGETTE = os.path.join(FONTES, 'Courgette-Regular.ttf')
FIGTREE = os.path.join(FONTES, 'Figtree[wght].ttf')

PALETAS = {p['id']: p['cores'] for p in json.load(open(os.path.join(V2, '02-paletas', 'paletas.json'), encoding='utf-8'))}
# Cada rota é mostrada na paleta que mais combina com ela; qualquer rota funciona com qualquer paleta.
PALETA_DA_ROTA = {'a': 1, 'b': 2, 'c': 3}
f = mc.fmt


# ---------------------------------------------------------------- utilidades
def texto(path, s, tam, x, base, cor, axes=(), tracking=0, anchor='start'):
    gl, larg = mc.glifos(path, s, tam, 0, base, axes, tracking)
    x0 = x - larg if anchor == 'end' else x - larg / 2 if anchor == 'middle' else x
    gl, _ = mc.glifos(path, s, tam, x0, base, axes, tracking)
    return f'<path fill="{cor}" d="{mc.d_de(gl)}"/>', mc.bbox_de(gl), gl


def descritor(cx, base, cor, tam=13, linhas=('PET SITTER & DOG WALKER', 'UBATUBA')):
    partes, bbs = [], []
    for i, l in enumerate(linhas):
        p, bb, _ = texto(FIGTREE, l, tam, cx, base + i * tam * 1.75, cor, (('wght', 600),), 160, 'middle')
        partes.append(p); bbs.append(bb)
    return ''.join(partes), (min(b[0] for b in bbs), min(b[1] for b in bbs), max(b[2] for b in bbs), max(b[3] for b in bbs))


def onda(x0, x1, y, amp, periodos):
    """Onda suave (curvas quadráticas) de x0 a x1 em torno de y."""
    n = max(2, round(periodos * 2)); passo = (x1 - x0) / n
    d = f'M{f(x0)} {f(y)}'
    for i in range(n):
        sinal = -1 if i % 2 == 0 else 1
        d += f' Q{f(x0 + passo * (i + .5))} {f(y + sinal * amp * 2)} {f(x0 + passo * (i + 1))} {f(y)}'
    return d


def uniao(*bbs):
    return min(b[0] for b in bbs), min(b[1] for b in bbs), max(b[2] for b in bbs), max(b[3] for b in bbs)


# ---------------------------------------------------------------- ROTA A · Com eles
# Selo de 200 x 200: céu, sol, serra, mar, areia; a Clara de costas entre o cão e o gato.
CLARA = ('<circle cx="104" cy="86" r="6"/><circle cx="104" cy="100" r="12"/>'
         '<path d="M98 111C96 115 89 117 85 120C79 124 78 134 79 144C80 154 74 162 70 170L138 170'
         'C134 162 128 154 129 144C130 134 129 124 123 120C119 117 112 115 110 111Z"/>')
# cão sentado de perfil, olhando para a Clara: cabeça, focinho, orelha caída, corpo e rabo
CAO_COSTAS = ('<circle cx="52" cy="120" r="10"/>'
              '<path d="M54 114L67 116C72 117 73 124 68 126L54 128Z"/>'
              '<path d="M46 111C40 112 38 123 41 130C43 134 48 131 48 125Z"/>'
              '<path d="M33 170C31 153 35 139 45 130L58 129C62 139 63 155 63 170Z"/>')
CAUDA_CAO = 'M34 167C25 167 23 158 27 152'
GATO_COSTAS = ('<circle cx="154" cy="134" r="8"/><path d="M147 131L148 119L154.5 127Z"/><path d="M161 131L160 119L153.5 127Z"/>'
               '<path d="M148 140C142 148 141 160 141 170L167 170C167 160 166 148 160 140Z"/>')
CAUDA_GATO = 'M166 168C174 168 177 160 172 154'


def simbolo_a(c, uma_cor=None, anel=True):
    k = uma_cor
    if k:
        return ((f'<circle cx="100" cy="100" r="94" fill="none" stroke="{k}" stroke-width="6"/>' if anel else '') +
                f'<circle cx="146" cy="94" r="14" fill="{k}"/>'
                f'<path d="M14 128L44 104L64 116L92 92L126 118L150 108L186 128" fill="none" stroke="{k}" stroke-width="5" stroke-linejoin="round"/>'
                f'<path d="{onda(20, 70, 140, 1.6, 2)}M130 140Q140 136.8 150 140T170 140" fill="none" stroke="{k}" stroke-width="4" stroke-linecap="round"/>'
                f'<g fill="{k}">{CLARA}{CAO_COSTAS}{GATO_COSTAS}</g>'
                f'<path d="{CAUDA_GATO}{CAUDA_CAO}" fill="none" stroke="{k}" stroke-width="4.5" stroke-linecap="round"/>'
                f'<path d="M22 170L178 170" stroke="{k}" stroke-width="5" stroke-linecap="round"/>')
    return (f'<clipPath id="sa"><circle cx="100" cy="100" r="96"/></clipPath><g clip-path="url(#sa)">'
            f'<rect width="200" height="200" fill="{c["salvia_claro"]}"/>'
            f'<circle cx="146" cy="94" r="15" fill="{c["sol"]}"/>'
            f'<path d="M-4 130L40 102L64 116L92 90L128 120L150 108L204 130V200H-4Z" fill="{c["salvia"]}"/>'
            f'<rect y="126" width="200" height="22" fill="{c["mar"]}"/>'
            f'<path d="{onda(16, 64, 137, 1.4, 2)}M136 137Q146 134.2 156 137T176 137" fill="none" stroke="{c["superficie"]}" stroke-width="3" stroke-linecap="round"/>'
            f'<rect y="148" width="200" height="60" fill="{c["fundo"]}"/>'
            f'<g fill="{c["texto"]}">{CLARA}{CAO_COSTAS}{GATO_COSTAS}</g>'
            f'<path d="{CAUDA_GATO}{CAUDA_CAO}" fill="none" stroke="{c["texto"]}" stroke-width="4.5" stroke-linecap="round"/>'
            f'</g>' + (f'<circle cx="100" cy="100" r="96" fill="none" stroke="{c["texto"]}" stroke-width="4"/>' if anel else ''))


def assinatura_a(c):
    nome, bbn, _ = texto(FIGTREE, 'TIA CLARA', 58, 100, 278, c['texto'], (('wght', 800),), 60, 'middle')
    desc, bbd = descritor(100, 310, c['texto'], 13)
    corpo = f'<g>{simbolo_a(c)}</g>{nome}{desc}'
    return corpo, uniao((4, 4, 196, 196), bbn, bbd)


# ---------------------------------------------------------------- ROTA B · Assinatura
def nome_b(c, x=0, base=0, tam=120, cor=None, cor_sol=None, cor_onda=None):
    """'Tia Clara' em Norican; o pingo do i vira sol; uma onda sublinha 'Clara'."""
    cor = cor or c['texto']
    gl, larg = mc.glifos(NORICAN, 'Tia Clara', tam, x, base)
    i = next(g for g in gl if g['nome'] in ('i', 'uni0069') or g['nome'].startswith('i'))
    pingo = min(i['contornos'], key=lambda k: (k['bbox'][2] - k['bbox'][0]) * (k['bbox'][3] - k['bbox'][1]))
    i['contornos'] = [k for k in i['contornos'] if k is not pingo]
    px, py = (pingo['bbox'][0] + pingo['bbox'][2]) / 2, (pingo['bbox'][1] + pingo['bbox'][3]) / 2
    r = max(pingo['bbox'][2] - pingo['bbox'][0], pingo['bbox'][3] - pingo['bbox'][1]) * .72
    bb = mc.bbox_de(gl)
    clara = [g for g in gl if g['nome'] not in ('T', 'i', 'a', 'space')][:1]
    x_onda0 = mc.bbox_de(clara)[0] + tam * .06 if clara else bb[0]
    y_onda = base + tam * .2
    partes = (f'<path fill="{cor}" d="{mc.d_de(gl)}"/>'
              f'<circle cx="{f(px + r * .25)}" cy="{f(py - r * .75)}" r="{f(r)}" fill="{cor_sol or c["sol"]}"/>'
              f'<path d="{onda(x_onda0, bb[2] - tam * .02, y_onda, tam * .022, 2.5)}" fill="none" stroke="{cor_onda or c["salvia"]}" '
              f'stroke-width="{f(tam * .045)}" stroke-linecap="round"/>')
    return partes, uniao(bb, (px - r, py - r * 1.2, px + r, py + r), (x_onda0, y_onda - tam * .06, bb[2], y_onda + tam * .06))


def assinatura_b(c):
    nome, bb = nome_b(c, 0, 0, 120)
    cx = (bb[0] + bb[2]) / 2
    desc, bbd = descritor(cx, bb[3] + 34, c['texto'], 13)
    return nome + desc, uniao(bb, bbd)


def reduzida_b(c, uma_cor=None):
    """Avatar: 'Tc' em Norican sobre sálvia, com o sol no lugar do pingo."""
    fundo, letra, sol = (None, uma_cor, uma_cor) if uma_cor else (c['salvia'], c['superficie'], c['sol'])
    gl, larg = mc.glifos(NORICAN, 'Tc', 118, 0, 0)
    bb = mc.bbox_de(gl)
    dx, dy = 100 - (bb[0] + bb[2]) / 2 - 4, 100 - (bb[1] + bb[3]) / 2 + 6
    gl, _ = mc.glifos(NORICAN, 'Tc', 118, dx, dy)
    base = (f'<circle cx="100" cy="100" r="96" fill="{fundo}"/>' if fundo else
            f'<circle cx="100" cy="100" r="93" fill="none" stroke="{uma_cor}" stroke-width="6"/>')
    bb = mc.bbox_de(gl)
    return (base + f'<path fill="{letra}" d="{mc.d_de(gl)}"/>'
            f'<circle cx="{f(bb[2] + 2)}" cy="{f(bb[1] + 26)}" r="11" fill="{sol}"/>'
            f'<path d="{onda(58, 142, 150, 2.2, 2)}" fill="none" stroke="{letra}" stroke-width="6" stroke-linecap="round"/>')


# ---------------------------------------------------------------- ROTA C · As ilhas
# Horizonte em y=128. Gato à esquerda (orelhas em ponta), cão à direita (orelhas caídas), de frente.
GATO_ILHA = 'M44 128C44 116 45 108 48 102L51 83L63 95C66 94.3 74 94.3 77 95L89 83L92 102C95 108 96 116 96 128Z'
CAO_CABECA = 'M110 128C110 104 119 91 133 91C147 91 156 104 156 128Z'
CAO_ORELHAS = ('M116 96C106 96 101 105 102 117C103 125 109 127 112 121C114 115 115 107 119 101Z'
               'M150 96C160 96 165 105 164 117C163 125 157 127 154 121C152 115 151 107 147 101Z')


def simbolo_c(c, uma_cor=None, anel=True):
    if uma_cor:
        k = uma_cor
        return (f'<mask id="mc"><rect width="200" height="200" fill="#fff"/>'
                f'<path d="{GATO_ILHA}{CAO_CABECA}{CAO_ORELHAS}" fill="#000" stroke="#000" stroke-width="10" stroke-linejoin="round"/></mask>'
                + (f'<circle cx="100" cy="100" r="93" fill="none" stroke="{k}" stroke-width="6"/>' if anel else '') +
                f'<circle cx="100" cy="101" r="31" fill="{k}" mask="url(#mc)"/>'
                f'<path d="{GATO_ILHA}{CAO_CABECA}{CAO_ORELHAS}" fill="{k}"/>'
                f'<path d="M26 128H174" stroke="{k}" stroke-width="5" stroke-linecap="round"/>'
                f'<path d="{onda(46, 154, 148, 2, 3)}M66 166Q76 162 86 166T106 166T126 166T136 166" fill="none" stroke="{k}" stroke-width="5" stroke-linecap="round"/>')
    return (f'<clipPath id="sc"><circle cx="100" cy="100" r="96"/></clipPath><g clip-path="url(#sc)">'
            f'<rect width="200" height="200" fill="{c["salvia_claro"]}"/>'
            f'<circle cx="100" cy="101" r="31" fill="{c["sol"]}"/>'
            f'<rect y="128" width="200" height="72" fill="{c["salvia"]}"/>'
            f'<path d="{onda(46, 154, 148, 2, 3)}M66 166Q76 162 86 166T106 166T126 166T136 166" fill="none" stroke="{c["superficie"]}" stroke-width="4.5" stroke-linecap="round"/>'
            f'<path d="{GATO_ILHA}{CAO_CABECA}{CAO_ORELHAS}" fill="{c["texto"]}"/>'
            f'</g>')


def assinatura_c(c):
    nome, bbn, _ = texto(COURGETTE, 'Tia Clara', 64, 100, 282, c['texto'], (), 0, 'middle')
    desc, bbd = descritor(100, 318, c['texto'], 13)
    return f'<g>{simbolo_c(c)}</g>{nome}{desc}', uniao((4, 4, 196, 196), bbn, bbd)


# ---------------------------------------------------------------- versões reduzidas (avatar)
def _zoom(conteudo, esc, cx, cy, fundo=None, anel=None, idc='rz'):
    """Amplia a parte central do símbolo dentro do círculo, mantendo o anel sem escala."""
    t = f'translate({f(100 - cx * esc)} {f(100 - cy * esc)}) scale({f(esc)})'
    base = f'<circle cx="100" cy="100" r="96" fill="{fundo}"/>' if fundo else ''
    borda = f'<circle cx="100" cy="100" r="93" fill="none" stroke="{anel}" stroke-width="6"/>' if anel else ''
    return (f'<clipPath id="{idc}"><circle cx="100" cy="100" r="{90 if anel else 96}"/></clipPath>{base}'
            f'<g clip-path="url(#{idc})"><g transform="{t}">{conteudo}</g></g>{borda}')


def reduzida_a(c, uma_cor=None):
    if uma_cor:
        miolo = (f'<circle cx="146" cy="94" r="14" fill="{uma_cor}"/><g fill="{uma_cor}">{CLARA}{CAO_COSTAS}{GATO_COSTAS}</g>'
                 f'<path d="{CAUDA_GATO}{CAUDA_CAO}" fill="none" stroke="{uma_cor}" stroke-width="4.5" stroke-linecap="round"/>'
                 f'<path d="M20 170H180" stroke="{uma_cor}" stroke-width="5"/>')
        return _zoom(miolo, 1.35, 102, 128, anel=uma_cor, idc='ra1')
    return _zoom(simbolo_a(c, anel=False), 1.35, 102, 128, idc='ra')


def reduzida_c(c, uma_cor=None):
    if uma_cor:
        return _zoom(simbolo_c(c, uma_cor, anel=False), 1.3, 100, 116, anel=uma_cor, idc='rc1')
    return _zoom(simbolo_c(c), 1.3, 100, 116, idc='rc')


# ---------------------------------------------------------------- geração
def gerar():
    arquivos = {}

    def salva(rota, nome, conteudo, vb, titulo):
        pasta = os.path.join(SAIDA, f'rota-{rota}')
        os.makedirs(pasta, exist_ok=True)
        with open(os.path.join(pasta, nome), 'w', encoding='utf-8') as fh:
            fh.write(mc.svg_doc(conteudo, vb, titulo))
        arquivos.setdefault(rota, []).append(nome)
        print('ok', f'rota-{rota}/{nome}')

    quadrado = (0, 0, 200, 200)
    for rota, simb, assin, red in (
        ('a', simbolo_a, assinatura_a, reduzida_a),
        ('b', None, assinatura_b, reduzida_b),
        ('c', simbolo_c, assinatura_c, reduzida_c),
    ):
        c = PALETAS[PALETA_DA_ROTA[rota]]
        titulo = f'Tia Clara — rota {rota.upper()}'
        if simb:
            salva(rota, f'tc-{rota}-simbolo.svg', simb(c), quadrado, titulo + ' · símbolo')
        conteudo, bb = assin(c)
        salva(rota, f'tc-{rota}-assinatura.svg', conteudo, mc.com_margem(bb, 18), titulo + ' · assinatura')
        salva(rota, f'tc-{rota}-reduzida.svg', red(c), quadrado, titulo + ' · reduzida')
        salva(rota, f'tc-{rota}-1cor.svg', red(c, uma_cor=c['texto']), quadrado, titulo + ' · 1 cor')
        salva(rota, f'tc-{rota}-1cor-branco.svg', red(c, uma_cor='#FFFFFF'), quadrado, titulo + ' · 1 cor branco')

    # prancha de redução (mesma lógica de _fonte/teste-L1.html)
    linhas = []
    for rota in 'abc':
        c = PALETAS[PALETA_DA_ROTA[rota]]
        p = f'rota-{rota}/tc-{rota}-'
        tamanhos = ''.join(f'<div class="t"><img src="{p}reduzida.svg" width="{t}" height="{t}"><span>{t} px</span></div>' for t in (16, 32, 48, 120))
        linhas.append(f'''<section><h2>Rota {rota.upper()}</h2>
<div class="lin">{tamanhos}
<div class="t"><img src="{p}1cor.svg" width="48" height="48"><img src="{p}1cor.svg" width="120" height="120"><span>1 cor</span></div>
<div class="t esc" style="background:{c["texto"]}"><img src="{p}1cor-branco.svg" width="48" height="48"><img src="{p}1cor-branco.svg" width="120" height="120"><span>1 cor sobre escuro</span></div>
<div class="t av"><img src="{p}reduzida.svg" width="56" height="56" style="border-radius:50%"><span>avatar do WhatsApp (lista de conversas)</span></div>
</div></section>''')
    html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>
@font-face{{font-family:Fig;src:url("../fontes/Figtree[wght].ttf");font-weight:300 900}}
body{{margin:0;width:1600px;background:#FBF9F4;color:#2F3B33;font:14px Fig;padding:36px 40px}}
h1{{font:700 26px Fig;margin:0 0 4px}} .sub{{color:#5B665E;margin:0 0 20px}} h2{{font:700 18px Fig;margin:20px 0 10px}}
.lin{{display:flex;gap:28px;align-items:flex-end;background:#fff;border:1px solid #E6E2D8;border-radius:14px;padding:22px}}
.t{{display:flex;flex-direction:column;align-items:center;gap:8px}} .t span{{font:600 12px Fig;color:#5B665E}}
.t.esc{{padding:14px;border-radius:10px;flex-direction:row;align-items:flex-end;gap:14px}} .t.esc span{{color:#fff}}
.t.av{{margin-left:auto}}
</style></head><body><h1>Teste de redução: as três rotas</h1>
<p class="sub">O símbolo precisa ser reconhecível a 32 px (avatar do WhatsApp) e funcionar em 1 cor, sobre claro e sobre escuro.</p>
{"".join(linhas)}</body></html>'''
    with open(os.path.join(SAIDA, 'teste-reducao.html'), 'w', encoding='utf-8') as fh:
        fh.write(html)
    print('ok teste-reducao.html')
    return arquivos


if __name__ == '__main__':
    gerar()
