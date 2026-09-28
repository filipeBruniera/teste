"""
Tia Clara — construção geométrica da marca (fonte única da verdade).

Gera os SVGs mestres em 04-logo/master/ com TODO texto convertido em curvas:
nenhum arquivo final depende de fonte instalada.

    python3 tia-clara/_fonte/marca.py

Requer: fonttools, uharfbuzz  (pip install fonttools uharfbuzz)
"""
import functools, os
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.boundsPen import BoundsPen

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
FONTES = os.path.join(RAIZ, '05-design-system', 'fontes')
SAIDA = os.path.join(RAIZ, '04-logo', 'master')
LIT = os.path.join(FONTES, 'Literata[opsz,wght].ttf')
LITI = os.path.join(FONTES, 'Literata-Italic[opsz,wght].ttf')
INS = os.path.join(FONTES, 'InstrumentSans[wdth,wght].ttf')

# ---------------------------------------------------------------- cores
PINHO, PINHO_PROF, LINHO, PAPEL = '#1E3B33', '#142A24', '#F4EEE3', '#FBF8F2'
LATAO, ARGILA, SALVIA, PRETO, BRANCO = '#C6A15E', '#A94E2A', '#DDE1D4', '#000000', '#FFFFFF'

# ---------------------------------------------------------------- eixos tipográficos da marca
AX_CLARA = (('opsz', 48), ('wght', 680))      # "Clara": redondo, firme  (Guardiã)
AX_TIA = (('opsz', 48), ('wght', 500))        # "Tia": itálico, gesto    (Cuidadora)
AX_C = (('opsz', 36), ('wght', 690))          # C do símbolo (opsz médio: menos contraste, mais firme)
AX_C_COMPACTO = (('opsz', 14), ('wght', 790)) # C reforçado para 16–32 px
AX_DESC = (('wdth', 100), ('wght', 560))      # descritor


# ---------------------------------------------------------------- texto -> curvas
@functools.lru_cache(None)
def _fonte(path, axes):
    tt = TTFont(path)
    font = hb.Font(hb.Face(hb.Blob.from_file_path(path)))
    if axes:
        font.set_variations(dict(axes))
    gs = tt.getGlyphSet(location=dict(axes)) if axes else tt.getGlyphSet()
    return tt, font, gs, tt['head'].unitsPerEm


def glifos(path, texto, tam, x=0, y=0, axes=(), tracking=0):
    """Glifos moldados (HarfBuzz, com kerning) e separados por contorno, já em coordenadas SVG."""
    tt, font, gs, upem = _fonte(path, tuple(axes))
    buf = hb.Buffer(); buf.add_str(texto); buf.guess_segment_properties()
    hb.shape(font, buf, {'kern': True, 'liga': True})
    ordem = tt.getGlyphOrder(); s = tam / upem; cx = 0; saida = []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        nome = ordem[info.codepoint]
        rec = DecomposingRecordingPen(gs); gs[nome].draw(rec)  # decompõe glifos compostos (ex.: i = haste + pingo)
        conts, cur = [], []
        for op in rec.value:
            cur.append(op)
            if op[0] in ('closePath', 'endPath'):
                conts.append(cur); cur = []
        tr = (s, 0, 0, -s, x + (cx + pos.x_offset) * s, y - pos.y_offset * s)
        cs = []
        for c in conts:
            sp, bp = SVGPathPen(None), BoundsPen(None)
            tp, tb = TransformPen(sp, tr), TransformPen(bp, tr)
            for op, args in c:
                getattr(tp, op)(*args); getattr(tb, op)(*args)
            cs.append({'d': sp.getCommands(), 'bbox': bp.bounds})
        saida.append({'nome': nome, 'contornos': cs})
        cx += pos.x_advance + tracking * upem / 1000
    largura = (cx - tracking * upem / 1000) * s
    return saida, largura


def bbox_de(gl):
    bs = [c['bbox'] for g in gl for c in g['contornos'] if c['bbox']]
    return min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs)


def d_de(gl):
    return ' '.join(c['d'] for g in gl for c in g['contornos'])


def fmt(v):
    return f'{v:.2f}'.rstrip('0').rstrip('.')


# ---------------------------------------------------------------- SÍMBOLO: a plaquinha
# Unidade: plaquinha 100 x 112. Topo = semicírculo r50; cantos inferiores r22; furo r7.5 em (50,19).
PLQ_L, PLQ_A, PLQ_R = 100, 112, 22
FURO = (50, 19, 7.5)


