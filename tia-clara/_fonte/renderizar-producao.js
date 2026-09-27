// Renderiza cada modelo de 07-producao/modelos no tamanho exato. uso: NODE_PATH=$(npm root -g) node tia-clara/_fonte/renderizar-producao.js
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const D = path.resolve(__dirname, '..', '07-producao'); const lista = JSON.parse(fs.readFileSync(path.join(D, 'modelos', 'lista.json')));
(async () => { const b = await chromium.launch(); const p = await b.newPage();
  for (const [nome, w, h] of lista) { await p.setViewportSize({ width: w, height: h });
    await p.goto('file://' + path.join(D, 'modelos', nome + '.html')); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(80);
    await p.screenshot({ path: path.join(D, 'png', nome + '.png') }); process.stdout.write('.'); }
  await b.close(); console.log(' ok'); })();
