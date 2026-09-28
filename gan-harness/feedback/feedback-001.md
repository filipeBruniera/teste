# Avaliação — Iteração 001

## Scores

## Evaluation Mode

**Achieved:** `screenshot` (Playwright headless + interações por script; MCP Playwright indisponível nesta sessão).

Rodei `gan-harness/tools/avaliar.js 001` (Playwright headless real, 390/768/1024/1440px, com cliques, teclado, Esc, `prefers-reduced-motion`, `prefers-color-scheme` e página sem JS), inspecionei todos os PNGs gerados com a ferramenta de leitura de imagem, comparei com `07-producao/png/site-home-desktop.png`, `site-home-celular.png`, `relatorio-whatsapp.png` e `ig-01-autoridade-protocolo.png`, li `index.html`/`css/site.css` linha a linha e escrevi dois scripts Playwright auxiliares próprios (um para recortar/ampliar a área do card do herói e confirmar visualmente o corte do marcador de foto, outro para inspecionar `getComputedStyle` dos rótulos `.tc-etiqueta` em todas as seções e confirmar a causa exata de uma inconsistência de cor). Não editei nenhum arquivo do site.

| Criterion | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Design Quality | 7.0/10 | 0.35 | 2.45 |
| Originality (fidelidade à marca) | 8.5/10 | 0.30 | 2.55 |
| Craft | 6.0/10 | 0.25 | 1.50 |
| Functionality | 7.5/10 | 0.10 | 0.75 |
| **TOTAL** | | | **7.3/10** |

## Verdict: FAIL (threshold: 7.5)

Fica muito perto da aprovação — e a maior parte do trabalho é genuinamente boa (o relatório de visita e os protocolos são reconstruções quase 1:1 das peças oficiais, a tipografia e o ritmo de fundos são de estúdio). Mas o herói — a primeira coisa que qualquer visitante vê, na resolução mais comum de desktop — tem um marcador de dado pendente parcialmente ilegível por sobreposição de layout, e isso, somado a um vazio decorativo grande no FAQ e a um bug de CSS que deixa dois rótulos de seção com a cor errada, empurra a nota para baixo do corte. Nenhuma das quatro falhas críticas listadas na rubrica (rolagem horizontal, contraste <4,5:1 de fato renderizado, motivo proibido/dado inventado, seção ausente) ocorre na página **como ela é renderizada** — então a nota não está travada em 6,0 — mas os problemas abaixo são reais, verificados no código e nos PNGs, não hipóteses.

## Critical Issues (must fix)

1. **Marcador "FOTO A CONFIRMAR" do herói cortado pelo cartão de relatório em todas as larguras ≥ 860px (inclui 1024 e 1440, ou seja, a maioria dos desktops/laptops reais)** → Em `tia-clara/10-site/css/site.css`, `.tc-foto__legenda` está alinhada com `align-items: flex-end` dentro de `.tc-foto` (linha 210-213), então a etiqueta tracejada "Foto a confirmar" fica ancorada no rodapé da forma-plaquinha. Ao mesmo tempo, `.tc-hero__cartao` recebe `margin: calc(var(--tc-e9) * -1) 0 0 0` em telas ≥860px (linha 390, `--tc-e9` = 96px) para subir o cartão de relatório sobre a foto — só que a margem negativa é grande o bastante para cobrir exatamente a etiqueta, cortando o texto ao meio (verifiquei com um recrop/zoom do PNG `secao-1440-01-hero.png`: a base das letras de "FOTO A CONFIRMAR" desaparece atrás do cartão branco, ver também `dobra-1024.png`). No modelo aprovado (`07-producao/png/site-home-desktop.png`) o rótulo fica centralizado na forma, longe da sobreposição do cartão — este é um desvio real do ponto de partida, não uma escolha de composição. Como corrigir: ou (a) mover `.tc-foto__legenda` para `align-items: center` / `flex-start` como no modelo aprovado, reservando a base da forma para a sobreposição do cartão; ou (b) reduzir a margem negativa do cartão em telas ≥860px (ou aumentar `padding-bottom` da `.tc-hero__foto`) até que a etiqueta fique inteiramente acima do cartão; ou (c) subir o `z-index`/mover a etiqueta para dentro do próprio cartão como um selo. Qualquer uma resolve — o ponto é que hoje um dos 12 marcadores de dado pendente, que a spec exige "visível e inconfundível", está parcialmente ilegível no primeiro dobra, na largura mais comum de desktop.

