// Avaliação automática da landing page da Tia Clara (harness gan-design).
// Uso: NODE_PATH=$(npm root -g) node gan-harness/tools/avaliar.js <iteracao> [url]
// Saída: gan-harness/screenshots/iter-<iteracao>/ (PNGs + relatorio.json + relatorio.md)
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const iter = (process.argv[2] || '000').padStart(3, '0');
const URL_BASE = process.argv[3] || 'http://localhost:3000/';
const OUT = path.join(__dirname, '..', 'screenshots', `iter-${iter}`);
fs.mkdirSync(OUT, { recursive: true });

const LARGURAS = [
  { w: 390, h: 844 },
  { w: 768, h: 1024 },
  { w: 1024, h: 768 },
  { w: 1440, h: 900 },
];

const PALETA = {
  pinho: [30, 59, 51], 'pinho-profundo': [20, 42, 36], musgo: [86, 98, 90], linho: [244, 238, 227],
  papel: [251, 248, 242], salvia: [221, 225, 212], latao: [198, 161, 94], argila: [169, 78, 42],
  'argila-clara': [231, 184, 154], tinta: [27, 29, 26], 'apoio-escuro': [36, 70, 60],
  branco: [255, 255, 255], preto: [0, 0, 0],
};

const PROIBIDAS = ['aumigo', 'filho de quatro patas', 'mãe de pet', 'mae de pet', 'fofur', 'risco zero', '100% seguro',
  'como se fosse meu', 'diagnóstico', 'diagnostico', 'tratamento', 'consulta', 'saúde', 'saude', 'monitoramento 24',
  'garantia total', 'patinha', 'tia clara pet sitter e dog walker', 'pet sitter + dog walker'];

