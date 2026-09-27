"""Gera 06-motion/logo-reveal.html: a plaquinha balança e assenta; o logotipo entra com firmeza."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import marca as m

def gerar():
    tam = 100
    # símbolo em (0,0) escala 1, logotipo à direita — mesma geometria da assinatura horizontal
    lg_svg, (lx0, ly0, lx1, ly1) = m.logotipo(0, 0, tam, m.PINHO)
    desc, (_, _, dx1, dy1) = m.descritor(lx0, 44, 15.5, m.PINHO)
    altura = dy1 - ly0
    esc = altura * 1.02 / m.PLQ_A
    ls = m.PLQ_L * esc
    sx, sy = lx0 - ls * 0.34 - ls, ly0 - altura * 0.01
    simb = m.simbolo(sx, sy, esc, m.PINHO)
    piv_x, piv_y = sx + m.FURO[0] * esc, sy + m.FURO[1] * esc
    # separa "Tia" (1o path) e "Clara" (2o path) e a argola (dentro do path de Tia)
    tia_path, clara_path = lg_svg.split('/>')[0] + '/>', lg_svg.split('/>')[1] + '/>'
    vb = (sx - 30, ly0 - 40, (lx1 - sx) + 60, (dy1 - ly0) + 80)
    html = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tia Clara — assinatura em movimento</title>
<style>
:root{{--linho:#F4EEE3;--pinho:#1E3B33;--latao:#C6A15E;--firme:cubic-bezier(.2,0,0,1);--assentar:cubic-bezier(.34,1.2,.64,1)}}
html,body{{margin:0;height:100%;background:var(--linho)}}
body{{display:grid;place-items:center}}
svg{{width:min(86vw,900px);height:auto;overflow:visible}}
#plaquinha{{transform-box:view-box;transform-origin:{piv_x:.2f}px {piv_y:.2f}px;animation:entra 1.6s var(--firme) both, balanca 1.4s .25s both}}
@keyframes entra{{from{{opacity:0;translate:0 -26px}}to{{opacity:1;translate:0 0}}}}
@keyframes balanca{{0%{{rotate:-9deg}}30%{{rotate:6deg}}55%{{rotate:-3deg}}78%{{rotate:1.2deg}}100%{{rotate:0deg}}}}
#clara{{animation:sobe .72s 1.05s var(--firme) both}}
#tia{{animation:gesto .72s 1.25s var(--firme) both}}
#descritor{{animation:desc .72s 1.55s var(--firme) both}}
@keyframes sobe{{from{{opacity:0;translate:0 14px}}to{{opacity:1;translate:0 0}}}}
@keyframes gesto{{from{{opacity:0;translate:-10px 0}}to{{opacity:1;translate:0 0}}}}
@keyframes desc{{from{{opacity:0;letter-spacing:.3em}}to{{opacity:.999}}}}
button{{position:fixed;bottom:24px;left:50%;translate:-50% 0;font:600 13px/1 "Helvetica Neue",Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--pinho);background:none;border:1px solid #1E3B3340;border-radius:999px;padding:12px 18px;cursor:pointer}}
@media (prefers-reduced-motion:reduce){{#plaquinha,#clara,#tia,#descritor{{animation:none}}}}
</style></head>
<body>
<svg viewBox="{' '.join(f'{v:.2f}' for v in vb)}" role="img" aria-label="Tia Clara — Pet Sitter &amp; Dog Walker">
<g id="plaquinha">{simb}</g>
<g id="tia">{tia_path}</g>
<g id="clara">{clara_path}</g>
<g id="descritor">{desc}</g>
</svg>
<button onclick="document.querySelectorAll('svg g').forEach(g=>{{g.style.animation='none';g.offsetWidth;g.style.animation=''}})">Rever</button>
</body></html>'''
    out = os.path.join(m.RAIZ, '06-motion', 'logo-reveal.html')
    open(out, 'w').write(html)
    return out

if __name__ == '__main__':
    print(gerar())
