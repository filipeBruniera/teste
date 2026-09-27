"""Gera os modelos de produção (HTML) em 07-producao/modelos. Renderize com _fonte/renderizar-producao.js."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import marca as mc
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RAIZ, '07-producao', 'modelos')
LOGO = '../../04-logo/master/'

ICON = {  # grade 24, traço 1.5, sem preenchimento
 'chave': '<circle cx="8" cy="12" r="4"/><path d="M12 12h8.5M17.5 12v3M20.5 12v2.2"/>',
 'guia': '<circle cx="7" cy="6.5" r="3.2"/><path d="M9.3 8.8c2.6 2.4 4.9 4.9 7.2 7.4"/><rect x="15.4" y="15.6" width="4.4" height="5.6" rx="1.6" transform="rotate(-42 17.6 18.4)"/>',
 'relogio': '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
 'prancheta': '<rect x="5" y="4.5" width="14" height="16" rx="2"/><path d="M9 4.5V3h6v1.5M9 13l2 2 4-4"/>',
 'calendario': '<rect x="4" y="5.5" width="16" height="14" rx="2"/><path d="M4 10h16M8 3.5v4M16 3.5v4"/>',
 'camera': '<rect x="3.5" y="7" width="17" height="12" rx="2"/><circle cx="12" cy="13" r="3.2"/><path d="M9 7l1.4-2.3h3.2L15 7"/>',
 'casa': '<path d="M4 11l8-6.5 8 6.5M6.5 9.5V19.5h11V9.5"/>',
 'plaquinha': '<path d="M6 10a6 6 0 0 1 12 0v8a2.5 2.5 0 0 1-2.5 2.5h-7A2.5 2.5 0 0 1 6 18z"/><circle cx="12" cy="8.2" r="1.3"/>',
 'balao': '<path d="M5 5.5h14a1.5 1.5 0 0 1 1.5 1.5v8.5A1.5 1.5 0 0 1 19 17H10l-4.5 3.5V17H5a1.5 1.5 0 0 1-1.5-1.5V7A1.5 1.5 0 0 1 5 5.5z"/>',
 'check': '<path d="M5 12.5l4.2 4.2L19 7"/>',
}
def ic(nome, tam=24, cor='currentColor', traco=1.5):
    return f'<svg class="ic" width="{tam}" height="{tam}" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="{traco}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[nome]}</svg>'

BASE = '''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<link rel="stylesheet" href="../../05-design-system/tokens.css">
<style>
*{box-sizing:border-box;margin:0}
body{width:%(w)dpx;height:%(h)dpx;overflow:hidden;background:var(--tc-linho);color:var(--tc-pinho);font-family:var(--tc-fonte-metodo);-webkit-font-smoothing:antialiased}
.voz{font-family:var(--tc-fonte-voz);font-weight:600;font-variation-settings:'opsz' 72;letter-spacing:-.01em}
.afeto{font-family:var(--tc-fonte-voz);font-style:italic;font-weight:400}
.rot{font-weight:600;letter-spacing:.14em;text-transform:uppercase}
.rot::before{content:"";display:inline-block;width:.5em;height:.5em;margin-right:.75em;border:.16em solid currentColor;border-radius:50%%;vertical-align:.1em}
.tab{font-variant-numeric:tabular-nums}
.foto{background:var(--tc-salvia) repeating-linear-gradient(135deg,transparent 0 22px,rgb(30 59 51/.07) 22px 24px);display:flex;align-items:flex-end;padding:28px;color:var(--tc-musgo);font-weight:600;letter-spacing:.1em;text-transform:uppercase}
.plq{border-radius:50%% 50%% 22%% 22%% / 44.6%% 44.6%% 19.6%% 19.6%%;aspect-ratio:100/112;overflow:hidden}
.ic{flex:none}
%(css)s
</style></head><body>%(body)s</body></html>'''

def pagina(nome, w, h, body, css=''):
    open(os.path.join(OUT, nome + '.html'), 'w').write(BASE % dict(w=w, h=h, body=body, css=css))
    return nome, w, h

M = []  # (nome, w, h)

# 1 · Autoridade / protocolo — IG 1080x1350
M.append(pagina('ig-01-autoridade-protocolo', 1080, 1350, f'''
<div style="background:var(--tc-pinho);color:var(--tc-linho);height:100%;padding:96px 88px 80px;display:flex;flex-direction:column">
 <div class="rot" style="font-size:28px;color:var(--tc-latao)">Protocolo de saída</div>
 <h1 class="voz" style="font-size:88px;line-height:1.04;margin:56px 0 72px">Antes de sair da sua casa, eu confiro três coisas.</h1>
 <div style="display:flex;flex-direction:column;gap:0;border-top:2px solid var(--tc-latao)">
  {''.join(f'<div style="display:flex;gap:36px;align-items:center;padding:34px 0;border-bottom:1px solid rgb(244 238 227/.18)"><span class="voz tab" style="font-size:44px;color:var(--tc-latao);width:56px">{n}</span><span style="font-size:40px;line-height:1.3">{t}</span></div>' for n,t in [('1','Janelas e portas travadas.'),('2','Água fresca e pote limpo.'),('3','Chave de volta ao chaveiro codificado.')])}
 </div>
 <div style="margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end">
  <div class="afeto" style="font-size:40px">Pode deixar comigo.</div>
  <img src="{LOGO}tc-simbolo-latao.svg" style="height:112px">
 </div>
</div>'''))

# 2 · Prova de serviço — IG 1080x1350
M.append(pagina('ig-02-prova-de-servico', 1080, 1350, f'''
<div style="padding:80px 80px 72px;height:100%;display:flex;flex-direction:column">
 <div style="display:flex;justify-content:space-between;align-items:center"><div class="rot" style="font-size:28px">Relatório da semana</div><div class="tab" style="font-size:28px;color:var(--tc-musgo)">9 dias · 18 visitas</div></div>
 <div style="display:grid;grid-template-columns:470px 1fr;gap:56px;margin-top:64px;align-items:start">
  <div class="plq foto" style="font-size:22px;justify-content:center;text-align:center;align-items:center">foto · pet em casa<br>luz natural</div>
  <div style="padding-top:24px"><h2 class="voz" style="font-size:76px;line-height:1.05">Luna ficou no território dela.</h2>
  <p style="font-size:34px;line-height:1.45;margin-top:32px;color:var(--tc-musgo)">Gata, 11 anos. Nove dias de viagem da família, rotina intacta.</p></div>
 </div>
 <div style="margin-top:auto;background:var(--tc-papel);border-radius:20px;padding:40px 48px;display:grid;grid-template-columns:repeat(3,1fr);gap:24px">
  {''.join(f'<div><div class="voz tab" style="font-size:72px">{n}</div><div style="font-size:28px;color:var(--tc-musgo);margin-top:6px">{t}</div></div>' for n,t in [('18','relatórios enviados'),('2','visitas por dia'),('1','cuidadora, sempre a mesma')])}
 </div>
 <div style="display:flex;justify-content:space-between;align-items:center;margin-top:44px"><span class="afeto" style="font-size:36px">Tudo certo por aqui.</span><img src="{LOGO}tc-assinatura-horizontal-compacta.svg" style="height:52px"></div>
</div>'''))

# 3 · Carrossel educativo (3 lâminas)
M.append(pagina('ig-03a-carrossel-capa', 1080, 1350, f'''
<div style="height:100%;padding:96px 88px 80px;display:flex;flex-direction:column;background:var(--tc-linho)">
 <div class="rot" style="font-size:28px;color:var(--tc-argila)">Passo a passo</div>
 <h1 class="voz" style="font-size:112px;line-height:1.0;margin-top:48px">Como funciona a primeira visita.</h1>
 <p style="font-size:38px;line-height:1.4;margin-top:48px;color:var(--tc-musgo);max-width:780px">Antes de cuidar do seu pet, eu preciso conhecer a rotina dele. É assim que começa.</p>
 <div style="margin-top:auto;display:flex;justify-content:space-between;align-items:center"><img src="{LOGO}tc-assinatura-horizontal-compacta.svg" style="height:56px"><span class="rot" style="font-size:26px">Arraste →</span></div>
</div>'''))
M.append(pagina('ig-03b-carrossel-passo', 1080, 1350, f'''
<div style="height:100%;padding:96px 88px 80px;display:flex;flex-direction:column;background:var(--tc-papel)">
 <div style="display:flex;justify-content:space-between;align-items:center"><span class="voz tab" style="font-size:160px;line-height:.8;color:var(--tc-argila)">1</span>{ic('casa',120,'var(--tc-pinho)',1.3)}</div>
 <h2 class="voz" style="font-size:88px;line-height:1.05;margin-top:72px">Visita de apresentação</h2>
 <p style="font-size:38px;line-height:1.45;margin-top:40px;max-width:860px">Eu vou até a sua casa, conheço o pet, os cantos preferidos, os horários e as manias. Você me mostra tudo com calma.</p>
 <div style="margin-top:56px;background:var(--tc-linho);border-radius:20px;padding:36px 40px">
  <div class="rot" style="font-size:28px">Ficha do pet</div>
  {''.join(f'<div style="display:flex;justify-content:space-between;gap:24px;padding:16px 0;border-bottom:1px solid var(--tc-borda);font-size:30px"><span style="color:var(--tc-musgo)">{a}</span><span style="font-weight:600">{b}</span></div>' for a,b in [('Alimentação','2x ao dia · 1 medida'),('Passeio','manhã · 40 min'),('Medos','moto, fogos'),('Veterinário de confiança','do tutor · na ficha')])}
 </div>
 <div style="margin-top:auto;border-top:1px solid var(--tc-borda);padding-top:36px;display:flex;gap:18px;align-items:center;font-size:30px;color:var(--tc-musgo)">{ic('check',36,'var(--tc-pinho)',2)}Saio com a ficha do pet preenchida.</div>
</div>'''))
M.append(pagina('ig-03c-carrossel-fecho', 1080, 1350, f'''
<div style="height:100%;padding:96px 88px 80px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;background:var(--tc-pinho);color:var(--tc-linho)">
 <img src="{LOGO}tc-simbolo-linho.svg" style="height:200px">
 <h2 class="voz" style="font-size:104px;line-height:1.02;margin-top:64px">Pode deixar comigo.</h2>
 <p style="font-size:36px;line-height:1.45;margin-top:40px;color:var(--tc-salvia);max-width:760px">Agende a visita de apresentação pelo WhatsApp.</p>
 <div style="margin-top:64px;background:var(--tc-argila);color:var(--tc-linho);font-size:32px;font-weight:600;padding:26px 48px;border-radius:999px;display:flex;gap:16px;align-items:center">{ic('balao',36,'var(--tc-linho)',2)}Chamar no WhatsApp</div>
</div>'''))

# 4 · Estatística
M.append(pagina('ig-04-estatistica', 1080, 1350, f'''
<div style="height:100%;padding:96px 88px 80px;display:flex;flex-direction:column;background:var(--tc-salvia)">
 <div class="rot" style="font-size:28px">Você não é o único</div>
 <div class="voz tab" style="font-size:320px;line-height:.9;margin-top:72px;letter-spacing:-.03em">83%</div>
 <p class="voz" style="font-size:64px;line-height:1.12;margin-top:40px;font-weight:500">dos tutores se preocupam com o pet quando estão longe.</p>
 <p style="font-size:28px;margin-top:24px;color:var(--tc-musgo)">Fonte: pesquisa Rover, 2026.</p>
 <div style="margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;border-top:2px solid var(--tc-pinho);padding-top:36px">
  <p style="font-size:36px;line-height:1.35;max-width:640px">Por isso cada visita termina com um relatório: horário, fotos e o que aconteceu.</p>
  <img src="{LOGO}tc-simbolo.svg" style="height:120px">
 </div>
</div>'''))

# 5 · Anúncio
M.append(pagina('ig-05-anuncio-agenda', 1080, 1350, f'''
<div style="height:100%;padding:96px 88px 80px;display:flex;flex-direction:column">
 <div style="align-self:flex-start;background:var(--tc-argila);color:var(--tc-linho);border-radius:999px;padding:18px 32px" class="rot"><span style="font-size:28px">Agenda aberta</span></div>
 <h1 class="voz" style="font-size:108px;line-height:1.0;margin-top:64px">Férias de fim de ano.</h1>
 <p class="afeto" style="font-size:52px;margin-top:28px;color:var(--tc-argila)">Viaje. A rotina dele fica.</p>
 <div style="margin-top:72px;display:grid;grid-template-columns:1fr 1fr;gap:28px">
  {''.join(f'<div style="background:var(--tc-papel);border-radius:20px;padding:36px;display:flex;flex-direction:column;gap:18px">{ic(i,56,"var(--tc-pinho)",1.5)}<div class="voz" style="font-size:44px">{t}</div><div style="font-size:30px;line-height:1.35;color:var(--tc-musgo)">{d}</div></div>' for i,t,d in [('chave','Pet sitting','Visitas na sua casa, 1 ou 2 por dia.'),('guia','Passeios','Individuais, com peitoral e guia com trava.')])}
 </div>
 <div style="margin-top:auto;display:flex;justify-content:space-between;align-items:center"><span style="font-size:30px">Reservas por ordem de contato · <b>visita de apresentação antes</b></span></div>
 <img src="{LOGO}tc-assinatura-horizontal.svg" style="height:92px;margin-top:40px;align-self:flex-start">
</div>'''))

# 6 · Story — relatório do dia
M.append(pagina('story-01-tudo-certo', 1080, 1920, f'''
<div style="height:100%;padding:250px 72px 340px;display:flex;flex-direction:column;background:var(--tc-pinho);color:var(--tc-linho)">
 <div style="display:flex;align-items:center;gap:24px"><img src="{LOGO}tc-simbolo-linho.svg" style="height:84px"><div class="rot" style="font-size:28px;color:var(--tc-latao)">Relatório · 14:10</div></div>
 <div class="plq foto" style="width:640px;margin:72px auto 0;font-size:24px;align-items:center;justify-content:center;text-align:center">foto · o pet agora</div>
 <h1 class="afeto" style="font-size:104px;line-height:1.02;margin-top:72px;text-align:center">Tudo certo por aqui.</h1>
 <p class="tab" style="font-size:36px;text-align:center;margin-top:28px;color:var(--tc-salvia)">Thor · passeio de 40 min · água trocada</p>
</div>'''))

# 7 · Capa de reel
M.append(pagina('reel-01-capa', 1080, 1920, f'''
<div class="foto" style="position:absolute;inset:0;font-size:26px;align-items:flex-start;padding:280px 72px">vídeo · cão na guia, altura dos olhos, luz natural</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:980px;background:var(--tc-pinho);color:var(--tc-linho);padding:88px 72px 340px;display:flex;flex-direction:column;border-radius:48px 48px 0 0">
 <div class="rot" style="font-size:28px;color:var(--tc-latao)">Passeio · do começo ao fim</div>
 <h1 class="voz" style="font-size:104px;line-height:1.02;margin-top:40px">40 minutos com o Thor.</h1>
 <div style="margin-top:auto;display:flex;align-items:center;gap:22px"><img src="{LOGO}tc-simbolo-latao.svg" style="height:72px"><span style="font-size:32px;color:var(--tc-salvia)">Tia Clara · Pet Sitter &amp; Dog Walker</span></div>
</div>'''))

# 8 · Relatório de visita (WhatsApp) — peça-chave da Curadora
linhas = [('08:02','Entrada','','chave'),('08:05','Ração','1 medida, comeu tudo','check'),('08:07','Água','trocada, pote lavado','check'),('08:12','Passeio','40 min · praça','guia'),('08:54','Patas limpas','','check'),('09:04','Saída','chave no chaveiro TC-014','chave')]
M.append(pagina('relatorio-whatsapp', 1080, 1350, f'''
<div style="height:100%;display:flex;flex-direction:column;background:var(--tc-linho)">
 <div style="background:var(--tc-pinho);color:var(--tc-linho);padding:52px 72px;display:flex;align-items:center;gap:28px">
  <img src="{LOGO}tc-simbolo-linho.svg" style="height:92px">
  <div><div class="rot" style="font-size:26px;color:var(--tc-latao)">Relatório de visita</div><div class="tab" style="font-size:30px;margin-top:10px;color:var(--tc-salvia)">nº 0142 · sábado, 14 set</div></div>
 </div>
 <div style="padding:52px 72px 0;display:grid;grid-template-columns:1fr 330px;gap:44px">
  <div><h1 class="voz" style="font-size:96px;line-height:1">Thor</h1>
   <div style="margin-top:28px;border-top:2px solid var(--tc-pinho)">
   {''.join(f'<div style="display:grid;grid-template-columns:110px 40px 1fr;gap:18px;align-items:center;padding:17px 0;border-bottom:1px solid var(--tc-borda)"><span class="tab" style="font-size:30px;font-weight:500">{h}</span>{ic(i,34,"var(--tc-pinho)",1.8)}<span style="font-size:30px"><b style="font-weight:600">{t}</b>{" · <span style=color:var(--tc-musgo)>"+d+"</span>" if d else ""}</span></div>' for h,t,d,i in linhas)}
   </div></div>
  <div class="plq foto" style="font-size:20px;align-items:center;justify-content:center;text-align:center;margin-top:24px">foto<br>do passeio</div>
 </div>
 <div style="margin:36px 72px 0;background:var(--tc-papel);border-radius:20px;padding:30px 36px;display:flex;gap:20px;align-items:flex-start">
  <span style="flex:none;width:26px;height:26px;border:5px solid var(--tc-argila);border-radius:50%;margin-top:8px"></span>
  <p style="font-size:30px;line-height:1.4"><b style="color:var(--tc-argila)">Observação:</b> encontrou o Bob na praça e brincou um pouco. Voltou cansado e foi direto para a caminha.</p>
 </div>
 <div style="margin:auto 72px 56px;display:flex;justify-content:space-between;align-items:flex-end">
  <span class="afeto" style="font-size:52px">Tudo certo por aqui.</span><span style="font-size:30px;color:var(--tc-musgo)">— Clara</span>
 </div>
</div>'''))

# 9 · Capas de destaque
dest = [('Serviços','casa'),('Relatórios','prancheta'),('Protocolos','chave'),('Passeios','guia'),('Agenda','calendario')]
for i,(t,n) in enumerate(dest):
    slug={'Serviços':'servicos','Relatórios':'relatorios'}.get(t,t.lower())
    M.append(pagina(f'destaque-{i+1}-{slug}', 1080, 1920, f'''<div style="height:100%;background:var(--tc-pinho);display:grid;place-items:center">{ic(n,420,'var(--tc-linho)',1.4)}</div>'''))
M.append(pagina('destaques-folha', 1200, 330, f'''
<div style="height:100%;display:flex;gap:56px;justify-content:center;align-items:center;background:var(--tc-papel)">
 {''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:16px"><div style="width:150px;height:150px;border-radius:50%;background:var(--tc-pinho);display:grid;place-items:center;outline:3px solid var(--tc-linho);box-shadow:0 0 0 6px #d8d2c6">{ic(n,64,"var(--tc-linho)",1.5)}</div><span style="font-size:20px">{t}</span></div>' for t,n in dest)}
</div>'''))

# 10 · Cartão de visita 90x50 mm @300dpi = 1063x591 (+ sangria mostrada fora)
M.append(pagina('cartao-frente', 1063, 591, f'''<div style="height:100%;background:var(--tc-pinho);display:grid;place-items:center"><img src="{LOGO}tc-simbolo-latao.svg" style="height:250px"></div>'''))
M.append(pagina('cartao-verso', 1063, 591, f'''
<div style="height:100%;padding:70px 72px;display:grid;grid-template-columns:1fr auto;gap:40px;background:var(--tc-linho)">
 <div style="display:flex;flex-direction:column">
  <img src="{LOGO}tc-assinatura-horizontal.svg" style="height:92px;align-self:flex-start">
  <div style="margin-top:auto;font-size:27px;line-height:1.55">
   <div style="display:flex;gap:14px;align-items:center">{ic('balao',28,'var(--tc-pinho)',1.8)}<span class="tab">(00) 0 0000-0000</span></div>
   <div style="display:flex;gap:14px;align-items:center">{ic('casa',28,'var(--tc-pinho)',1.8)}<span>Bairro · Cidade</span></div>
  </div></div>
 <div style="display:flex;flex-direction:column;justify-content:space-between;align-items:flex-end">
  <div style="width:200px;height:200px;background:var(--tc-papel);border:2px dashed var(--tc-musgo);display:grid;place-items:center;font-size:18px;font-weight:600;letter-spacing:.12em;color:var(--tc-musgo);text-align:center">QR<br>WHATSAPP</div>
  <span class="afeto" style="font-size:32px">Pode deixar comigo.</span>
 </div>
</div>'''))

# 11 · Objetos: plaquinha de passeio + chaveiro codificado (desenho técnico)
M.append(pagina('objetos-plaquinha-chaveiro', 1600, 900, f'''
<div style="height:100%;padding:64px 72px;background:var(--tc-papel);display:grid;grid-template-columns:1fr 1fr;gap:72px">
 <div>
  <div class="rot" style="font-size:18px;color:var(--tc-argila)">Objeto 1 · plaquinha de passeio</div>
  <h2 class="voz" style="font-size:44px;margin-top:14px;line-height:1.1">Vai presa ao peitoral durante o passeio.</h2>
  <div style="display:flex;gap:40px;margin-top:40px;align-items:flex-end">
   <div style="text-align:center"><svg viewBox="0 -30 100 142" width="230"><circle cx="50" cy="3" r="14" fill="none" stroke="#9a7a40" stroke-width="4"/>{mc.simbolo(0,0,1,"#C6A15E",recorte="#8C6B32",vazado=False).replace('fill="#8C6B32" d="M','fill="#8C6B32" d="M',1)}<circle cx="50" cy="19" r="7.5" fill="#FBF8F2"/></svg><div style="font-size:16px;color:var(--tc-musgo);margin-top:10px">frente · C gravado</div></div>
   <div style="text-align:center"><svg viewBox="0 -30 100 142" width="230"><circle cx="50" cy="3" r="14" fill="none" stroke="#9a7a40" stroke-width="4"/><path fill="#C6A15E" d="M0,50 A50,50 0 0 1 100,50 V90 A22,22 0 0 1 78,112 H22 A22,22 0 0 1 0,90 Z"/><circle cx="50" cy="19" r="7.5" fill="#FBF8F2"/><text x="50" y="52" text-anchor="middle" font-family="Instrument Sans" font-weight="700" font-size="7.5" letter-spacing=".9" fill="#5b4520">EM PASSEIO COM</text><text x="50" y="68" text-anchor="middle" font-family="Literata" font-weight="600" font-size="13" fill="#5b4520">Tia Clara</text><text x="50" y="84" text-anchor="middle" font-family="Instrument Sans" font-weight="600" font-size="7.2" fill="#5b4520">SE ME ACHAR, LIGUE</text><text x="50" y="96" text-anchor="middle" font-family="Instrument Sans" font-weight="700" font-size="9" fill="#5b4520">(00) 0 0000-0000</text></svg><div style="font-size:16px;color:var(--tc-musgo);margin-top:10px">verso · contato de emergência</div></div>
  </div>
  <ul style="margin-top:32px;padding-left:0;list-style:none;font-size:19px;line-height:1.7">
   <li>◦ Latão escovado 1,2 mm · 30 × 33,6 mm · gravação a laser</li><li>◦ Argola de aço inox 16 mm + mosquetão pequeno</li><li>◦ Não substitui a plaquinha do tutor: soma a ela</li></ul>
 </div>
 <div>
  <div class="rot" style="font-size:18px;color:var(--tc-argila)">Objeto 2 · chaveiro codificado</div>
  <h2 class="voz" style="font-size:44px;margin-top:14px;line-height:1.1">A chave nunca sai com o endereço.</h2>
  <div style="display:flex;gap:40px;margin-top:40px;align-items:flex-end">
   <div style="text-align:center"><svg viewBox="0 -30 100 142" width="230"><circle cx="50" cy="3" r="14" fill="none" stroke="#6d7a74" stroke-width="4"/><path fill="#1E3B33" d="M0,50 A50,50 0 0 1 100,50 V90 A22,22 0 0 1 78,112 H22 A22,22 0 0 1 0,90 Z"/><circle cx="50" cy="19" r="7.5" fill="#FBF8F2"/><text x="50" y="72" text-anchor="middle" font-family="Instrument Sans" font-weight="700" font-size="21" letter-spacing="1" fill="#C6A15E">TC·014</text><text x="50" y="92" text-anchor="middle" font-family="Instrument Sans" font-weight="600" font-size="6.5" letter-spacing="1" fill="#DDE1D4">CÓDIGO DO CLIENTE</text></svg><div style="font-size:16px;color:var(--tc-musgo);margin-top:10px">acrílico ou couro Pinho · código em Latão</div></div>
   <div style="flex:1;background:var(--tc-linho);border-radius:12px;padding:24px 28px;font-size:19px;line-height:1.6">
    <div class="rot" style="font-size:14px">Protocolo</div>
    <div class="tab" style="margin-top:10px">◦ Código ≠ nome ≠ endereço<br>◦ Tabela de códigos só com a Clara, fora do celular do dia a dia<br>◦ Entrega e devolução registradas no relatório<br>◦ Chave perdida = aviso imediato ao tutor</div>
   </div>
  </div>
 </div>
</div>'''))

# 12 · Site: primeira dobra (desktop 1440x900)
M.append(pagina('site-home-desktop', 1440, 900, f'''
<header style="height:88px;padding:0 72px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--tc-borda);background:var(--tc-papel)">
 <img src="{LOGO}tc-assinatura-horizontal-compacta.svg" style="height:40px">
 <nav style="display:flex;gap:40px;font-size:16px;font-weight:500"><span>Serviços</span><span>Como funciona</span><span>Relatórios</span><span>Avaliações</span></nav>
 <span style="background:var(--tc-argila);color:var(--tc-linho);font-weight:600;font-size:15px;padding:14px 22px;border-radius:999px">Agendar apresentação</span>
</header>
<main style="padding:72px 72px 0;display:grid;grid-template-columns:1.1fr .9fr;gap:72px">
 <div style="padding-top:36px">
  <div class="rot" style="font-size:13px;color:var(--tc-argila)">Pet sitter &amp; dog walker · Bairro, Cidade</div>
  <h1 class="voz" style="font-size:84px;line-height:1.02;margin-top:28px">Pode deixar comigo.</h1>
  <p style="font-size:21px;line-height:1.55;margin-top:28px;max-width:560px;color:var(--tc-musgo)">Visitas na sua casa e passeios com protocolo, relatório de cada visita e <b style="color:var(--tc-pinho);font-weight:600">sempre a mesma pessoa</b> cuidando do seu pet.</p>
  <div style="display:flex;gap:16px;margin-top:40px"><span style="background:var(--tc-argila);color:var(--tc-linho);font-weight:600;font-size:17px;padding:18px 28px;border-radius:999px">Agendar visita de apresentação</span><span style="border:1.5px solid var(--tc-pinho);font-weight:600;font-size:17px;padding:17px 26px;border-radius:999px">Ver como funciona</span></div>
  <div style="display:flex;gap:36px;margin-top:72px;font-size:15px;font-weight:500">{''.join(f'<span style="display:flex;gap:10px;align-items:center">{ic(i,22,"var(--tc-pinho)",1.6)}{t}</span>' for i,t in [('chave','Chaves codificadas'),('prancheta','Relatório de cada visita'),('plaquinha','Plaquinha de passeio')])}</div>
 </div>
 <div style="position:relative;height:720px">
  <div class="plq foto" style="width:470px;position:absolute;right:20px;top:0;font-size:15px;align-items:center;justify-content:center;text-align:center">foto · pet em casa<br>altura dos olhos</div>
  <div style="position:absolute;left:0;bottom:90px;width:330px;background:var(--tc-papel);border-radius:20px;padding:24px 26px;box-shadow:0 0 0 1px var(--tc-borda)">
   <div style="display:flex;justify-content:space-between;align-items:center"><span class="rot" style="font-size:11px">Relatório · Thor</span><img src="{LOGO}tc-simbolo.svg" style="height:26px"></div>
   {''.join(f'<div style="display:flex;gap:12px;align-items:center;padding:9px 0;border-bottom:1px solid var(--tc-borda);font-size:15px"><span class="tab" style="width:44px;font-weight:500">{h}</span>{ic("check",18,"var(--tc-pinho)",2)}{t}</div>' for h,t in [('08:02','Entrada'),('08:12','Passeio · 40 min'),('09:04','Saída')])}
   <div class="afeto" style="font-size:22px;margin-top:14px">Tudo certo por aqui.</div>
  </div>
 </div>
</main>'''))

# 13 · Site no celular 390x844
M.append(pagina('site-home-celular', 390, 844, f'''
<header style="height:64px;padding:0 16px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--tc-borda);background:var(--tc-papel)"><img src="{LOGO}tc-assinatura-horizontal-compacta.svg" style="height:28px"><span style="font-size:14px;font-weight:600">Menu</span></header>
<div style="padding:32px 16px">
 <div class="rot" style="font-size:12px;color:var(--tc-argila)">Pet sitter &amp; dog walker</div>
 <h1 class="voz" style="font-size:46px;line-height:1.04;margin-top:16px">Pode deixar comigo.</h1>
 <p style="font-size:17px;line-height:1.55;margin-top:16px;color:var(--tc-musgo)">Visitas na sua casa e passeios com protocolo, relatório de cada visita e sempre a mesma pessoa.</p>
 <div style="background:var(--tc-argila);color:var(--tc-linho);font-weight:600;font-size:16px;padding:16px;border-radius:999px;text-align:center;margin-top:24px">Agendar visita de apresentação</div>
 <div class="plq foto" style="width:260px;margin:32px auto 0;font-size:12px;align-items:center;justify-content:center;text-align:center">foto · pet em casa</div>
</div>'''))

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    import json
    json.dump(M, open(os.path.join(OUT, 'lista.json'), 'w'))
    print(len(M), 'modelos')