def plaquinha_d(x=0, y=0, esc=1.0):
    L, A, r = PLQ_L * esc, PLQ_A * esc, PLQ_R * esc
    return (f'M{fmt(x)},{fmt(y + L / 2)} A{fmt(L / 2)},{fmt(L / 2)} 0 0 1 {fmt(x + L)},{fmt(y + L / 2)} '
            f'V{fmt(y + A - r)} A{fmt(r)},{fmt(r)} 0 0 1 {fmt(x + L - r)},{fmt(y + A)} '
            f'H{fmt(x + r)} A{fmt(r)},{fmt(r)} 0 0 1 {fmt(x)},{fmt(y + A - r)} Z')


def circulo_d(cx, cy, r, horario=False):
    """Círculo como path. Anti-horário por padrão (= furo sob a regra nonzero, oposto à plaquinha)."""
    sw = 1 if horario else 0
    return f'M{fmt(cx - r)},{fmt(cy)} a{fmt(r)},{fmt(r)} 0 1 {sw} {fmt(2 * r)},0 a{fmt(r)},{fmt(r)} 0 1 {sw} {fmt(-2 * r)},0 Z'


def simbolo(x=0, y=0, esc=1.0, cor=PINHO, recorte=LINHO, compacto=False, vazado=True):
    """Plaquinha + furo + C.  vazado=True: C e furo são recortes (transparentes) — versão de produção.
    vazado=False: C e furo pintados na cor `recorte` (útil só para pré-visualização)."""
    axes = AX_C_COMPACTO if compacto else AX_C
    tam = (80 if compacto else 71) * esc
    gl, _ = glifos(LIT, 'C', tam, 0, 0, axes)
    bx0, by0, bx1, by1 = bbox_de(gl)
    # centro óptico: centro da área útil (do furo à base) +1u, e 2.6u à direita (o C é aberto à direita e pesa à esquerda)
    fx, fy, fr = FURO
    if compacto:
        fy, fr = 18, 9.5  # furo maior: sobrevive a 16 px
    topo_util = y + (fy + fr) * esc
    alvo_cy = (topo_util + y + PLQ_A * esc) / 2 + 1.0 * esc
    alvo_cx = x + (PLQ_L / 2 + 2.6) * esc
    dx = alvo_cx - (bx0 + bx1) / 2
    dy = alvo_cy - (by0 + by1) / 2
    gl, _ = glifos(LIT, 'C', tam, dx, dy, axes)
    corpo = plaquinha_d(x, y, esc)
    furo = circulo_d(x + fx * esc, y + fy * esc, fr * esc)
    if vazado:
        return f'<path fill="{cor}" fill-rule="evenodd" d="{corpo} {furo} {d_de(gl)}"/>'
    return (f'<path fill="{cor}" d="{corpo}"/><path fill="{recorte}" d="{furo}"/>'
            f'<path fill="{recorte}" d="{d_de(gl)}"/>')


# ---------------------------------------------------------------- LOGOTIPO: "Tia Clara"
def logotipo(x=0, base=0, tam=100, cor=PINHO, cor_tia=None, argola=True):
    """'Tia' em Literata Itálico 500 + 'Clara' em Literata 680. O pingo do i vira argola (a mesma do furo da plaquinha)."""
    cor_tia = cor_tia or cor
    tia, w_tia = glifos(LITI, 'Tia', tam, x, base, AX_TIA)
    partes = []
    for g in tia:
        cs = g['contornos']
        if g['nome'].startswith('i') and argola:
            cs = sorted(cs, key=lambda c: c['bbox'][1])
            pingo, resto = cs[0], cs[1:]
            x0, y0, x1, y1 = pingo['bbox']
            r = (x1 - x0) / 2 * 1.06
            esp = r * 0.58
            cx, cy = (x0 + x1) / 2 + r * 0.04, (y0 + y1) / 2 - r * 0.1
            anel = circulo_d(cx, cy, r, horario=True) + ' ' + circulo_d(cx, cy, r - esp)
            partes.append(('tia', ' '.join(c['d'] for c in resto)))
            partes.append(('tia', anel))
        else:
            partes.append(('tia', ' '.join(c['d'] for c in cs)))
    espaco = tam * 0.235
    clara, w_clara = glifos(LIT, 'Clara', tam, x + w_tia + espaco, base, AX_CLARA)
    partes.append(('clara', d_de(clara)))
    d_tia = ' '.join(d for k, d in partes if k == 'tia')
    d_clara = ' '.join(d for k, d in partes if k == 'clara')
    svg = (f'<path fill="{cor_tia}" d="{d_tia}"/>'
           f'<path fill="{cor}" d="{d_clara}"/>')
    todos = tia + clara
    return svg, bbox_de(todos)


