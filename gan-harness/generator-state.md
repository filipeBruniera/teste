# Generator State — Iteração 001

## O que foi construído

Landing page one-page completa da Tia Clara em `tia-clara/10-site/`, HTML+CSS estático (JS vanilla mínimo e opcional), autocontida e sem build, seguindo à risca `tokens.css`/`design-system.md`.

Arquivos criados:
- `tia-clara/10-site/index.html` — as 10 seções do briefing na ordem pedida, `lang="pt-BR"`, um único `h1`, landmarks, link "Pular para o conteúdo", JSON-LD `LocalBusiness`.
- `tia-clara/10-site/css/tokens.css` — cópia fiel de `05-design-system/tokens.css`, só com os caminhos das fontes ajustados para `../assets/fontes/…`.
- `tia-clara/10-site/css/site.css` — todo o estilo do site, só com `var(--tc-…)`; zero cor/fonte/raio/sombra fora dos tokens.
- `tia-clara/10-site/js/site.js` — opcional: liga o botão do menu do cabeçalho (mostra/esconde, Esc fecha, fecha ao clicar num link). Sem JS, a navegação continua visível e funcional (lista empilhada abaixo do cabeçalho) — testado com JS desligado.
- `tia-clara/10-site/assets/logo/*.svg` — assinatura horizontal compacta, versão "sobre-pinho" (rodapé), símbolo (Pinho e Latão), ícone do app, copiados de `04-logo/master`.
- `tia-clara/10-site/assets/fontes/*` — Literata e Instrument Sans + licenças OFL, copiadas de `05-design-system/fontes`.
- `tia-clara/10-site/assets/og-capa.png` — imagem de Open Graph gerada no estilo das peças de autoridade da marca (Pinho + Literata + filete de latão), não é fotografia.
- `favicon.svg` (símbolo, vetorial), `favicon.ico` e `apple-touch-icon.png` — gerados a partir de `04-logo/master/tc-app-icon.svg` via Playwright (renderização + montagem manual do contêiner ICO), já que não havia rsvg-convert/ImageMagick disponíveis.
- `tia-clara/10-site/README.md` — como publicar (GitHub Pages/Netlify/local) e a lista completa dos 12 marcadores `data-marcador`, dos 3 links `wa.me/55XXXXXXXXXXX` e dos campos placeholder do JSON-LD, mais a lista de hipóteses ⚑ da estratégia usadas no texto.

## Decisões de composição por seção

- **Cabeçalho**: assinatura horizontal compacta + navegação por âncoras + "Agendar apresentação" (Argila), sempre ligado a um `wa.me` real. Menu do celular é um `<nav>` simples sempre no DOM: sem JS a lista fica visível e empilhada (funciona sem JavaScript); com JS (classe `tc-js` ligada por um script inline mínimo), o botão hambúrguer→X esconde/mostra a lista, sincroniza `aria-expanded`, fecha com Esc e ao clicar fora ou num link.
- **Hero**: reconstrução fiel da primeira dobra aprovada (`site-home-desktop.html`/`celular.html`) — rótulo com argola, "Pode deixar comigo." em Literata, 2 CTAs, 3 provas com ícone, foto-plaquinha com hachura Sálvia + marcador de foto, cartão de relatório reduzido (Thor) sobreposto por baixo, único acento Argila.
- **Serviços** (fundo Papel): dueto assimétrico com filete divisório central — pet sitting (casa) e passeios (guia) — em vez de grade de cards idênticos; preço sempre como marcador, nunca valor inventado.
- **Como funciona** (fundo Linho): linha do tempo tipográfica com numerais grandes em Argila e traço superior, não cartões.
- **Relatório de visita** (fundo Sálvia — "fundo de relatório" no design system): a peça-assinatura, réplica fiel de `relatorio-whatsapp.png` — faixa Pinho com rótulo em Latão, nome do pet ("Thor", mesmo exemplo das peças oficiais, identificado como "exemplo ilustrativo"), linhas de registro com ícones (chave/checagem/guia), foto-marcador, observação com filete Argila, fecho "Tudo certo por aqui." em itálico.
- **Protocolos** (fundo Pinho, único acento Latão): lista numerada 01–05 com filetes de latão entre itens, réplica do território de `ig-01-autoridade-protocolo.png`, fecho "Pode deixar comigo." em itálico — nenhum marcador aqui (protocolos ⚑ documentados no README, não como dado pendente visível).
- **Avaliações**: estatística de 83% como bloco-marcador "NÃO CONFIRMADO" à esquerda + três blocos-depoimento deliberadamente assimétricos (alturas e larguras diferentes, terceiro deslocado) para não parecer grade de cards repetidos — todos com `data-marcador` e texto que deixa claro que é placeholder.
- **FAQ**: `<details>/<summary>` nativos, perguntas em Literata (voz) sobre fundo Papel, sem cartões — 6 perguntas reais das objeções da estratégia (chave, emergência, gatos, medicação, grupo, relatório).
- **CTA WhatsApp**: painel Papel elevado sobre Linho, único acento Argila, número do WhatsApp como marcador visível ao lado do botão.
- **Rodapé** (fundo Pinho): assinatura "sobre-pinho", marcadores de telefone/Instagram, filete de latão, uma linha de privacidade (sem fachada/endereço/geolocalização), créditos OFL.

