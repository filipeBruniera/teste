## GAN Harness Build Report

**Brief:** Landing page one-page da Tia Clara Pet Sitter & Dog Walker, HTML/CSS estático em `tia-clara/10-site/`, fiel ao brand book (ver `spec.md`).
**Comando:** `/ecc:gan-design … --max-iterations 4` (limiar padrão do modo design: 7,5)
**Result:** PASS
**Iterations:** 2 / 4
**Final Score:** 7.7 / 10
**Modo de avaliação:** screenshot (Playwright headless via `tools/avaliar.js` + scripts próprios do avaliador). O Playwright MCP não estava disponível na sessão.

### Score Progression
| Iter | Design (0,35) | Fidelidade à marca (0,30) | Acabamento (0,25) | Funcionalidade (0,10) | Total |
|------|------|------|------|------|------|
| 1 | 7,0 | 8,5 | 6,0 | 7,5 | 7,3 ❌ |
| 2 | 7,5 | 8,7 | 6,5 | 8,0 | **7,7 ✅** |

`iteration 1: 7,3 → iteration 2: 7,7`

### Ajustes do harness em relação ao comando padrão
- **Originalidade redefinida como fidelidade à marca**, por pedido explícito no brief ("originalidade = fidelidade à marca, não efeitos"). O gerador não recebeu a instrução padrão de buscar "layouts incomuns e animações próprias".
- **HTML/CSS estático** no lugar do padrão React + TypeScript do gerador.
- **Avaliação automática** com checagens da marca (paleta, gradientes, sombras, itálico por seção, plaquinha em controle, palavras proibidas, marcadores) além de contraste, rolagem horizontal, foco, menu e FAQ.

### Correção depois da aprovação (fora do ciclo)
O avaliador da rodada 2 aprovou, mas apontou um problema de acabamento que já existia na rodada 1: **entre 900 e 1099 px o cabeçalho quebrava em duas linhas** e o botão "Agendar apresentação" ficava sozinho na segunda linha (inclui 1024 px).
- O breakpoint do cabeçalho passou de 860 para **1100 px**, a menor largura em que a marca, os 6 links e o CTA cabem numa linha.
- Entre 640 e 1099 px, com JS, o botão "Menu" fica na mesma linha do CTA. Sem JS, a lista continua empilhada e visível.
- Validado com script em 390, 768, 860, 900, 1000, 1024, 1075, 1099, 1100, 1200, 1280 e 1440 px: cabeçalho com 73 px de altura de 640 px para cima, sem rolagem horizontal. A avaliação automática completa (`screenshots/iter-003/relatorio.md`) segue sem nenhum alerta.
- **Essa correção não passou por uma nova nota do avaliador.**

### Remaining Issues
- **Véu do menu no celular** usa `rgb(30 59 51 / 0.45)` (Pinho com opacidade) literal em `css/site.css`. Não é cor nova, mas está fora do vocabulário nomeado de `tokens.css` (Gate D1). Para resolver, criar um token no design system de origem.
- **Modo escuro desligado** (`data-tema="claro"`): com ele ligado havia 32 falhas de contraste. O spec o trata como desejável, não obrigatório.
- **Peso da página: ~1,2 MB**, quase tudo fonte TTF variável. Converter para WOFF2 com subconjunto latino reduziria bastante.
- **Dados reais pendentes** (marcadores `data-marcador`, listados em `tia-clara/10-site/README.md`): bairro/cidade, telefone e link do WhatsApp, Instagram, preços, fotos, depoimentos e a estatística de 83%. Os protocolos da estratégia são hipóteses ⚑ e precisam ser confirmados com a Clara.

### Files Created
- `gan-harness/spec.md`, `gan-harness/eval-rubric.md`, `gan-harness/tools/avaliar.js`
- `gan-harness/feedback/feedback-001.md`, `gan-harness/feedback/feedback-002.md`
- `gan-harness/generator-state.md`
- `gan-harness/build-report.md`
- `tia-clara/10-site/` (index.html, css/, js/, assets/, favicons, README.md)
- Screenshots em `gan-harness/screenshots/` (fora do git)

### Custo
4 agentes (2 gerações e 2 avaliações), ~700 mil tokens de subagentes, cerca de 50 minutos de relógio.
