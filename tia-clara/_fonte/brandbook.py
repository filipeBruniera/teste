"""Gera o brand book: 08-brand-book/brand-book.html (página para publicar) e index.html (versão local completa)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import marca as m

OUT = os.path.join(m.RAIZ, '08-brand-book')
A = 'assets/'


def cc(svg):
    """troca as cores fixas do logo por currentColor, para herdar do tema"""
    for c in (m.PINHO, m.LINHO):
        svg = svg.replace(f'fill="{c}"', 'fill="currentColor"')
    return svg


# ---------- hero: assinatura animada (mesma geometria da horizontal)
lg_svg, (lx0, ly0, lx1, ly1) = m.logotipo(0, 0, 100, m.LINHO)
desc, (_, _, _, dy1) = m.descritor(lx0, 44, 15.5, m.LINHO)
alt = dy1 - ly0
esc = alt * 1.02 / m.PLQ_A
ls = m.PLQ_L * esc
sx, sy = lx0 - ls * 0.34 - ls, ly0 - alt * 0.01
PIV = (sx + m.FURO[0] * esc, sy + m.FURO[1] * esc)
tia_p, clara_p = lg_svg.split('/>')[0] + '/>', lg_svg.split('/>')[1] + '/>'
HERO_SVG = (f'<svg class="assinatura" viewBox="{sx - 6:.1f} {ly0 - 34:.1f} {(lx1 - sx) + 12:.1f} {(dy1 - ly0) + 50:.1f}" role="img" aria-label="Tia Clara — Pet Sitter &amp; Dog Walker">'
            f'<g id="a-plq">{m.simbolo(sx, sy, esc, m.LINHO)}</g><g id="a-tia">{tia_p}</g><g id="a-clara">{clara_p}</g><g id="a-desc">{desc}</g></svg>')

# ---------- diagrama de construção do símbolo
simb = m.simbolo(0, 0, 1, m.PINHO)
CONSTR = f'''<svg viewBox="-58 -26 230 170" class="diagrama" role="img" aria-label="Construção da plaquinha">
<g style="color:var(--tinta)">{cc(simb)}</g>
<g fill="none" style="stroke:var(--destaque)" stroke-width=".6" stroke-dasharray="2 2">
<circle cx="50" cy="50" r="50"/><line x1="-6" y1="50" x2="106" y2="50"/><line x1="50" y1="-8" x2="50" y2="120"/>
<circle cx="78" cy="90" r="22"/><circle cx="22" cy="90" r="22"/><circle cx="50" cy="19" r="11"/></g>
<g style="stroke:var(--mudo)" stroke-width=".5" fill="none"><path d="M0,124 V130 M100,124 V130 M0,127 H100"/><path d="M112,0 H118 M112,112 H118 M115,0 V112"/></g>
<g class="cota" style="fill:var(--mudo)"><text x="50" y="138" text-anchor="middle">100 u</text><text x="121" y="59">112 u</text>
<text x="-54" y="24">topo: semicírculo r 50</text><text x="-54" y="33">furo: r 7,5 em (50, 19)</text><text x="112" y="100">cantos r 22</text>
<text x="-54" y="104">C: Literata</text><text x="-54" y="113">opsz 36 · peso 690</text></g></svg>'''

# ---------- área de proteção
hz, (hx0, hy0, hx1, hy1), hls = m.comp_horizontal(m.PINHO)
xu = hls * 0.25
PROT = f'''<svg viewBox="{hx0 - xu * 1.6:.1f} {hy0 - xu * 1.6:.1f} {(hx1 - hx0) + xu * 3.2:.1f} {(hy1 - hy0) + xu * 3.2:.1f}" class="diagrama" role="img" aria-label="Área de proteção da assinatura">
<rect x="{hx0 - xu:.1f}" y="{hy0 - xu:.1f}" width="{(hx1 - hx0) + 2 * xu:.1f}" height="{(hy1 - hy0) + 2 * xu:.1f}" fill="none" style="stroke:var(--destaque)" stroke-width="1.2" stroke-dasharray="5 4"/>
<g style="color:var(--tinta)">{cc(hz)}</g>
<g style="fill:var(--destaque)" opacity=".22"><rect x="{hx0 - xu:.1f}" y="{hy0 - xu:.1f}" width="{xu:.1f}" height="{xu:.1f}"/><rect x="{hx1:.1f}" y="{hy1:.1f}" width="{xu:.1f}" height="{xu:.1f}"/><rect x="{hx0:.1f}" y="{hy0 - xu:.1f}" width="{hls:.1f}" height="{xu:.1f}" opacity=".5"/></g>
<g class="cota-g" style="fill:var(--destaque)"><text x="{hx0 - xu + 4:.1f}" y="{hy0 - xu + xu * .7:.1f}">x</text><text x="{hx1 + 4:.1f}" y="{hy1 + xu * .7:.1f}">x</text></g></svg>'''

ICON = {
 'chave': '<circle cx="8" cy="12" r="4"/><path d="M12 12h8.5M17.5 12v3M20.5 12v2.2"/>',
 'guia': '<circle cx="7" cy="6.5" r="3.2"/><path d="M9.3 8.8c2.6 2.4 4.9 4.9 7.2 7.4"/><rect x="15.4" y="15.6" width="4.4" height="5.6" rx="1.6" transform="rotate(-42 17.6 18.4)"/>',
 'relogio': '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
 'prancheta': '<rect x="5" y="4.5" width="14" height="16" rx="2"/><path d="M9 4.5V3h6v1.5M9 13l2 2 4-4"/>',
 'calendario': '<rect x="4" y="5.5" width="16" height="14" rx="2"/><path d="M4 10h16M8 3.5v4M16 3.5v4"/>',
 'camera': '<rect x="3.5" y="7" width="17" height="12" rx="2"/><circle cx="12" cy="13" r="3.2"/><path d="M9 7l1.4-2.3h3.2L15 7"/>',
 'casa': '<path d="M4 11l8-6.5 8 6.5M6.5 9.5V19.5h11V9.5"/>',
 'plaquinha': '<path d="M6 10a6 6 0 0 1 12 0v8a2.5 2.5 0 0 1-2.5 2.5h-7A2.5 2.5 0 0 1 6 18z"/><circle cx="12" cy="8.2" r="1.3"/>',
 'balao': '<path d="M5 5.5h14a1.5 1.5 0 0 1 1.5 1.5v8.5A1.5 1.5 0 0 1 19 17H10l-4.5 3.5V17H5a1.5 1.5 0 0 1-1.5-1.5V7A1.5 1.5 0 0 1 5 5.5z"/>',
}
def ic(n, t=28):
    return f'<svg width="{t}" height="{t}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[n]}</svg>'

CAPS = [('decisoes', 'Decisões'), ('ideia', 'Ideia de marca'), ('posicionamento', 'Posicionamento'), ('arquetipos', 'Arquétipos'),
        ('logo', 'Logo'), ('cor', 'Cor'), ('tipografia', 'Tipografia'), ('composicao', 'Composição'), ('imagem', 'Imagem e ícones'),
        ('movimento', 'Movimento'), ('voz', 'Tom de voz'), ('aplicacoes', 'Aplicações'), ('faca', 'Faça / não faça'),
        ('arquivos', 'Arquivos'), ('qa', 'QA')]
TOC = ''.join(f'<li><a href="#{i}"><span class="n">{k:02d}</span>{t}</a></li>' for k, (i, t) in enumerate(CAPS))

def cap(i, titulo, lead=''):
    k = [c[0] for c in CAPS].index(i)
    return f'<header class="cap"><span class="cap-n">{k:02d}</span><h2>{titulo}</h2>{f"<p class=lead>{lead}</p>" if lead else ""}</header>'

SW = [('Pinho', '#1E3B33', '#F4EEE3', 'Guardiã. Cor-mãe: logo, títulos, fundos de autoridade.', 'Linho 10,5 · Papel 11,5'),
      ('Linho', '#F4EEE3', '#1E3B33', 'Fundo padrão. Calor sem doçura.', 'Pinho 10,5 · Argila 4,8'),
      ('Papel', '#FBF8F2', '#1E3B33', 'Superfície elevada, cartões.', 'Pinho 11,5'),
      ('Sálvia', '#DDE1D4', '#1E3B33', 'Blocos de apoio, relatório.', 'Pinho 9,1 · Musgo 4,8'),
      ('Argila', '#A94E2A', '#F4EEE3', 'Cuidadora. Botão, destaque, calor.', 'Sobre Linho 4,8 · Papel 5,2'),
      ('Latão', '#C6A15E', '#1E3B33', 'O metal da plaquinha. Só sobre Pinho.', 'Sobre Pinho 5,0 · nunca sobre claro'),
      ('Musgo', '#56625A', '#F4EEE3', 'Texto secundário.', 'Sobre Linho 5,5'),
      ('Pinho Profundo', '#142A24', '#F4EEE3', 'Modo escuro, alto contraste.', 'Linho 13,1')]
SWATCHES = ''.join(f'<figure class="sw"><div class="sw-c" style="background:{h};color:{t}"><span>{n}</span><code>{h}</code></div><figcaption>{r}<small>{c}</small></figcaption></figure>' for n, h, t, r, c in SW)

PROD = [('prod-relatorio-whatsapp.png', 'Relatório de visita (WhatsApp)', 'A peça mais importante: sai ao fim de cada visita.'),
        ('prod-ig-01-autoridade-protocolo.png', 'Autoridade / protocolo', 'Pinho + Latão: o método à mostra.'),
        ('prod-ig-02-prova-de-servico.png', 'Prova de serviço', 'Números reais do atendimento.'),
        ('prod-ig-03a-carrossel-capa.png', 'Carrossel · capa', ''), ('prod-ig-03b-carrossel-passo.png', 'Carrossel · passo', ''),
        ('prod-ig-03c-carrossel-fecho.png', 'Carrossel · fecho', 'CTA em Argila.'),
        ('prod-ig-04-estatistica.png', 'Estatística', 'Um número e a resposta da Clara.'),
        ('prod-ig-05-anuncio-agenda.png', 'Anúncio', 'Agenda e novidades.')]
PRODG = ''.join(f'<figure class="app"><img src="{A}{f}" alt="{t}" loading="lazy" width="720" height="900"><figcaption><b>{t}</b>{" · " + d if d else ""}</figcaption></figure>' for f, t, d in PROD)

BODY = f'''<title>Tia Clara · Brand Book</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&family=Literata:ital,opsz,wght@0,7..72,300..800;1,7..72,300..800&display=swap">
<style>
:root{{--fundo:#F4EEE3;--sup:#FBF8F2;--apoio:#DDE1D4;--tinta:#1E3B33;--mudo:#56625A;--linha:rgb(30 59 51/.16);--destaque:#A94E2A;--metal:#C6A15E;--hero:#1E3B33;--hero-t:#F4EEE3;
--voz:"Literata",Georgia,"Times New Roman",serif;--met:"Instrument Sans","Helvetica Neue",Arial,sans-serif;--firme:cubic-bezier(.2,0,0,1)}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{color-scheme:dark;--fundo:#142A24;--sup:#1E3B33;--apoio:#24463C;--tinta:#F4EEE3;--mudo:#DDE1D4;--linha:rgb(244 238 227/.16);--destaque:#E7B89A;--hero:#1E3B33}}}}
:root[data-theme="dark"]{{color-scheme:dark;--fundo:#142A24;--sup:#1E3B33;--apoio:#24463C;--tinta:#F4EEE3;--mudo:#DDE1D4;--linha:rgb(244 238 227/.16);--destaque:#E7B89A;--hero:#1E3B33}}
*{{box-sizing:border-box}}
body{{background:var(--fundo);color:var(--tinta);font:400 17px/1.6 var(--met);-webkit-font-smoothing:antialiased;margin:0}}
h1,h2,h3{{font-family:var(--voz);font-weight:600;text-wrap:balance;margin:0;line-height:1.1}}
p{{margin:0}} a{{color:inherit}} code{{font:500 .86em var(--met);font-variant-numeric:tabular-nums}}
.rot{{font:600 12px/1.2 var(--met);letter-spacing:.14em;text-transform:uppercase}}
.rot::before{{content:"";display:inline-block;width:.5em;height:.5em;margin-right:.75em;border:.16em solid currentColor;border-radius:50%;vertical-align:.1em}}
.afeto{{font-family:var(--voz);font-style:italic;font-weight:400}}
/* hero */
.hero{{background:var(--hero);color:var(--hero-t);padding-block:48px 56px;padding-inline:max(16px,calc((100vw - 1180px)/2))}}
.hero-top{{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;color:#C6A15E}}
.assinatura{{display:block;width:min(100%,760px);height:auto;margin:56px 0 40px;overflow:visible}}
#a-plq{{transform-box:view-box;transform-origin:{PIV[0]:.2f}px {PIV[1]:.2f}px;animation:entra 1.6s var(--firme) both,balanca 1.4s .25s both}}
#a-clara{{animation:sobe .72s 1.05s var(--firme) both}} #a-tia{{animation:gesto .72s 1.25s var(--firme) both}} #a-desc{{animation:aparece .72s 1.55s var(--firme) both}}
@keyframes entra{{from{{opacity:.001;translate:0 -26px}}}} @keyframes balanca{{0%{{rotate:-9deg}}30%{{rotate:6deg}}55%{{rotate:-3deg}}78%{{rotate:1.2deg}}100%{{rotate:0deg}}}}
@keyframes sobe{{from{{opacity:.001;translate:0 14px}}}} @keyframes gesto{{from{{opacity:.001;translate:-10px 0}}}} @keyframes aparece{{from{{opacity:.001}}}}
.hero-bottom{{display:flex;justify-content:space-between;align-items:end;gap:24px;flex-wrap:wrap}}
.hero h1{{font-size:clamp(40px,6vw,76px);font-weight:500;font-style:italic;line-height:1.02}}
.hero p.meta{{color:#DDE1D4;max-width:34ch}}
.btn{{font:600 13px var(--met);letter-spacing:.12em;text-transform:uppercase;color:inherit;background:none;border:1px solid currentColor;border-radius:999px;padding:12px 18px;cursor:pointer;opacity:.85}}
.btn:focus-visible,a:focus-visible{{outline:2px solid var(--destaque);outline-offset:3px}}
/* estrutura */
.wrap{{display:grid;grid-template-columns:220px minmax(0,1fr);gap:56px;max-width:1180px;margin:0 auto;padding-inline:16px;padding-block:56px 96px}}
.toc{{position:sticky;top:calc(env(safe-area-inset-top,0px) + 24px);align-self:start}}
.toc ol{{list-style:none;padding:0;margin:12px 0 0;display:grid;gap:2px}}
.toc a{{display:flex;gap:12px;text-decoration:none;padding:6px 0;font-size:15px;color:var(--mudo);border-bottom:1px solid transparent}}
.toc a:hover{{color:var(--tinta)}} .toc .n{{font-variant-numeric:tabular-nums;color:var(--destaque);font-weight:600;width:22px}}
main{{display:grid;gap:112px;min-width:0}}
section{{display:grid;gap:32px;scroll-margin-top:24px}}
.cap{{display:grid;gap:14px;border-top:2px solid var(--tinta);padding-top:20px}}
.cap-n{{font:600 14px var(--met);color:var(--destaque);font-variant-numeric:tabular-nums;letter-spacing:.1em}}
.cap h2{{font-size:clamp(32px,4.4vw,48px)}}
.lead{{font-size:20px;line-height:1.5;color:var(--mudo);max-width:62ch}}
h3{{font-size:24px}}
.prosa{{max-width:66ch;display:grid;gap:14px}}
.grid2{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:20px}}
.grid3{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:20px}}
.bloco{{background:var(--sup);border-radius:12px;padding:24px;display:grid;gap:10px;align-content:start}}
.bloco h3{{font-size:22px}} .bloco p{{color:var(--mudo);font-size:16px}}
.citacao{{font-family:var(--voz);font-size:clamp(26px,3.4vw,38px);line-height:1.2;font-weight:500;max-width:28ch}}
table{{border-collapse:collapse;width:100%;font-size:15px}} .tbl{{overflow-x:auto}}
th,td{{text-align:left;vertical-align:top;padding:12px 14px 12px 0;border-bottom:1px solid var(--linha)}}
th{{font:600 12px var(--met);letter-spacing:.12em;text-transform:uppercase;color:var(--mudo)}}
td:first-child{{font-weight:600}}
.tile{{border-radius:12px;padding:32px;display:grid;place-items:center;min-height:180px}}
.t-linho{{background:#F4EEE3}} .t-pinho{{background:#1E3B33}} .t-branco{{background:#fff}} .t-preto{{background:#000}} .t-papel{{background:#FBF8F2}}
.tile img{{max-height:120px;width:auto}}
.tile.l img{{max-height:none;width:100%;max-width:520px}}
.leg{{font-size:14px;color:var(--mudo);margin-top:8px}}
figure{{margin:0}} img{{max-width:100%;height:auto;display:block}}
.fig{{border-radius:12px;overflow:hidden;border:1px solid var(--linha)}}
.diagrama{{width:100%;height:auto;max-height:420px}} .cota text{{font:500 6px var(--met)}} .cota-g text{{font:600 14px var(--met)}}
.sws{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,200px),1fr));gap:20px}}
.sw-c{{aspect-ratio:1.35;border-radius:12px;padding:16px;display:flex;flex-direction:column;justify-content:flex-end;gap:2px;border:1px solid var(--linha)}}
.sw-c span{{font:600 18px var(--voz)}} .sw figcaption{{font-size:14px;margin-top:10px;display:grid;gap:4px}} .sw small{{color:var(--mudo);font-variant-numeric:tabular-nums}}
.prop{{display:flex;height:56px;border-radius:12px;overflow:hidden;border:1px solid var(--linha)}}
.prop div{{display:flex;align-items:flex-end;padding:8px 10px;font:600 12px var(--met)}}
.esp{{display:grid;gap:18px}} .esp .r{{display:grid;grid-template-columns:170px minmax(0,1fr);gap:20px;align-items:baseline;border-bottom:1px solid var(--linha);padding-bottom:18px}}
.esp .r small{{color:var(--mudo);font-size:13px;line-height:1.4}}
.icones{{display:flex;flex-wrap:wrap;gap:12px}} .icones div{{display:grid;justify-items:center;gap:8px;background:var(--sup);border-radius:12px;padding:18px 14px;width:104px;font-size:13px;color:var(--mudo)}} .icones svg{{color:var(--tinta)}}
.apps{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,240px),1fr));gap:24px}}
.app img{{border-radius:8px;border:1px solid var(--linha);width:100%}} .app figcaption{{font-size:14px;color:var(--mudo);margin-top:10px}} .app b{{color:var(--tinta);font-weight:600}}
.ok,.nao{{border-radius:12px;padding:20px;display:grid;gap:8px;background:var(--sup)}} .ok h3,.nao h3{{font:600 13px var(--met);letter-spacing:.12em;text-transform:uppercase}}
.ok h3{{color:var(--tinta)}} .nao h3{{color:var(--destaque)}} ul.l{{margin:0;padding-left:18px;display:grid;gap:6px;font-size:15px}}
.dont{{display:grid;gap:10px}} .dont .tile{{min-height:150px;position:relative;overflow:hidden}} .dont p{{font-size:14px;color:var(--mudo)}} .dont p b{{color:var(--destaque)}}
.textura{{background:#b89a72 url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='200'><filter id='n'><feTurbulence baseFrequency='.04' numOctaves='3' seed='4'/><feColorMatrix values='0 0 0 0 .5  0 0 0 0 .4  0 0 0 0 .28  0 0 0 1.3 -.2'/></filter><rect width='300' height='200' filter='url(%23n)'/></svg>") center/cover}}
.decide{{display:grid;gap:16px}} .decide .bloco{{border-left:0}} .tag{{display:inline-block;font:600 11px var(--met);letter-spacing:.12em;text-transform:uppercase;padding:5px 10px;border-radius:999px;background:var(--apoio);color:var(--tinta)}}
.tag.voce{{background:var(--destaque);color:var(--fundo)}}
.score{{display:grid;gap:10px}} .score .r{{display:grid;grid-template-columns:minmax(0,1fr) 120px 48px;gap:14px;align-items:center;font-size:15px}}
.bar{{height:8px;border-radius:999px;background:var(--apoio);overflow:hidden}} .bar i{{display:block;height:100%;background:var(--tinta)}}
.tabnum{{font-variant-numeric:tabular-nums;text-align:right;font-weight:600}}
footer{{border-top:1px solid var(--linha);padding-block:32px;padding-inline:16px;text-align:center;color:var(--mudo);font-size:14px}}
@media (max-width:860px){{.wrap{{grid-template-columns:minmax(0,1fr);gap:40px}} .toc{{position:static}} .toc ol{{grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}} main{{gap:80px}} .esp .r{{grid-template-columns:minmax(0,1fr)}}}}
@media (prefers-reduced-motion:reduce){{#a-plq,#a-clara,#a-tia,#a-desc{{animation:none}}}}
</style>

<header class="hero">
 <div class="hero-top"><span class="rot">Brand book · versão 1.0</span><span class="rot">Setembro 2026</span></div>
 {HERO_SVG}
 <div class="hero-bottom">
  <div style="display:grid;gap:14px"><h1>Pode deixar comigo.</h1><p class="meta">Identidade visual e manual de uso da Tia Clara, pet sitter &amp; dog walker. Guardiã na postura, Curadora no critério, Cuidadora no tom.</p></div>
  <button class="btn" id="rever" type="button">Rever animação</button>
 </div>
</header>

<div class="wrap">
<nav class="toc" aria-label="Capítulos"><span class="rot" style="color:var(--mudo)">Capítulos</span><ol>{TOC}</ol></nav>
<main>

<section id="decisoes">{cap('decisoes', 'O que foi decidido e o que é seu', 'Segui em modo autônomo. Estas são as escolhas que fiz, todas reversíveis, e as que só você pode tomar.')}
 <div class="grid2">
  <div class="bloco decide"><span class="tag">Decidido · reversível</span><h3>Hierarquia dos arquétipos</h3><p>Três arquétipos com o mesmo peso viram fantasia genérica. <b>Guardiã</b> lidera, <b>Curadora</b> apoia e <b>Cuidadora</b> dá a temperatura. Se a Cuidadora liderasse, a marca cairia no "boazinha".</p></div>
  <div class="bloco decide"><span class="tag">Decidido · reversível</span><h3>Território A: a plaquinha</h3><p>É o único que carrega os dois serviços (pet e casa), ocupa códigos livres na categoria e vira objeto físico. Do território B, entra a gramática do relatório.</p></div>
  <div class="bloco decide"><span class="tag">Decidido · reversível</span><h3>"Tia" em itálico, "Clara" firme</h3><p>O afeto fica no gesto e a firmeza no nome. Isso reduz o peso infantil de "tia" sem mudar o nome.</p></div>
  <div class="bloco decide"><span class="tag voce">Precisa de você</span><h3>O nome</h3><p>A pesquisa achou dois riscos: "tia + nome" é o padrão de creches e hotelzinhos, e Tia Clara é a personagem "adorável e desastrada" de <i>A Feiticeira</i>. A identidade foi feita para funcionar com o nome como está (recomendado). Se um dia quiser que "Clara" assuma sozinha, o símbolo C já está pronto para isso.</p></div>
  <div class="bloco decide"><span class="tag voce">Precisa de você</span><h3>O que você já faz</h3><p>Confirme quais protocolos você pratica: visita de apresentação, ficha do pet, chaves codificadas, relatório, contrato, seguro. A marca só pode prometer o que é verdade.</p></div>
  <div class="bloco decide"><span class="tag voce">Precisa de você</span><h3>Dados, fotos e INPI</h3><p>Cidade/bairro, telefone e perfil para os modelos; fotos reais dentro das regras; busca de anterioridade no INPI (classe 45) antes de imprimir em escala.</p></div>
 </div>
</section>

<section id="ideia">{cap('ideia', 'O nome abraça. A identidade garante.')}
 <div class="prosa"><p>"Tia" entrega proximidade antes de qualquer desenho. É a pessoa de confiança da família. Mas também carrega o código da escolinha, do diminutivo e da boazinha que faz favor.</p>
 <p>Por isso a identidade não adiciona doçura. Ela soma o que o nome não diz sozinho: <b>segurança e competência</b>. O afeto aparece no tom, na fotografia e nos detalhes, nunca na fofura.</p>
 <p>E o nome traz um presente: <b>Clara é clareza</b>. Protocolo, preço e relatório, tudo explícito.</p></div>
 <p class="citacao">A plaquinha é o objeto que o tutor entrega junto com o pet. O chaveiro, junto com a casa. Um só desenho para as duas guardas.</p>
</section>

<section id="posicionamento">{cap('posicionamento', 'Tudo em ordem enquanto você não está.', 'Para tutores que precisam se ausentar e não abrem mão de saber que está tudo bem, a Tia Clara cuida do pet e da casa com afeto e com método: cada visita segue um protocolo claro.')}
 <div class="grid2">
  <div class="bloco"><span class="rot">Segurança · Guardiã</span><h3>Sua casa e seu pet sob protocolo</h3><p>Chaves codificadas, peitoral e guia com trava, plano de emergência. Nunca prometer "risco zero".</p></div>
  <div class="bloco"><span class="rot">Rotina preservada · Curadora</span><h3>Ele fica no território dele</h3><p>Ficha do pet e visita de apresentação. Nenhuma promessa de saúde.</p></div>
  <div class="bloco"><span class="rot">Clareza · Clara</span><h3>Você sabe de tudo</h3><p>Relatório de cada visita com horário, foto e observação.</p></div>
  <div class="bloco"><span class="rot">Afeto com método · Cuidadora</span><h3>Carinho de verdade, com critério</h3><p>Sempre a mesma pessoa, que conhece o pet pelo nome e pelas manias.</p></div>
 </div>
 <div class="tbl"><table><thead><tr><th>A Tia Clara nunca pode parecer…</th><th>Por quê</th></tr></thead><tbody>
  <tr><td>loja de brinquedo ou festa infantil</td><td>Patinhas, ossinhos e cores de doce são o template da categoria</td></tr>
  <tr><td>a vizinha boazinha que faz favor</td><td>É profissional, com processo e preço</td></tr>
  <tr><td>clínica veterinária</td><td>Cruz, estetoscópio, turquesa e termos clínicos confundem o papel dela</td></tr>
  <tr><td>segurança privada</td><td>Escudo e tom de ameaça vendem medo, não confiança</td></tr>
  <tr><td>aplicativo de plataforma</td><td>O diferencial estrutural é ser sempre a mesma pessoa</td></tr>
  <tr><td>"mãe de pet" melosa</td><td>Afeto adulto: o detalhe específico, não o diminutivo</td></tr></tbody></table></div>
</section>

<section id="arquetipos">{cap('arquetipos', 'Guardiã na postura. Curadora no critério. Cuidadora no tom.')}
 <div class="tbl"><table><thead><tr><th></th><th>Guardiã · primário</th><th>Curadora · secundário</th><th>Cuidadora · temperatura</th></tr></thead><tbody>
 <tr><td>Motivação</td><td>Proteger o que é precioso para o outro</td><td>Saber o que é melhor para cada pet</td><td>Fazer o outro se sentir acolhido</td></tr>
 <tr><td>No seu melhor</td><td>Vigilante, firme, calma sob pressão</td><td>Criteriosa, observadora, organizada</td><td>Presente, gentil, atenta</td></tr>
 <tr><td>Sombra</td><td>Controladora, alarmista, fria</td><td>Professoral, pseudo-veterinária</td><td>Boazinha, melosa, infantil</td></tr>
 <tr><td>No visual</td><td>Forma cheia e estável, contraste alto</td><td>Grid, registros, horários, check</td><td>Itálico, luz natural, Argila pontual</td></tr></tbody></table></div>
</section>

<section id="logo">{cap('logo', 'A plaquinha', 'Plaquinha de identificação + furo + C. Da pesquisa até o mestre: 12 rotas, 6 pré-selecionadas, 3 famílias, 1 mestre. Tudo em vetor, com o texto convertido em curvas.')}
 <div class="grid2">
  <div class="tile t-linho l"><img src="{A}tc-assinatura-horizontal.svg" alt="Assinatura horizontal" width="645" height="178"></div>
  <div class="tile t-pinho l"><img src="{A}tc-assinatura-vertical-linho.svg" alt="Assinatura vertical em Linho sobre Pinho" style="max-width:320px" width="509" height="360"></div>
 </div>
 <div class="grid2" style="align-items:center">
  <figure>{CONSTR}<figcaption class="leg">Construção. O C fica 1 u abaixo e 2,6 u à direita do centro da área útil: o C é aberto à direita e pesa à esquerda. <b>Dupla leitura intencional:</b> o furo e o C também formam uma figura com cabeça e braços que envolvem.</figcaption></figure>
  <div class="prosa"><h3>Logotipo</h3><p>"<i>Tia</i>" em Literata Itálico 500 é o gesto. "<b>Clara</b>" em Literata 680 é a firmeza. O pingo do i vira <b>argola</b>, o mesmo anel do furo da plaquinha, e é o único detalhe customizado. O descritor PET SITTER &amp; DOG WALKER vai em Instrument Sans, com espaçamento aberto.</p>
  <div class="tile t-papel" style="min-height:0;padding:24px"><img src="{A}tc-logotipo.svg" alt="Logotipo" style="max-height:none;width:100%;max-width:420px" width="560" height="175"></div></div>
 </div>
 <h3>Versões</h3>
 <div class="grid3">
  <figure><div class="tile t-linho"><img src="{A}tc-simbolo.svg" alt="Símbolo Pinho" width="150" height="162"></div><figcaption class="leg">Símbolo · Pinho</figcaption></figure>
  <figure><div class="tile t-pinho"><img src="{A}tc-simbolo-latao.svg" alt="Símbolo Latão" width="150" height="162"></div><figcaption class="leg">Símbolo · Latão sobre Pinho</figcaption></figure>
  <figure><div class="tile t-branco"><img src="{A}tc-assinatura-horizontal-preto.svg" alt="Preto" style="max-height:none;width:100%" width="645" height="178"></div><figcaption class="leg">1 cor · preto</figcaption></figure>
  <figure><div class="tile t-preto"><img src="{A}tc-assinatura-horizontal-branco.svg" alt="Branco" style="max-height:none;width:100%" width="645" height="178"></div><figcaption class="leg">1 cor · negativo</figcaption></figure>
  <figure><div class="tile t-linho"><img src="{A}tc-assinatura-horizontal-compacta.svg" alt="Compacta" style="max-height:none;width:100%" width="590" height="129"></div><figcaption class="leg">Horizontal compacta · abaixo de 60 px de altura</figcaption></figure>
  <figure><div class="tile t-papel" style="gap:14px;grid-auto-flow:column"><img src="{A}tc-avatar.svg" alt="Avatar" style="border-radius:50%;width:96px" width="96" height="96"><img src="{A}tc-app-icon.svg" alt="Ícone de app" style="border-radius:14px;width:64px" width="64" height="64"><img src="{A}tc-favicon.svg" alt="Favicon" style="width:32px" width="32" height="32"></div><figcaption class="leg">Avatar circular · ícone de app · favicon</figcaption></figure>
 </div>
 <div class="grid2" style="align-items:center">
  <figure>{PROT}<figcaption class="leg">Área de proteção: <b>x = ¼ da largura da plaquinha</b>, livre em todos os lados.</figcaption></figure>
  <div class="tbl"><table><thead><tr><th>Peça</th><th>Mínimo digital</th><th>Impresso</th></tr></thead><tbody>
   <tr><td>Horizontal c/ descritor</td><td>60 px de altura</td><td>18 mm</td></tr><tr><td>Horizontal compacta</td><td>24 px de altura</td><td>8 mm</td></tr>
   <tr><td>Vertical c/ descritor</td><td>140 px de largura</td><td>35 mm</td></tr><tr><td>Símbolo</td><td>32 px</td><td>8 mm</td></tr><tr><td>Símbolo compacto</td><td>16 px</td><td>5 mm</td></tr></tbody></table></div>
 </div>
 <figure><img class="fig" src="{A}teste-L1.png" alt="Folha de testes de reprodução do logo" loading="lazy" width="1600" height="922"><figcaption class="leg">Gate L1: 16–32 px, 1 cor, escala de cinza, tela ruim, avatar circular, cabeçalho, coluna estreita e fundo carregado. Todos aprovados.</figcaption></figure>
 <details><summary class="rot" style="cursor:pointer;padding:8px 0">Como chegamos aqui: exploração e territórios</summary>
  <div style="display:grid;gap:20px;margin-top:16px">
   <img class="fig" src="{A}exploracao-12-rotas.png" alt="12 rotas de símbolo" loading="lazy" width="1000" height="840">
   <img class="fig" src="{A}territorio-A-plaquinha.png" alt="Território A" loading="lazy" width="1400" height="875">
   <img class="fig" src="{A}territorio-B-afeto-com-metodo.png" alt="Território B" loading="lazy" width="1400" height="875">
   <img class="fig" src="{A}territorio-C-passeio.png" alt="Território C" loading="lazy" width="1400" height="875">
  </div></details>
</section>

<section id="cor">{cap('cor', 'Profunda e terrosa. O Pinho lidera.', 'A categoria fala rosa, turquesa e laranja-doce; a veterinária, azul e branco. A Tia Clara fala pinho, linho, latão e argila. Os números são o contraste com o texto (WCAG).')}
 <div class="sws">{SWATCHES}</div>
 <div><div class="prop" aria-label="Proporção de uso"><div style="flex:60;background:#F4EEE3;color:#1E3B33">Linho/Papel 60</div><div style="flex:25;background:#1E3B33;color:#F4EEE3">Pinho 25</div><div style="flex:10;background:#DDE1D4;color:#1E3B33">Sálvia 10</div><div style="flex:5;background:#A94E2A"></div></div>
 <p class="leg">Proporção. Os 5% finais são <b>um</b> acento por peça: Argila (calor, CTA) <b>ou</b> Latão (protocolo, sobre Pinho).</p></div>
 <div class="grid2"><div class="nao"><h3>Proibido</h3><ul class="l"><li>Azul-hospital, turquesa, verde-menta, vermelho de alarme</li><li>Rosa, lilás, azul-bebê</li><li>Gradiente, neon, brilho</li><li>Latão em texto sobre fundo claro (2,1:1)</li></ul></div>
 <div class="ok"><h3>Modo escuro</h3><ul class="l"><li>Fundo Pinho Profundo, superfície Pinho</li><li>Texto Linho, secundário Sálvia</li><li>Destaque Argila Clara <code>#E7B89A</code></li><li>Metal: Latão</li></ul></div></div>
</section>

<section id="tipografia">{cap('tipografia', 'Duas vozes: a serifa fala, a grotesca organiza.', 'Literata é a voz; o itálico é o afeto, no máximo uma vez por peça. Instrument Sans é o método: texto, rótulos, horários. As duas são livres (OFL) e estão no Google Fonts.')}
 <div class="esp">
  <div class="r"><small>Display · Literata 600<br>56 / 1,05</small><span style="font:600 clamp(36px,5vw,56px)/1.05 var(--voz);font-variation-settings:'opsz' 72">Pode deixar comigo.</span></div>
  <div class="r"><small>Título · Literata 600<br>30 / 1,15</small><span style="font:600 30px/1.15 var(--voz)">Sua chave nunca sai com o seu endereço.</span></div>
  <div class="r"><small>Afeto · Literata Itálico 400<br>22 / 1,4 · 1 por peça</small><span class="afeto" style="font-size:24px">Tudo certo por aqui.</span></div>
  <div class="r"><small>Corpo · Instrument Sans 400<br>17 / 1,55</small><span style="max-width:58ch">Antes do primeiro serviço, eu conheço o pet, a casa e a rotina. Saio da visita de apresentação com a ficha preenchida.</span></div>
  <div class="r"><small>Rótulo · Instrument Sans 600<br>12 · +0,14em · com argola</small><span class="rot">Protocolo de chaves</span></div>
  <div class="r"><small>Dado · Instrument Sans 500<br>algarismos tabulares</small><span style="font:500 17px var(--met);font-variant-numeric:tabular-nums">08:02 entrada · 08:12 passeio 40 min · 09:04 saída</span></div>
 </div>
 <p class="leg">Social (tela de 1080 px de largura): display 112 · título 76 · subtítulo 48 · corpo 36 · rótulo 28. <b>Nada abaixo de 28 px.</b></p>
</section>

<section id="composicao">{cap('composicao', 'Uma mensagem por peça.')}
 <div class="grid3">
  <div class="bloco"><span class="rot">Instagram 1080×1350</span><p>Margem 72–96 · 6 colunas · calha 24. Alinhado à esquerda. Centralizado só em capa e fecho.</p></div>
  <div class="bloco"><span class="rot">Stories 1080×1920</span><p>Margem lateral 72 · zona segura: 250 px no topo, 340 px na base. Nada importante fora dela.</p></div>
  <div class="bloco"><span class="rot">Web</span><p>12 colunas · máx. 1200 · calha 24 · margem 16 no celular. Medida máxima de 68 caracteres.</p></div>
 </div>
 <div class="grid2">
  <div class="bloco"><span class="rot">Moldura-plaquinha</span><p>Arco 100×112, usado para foto de pet e selo. Nunca em botão ou campo. Em CSS: <code>border-radius: 50% 50% 22% 22% / 44.6% 44.6% 19.6% 19.6%</code>.</p></div>
  <div class="bloco"><span class="rot">Sem sombra</span><p>A elevação vem da cor (Papel sobre Linho). Raios: 6 campos · 12 cartões · 20 painéis · pílula nos botões.</p></div>
 </div>
</section>

<section id="imagem">{cap('imagem', 'Fotografia documental. Sem mascote, sem patinha.', 'O pet na casa dele, na altura dos olhos, com luz de janela. As mãos da Clara fazendo certo: ajustando o peitoral, enchendo o pote, segurando a guia.')}
 <div class="grid2">
  <div class="ok"><h3>Faça</h3><ul class="l"><li>Pet no território dele, na rotina dele</li><li>Luz natural, cor neutra-quente</li><li>Detalhes de rotina: pote, guia no gancho, chaveiro codificado</li><li>Passeio em lugar genérico: praça, calçada arborizada</li></ul></div>
  <div class="nao"><h3>Não faça</h3><ul class="l"><li>Banco de imagem de "cão pulando feliz"</li><li>Pet fantasiado, filtro pesado, flash</li><li>Ambiente de clínica, jaleco, maca</li><li><b>Fachada, número, portão, placa de rua</b></li></ul></div>
 </div>
 <div class="bloco"><span class="rot">Protocolo de privacidade</span><p>A Guardiã também está no conteúdo:</p><ul class="l"><li>publique <b>depois</b> do serviço;</li><li>nunca diga em tempo real que o tutor está fora;</li><li>não geolocalize;</li><li>chave só aparece em chaveiro codificado;</li><li>peça autorização de imagem ao tutor.</li></ul></div>
 <h3>Ícones</h3>
 <div class="icones">{''.join(f'<div>{ic(n,32)}<span>{t}</span></div>' for n,t in [('chave','Pet sitting'),('guia','Passeio'),('relogio','Rotina'),('prancheta','Relatório'),('calendario','Agenda'),('camera','Fotos'),('casa','Domicílio'),('plaquinha','Identificação'),('balao','Contato')])}</div>
 <p class="leg">Linear, 1,5 px, grade 24, cantos arredondados, no máximo 3 formas. <b>A argola ◦ substitui a patinha</b> em todas as funções em que o mercado usaria uma. Proibidos: patinha, osso, coração, cruz, estetoscópio, pílula, escudo.</p>
</section>

<section id="movimento">{cap('movimento', 'O balanço que assenta.', 'Firme, calma, precisa, acolhedora. A plaquinha entra pendurada pelo furo, balança e para. Inquietação que vira calma, como o tutor ao receber o relatório.')}
 <figure><img class="fig" src="{A}storyboard-logo.png" alt="Quadros-chave da assinatura animada" loading="lazy" width="1596" height="334"><figcaption class="leg">Quadros-chave. A versão ao vivo está no topo desta página: toque em "Rever animação".</figcaption></figure>
 <div class="tbl"><table><thead><tr><th>Token</th><th>Valor</th><th>Uso</th></tr></thead><tbody>
  <tr><td>micro</td><td><code>160 ms</code></td><td>Estados, checks</td></tr><tr><td>padrão</td><td><code>320 ms</code></td><td>Texto e blocos</td></tr>
  <tr><td>ênfase</td><td><code>720 ms</code></td><td>Título, logotipo</td></tr><tr><td>assentar</td><td><code>1400 ms</code></td><td>Só a plaquinha</td></tr>
  <tr><td>curva firme</td><td><code>cubic-bezier(.2,0,0,1)</code></td><td>Padrão: sai decidida, chega suave</td></tr></tbody></table></div>
 <p class="leg">Em vídeo, o primeiro 1–2 s é uma âncora estável, com fundo fixo. Legenda em Instrument Sans 600, 44–52 px. Som opcional: um "tlim" de latão quando a plaquinha para. Nunca latido nem efeito cartoon.</p>
</section>

<section id="voz">{cap('voz', 'Firme e gentil. Afeto adulto.')}
 <div class="grid2">
  <div class="bloco"><span class="rot">Princípios</span><ul class="l"><li><b>Firme e gentil:</b> frases curtas e afirmativas.</li><li><b>Clara:</b> sem letras miúdas.</li><li><b>Afeto no detalhe</b> ("o Thor só come depois do passeio"), não no diminutivo. No máximo 1 por peça.</li><li><b>Não é veterinária:</b> "rotina", "bem-estar", "cuidado". Nunca "tratamento" ou "diagnóstico".</li></ul></div>
  <div class="bloco"><span class="rot">Frases da marca</span><ul class="l"><li><b>Pode deixar comigo.</b> · assinatura</li><li><i>Tudo certo por aqui.</i> · fecho de relatório</li><li>Tudo em ordem enquanto você não está.</li><li>Sua chave nunca sai com o seu endereço.</li><li>Administro a medicação prescrita pelo veterinário de vocês.</li></ul></div>
 </div>
 <p class="leg"><b style="color:var(--destaque)">Evitar:</b> "aumigos", "filho de quatro patas", "mãe de pet", "fofurices", "risco zero", "100% seguro", "cuido como se fosse meu".</p>
</section>

<section id="aplicacoes">{cap('aplicacoes', 'O sistema em uso', 'Os modelos editáveis estão em 07-producao/modelos. As fotos são marcadores com a descrição da foto certa.')}
 <div class="apps">{PRODG}</div>
 <div class="grid2">
  <figure class="app"><img src="{A}prod-story-01-tudo-certo.png" alt="Story" loading="lazy" width="720" height="1280" style="max-width:280px"><figcaption><b>Story</b> · "tudo certo por aqui", publicado depois do serviço</figcaption></figure>
  <figure class="app"><img src="{A}prod-reel-01-capa.png" alt="Capa de reel" loading="lazy" width="720" height="1280" style="max-width:280px"><figcaption><b>Capa de reel</b> · título dentro da zona segura</figcaption></figure>
 </div>
 <figure class="app"><img src="{A}prod-objetos-plaquinha-chaveiro.png" alt="Plaquinha de passeio e chaveiro codificado" loading="lazy" width="1440" height="810"><figcaption><b>Objetos</b> · plaquinha de passeio em latão (vai presa ao peitoral) e chaveiro codificado. A marca vira protocolo.</figcaption></figure>
 <div class="grid2">
  <figure class="app"><img src="{A}prod-cartao-frente.png" alt="Cartão frente" loading="lazy" width="720" height="400"><figcaption><b>Cartão</b> · frente Pinho, símbolo em latão (hot stamping)</figcaption></figure>
  <figure class="app"><img src="{A}prod-cartao-verso.png" alt="Cartão verso" loading="lazy" width="720" height="400"><figcaption><b>Cartão</b> · verso</figcaption></figure>
 </div>
 <figure class="app"><img src="{A}prod-site-home-desktop.png" alt="Site, primeira dobra" loading="lazy" width="1440" height="900"><figcaption><b>Site</b> · primeira dobra, com CTA em Argila e cartão de relatório como prova</figcaption></figure>
 <figure class="app"><img src="{A}prod-destaques-folha.png" alt="Capas de destaque" loading="lazy" width="720" height="198"><figcaption><b>Capas de destaque</b> · Serviços, Relatórios, Protocolos, Passeios, Agenda</figcaption></figure>
</section>

<section id="faca">{cap('faca', 'Faça / não faça')}
 <div class="grid3">
  <div class="dont"><div class="tile t-linho"><img src="{A}tc-assinatura-horizontal.svg" alt="" style="max-height:none;width:80%;transform:scaleX(1.35)"></div><p><b>✗ Esticar</b> ou comprimir</p></div>
  <div class="dont"><div class="tile t-linho"><img src="{A}tc-simbolo.svg" alt="" style="transform:rotate(-14deg)"></div><p><b>✗ Girar</b>: a plaquinha só balança na animação</p></div>
  <div class="dont"><div class="tile t-pinho"><img src="{A}tc-simbolo-argila.svg" alt=""></div><p><b>✗ Argila sobre Pinho</b>: vibra e perde contraste</p></div>
  <div class="dont"><div class="tile t-linho"><img src="{A}tc-simbolo.svg" alt="" style="filter:drop-shadow(6px 8px 6px rgb(0 0 0/.45))"></div><p><b>✗ Sombra</b>, contorno, brilho ou gradiente</p></div>
  <div class="dont"><div class="tile textura"><img src="{A}tc-assinatura-horizontal.svg" alt="" style="max-height:none;width:88%"></div><p><b>✗ Direto sobre foto</b> ou textura. Use uma placa Linho com 1x de margem</p></div>
  <div class="dont"><div class="tile t-linho"><span style="font:680 clamp(28px,4vw,40px) var(--voz);color:#1E3B33">Tia Clara</span></div><p><b>✗ Redigitar o logo</b> ou deixar "Tia" e "Clara" no mesmo estilo</p></div>
 </div>
 <div class="grid2"><div class="ok"><h3>Faça</h3><ul class="l"><li>Use os arquivos mestres (SVG) e as versões compactas nos tamanhos pequenos</li><li>Um acento por peça</li><li>Relatório ao fim de cada visita, fechando com "Tudo certo por aqui."</li><li>Foto real, depois do serviço</li></ul></div>
 <div class="nao"><h3>Não faça</h3><ul class="l"><li>Patinha no lugar da argola</li><li>Plaquinha sem o furo: vira lápide</li><li>Mais de 2 famílias tipográficas</li><li>Texto abaixo de 28 px em peça de 1080</li></ul></div></div>
</section>

<section id="arquivos">{cap('arquivos', 'Onde está cada coisa', 'Pasta tia-clara/ no repositório. Tudo é regenerável por script a partir de _fonte/.')}
 <div class="tbl"><table><thead><tr><th>Pasta</th><th>Conteúdo</th></tr></thead><tbody>
  <tr><td>00-brief</td><td>Briefing estruturado (JSON)</td></tr><tr><td>01-estrategia</td><td>Estratégia: posicionamento, arquétipos, pilares, anti-posicionamento</td></tr>
  <tr><td>02-inteligencia-visual</td><td>Mapa da categoria, códigos, espaço em branco, riscos</td></tr><tr><td>03-territorios</td><td>3 territórios e a decisão</td></tr>
  <tr><td>04-logo/master</td><td>36 SVGs mestres: assinaturas, compactas, símbolo, logotipo, avatar, favicon, ícone de app</td></tr>
  <tr><td>04-logo/png</td><td>105 PNGs transparentes + favicon.ico</td></tr><tr><td>04-logo/testes</td><td>Folha de testes de reprodução</td></tr>
  <tr><td>05-design-system</td><td>tokens.json (W3C), tokens.css, fontes (OFL), guia do sistema</td></tr>
  <tr><td>06-motion</td><td>Assinatura animada (HTML + vídeo), storyboard, regras</td></tr>
  <tr><td>07-producao</td><td>21 modelos HTML + PNG: posts, carrossel, stories, reel, relatório, destaques, cartão, objetos, site</td></tr>
  <tr><td>09-qa</td><td>QA e riscos abertos</td></tr><tr><td>_fonte</td><td>Scripts: marca.py, exportar.js, producao.py, motion.py, brandbook.py</td></tr></tbody></table></div>
</section>

<section id="qa">{cap('qa', 'QA: 88/100, sem falha crítica', 'A nota orienta, mas quem decide são as falhas críticas: nenhuma. Os riscos abertos não bloqueiam o uso.')}
 <div class="score">{''.join(f'<div class="r"><span>{n}</span><div class="bar"><i style="width:{v/p*100:.0f}%"></i></div><span class="tabnum">{v}/{p}</span></div>' for n,v,p in [('Relevância estratégica',18,20),('Distinção',16,20),('Reprodutibilidade',14,15),('Escala entre canais',14,15),('Legibilidade e acessibilidade',9,10),('Coerência do sistema',9,10),('Movimento e digital',8,10)])}</div>
 <div class="bloco"><span class="rot">Riscos abertos</span><ul class="l"><li>O nome e o registro "tia de creche": decisão sua</li><li>Busca no INPI antes de imprimir em escala</li><li>Fotografia real ainda não produzida</li><li>Confirmar os protocolos praticados e a estatística dos 83% na fonte</li><li>Recriar o relatório no Canva para o uso diário</li></ul></div>
</section>

</main></div>
<footer>Tia Clara · Pet Sitter &amp; Dog Walker · Brand book v1.0 · Literata e Instrument Sans (SIL Open Font License)</footer>
<script>
document.getElementById('rever').addEventListener('click',()=>{{document.querySelectorAll('.assinatura g').forEach(g=>{{g.style.animation='none';void g.getBoundingClientRect();g.style.animation=''}})}});
</script>
'''

def gerar():
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, 'brand-book.html'), 'w').write(BODY)
    # versão local: fontes do próprio repositório (funciona offline)
    local = ('@font-face{font-family:"Literata";src:url("../05-design-system/fontes/Literata[opsz,wght].ttf");font-weight:200 900}'
             '@font-face{font-family:"Literata";font-style:italic;src:url("../05-design-system/fontes/Literata-Italic[opsz,wght].ttf");font-weight:200 900}'
             '@font-face{font-family:"Instrument Sans";src:url("../05-design-system/fontes/InstrumentSans[wdth,wght].ttf");font-weight:400 700}')
    open(os.path.join(OUT, 'index.html'), 'w').write('<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
        + BODY.replace('\n<style>', '\n<style>' + local, 1) + '\n</html>\n')
    print('ok', len(BODY) // 1024, 'KB')

if __name__ == '__main__':
    gerar()