// Roda dentro da página: coleta de regras visuais e de acessibilidade.
function coletarNoNavegador(args) {
  const { PALETA, PROIBIDAS } = args;
  const parse = (c) => {
    const m = c && c.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number);
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };
  const lum = ({ r, g, b }) => {
    const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  };
  const ratio = (a, b) => { const [x, y] = [lum(a), lum(b)].sort((m, n) => n - m); return (x + 0.05) / (y + 0.05); };
  const blend = (fg, bg) => ({ r: fg.r * fg.a + bg.r * (1 - fg.a), g: fg.g * fg.a + bg.g * (1 - fg.a), b: fg.b * fg.a + bg.b * (1 - fg.a), a: 1 });
  const nomeCor = (c) => {
    if (!c || c.a === 0) return 'transparente';
    let best = null, dist = 1e9;
    for (const [n, [r, g, b]] of Object.entries(PALETA)) {
      const d = Math.abs(r - c.r) + Math.abs(g - c.g) + Math.abs(b - c.b);
      if (d < dist) { dist = d; best = n; }
    }
    return dist <= 6 ? best : null;
  };
  const sel = (el) => {
    let s = el.tagName.toLowerCase();
    if (el.id) s += '#' + el.id;
    if (el.classList.length) s += '.' + [...el.classList].slice(0, 2).join('.');
    return s;
  };
  const secaoDe = (el) => {
    const s = el.closest('section[id], header, footer, [data-secao], section, aside');
    return s ? (s.id || s.getAttribute('data-secao') || s.tagName.toLowerCase()) : 'fora-de-secao';
  };
  const fundoEfetivo = (el) => {
    let cor = { r: 255, g: 255, b: 255, a: 1 };
    const pilha = [];
    for (let n = el; n && n.nodeType === 1; n = n.parentElement) pilha.push(n);
    let base = { r: 255, g: 255, b: 255, a: 1 };
    for (let i = pilha.length - 1; i >= 0; i--) {
      const bg = parse(getComputedStyle(pilha[i]).backgroundColor);
      if (bg && bg.a > 0) base = blend(bg, base);
    }
    cor = base;
    return cor;
  };
  const visivel = (el) => {
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none' && Number(cs.opacity) > 0.05;
  };

  const res = {
    contraste: [], coresForaDaPaleta: {}, gradientes: [], sombras: [], italicoPorSecao: {}, italicoForaLiterata: [],
    plaquinhaEmControle: [], textoPequeno: [], fontesFallback: [],
  };
  const todos = [...document.querySelectorAll('body *')];
  for (const el of todos) {
    if (!visivel(el)) continue;
    const cs = getComputedStyle(el);
    const temTexto = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim().length > 0);
    // cores
    const props = [['color', cs.color, temTexto], ['background-color', cs.backgroundColor, true]];
    for (const lado of ['Top', 'Right', 'Bottom', 'Left']) {
      if (parseFloat(cs['border' + lado + 'Width']) > 0 && cs['border' + lado + 'Style'] !== 'none') props.push(['border-color', cs['border' + lado + 'Color'], true]);
    }
    if (el instanceof SVGElement) { props.push(['fill', cs.fill, true], ['stroke', cs.stroke, true]); }
    for (const [prop, val, conta] of props) {
      if (!conta) continue;
      const c = parse(val);
      if (!c || c.a === 0) continue;
      if (!nomeCor(c)) {
        const k = `${prop}: ${val}`;
        (res.coresForaDaPaleta[k] = res.coresForaDaPaleta[k] || []).length < 4 && res.coresForaDaPaleta[k].push(sel(el));
      }
    }
    // gradientes e sombras
    if (/gradient/.test(cs.backgroundImage) && !/^repeating-linear-gradient/.test(cs.backgroundImage.trim())) res.gradientes.push({ el: sel(el), valor: cs.backgroundImage.slice(0, 120) });
    if (cs.boxShadow !== 'none') {
      const temBlur = cs.boxShadow.split(/,(?![^(]*\))/).some((s) => { const nums = s.replace(/rgba?\([^)]*\)/, '').trim().split(/\s+/).map(parseFloat); return (nums[2] || 0) > 0; });
      res.sombras.push({ el: sel(el), valor: cs.boxShadow.slice(0, 100), comDesfoque: temBlur });
    }
    if (cs.textShadow !== 'none') res.sombras.push({ el: sel(el), valor: 'text-shadow ' + cs.textShadow, comDesfoque: true });
    // plaquinha em controles
    if (/^(A|BUTTON|INPUT|SELECT|TEXTAREA|SUMMARY)$/.test(el.tagName) && /%/.test(cs.borderTopLeftRadius + cs.borderBottomLeftRadius) && cs.borderTopLeftRadius !== cs.borderBottomLeftRadius) res.plaquinhaEmControle.push(sel(el));
    if (!temTexto) continue;
    const texto = [...el.childNodes].filter((n) => n.nodeType === 3).map((n) => n.textContent.trim()).join(' ').slice(0, 60);
    // itálico
    if (cs.fontStyle === 'italic') {
      const s = secaoDe(el);
      if (/Literata/i.test(cs.fontFamily)) (res.italicoPorSecao[s] = res.italicoPorSecao[s] || []).push(texto);
      else res.italicoForaLiterata.push({ secao: s, texto });
    }
    // fonte pequena
    const fs = parseFloat(cs.fontSize);
    if (fs < 12) res.textoPequeno.push({ el: sel(el), px: fs, texto });
    // contraste
    const fg = parse(cs.color);
    if (fg) {
      const bg = fundoEfetivo(el);
      const r = ratio(blend(fg, bg), bg);
      const grande = fs >= 24 || (fs >= 18.66 && Number(cs.fontWeight) >= 700);
      const min = grande ? 3 : 4.5;
      if (r < min) res.contraste.push({ el: sel(el), secao: secaoDe(el), texto, razao: +r.toFixed(2), minimo: min, cor: cs.color, fundo: `rgb(${Math.round(bg.r)}, ${Math.round(bg.g)}, ${Math.round(bg.b)})` });
    }
  }
  // títulos
  res.titulos = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map((h) => `${h.tagName} ${h.textContent.trim().slice(0, 70)}`);
  res.secoes = [...document.querySelectorAll('section, header, footer, main, nav')].map((s) => `${s.tagName.toLowerCase()}${s.id ? '#' + s.id : ''}${s.getAttribute('aria-label') ? ' [' + s.getAttribute('aria-label') + ']' : ''}`);
  // imagens
  res.imagensSemAlt = [...document.querySelectorAll('img:not([alt])')].map(sel);
  // links
  const ids = new Set([...document.querySelectorAll('[id]')].map((e) => e.id));
  res.linksQuebrados = [...document.querySelectorAll('a')].filter((a) => {
    const h = a.getAttribute('href');
    if (h === null || h === '' || h === '#') return true;
    if (h.startsWith('#')) return !ids.has(decodeURIComponent(h.slice(1)));
    return false;
  }).map((a) => `${sel(a)} href="${a.getAttribute('href')}" "${a.textContent.trim().slice(0, 40)}"`);
  res.linksWhatsApp = [...document.querySelectorAll('a[href*="wa.me"], a[href*="whatsapp"]')].map((a) => a.getAttribute('href'));
  // textos
  const corpo = document.body.innerText;
  const baixo = corpo.toLowerCase();
  res.palavrasProibidas = PROIBIDAS.filter((p) => baixo.includes(p));
  res.ocorrencias83 = [...document.querySelectorAll('body *')].filter((e) => [...e.childNodes].some((n) => n.nodeType === 3 && /83\s*%/.test(n.textContent)))
    .map((e) => ({ el: sel(e), dentroDeMarcador: !!e.closest('[data-marcador]') }));
  res.marcadores = [...document.querySelectorAll('[data-marcador]')].map((e) => `${e.getAttribute('data-marcador') || ''} → "${e.textContent.trim().slice(0, 60)}"`);
  res.tituloDocumento = document.title;
  res.lang = document.documentElement.lang;
  res.meta = Object.fromEntries([...document.querySelectorAll('meta[name], meta[property]')].map((m) => [m.getAttribute('name') || m.getAttribute('property'), (m.content || '').slice(0, 80)]));
  res.jsonld = [...document.querySelectorAll('script[type="application/ld+json"]')].map((s) => { try { const j = JSON.parse(s.textContent); return { ok: true, tipo: j['@type'] }; } catch (e) { return { ok: false, erro: String(e) }; } });
  res.pularParaConteudo = !!document.querySelector('a[href^="#"]:first-of-type') && /pular|conteúdo|conteudo/i.test((document.querySelector('body a') || {}).textContent || '');
  return res;
}