## Major Issues (should fix)

1. **Seção FAQ com ~40% da largura em branco decorativo em 1440px** → `tia-clara/10-site/css/site.css` linha 552: `.tc-faq__envolucro > .tc-faq__lista { max-width: 780px; }` deixa a lista de perguntas presa a uma coluna estreita dentro de um `.tc-envolucro` de 1264px, sem nenhum segundo elemento, citação ou imagem preenchendo a metade direita (ver `secao-1440-07-faq.png` e a seção correspondente em `pagina-inteira-1440.png`). O próprio `design-system.md` (§3, "Comportamento") proíbe isso: "respiro sim, vazio decorativo não." Como corrigir: reduza o `.tc-envolucro` desta seção para algo perto de 900-960px e centralize (ou aumente `max-width` da lista para acompanhar a leitura em duas colunas), ou preencha a coluna direita com um elemento da marca (ex. um bloco de contato rápido, uma citação "Pode deixar comigo." em Literata, ou o ícone de telefone com o CTA do WhatsApp) para não deixar bloco vazio.

2. **Bug de especificidade de CSS deixa 2 dos 8 rótulos de seção com a cor errada** → `tia-clara/10-site/css/site.css`: `.tc-etiqueta { color: var(--tc-argila); }` (linha 90) deveria valer para todo `.tc-rotulo` de abertura de seção, mas a regra combinada das linhas 99-104 (`.tc-relatorio__intro > p, .tc-avaliacoes__intro > p { color: var(--tc-texto-secundario); ... }`) tem especificidade maior (classe + combinador de tipo vence classe isolada) e vem depois no arquivo, então captura por acidente os `<p class="tc-etiqueta tc-rotulo">` que também são filhos diretos de `.tc-relatorio__intro`/`.tc-avaliacoes__intro` (`index.html` linhas 204 e 325). Confirmei via `getComputedStyle` ao vivo: "A peça-assinatura" e "Avaliações" renderizam em Musgo (`rgb(86,98,90)`), enquanto "Serviços", "Como funciona", "Perguntas frequentes" e "Fale com a Clara" renderizam em Argila (`rgb(169,78,42)`) — mesma classe, cor diferente, sem nenhuma intenção documentada. Nota à parte: calculei o contraste de Argila `#A94E2A` sobre Sálvia `#DDE1D4` = **4,15:1**, abaixo do mínimo AA de 4,5:1 para texto pequeno (bate com a própria tabela do `design-system.md`, que já avisa "Sálvia só em texto grande (4,2)") — então este acidente de cascata coincidentemente evitou uma falha de contraste real, mas não por design. Como corrigir: dê à `.tc-etiqueta` uma seletor mais específico (ex. `.tc-relatorio__intro > .tc-etiqueta`) ou marque os parágrafos de corpo com uma classe própria (`.tc-intro__texto`) em vez de depender de `> p` cru, para que o cascade pare de vazar entre elementos com papéis diferentes. Depois, decida conscientemente a cor do rótulo sobre Sálvia (Musgo é uma opção válida e seria a mesma escolha seria plausível para consistência com contraste, mas hoje é sorte, não escolha).

3. **README do site afirma uma implementação de menu que não existe no código** → `tia-clara/10-site/README.md` linha 60 diz "Menu do celular é um `<details>/<summary>` nativo — funciona sem JavaScript; o `site.js` só sincroniza `aria-expanded` e fecha com Esc." Mas o `index.html` (linhas 41-52) usa `<nav id="tc-menu">` + `<button class="tc-menu__botao" aria-controls="tc-menu-lista" aria-expanded="false">` + `<ul id="tc-menu-lista">` — nada de `<details>/<summary>`. O próprio `generator-state.md` documenta que essa troca foi feita durante a construção ("troquei por `<nav>` simples com progressive enhancement") mas o README não foi atualizado. Como corrigir: reescreva a linha 60 do README para descrever a implementação real (`<nav>` sempre no DOM, lista empilhada sem JS, botão hambúrguer com `aria-expanded` sincronizado via `site.js` quando há JS).

