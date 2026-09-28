# Tia Clara · Pet Sitter & Dog Walker — Identidade Visual

**Brand book publicado:** https://claude.ai/artifact/1V1Eqd8Aw4mmLy64nD6zjK. A versão local fica em `08-brand-book/index.html`.

> **O nome abraça. A identidade garante.** Guardiã na postura, Curadora no critério, Cuidadora no tom.

| Pasta | O que tem |
|---|---|
| `00-brief/` | Briefing estruturado e estado do projeto |
| `01-estrategia/` | Posicionamento, arquétipos, pilares, tom de voz, anti-posicionamento |
| `02-inteligencia-visual/` | Mapa da categoria, códigos saturados e disponíveis, riscos |
| `03-territorios/` | 3 territórios criativos e a decisão |
| `04-logo/` | Símbolo e assinaturas em vetor (`master/`), PNGs, favicon, testes, exploração |
| `05-design-system/` | Tokens (JSON + CSS), fontes OFL, guia do sistema |
| `06-motion/` | Assinatura animada (HTML/vídeo) e regras de movimento |
| `07-producao/` | 21 modelos: Instagram, stories, reel, relatório de visita, destaques, cartão, objetos, site |
| `08-brand-book/` | Manual completo |
| `09-qa/` | Scorecard e riscos abertos |
| `10-site/` | Landing page estática (HTML/CSS), pronta para GitHub Pages ou Netlify depois dos dados reais |
| `11-lancamento/` | Como publicar o site, revisões de texto e SEO, guia do Perfil de Empresa no Google e checklist antes de publicar |
| `12-identidade-v2/` | **Nova identidade (em andamento):** a Clara rejeitou a logo e as cores da v1. Brief, diagnóstico, 3 paletas em verde-sálvia médio, 3 rotas de logo e pranchas para ela escolher. Ver o [PRD](../.claude/prds/tia-clara-nova-identidade.prd.md) |
| `_fonte/` | Scripts que geram tudo |

## Regenerar

```bash
pip install fonttools uharfbuzz pillow
python3 tia-clara/_fonte/marca.py                                    # SVGs mestres
NODE_PATH=$(npm root -g) node tia-clara/_fonte/exportar.js           # PNGs (precisa do Playwright)
python3 tia-clara/_fonte/producao.py && NODE_PATH=$(npm root -g) node tia-clara/_fonte/renderizar-producao.js
python3 tia-clara/_fonte/motion.py && python3 tia-clara/_fonte/brandbook.py
```

As fontes são **Literata** e **Instrument Sans**, ambas SIL Open Font License, livres para uso comercial.
