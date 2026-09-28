// Renderiza as pranchas da v2 (12-identidade-v2/04-apresentacao) no tamanho exato, a partir de lista.json.
// Mesma lógica de renderizar-producao.js. uso: NODE_PATH=$(npm root -g) node tia-clara/_fonte/v2_renderizar.js
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const D = path.resolve(__dirname, '..', '12-identidade-v2', '04-apresentacao'); const lista = JSON.parse(fs.readFileSync(path.join(D, 'lista.json')));
(async () => { const b = await chromium.launch(); const p = await b.newPage();
  for (const [nome, w, h] of lista) { await p.setViewportSize({ width: w, height: h });
    await p.goto('file://' + path.join(D, nome + '.html')); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(120);
    const pequenos = await p.evaluate(() => [...document.querySelectorAll('body *')].filter((e) => [...e.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim()) && parseFloat(getComputedStyle(e).fontSize) < 28).map((e) => e.textContent.trim().slice(0, 30)));
    const vaza = await p.evaluate(() => { const rod = document.querySelector('.rod'); const topo = rod ? rod.getBoundingClientRect().top - 8 : innerHeight;
      return document.documentElement.scrollWidth > innerWidth + 1 || [...document.body.children].filter((e) => e !== rod).some((e) => e.getBoundingClientRect().bottom > topo); });
    await p.screenshot({ path: path.join(D, nome + '.png') });
    console.log(nome, pequenos.length ? 'TEXTO < 28px: ' + pequenos.join(' | ') : 'ok', vaza ? '· VAZA OU ENCOSTA NO RODAPÉ' : ''); }
  await b.close(); })();
