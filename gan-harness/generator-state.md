# Generator State — Iteração 002

## O que foi corrigido (item a item do feedback-001.md)

### Critical
1. **Badge "FOTO A CONFIRMAR" cortado pelo cartão de relatório (≥860px)** — `.tc-foto` passou de `align-items: flex-end` para `align-items: center; justify-content: center; text-align: center` (igual ao modelo aprovado, que centraliza o texto na forma-plaquinha em vez de ancorá-lo no rodapé). A legenda agora fica bem acima da faixa onde `.tc-hero__cartao` sobrepõe a foto, em qualquer largura ≥860px. Mesma correção beneficia a foto do relatório (`#relatorio`), que usa o mesmo componente `.tc-foto`.

### Major
1. **Vazio de ~40% no FAQ em 1440px** — troquei a lista de perguntas de "uma coluna presa a 780px" para duas colunas (`column-count: 2` a partir de 900px, com `break-inside: avoid` em cada `<details>`), reaproveitando o próprio componente-acordeão em vez de esticar a largura ou inventar um bloco de preenchimento. `border-bottom` do envelope movido para o container da lista, para fechar as duas colunas com uma linha só.
2. **Bug de especificidade deixando rótulos/subtítulos com cor errada** — adicionei `:not([class])` a `.tc-servico > p`, `.tc-relatorio__intro > p` e `.tc-avaliacoes__intro > p`, para que esse seletor genérico de "parágrafo de corpo" pare de vazar para elementos com classe própria (`.tc-etiqueta`, `.tc-servico__sub`). Isso corrigiu **três** ocorrências, não só as duas que o avaliador tinha achado: "A peça-assinatura" e "Avaliações" (rótulos) **e também** os subtítulos "Cães e gatos, no território deles." / "Só cães, um passeio de verdade." em Serviços, que também estavam pegando a cor errada (e um `margin-top` maior do que o `.tc-servico__sub` pedia) pelo mesmo motivo — confirmei visualmente depois do fix, os três agora renderizam com a cor certa.
   Como a etiqueta "A peça-assinatura" volta a usar a regra base `.tc-etiqueta { color: var(--tc-argila) }` depois do fix, e essa seção tem fundo Sálvia (onde Argila só passa AA em texto grande — 4,15:1, documentado no design-system.md), adicionei uma regra consciente `.tc-secao--salvia .tc-etiqueta { color: var(--tc-musgo) }` (4,8:1, passa) em vez de deixar a etiqueta reproduzir a falha de contraste que o bug de cascata tinha mascarado por acidente. Documentei a decisão no README.
3. **README descrevendo um menu `<details>/<summary>` que não existe** — reescrevi o parágrafo para descrever a implementação real (`<nav>` sempre no DOM, lista empilhada sem JS, botão hambúrguer com `aria-expanded` sincronizado via `site.js` quando há JS) e aproveitei para documentar a decisão de travar o tema claro (`data-tema="claro"`), que antes só estava no `generator-state.md`.

### Minor
1. **Numeração inconsistente** — Protocolos foi de "01·02·03·04·05" para "1·2·3·4·5", alinhando com "Como funciona" **e** com a peça de referência `ig-01-autoridade-protocolo.png` (que usa "1 2 3" sem zero à esquerda — o zero-padding não vinha de nenhuma peça oficial).
2. **Menu mobile sem véu atrás do painel** — adicionei `.tc-menu__veu` (`<div hidden>` logo após o `</header>`, `position:fixed; inset:0; background: rgb(30 59 51 / 0.45)`, escondido por padrão via atributo `hidden` nativo — nunca aparece sem JS, que é o comportamento certo, já que sem JS não existe painel flutuante para destacar). `site.js` alterna `hidden` junto com `data-aberto`; o listener de "clique fora fecha o menu" que já existia cobre o clique no véu sem precisar de handler novo, porque o véu não é descendente de `#tc-menu`.
3. **`sameAs` do JSON-LD com URL de aparência real** — removido do JSON-LD até haver um `@` confirmado; README explica por quê e como adicionar de volta.
4. **`.tc-envolucro` 1264px vs "máx. 1200" da spec** — comentário no CSS explicando a conta (1200 de conteúdo + 2×32 de margem lateral = 1264).

### Nota do orquestrador (além do feedback)
- Subtítulo do hero: revertido de "Visitas na casa dele..." para "Visitas na sua casa..." (texto do modelo aprovado, `site-home-desktop.html`), em `index.html` e no `og:description`.
- Colunas da primeira dobra em 1440px: `.tc-hero__grade` passou a usar `align-items: center` (em vez de `start`) a partir de 860px — a coluna de texto (mais curta) passa a ficar centralizada na faixa de altura definida pela coluna da foto/cartão (mais alta, que não se move), distribuindo o vazio nas duas pontas em vez de deixá-lo todo embaixo do texto. Também limitei `.tc-hero__foto` a `width: min(470px, 100%)` em vez de esticar até a borda da coluna — largura igual à do modelo aprovado, que também reduz a altura total da coluna visual e aproxima ainda mais o equilíbrio.

## Verificação

Rodei `gan-harness/tools/avaliar.js` na iteração de teste `000` (apagada ao final) depois de todas as correções: sem rolagem horizontal em nenhuma largura, contraste reprovado 0 (claro e escuro), cores fora da paleta 0, gradientes proibidos 0, sombras 0, itálico exatamente 1 por seção onde aparece, 12 marcadores presentes, menu e FAQ funcionam, sem erros de console. Conferi visualmente (leitura de imagem) os PNGs de cada correção: `dobra-1440.png`/`dobra-1024.png` (badge legível, colunas equilibradas), `secao-1440-07-faq.png` (duas colunas, sem vazio), `secao-1440-02-servicos.png` (subtítulos em Argila), `secao-1440-04-relatorio.png` (rótulo em Musgo sobre Sálvia), `secao-1440-06-avaliacoes.png` (rótulo em Argila sobre Linho), `secao-1440-05-protocolos.png` (numeração 1-5), `menu-aberto-390.png` (véu atrás do painel), `dobra-390.png`/`pagina-inteira-1440.png` (nada quebrou no resto da página).

## Problemas conhecidos

- Modo escuro continua deliberadamente neutralizado (`data-tema="claro"` fixo), pelo mesmo motivo documentado na iteração 001 — não era item do feedback-001.md corrigir isso, só documentá-lo melhor no README, o que foi feito.
- `favicon.ico`/`apple-touch-icon.png` continuam gerados por script (não por ferramenta de design), como já documentado.
- Todos os dados pendentes e hipóteses ⚑ seguem listados em `tia-clara/10-site/README.md`, sem nenhum dado inventado como real.
- Não identifiquei nenhum outro "rótulo órfão" além dos três descritos acima (varredura feita lendo o CSS inteiro e conferindo visualmente cada seção com etiqueta/subtítulo depois do fix).

## Dev Server

- URL: http://localhost:3000/
- Status: rodando (não iniciado/parado por mim, conforme instrução)
- Comando: `python3 -m http.server 3000 --directory tia-clara/10-site`
