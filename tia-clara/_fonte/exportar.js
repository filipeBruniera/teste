// Exporta os SVGs mestres para PNG (fundo transparente) em tamanhos de uso comum.
// uso: NODE_PATH=$(npm root -g) node tia-clara/_fonte/exportar.js
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const RAIZ = path.resolve(__dirname, '..');
const M = path.join(RAIZ, '04-logo', 'master'), OUT = path.join(RAIZ, '04-logo', 'png');
const LOTES = [
  [/^tc-assinatura-(horizontal|vertical)(-compacta)?(-preto|-branco|-linho)?\.svg$/, [600, 1200, 2400]],
  [/^tc-assinatura-.*sobre-pinho\.svg$/, [1200, 2400]],
  [/^tc-logotipo.*\.svg$/, [600, 1200]],
  [/^tc-simbolo(-preto|-branco|-linho|-latao|-argila)?\.svg$/, [256, 512, 1024]],
  [/^tc-simbolo-compacto.*\.svg$/, [16, 32, 48, 64]],
  [/^tc-avatar.*\.svg$/, [320, 640, 1080]],
  [/^tc-favicon\.svg$/, [16, 32, 48, 192, 512]],
  [/^tc-app-icon\.svg$/, [180, 512]],
];
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage();
  for (const f of fs.readdirSync(M).filter(f => f.endsWith('.svg')).sort()) {
    const lote = LOTES.find(([re]) => re.test(f)); if (!lote) continue;
    const svg = fs.readFileSync(path.join(M, f), 'utf8');
    const [, , vw, vh] = svg.match(/viewBox="([^"]+)"/)[1].split(' ').map(Number);
    for (const w of lote[1]) {
      const h = Math.round(w * vh / vw);
      await p.setViewportSize({ width: w, height: h });
      await p.setContent(`<html><body style="margin:0;background:transparent">${svg.replace(/width="[^"]+" height="[^"]+"/, `width="${w}" height="${h}"`)}</body></html>`);
      await p.screenshot({ path: path.join(OUT, f.replace('.svg', `-${w}px.png`)), omitBackground: true, clip: { x: 0, y: 0, width: w, height: h } });
    }
    process.stdout.write('.');
  }
  await b.close(); console.log('\nok');
})();