## Minor Issues (nice to fix)

1. **Numeração inconsistente entre listas semelhantes** → "Como funciona" usa `1 · 2 · 3` (`index.html` em torno da linha 175) e "Protocolos" usa `01 · 02 · 03 · 04 · 05` (em torno da linha 274). Ambas são listas numeradas tipográficas paralelas na mesma página; escolha um padrão (zero-padding ou não) e aplique aos dois para reforçar que fazem parte do mesmo sistema de "registro".
2. **Painel do menu mobile cobre parte do rótulo do herói sem plano de fundo/dim** → em `menu-aberto-390.png`, o painel flutuante do menu sobrepõe o texto "PET SITTER..." e parte do badge "A CONFIRMAR" sem nenhum tratamento de contraste por trás (não é crítico — o menu tem fundo Papel opaco — mas vale avaliar um leve véu Pinho/opacidade atrás do painel para reforçar a hierarquia, como um estúdio faria).
3. **`sameAs` do JSON-LD aponta para uma URL com aparência real** → `index.html`, dentro do `<script type="application/ld+json">`: `"sameAs": ["https://instagram.com/USUARIO_A_CONFIRMAR"]`. Como é uma URL sintaticamente válida, crawlers podem tentar segui-la. Considere remover o campo até ter o @ real, ou usar algo inequivocamente inválido (ex. `"instagram: A CONFIRMAR"` fora de um campo de URL).
4. **`.tc-envolucro` usa `max-width: 1264px`** (`css/site.css` linha 57) contra o "máx. 1200" do grid da spec — na prática bate porque a diferença é só o padding lateral de 32px somado à área de conteúdo de 1200px, mas um comentário no CSS explicando essa conta evitaria dúvida numa auditoria futura.

## What Improved Since Last Iteration

N/A — esta é a primeira iteração avaliada (rodada 1 de 4). Não há linha de base anterior para comparação.

**Pontos fortes que valem registrar para as próximas rodadas não regredirem:**
- O cartão "Relatório de visita" (seção `#relatorio`) é uma reconstrução muito fiel de `relatorio-whatsapp.png` — cabeçalho Pinho com rótulo Latão, linha de registro tabular com ícones corretos, observação com filete Argila, fecho "Tudo certo por aqui." em itálico único, e o cuidado extra de rotular "Thor" como "(exemplo ilustrativo)" em vez de deixar parecer um caso real.
- A seção "Protocolos" reproduz o território de `ig-01-autoridade-protocolo.png` com disciplina: fundo Pinho, acento Latão único (números, filetes, rótulo), zero Argila competindo, fecho "Pode deixar comigo." em itálico.
- Ritmo de fundos entre as 9 seções não repete cor adjacente nenhuma vez (Linho→Papel→Linho→Sálvia→Pinho→Linho→Papel→Linho→Pinho) — evidência de que a alternância foi pensada, não aleatória.
- Nenhum motivo proibido (patinha, osso, coração, cruz, escudo, mascote), nenhuma cor/raio/sombra fora dos tokens (confirmado por grep em `site.css`: zero hex literal, zero `box-shadow`, zero `filter`, um único `gradient` permitido — a hachura do marcador de foto), itálico da Literata exatamente 1 por seção onde aparece e em nenhum outro lugar.
- A argola `◦` é reaproveitada como marcador de lista (`.tc-lista-argola li::before`, `css/site.css` linha 124-133) em vez do bullet padrão do navegador — um uso funcional do dispositivo da marca, não decorativo.
- A seção "Avaliações" evita qualquer depoimento fabricado com uma frase de contexto explícita ("nada aqui foi escrito por um tutor de verdade") em vez de só marcar os cartões — mais alinhado ao princípio "Clara = clareza" do que o mínimo pedido pela spec.
- Site funciona de ponta a ponta sem JavaScript (confirmado em `sem-js-pagina-inteira-390.png`): navegação continua empilhada e acessível, FAQ com `<details>` nativo abre normalmente.
- Foco de teclado visível em todas as 22 paradas (desktop) e 16 (celular), sem exceção.