def descritor(x, base, tam, cor=PINHO, anchor='start'):
    gl, w = glifos(INS, 'PET SITTER & DOG WALKER', tam, 0, 0, AX_DESC, tracking=150)
    b = bbox_de(gl)
    if anchor == 'middle':
        x -= (b[0] + b[2]) / 2
    else:
        x -= b[0]
    gl, _ = glifos(INS, 'PET SITTER & DOG WALKER', tam, x, base, AX_DESC, tracking=150)
    return f'<path fill="{cor}" d="{d_de(gl)}"/>', bbox_de(gl)


# ---------------------------------------------------------------- composições
def svg_doc(conteudo, vb, titulo, fundo=None):
    x, y, w, h = vb
    bg = f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" fill="{fundo}"/>' if fundo else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{fmt(x)} {fmt(y)} {fmt(w)} {fmt(h)}" '
            f'width="{fmt(w)}" height="{fmt(h)}" role="img" aria-label="{titulo}"><title>{titulo}</title>{bg}{conteudo}</svg>\n')


def comp_logotipo(cor=PINHO, cor_tia=None, com_descritor=True):
    tam = 100
    lg, (x0, y0, x1, y1) = logotipo(0, 0, tam, cor, cor_tia)
    partes = [lg]
    if com_descritor:
        d, (_, _, dx1, dy1) = descritor(x0, 44, 15.5, cor)
        partes.append(d)
        y1 = dy1
    return ''.join(partes), (x0, y0, x1, y1)


def comp_horizontal(cor=PINHO, recorte=None, cor_tia=None):
    """Assinatura principal: plaquinha à esquerda, logotipo + descritor à direita."""
    lg, (lx0, ly0, lx1, ly1) = comp_logotipo(cor, cor_tia)
    altura = ly1 - ly0
    esc = (altura * 1.02) / PLQ_A
    larg_s = PLQ_L * esc
    gap = larg_s * 0.34
    sx = lx0 - gap - larg_s
    sy = ly0 - altura * 0.01
    s = simbolo(sx, sy, esc, cor)
    return s + lg, (sx, min(sy, ly0), lx1, max(ly1, sy + PLQ_A * esc)), larg_s


def comp_horizontal_compacta(cor=PINHO, cor_tia=None):
    """Para alturas pequenas (< 60 px): sem descritor, plaquinha do tamanho da caixa-alta."""
    lg, (lx0, ly0, lx1, ly1) = logotipo(0, 0, 100, cor, cor_tia)
    altura = (0 - ly0) * 1.16
    esc = altura / PLQ_A
    larg_s = PLQ_L * esc
    sx = lx0 - larg_s * 0.36 - larg_s
    sy = 0 + altura * 0.06 - altura
    return simbolo(sx, sy, esc, cor) + lg, (sx, min(sy, ly0), lx1, max(ly1, sy + altura)), larg_s


def comp_vertical(cor=PINHO, cor_tia=None, com_descritor=True):
    """Assinatura vertical: plaquinha centrada acima, logotipo e descritor centrados."""
    tam = 100
    lg, (x0, y0, x1, y1) = logotipo(0, 0, tam, cor, cor_tia)
    cx = (x0 + x1) / 2
    d, dy1 = '', y1
    if com_descritor:
        d, (_, _, _, dy1) = descritor(cx, 44, 15.5, cor, anchor='middle')
    larg_s = (x1 - x0) * 0.30
    esc = larg_s / PLQ_L
    sy = y0 - 30 - PLQ_A * esc
    s = simbolo(cx - larg_s / 2, sy, esc, cor)
    return s + lg + d, (x0, sy, x1, dy1), larg_s


def com_margem(bb, m):
    x0, y0, x1, y1 = bb
    return (x0 - m, y0 - m, (x1 - x0) + 2 * m, (y1 - y0) + 2 * m)


