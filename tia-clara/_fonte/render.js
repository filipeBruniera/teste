// usage: node render.js input.html output.png width height [scale]
const { chromium } = require('playwright');
(async () => {
  const [,, input, output, w, h, s] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: +(s || 1) });
  await page.goto('file://' + require('path').resolve(input));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(150);
  await page.screenshot({ path: output, fullPage: true });
  await browser.close();
})();