## What Regressed Since Last Iteration

N/A — primeira iteração.

## Specific Suggestions for Next Iteration

1. Corrija a sobreposição do badge "Foto a confirmar" no herói (ver Critical Issues #1) e depois rode novamente `avaliar.js` para confirmar visualmente (leia `secao-1440-01-hero.png` e `dobra-1024.png` de novo) — esse é o item de maior prioridade porque afeta a primeira impressão em desktop.
2. Resolva o vazio do FAQ em 1440px antes de mexer em qualquer outra coisa de layout — é o segundo problema mais visível numa varredura rápida da página inteira.
3. Depois de corrigir a colisão de especificidade do CSS (Major #2), faça uma varredura de todos os `.tc-etiqueta`/`.tc-rotulo` da página com o mesmo script de `getComputedStyle` usado nesta avaliação, para garantir que não sobrou nenhum outro rótulo "órfão" pegando cor errada por herança de seletor de parágrafo.
4. Ao corrigir o README, aproveite para verificar se mais alguma afirmação do documento ficou desatualizada em relação às decisões tardias descritas em `generator-state.md` (ex. modo escuro travado em `data-tema="claro"` — o README não menciona isso explicitamente, seria bom que mencionasse, já que é uma decisão consciente de escopo).

## Screenshots

Todos em `gan-harness/screenshots/iter-001/`.

- `dobra-1440.png`, `dobra-1024.png`: primeira dobra em desktop — fiel ao modelo aprovado em composição, mas com o corte do badge "FOTO A CONFIRMAR" visível na base da forma-plaquinha, atrás do cartão de relatório.
- `dobra-768.png`, `dobra-390.png`: em coluna única (abaixo do breakpoint de 860px) o badge aparece inteiro, sem sobreposição — confirma que o bug é específico do layout de duas colunas.
- `secao-1440-01-hero.png`: recortada/ampliada via script próprio (`/tmp/.../crop-badge.png`) para confirmar pixel a pixel que o texto "FOTO A CONFIRMAR" é cortado ao meio pela borda superior do cartão branco.
- `secao-1440-04-relatorio.png`, `secao-1440-05-protocolos.png`, `secao-390-05-protocolos.png`: comparados lado a lado com `relatorio-whatsapp.png` e `ig-01-autoridade-protocolo.png` — fidelidade muito alta de tipografia, cor e disposição.
- `secao-1440-07-faq.png` e o trecho correspondente de `pagina-inteira-1440.png`: mostram claramente a coluna de perguntas ocupando menos da metade da largura do envelope, com o resto da seção em branco liso.
- `secao-1440-06-avaliacoes.png`, `secao-390-06-avaliacoes.png`: os três blocos de depoimento-marcador têm alturas/larguras levemente assimétricas (terceiro deslocado), evitando a leitura de "grade de cards idênticos" — funciona, mas a diferença é sutil o suficiente para quase passar despercebida numa varredura rápida.
- `menu-aberto-390.png`: menu mobile funcional, painel flutuante correto, mas sobrepõe parte do rótulo do herói sem véu de fundo.
- `faq-aberto-390.png`: `<details>` abre corretamente, seta gira, texto legível.
- `foco-1440.png`, `foco-390.png`: indicador de foco (contorno Pinho) nítido e consistente em todos os controles testados.
- `escuro-dobra-1440.png`, `escuro-dobra-390.png`: idênticos ao modo claro — confirma que `data-tema="claro"` está de fato neutralizando `prefers-color-scheme: dark`, como o gerador documentou.
- `sem-js-pagina-inteira-390.png`: página inteira sem JavaScript, todas as 9 seções presentes e legíveis, nada quebrado.