## Verificação automática

Rodei `gan-harness/tools/avaliar.js` várias vezes durante a construção (iteração de teste `000`, apagada ao final conforme instruído) em 390/768/1024/1440px. Estado final, tudo limpo:
- Sem rolagem horizontal em nenhuma largura; sem elementos fora da tela.
- Contraste reprovado: 0 (claro e escuro) · cores fora da paleta: 0 · gradientes proibidos: 0 (só a hachura permitida) · sombras: 0.
- Itálico Literata: exatamente 1 por seção onde aparece (hero, relatório, protocolos) — em nenhum outro lugar.
- Nenhuma plaquinha em botão/campo, nenhum texto < 12px, nenhum alvo de toque abaixo do mínimo (44px no celular / 24px no resto), foco visível em todas as 22 (desktop) / 16 (celular) paradas de teclado.
- Nenhuma palavra proibida do banco de produção; "83%" só aparece dentro de `[data-marcador]`.
- 12 marcadores `data-marcador` presentes e listados; JSON-LD `LocalBusiness` válido; menu e FAQ funcionam (testado clique + Esc); sem JS a navegação continua acessível; sem erros de console nem requisições falhas.
- Corrigi durante o processo: nav do cabeçalho estourando a viewport em 1024px (bug de `<details>` colapsando o layout — troquei por `<nav>` simples com progressive enhancement), modo escuro com 32 falhas de contraste (optei por travar o tema claro via `data-tema="claro"`, já que o modo escuro é "desejável, não obrigatório" e uma implementação completa exigiria auditar cada componente customizado), badge "Foto a confirmar" sendo cortado pela moldura-plaquinha, e o ícone do botão de WhatsApp renderizando em Pinho (baixo contraste) dentro do botão Argila em vez de herdar Linho.

## Problemas conhecidos

- Modo escuro (`prefers-color-scheme: dark`) está deliberadamente neutralizado (`data-tema="claro"` fixo no `<html>`) para não arriscar falhas de contraste em componentes customizados (marcadores, cartões, cabeçalho) que usam cor primitiva (`--tc-papel`/`--tc-pinho`) em vez da semântica. Pode ser retomado numa próxima iteração se for prioridade — exigiria trocar os usos diretos de `--tc-papel`/`--tc-pinho` por `--tc-fundo-elevado`/`--tc-fundo-inverso` nos componentes e testar contraste de novo.
- `favicon.ico`/`apple-touch-icon.png` foram gerados por script (Playwright + montagem manual do contêiner ICO), não por uma ferramenta de design; visualmente conferem com `tc-app-icon.svg`, mas vale um Ctrl+F por "gerado por script" antes de publicar se a Clara quiser trocar por arte oficial.
- Todos os dados pendentes (bairro/cidade, telefone, Instagram, preços, fotos, depoimentos, estatística de 83%, número de WhatsApp nos 3 links `wa.me/55XXXXXXXXXXX`) e as hipóteses ⚑ da estratégia (passeio em grupo, lista de protocolos como prática já estabelecida) estão documentados em `tia-clara/10-site/README.md` — nada foi inventado como se fosse real.

## Dev Server

- URL: http://localhost:3000/
- Status: rodando (não iniciado/parado por mim, conforme instrução)
- Comando: `python3 -m http.server 3000 --directory tia-clara/10-site`