def gerar():
    os.makedirs(SAIDA, exist_ok=True)
    arq = {}

    def salva(nome, svg):
        with open(os.path.join(SAIDA, nome), 'w') as f:
            f.write(svg)
        arq[nome] = svg

    # --- símbolo
    for nome, cor, fundo in [('simbolo', PINHO, None), ('simbolo-preto', PRETO, None),
                             ('simbolo-branco', BRANCO, None), ('simbolo-linho', LINHO, None),
                             ('simbolo-latao', LATAO, None), ('simbolo-argila', ARGILA, None)]:
        m = PLQ_L * 0.25
        salva(f'tc-{nome}.svg', svg_doc(simbolo(0, 0, 1, cor), (-m, -m, PLQ_L + 2 * m, PLQ_A + 2 * m), 'Tia Clara — símbolo', fundo))
    for nome, cor in [('simbolo-compacto', PINHO), ('simbolo-compacto-preto', PRETO), ('simbolo-compacto-branco', BRANCO)]:
        salva(f'tc-{nome}.svg', svg_doc(simbolo(0, 0, 1, cor, compacto=True), (-6, -6, 112, 124), 'Tia Clara — símbolo compacto'))

    # --- logotipo
    for nome, cor in [('logotipo', PINHO), ('logotipo-preto', PRETO), ('logotipo-branco', BRANCO), ('logotipo-linho', LINHO)]:
        c, bb = comp_logotipo(cor)
        salva(f'tc-{nome}.svg', svg_doc(c, com_margem(bb, 30), 'Tia Clara — logotipo'))
    c, bb = comp_logotipo(PINHO, com_descritor=False)
    salva('tc-logotipo-sem-descritor.svg', svg_doc(c, com_margem(bb, 26), 'Tia Clara — logotipo'))

    # --- assinaturas
    for nome, cor in [('horizontal', PINHO), ('horizontal-preto', PRETO), ('horizontal-branco', BRANCO), ('horizontal-linho', LINHO)]:
        c, bb, ls = comp_horizontal(cor)
        salva(f'tc-assinatura-{nome}.svg', svg_doc(c, com_margem(bb, ls * 0.25), 'Tia Clara — assinatura horizontal'))
    for nome, cor in [('vertical', PINHO), ('vertical-preto', PRETO), ('vertical-branco', BRANCO), ('vertical-linho', LINHO)]:
        c, bb, ls = comp_vertical(cor)
        salva(f'tc-assinatura-{nome}.svg', svg_doc(c, com_margem(bb, ls * 0.25), 'Tia Clara — assinatura vertical'))

    # --- versões compactas (sem descritor) para tamanhos pequenos
    for nome, cor in [('', PINHO), ('-preto', PRETO), ('-branco', BRANCO), ('-linho', LINHO)]:
        c, bb, ls = comp_horizontal_compacta(cor)
        salva(f'tc-assinatura-horizontal-compacta{nome}.svg', svg_doc(c, com_margem(bb, ls * 0.25), 'Tia Clara — assinatura horizontal compacta'))
        c, bb, ls = comp_vertical(cor, com_descritor=False)
        salva(f'tc-assinatura-vertical-compacta{nome}.svg', svg_doc(c, com_margem(bb, ls * 0.25), 'Tia Clara — assinatura vertical compacta'))

    # --- negativos sobre fundo de marca (arquivos de aplicação, com fundo)
    c, bb, ls = comp_horizontal(LINHO)
    salva('tc-assinatura-horizontal-sobre-pinho.svg', svg_doc(c, com_margem(bb, ls * 0.6), 'Tia Clara — assinatura sobre pinho', PINHO))
    c, bb, ls = comp_vertical(LINHO)
    salva('tc-assinatura-vertical-sobre-pinho.svg', svg_doc(c, com_margem(bb, ls * 0.6), 'Tia Clara — assinatura sobre pinho', PINHO))

    # --- avatar (círculo-seguro para Instagram/WhatsApp) e favicon
    av = 512
    esc = (av * 0.56) / PLQ_A
    sx, sy = av / 2 - PLQ_L * esc / 2, av / 2 - PLQ_A * esc / 2 - av * 0.005
    salva('tc-avatar.svg', svg_doc(f'<rect width="{av}" height="{av}" fill="{PINHO}"/>' + simbolo(sx, sy, esc, LINHO), (0, 0, av, av), 'Tia Clara — avatar'))
    salva('tc-avatar-linho.svg', svg_doc(f'<rect width="{av}" height="{av}" fill="{LINHO}"/>' + simbolo(sx, sy, esc, PINHO), (0, 0, av, av), 'Tia Clara — avatar claro'))
    fv = 64
    esc = (fv * 0.97) / PLQ_A
    estilo = f'<style>path{{fill:{PINHO}}}@media (prefers-color-scheme:dark){{path{{fill:{LINHO}}}}}</style>'
    salva('tc-favicon.svg', svg_doc(estilo + simbolo(fv / 2 - PLQ_L * esc / 2, fv / 2 - PLQ_A * esc / 2, esc, PINHO, compacto=True),
                                    (0, 0, fv, fv), 'Tia Clara'))
    # app icon / apple-touch: plaquinha Linho sobre quadrado Pinho (o sistema arredonda os cantos)
    ai = 180
    esc = (ai * 0.62) / PLQ_A
    salva('tc-app-icon.svg', svg_doc(f'<rect width="{ai}" height="{ai}" fill="{PINHO}"/>'
                                     + simbolo(ai / 2 - PLQ_L * esc / 2, ai / 2 - PLQ_A * esc / 2, esc, LINHO, compacto=True),
                                     (0, 0, ai, ai), 'Tia Clara'))
    return arq


if __name__ == '__main__':
    for k in gerar():
        print('ok', k)