async function main() {
  const browser = await chromium.launch();
  const relatorio = { iteracao: iter, url: URL_BASE, larguras: {}, console: [], requisicoesFalhas: [], pesoBytes: 0 };

  for (const { w, h } of LARGURAS) {
    const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    page.on('console', (m) => { if (m.type() === 'error' || m.type() === 'warning') relatorio.console.push(`[${w}] ${m.type()}: ${m.text().slice(0, 200)}`); });
    page.on('pageerror', (e) => relatorio.console.push(`[${w}] pageerror: ${String(e).slice(0, 200)}`));
    page.on('response', async (r) => {
      if (r.status() >= 400) relatorio.requisicoesFalhas.push(`[${w}] ${r.status()} ${r.url()}`);
      if (w === 1440) { try { relatorio.pesoBytes += (await r.body()).length; } catch (_) { /* redirecionamentos */ } }
    });
    await page.goto(URL_BASE, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const info = { };
    info.fontes = await page.evaluate(() => ({ literata: document.fonts.check('600 16px "Literata"'), instrument: document.fonts.check('400 16px "Instrument Sans"'), carregadas: [...document.fonts].filter((f) => f.status === 'loaded').map((f) => `${f.family} ${f.style} ${f.weight}`) }));
    info.overflow = await page.evaluate(() => {
      const W = document.documentElement.clientWidth;
      const fora = [...document.querySelectorAll('body *')].filter((e) => { const r = e.getBoundingClientRect(); return r.width > 0 && (r.right > W + 1 || r.left < -1); })
        .filter((e) => !e.closest('[aria-hidden="true"]') || true).slice(0, 12).map((e) => `${e.tagName.toLowerCase()}${e.id ? '#' + e.id : ''}${e.className && typeof e.className === 'string' ? '.' + e.className.split(' ')[0] : ''} (${Math.round(e.getBoundingClientRect().left)}→${Math.round(e.getBoundingClientRect().right)})`);
      return { scrollWidth: document.documentElement.scrollWidth, clientWidth: W, rolagemHorizontal: document.documentElement.scrollWidth > W, elementosForaDaTela: fora };
    });
    await page.screenshot({ path: path.join(OUT, `dobra-${w}.png`) });
    await page.screenshot({ path: path.join(OUT, `pagina-inteira-${w}.png`), fullPage: true });
    info.alturaPagina = await page.evaluate(() => document.documentElement.scrollHeight);

    if (w === 1440 || w === 390) {
      // screenshot por seção
      const ids = await page.evaluate(() => [...document.querySelectorAll('body > header, main > section, main > *[id], body > section, body > footer, footer')].map((e, i) => { e.setAttribute('data-aval', String(i)); return `${i}|${e.id || e.tagName.toLowerCase()}`; }));
      for (const item of [...new Set(ids)]) {
        const [i, nome] = item.split('|');
        const loc = page.locator(`[data-aval="${i}"]`).first();
        try { await loc.screenshot({ path: path.join(OUT, `secao-${w}-${String(i).padStart(2, '0')}-${nome}.png`) }); } catch (_) { /* vazio */ }
      }
      await page.evaluate(() => document.querySelectorAll('[data-aval]').forEach((e) => e.removeAttribute('data-aval')));
      info.regras = await page.evaluate(coletarNoNavegador, { PALETA, PROIBIDAS });

      // alvos de toque
      info.alvosPequenos = await page.evaluate((lim) => [...document.querySelectorAll('a, button, summary, input, [role="button"]')].filter((e) => { const r = e.getBoundingClientRect(); return r.width > 0 && (r.width < lim || r.height < lim); })
        .map((e) => `${e.tagName.toLowerCase()} "${e.textContent.trim().slice(0, 30)}" ${Math.round(e.getBoundingClientRect().width)}×${Math.round(e.getBoundingClientRect().height)}`).slice(0, 20), w === 390 ? 44 : 24);

      // foco por teclado
      await page.goto(URL_BASE, { waitUntil: 'networkidle' });
      const foco = [];
      for (let k = 0; k < 45; k++) {
        await page.keyboard.press('Tab');
        const f = await page.evaluate(() => {
          const e = document.activeElement;
          if (!e || e === document.body) return null;
          const cs = getComputedStyle(e);
          const r = e.getBoundingClientRect();
          const visivel = (cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0) || cs.boxShadow !== 'none';
          return { el: `${e.tagName.toLowerCase()} "${(e.textContent || e.getAttribute('aria-label') || '').trim().slice(0, 35)}"`, indicadorVisivel: visivel, naTela: r.width > 0 && r.height > 0 };
        });
        if (!f) break;
        foco.push(f);
        if (k === 1) await page.screenshot({ path: path.join(OUT, `foco-${w}.png`) });
      }
      info.foco = { total: foco.length, semIndicador: foco.filter((f) => !f.indicadorVisivel).map((f) => f.el), ordem: foco.map((f) => f.el).slice(0, 25) };
    }

    if (w === 390) {
      // menu do celular
      await page.goto(URL_BASE, { waitUntil: 'networkidle' });
      const botao = page.locator('button[aria-expanded], [aria-controls][aria-expanded]').first();
      if (await botao.count()) {
        await botao.click();
        await page.waitForTimeout(500);
        info.menu = { aberto: await botao.getAttribute('aria-expanded') };
        await page.screenshot({ path: path.join(OUT, 'menu-aberto-390.png') });
        await page.keyboard.press('Escape');
        await page.waitForTimeout(400);
        info.menu.depoisDoEsc = await botao.getAttribute('aria-expanded');
      } else info.menu = { aviso: 'nenhum botão com aria-expanded encontrado' };
      // FAQ
      const det = page.locator('details');
      info.faq = { details: await det.count() };
      if (info.faq.details) { await det.first().locator('summary').click(); info.faq.abreAoClicar = await det.first().evaluate((d) => d.open); await det.first().screenshot({ path: path.join(OUT, 'faq-aberto-390.png') }); }
    }
    relatorio.larguras[w] = info;
    await ctx.close();
  }

  // modo escuro, movimento reduzido e sem JavaScript
  for (const w of [1440, 390]) {
    const ctx = await browser.newContext({ viewport: { width: w, height: w === 390 ? 844 : 900 }, colorScheme: 'dark' });
    const page = await ctx.newPage();
    await page.goto(URL_BASE, { waitUntil: 'networkidle' });
    await page.screenshot({ path: path.join(OUT, `escuro-dobra-${w}.png`) });
    if (w === 1440) {
      await page.screenshot({ path: path.join(OUT, 'escuro-pagina-inteira-1440.png'), fullPage: true });
      const r = await page.evaluate(coletarNoNavegador, { PALETA, PROIBIDAS });
      relatorio.modoEscuro = { falhasDeContraste: r.contraste.length, exemplos: r.contraste.slice(0, 8) };
    }
    await ctx.close();
  }
  {
    const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce' });
    const page = await ctx.newPage();
    await page.goto(URL_BASE, { waitUntil: 'networkidle' });
    relatorio.movimentoReduzido = await page.evaluate(() => [...document.querySelectorAll('body *')].map((e) => { const cs = getComputedStyle(e); const t = Math.max(...cs.transitionDuration.split(',').map(parseFloat)) || 0; const a = cs.animationName !== 'none' ? (Math.max(...cs.animationDuration.split(',').map(parseFloat)) || 0) : 0; return { e: e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className.split(' ')[0] : ''), t, a }; }).filter((x) => x.t > 0.01 || x.a > 0.01).slice(0, 10));
    await ctx.close();
  }
  {
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, javaScriptEnabled: false });
    const page = await ctx.newPage();
    await page.goto(URL_BASE, { waitUntil: 'networkidle' });
    await page.screenshot({ path: path.join(OUT, 'sem-js-pagina-inteira-390.png'), fullPage: true });
    await ctx.close();
  }
  await browser.close();

  fs.writeFileSync(path.join(OUT, 'relatorio.json'), JSON.stringify(relatorio, null, 2));

  // resumo legível
  const L = relatorio.larguras;
  const linhas = [`# Relatório automático — iteração ${iter}`, '', `URL: ${URL_BASE} · peso total (1440): ${(relatorio.pesoBytes / 1024).toFixed(0)} KB`, ''];
  linhas.push('## Rolagem horizontal');
  for (const w of Object.keys(L)) linhas.push(`- ${w}px: ${L[w].overflow.rolagemHorizontal ? '❌ SIM' : '✅ não'} (scrollWidth ${L[w].overflow.scrollWidth}) · altura ${L[w].alturaPagina}px · fontes: Literata ${L[w].fontes.literata ? 'ok' : '❌'}, Instrument ${L[w].fontes.instrument ? 'ok' : '❌'}${L[w].overflow.elementosForaDaTela.length ? ' · fora da tela: ' + L[w].overflow.elementosForaDaTela.slice(0, 5).join(', ') : ''}`);
  linhas.push('', `## Console e rede`, relatorio.console.length ? relatorio.console.slice(0, 15).map((c) => '- ' + c).join('\n') : '- sem erros', relatorio.requisicoesFalhas.length ? relatorio.requisicoesFalhas.slice(0, 15).map((c) => '- ' + c).join('\n') : '- sem requisições falhas');
  for (const w of [1440, 390]) {
    const R = L[w].regras;
    linhas.push('', `## Regras de marca e acessibilidade — ${w}px`);
    linhas.push(`- Contraste reprovado: ${R.contraste.length}${R.contraste.length ? '\n' + R.contraste.slice(0, 10).map((c) => `  - ${c.el} [${c.secao}] "${c.texto}" ${c.razao}:1 (mín ${c.minimo}) cor ${c.cor} sobre ${c.fundo}`).join('\n') : ''}`);
    const fora = Object.entries(R.coresForaDaPaleta);
    linhas.push(`- Cores fora da paleta: ${fora.length}${fora.length ? '\n' + fora.slice(0, 12).map(([k, v]) => `  - ${k} em ${v.join(', ')}`).join('\n') : ''}`);
    linhas.push(`- Gradientes proibidos: ${R.gradientes.length}${R.gradientes.length ? ' → ' + R.gradientes.slice(0, 5).map((g) => g.el).join(', ') : ''}`);
    linhas.push(`- Sombras: ${R.sombras.length} (com desfoque: ${R.sombras.filter((s) => s.comDesfoque).length})${R.sombras.length ? ' → ' + R.sombras.slice(0, 6).map((s) => `${s.el} [${s.valor}]`).join('; ') : ''}`);
    linhas.push(`- Itálico Literata por seção: ${Object.entries(R.italicoPorSecao).map(([s, t]) => `${s}=${t.length}${t.length > 1 ? ' ❌' : ''} (${t.map((x) => '"' + x.slice(0, 30) + '"').join(', ')})`).join(' · ') || 'nenhum'}`);
    if (R.italicoForaLiterata.length) linhas.push(`- Itálico fora da Literata: ${R.italicoForaLiterata.slice(0, 5).map((x) => `${x.secao} "${x.texto}"`).join(', ')}`);
    linhas.push(`- Plaquinha em controle: ${R.plaquinhaEmControle.length ? '❌ ' + R.plaquinhaEmControle.join(', ') : 'nenhuma'}`);
    linhas.push(`- Texto < 12px: ${R.textoPequeno.length ? R.textoPequeno.slice(0, 6).map((t) => `${t.el} ${t.px}px "${t.texto}"`).join('; ') : 'nenhum'}`);
    linhas.push(`- Alvos de toque < ${w === 390 ? 44 : 24}px: ${L[w].alvosPequenos.length ? L[w].alvosPequenos.slice(0, 8).join('; ') : 'nenhum'}`);
    linhas.push(`- Foco por teclado: ${L[w].foco.total} paradas; sem indicador visível: ${L[w].foco.semIndicador.length ? L[w].foco.semIndicador.slice(0, 8).join('; ') : 'nenhuma'}`);
  }
  const R = L[1440].regras;
  linhas.push('', '## Estrutura e conteúdo');
  linhas.push(`- Título: "${R.tituloDocumento}" · lang=${R.lang} · link pular-para-conteúdo: ${R.pularParaConteudo ? 'sim' : 'não encontrado'}`);
  linhas.push(`- Meta: ${Object.keys(R.meta).join(', ') || 'nenhuma'}`);
  linhas.push(`- JSON-LD: ${R.jsonld.length ? R.jsonld.map((j) => j.ok ? j.tipo : '❌ ' + j.erro).join(', ') : 'nenhum'}`);
  linhas.push(`- Landmarks/seções: ${R.secoes.join(' · ')}`);
  linhas.push(`- Títulos (${R.titulos.filter((t) => t.startsWith('H1')).length} h1):\n${R.titulos.map((t) => '  - ' + t).join('\n')}`);
  linhas.push(`- Imagens sem alt: ${R.imagensSemAlt.length ? R.imagensSemAlt.join(', ') : 'nenhuma'}`);
  linhas.push(`- Links quebrados/vazios: ${R.linksQuebrados.length ? '\n' + R.linksQuebrados.map((l) => '  - ' + l).join('\n') : 'nenhum'}`);
  linhas.push(`- Links de WhatsApp: ${R.linksWhatsApp.length ? R.linksWhatsApp.join(' | ') : '❌ nenhum'}`);
  linhas.push(`- Palavras proibidas encontradas: ${R.palavrasProibidas.length ? '❌ ' + R.palavrasProibidas.join(', ') : 'nenhuma'}`);
  linhas.push(`- "83%": ${R.ocorrencias83.length ? R.ocorrencias83.map((o) => `${o.el} (${o.dentroDeMarcador ? 'dentro de [data-marcador]' : '❌ fora de marcador'})`).join(', ') : 'não aparece'}`);
  linhas.push(`- Marcadores [data-marcador] (${R.marcadores.length}):\n${R.marcadores.slice(0, 30).map((m) => '  - ' + m).join('\n')}`);
  linhas.push('', '## Interação');
  linhas.push(`- Menu 390: ${JSON.stringify(L[390].menu)}`);
  linhas.push(`- FAQ 390: ${JSON.stringify(L[390].faq)}`);
  linhas.push(`- Movimento reduzido (elementos ainda animando): ${relatorio.movimentoReduzido.length ? JSON.stringify(relatorio.movimentoReduzido) : 'nenhum'}`);
  linhas.push(`- Modo escuro: ${relatorio.modoEscuro.falhasDeContraste} falhas de contraste${relatorio.modoEscuro.exemplos.length ? ' → ' + relatorio.modoEscuro.exemplos.slice(0, 5).map((c) => `${c.el} "${c.texto}" ${c.razao}:1`).join('; ') : ''}`);
  linhas.push('', '## Arquivos', fs.readdirSync(OUT).filter((f) => f.endsWith('.png')).map((f) => '- ' + f).join('\n'));
  fs.writeFileSync(path.join(OUT, 'relatorio.md'), linhas.join('\n') + '\n');
  console.log(linhas.join('\n'));
}

main().catch((e) => { console.error(e); process.exit(1); });
