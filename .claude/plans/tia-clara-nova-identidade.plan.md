# Plano: Tia Clara, nova identidade (v2)

**PRD de origem**: `.claude/prds/tia-clara-nova-identidade.prd.md`
**Marco escolhido**: 1 · Direção escolhida. A Clara escolhe 1 entre 3 paletas em verde-sálvia médio e 1 entre 2 ou 3 caminhos de logo inspirados na referência.
**Complexidade**: Médio

## Resumo
O marco produz as opções para a Clara decidir. Ele **não** entrega a identidade final (isso é o marco 2).

Entregas:
- 3 paletas em verde-sálvia médio, com contraste validado;
- 2 ou 3 caminhos (rotas) de logo em vetor, cada um com símbolo, assinatura e versão reduzida testada em tamanho pequeno;
- as rotas aplicadas em três peças mínimas: avatar, cabeçalho do relatório e primeira dobra do site;
- pranchas em PNG no formato do WhatsApp, para ela responder "paleta X, rota Y".

Tudo fica numa pasta nova, `tia-clara/12-identidade-v2/`. A v1 continua intacta como histórico.

## Padrões a seguir
| Categoria | Origem | Padrão |
|---|---|---|
| Nomes | `tia-clara/_fonte/marca.py:254` | Arquivos `tc-{nome}.svg`, em português e sem acento; pastas numeradas (`03-territorios/`, `04-logo/`) |
| Geração de vetor | `tia-clara/_fonte/marca.py:39-89`, `:178` | Texto convertido em curvas com uharfbuzz e fontTools (`glifos`, `d_de`); documento montado por `svg_doc(conteudo, viewBox, título)`; o SVG final não depende de fonte instalada |
| Renderização | `tia-clara/_fonte/render.js:1`, `renderizar-producao.js:1` | HTML → PNG com Playwright (`node render.js in.html out.png w h [escala]`); lotes a partir de uma lista |
| Erros e registro | `tia-clara/_fonte/marca.py:308` | Scripts imprimem `ok` por item e deixam a exceção do Python estourar. Não há validador de contraste: `brandbook.py:81` só tem os valores escritos à mão. O gate de contraste deste plano é novo e mínimo (sai com código 1 e uma mensagem) |
| Testes | `tia-clara/_fonte/teste-L1.html` → `04-logo/testes/teste-L1.png` | Sem framework de testes. A validação é uma prancha de redução (16, 32 e 48 px), em 1 cor e sobre fundos claro e escuro, mais revisão visual |
| Documento de opções | `tia-clara/03-territorios/territorios.md:1-30` | Tabela comparando as rotas (ideia, símbolo, tipografia, cor, o que distingue, o que pode dar errado), mais um scorecard do gate |
| Estado do projeto | `tia-clara/00-brief/brand-state.json` | Fase, gates concluídos, locais dos arquivos e pendências |

## Arquivos a alterar
| Arquivo | Ação | Por quê |
|---|---|---|
| `tia-clara/00-brief/brief.json` | UPDATE | Bloco `v2`: Ubatuba (região central), credencial, verde-sálvia médio, lista "não pode" (colega, "Cuidar também é um ato de amor", Clínica Itaguá), referência |
| `tia-clara/00-brief/brand-state.json` | UPDATE | Reabre as fases C1 e L1 para a v2; registra as pendências novas |
| `tia-clara/12-identidade-v2/00-brief-v2.md` | CREATE | Requisitos da v2 numa página só (derivados do PRD) |
| `tia-clara/12-identidade-v2/01-diagnostico.md` | CREATE | O que falhou na v1 e o que a Clara gosta na referência, com os riscos (genérico, ilegível em tamanho pequeno) |
| `tia-clara/_fonte/v2_paletas.py` | CREATE | Define as 3 paletas, mede o contraste e o "quão claro", gera a prancha HTML; sai com código 1 se algum par de texto reprovar |
| `tia-clara/12-identidade-v2/02-paletas/` | CREATE | `paletas.json`, `paletas.html` e `paletas.png` |
| `tia-clara/12-identidade-v2/fontes/` | CREATE | Fontes OFL novas (cursiva e sans humanista), com as licenças |
| `tia-clara/_fonte/v2_rotas.py` | CREATE | Gera os SVGs de cada rota (símbolo, assinatura com "Ubatuba" e descritor, versão reduzida), com o mesmo método de `marca.py` |
| `tia-clara/12-identidade-v2/03-rotas/` | CREATE | `rota-{a,b,c}/tc-*.svg`, `teste-reducao.html` e `.png`, `rotas.md` |
| `tia-clara/_fonte/v2_apresentacao.py` | CREATE | Monta as aplicações mínimas e as pranchas para a Clara |
| `tia-clara/12-identidade-v2/04-apresentacao/` | CREATE | `1-paletas.png`, `2-rotas.png`, `3-aplicacoes-rota-*.png` (1080×1350) |
| `tia-clara/README.md` | UPDATE | Linha da pasta `12-identidade-v2/` |
| `.claude/prds/tia-clara-nova-identidade.prd.md` | UPDATE | Marco 1 `in-progress` agora e `complete` quando a Clara escolher |

## Tarefas

### Tarefa 1: consolidar os requisitos da v2
- **Ação**:
  - Escrever `00-brief-v2.md` com o que precisa ser verdade e o que não pode acontecer, conforme o PRD: sálvia médio, credencial, região central de Ubatuba, frase de apoio com "quem mais importa", e a lista "não pode".
  - Acrescentar o bloco `v2` ao `brief.json` e atualizar o `brand-state.json`.
- **Seguir**: estrutura de `brief.json` e `brand-state.json`.
- **Validar**: `python3 -c "import json; [json.load(open(f)) for f in ('tia-clara/00-brief/brief.json','tia-clara/00-brief/brand-state.json')]"`; cada item "não pode" do PRD aparece no brief.

### Tarefa 2: diagnóstico da v1 e da referência
- **Ação**: uma página com dois quadros.
  - **Por que a v1 falhou:** verde quase preto dominante; metal (latão); arco que lembra lápide; serifa pesada e dramática; pêssego sobre escuro, que leva ao "Barbie gótica"; e a parecença com a colega (TBD).
  - **O que a referência tem de bom e de arriscado:**
    - Bom: bicho ilustrado, litoral de Ubatuba, sol quente, cursiva.
    - Arriscado: silhueta no pôr do sol e selo com cão e gato são **clichês da categoria**; o detalhe some em 32 px; a patinha.
  - Daí saem os critérios das rotas.
- **Seguir**: formato de tabela de `03-territorios/territorios.md`.
- **Validar**: o documento termina com 5 a 7 critérios verificáveis, que serão reusados no scorecard da tarefa 5.

### Tarefa 3: três paletas em verde-sálvia médio
- **Ação**: em `v2_paletas.py`, definir 3 paletas com os mesmos papéis:
  - sálvia médio (cor principal);
  - verde de texto, escuro o bastante para ler, mas **não** quase preto;
  - fundo creme ou areia;
  - acento quente (o sol);
  - opcional: acento mar.
  - As 3 variam em temperatura: sálvia mais cinza, mais amarelado ou mais azulado.
  - "Sálvia médio" quantificado como **saturação 12–30 %** e **luminosidade 50–65 %** em HSL. O verde de texto precisa ter **luminosidade ≥ 25 %**, bem acima do pinho da v1, que tem ~17 %.
  - O script calcula o contraste WCAG de todos os pares de texto (≥ 4,5:1; ≥ 3:1 em texto grande) e gera `paletas.html` com amostras, pares e um mini-cartão de cada paleta.
- **Seguir**: tokens com nome e papel, como em `05-design-system/tokens.json`.
- **Validar**: `python3 tia-clara/_fonte/v2_paletas.py` sai com código 0 e imprime a tabela de contraste. Renderizar com `render.js` para `paletas.png`.

### Tarefa 4: tipografia da v2
- **Ação**: escolher e baixar para `12-identidade-v2/fontes/` duas famílias OFL:
  - uma **cursiva legível e adulta** para "Tia Clara", como na referência de que ela gosta, mas sem cara de convite infantil nem clichê;
  - uma **sans humanista** para o descritor, a credencial e os textos.
  - Critérios:
    - licença OFL;
    - acentos do português (ç ã é ô);
    - "Tia Clara" legível a 24 px;
    - não arredondada ao ponto de infantilizar.
  - Levar 2 cursivas candidatas para a tarefa 5.
- **Seguir**: `05-design-system/fontes/` (fonte + `*-OFL.txt`).
- **Validar**: um script com fontTools confirma que cada fonte tem os glifos de "Tia Clara Ubatuba Auxiliar de veterinário · Pet sitter & dog walker ÇÃÉÔ".

### Tarefa 5: rotas de logo (2 ou 3), em vetor
- **Ação**: `v2_rotas.py` gera, para cada rota, o símbolo, a assinatura completa (nome, descritor e "UBATUBA") e a **versão reduzida** (avatar e favicon). Proposta inicial, a ajustar pelo diagnóstico:
  - **Rota A · Selo do litoral:** selo com cão e gato de perfil em traço único (monoline, poucas linhas), sol e mar ou serra; nome na sans humanista. A redução é só o sol sobre o mar com uma orelha.
  - **Rota B · Assinatura:** "Tia Clara" na cursiva, com um símbolo pequeno e próprio (o sol nascendo sobre o mar de Ubatuba, com o contorno de cão e gato no horizonte). É a mais tipográfica, a mais legível em tamanho pequeno e a menos genérica.
  - **Rota C · A Clara com eles:** a silhueta dela com cão e gato, que a Clara gostou na referência, redesenhada com um elemento próprio. **Só entra se passar no critério de distinção**, porque é o maior risco de clichê.
  - Montar `teste-reducao.html` (16, 32 e 48 px; 1 cor; fundo claro e escuro) e `rotas.md` com a tabela comparativa e o scorecard dos critérios da tarefa 2.
- **Seguir**: `marca.py` (glifos em curvas, `svg_doc`, `salva`, prefixo `tc-`); prancha de `teste-L1.html`.
- **Validar**:
  - `python3 tia-clara/_fonte/v2_rotas.py` imprime `ok` por arquivo;
  - todo SVG sem `<text>`: `grep -L "<text" tia-clara/12-identidade-v2/02-rotas/*/*.svg`;
  - a prancha de redução renderizada e revisada: cada símbolo precisa ser reconhecível a 32 px;
  - `grep -ri "ato de amor" tia-clara/12-identidade-v2 --include=*.svg --include=*.html` não retorna nada. Os `.md` citam a frase como proibida.

### Tarefa 6: aplicações mínimas e pranchas para a Clara
- **Ação**: `v2_apresentacao.py` aplica cada rota, na paleta que combinar melhor com ela, em:
  1. avatar circular (Instagram e WhatsApp), em 110 px e em 32 px;
  2. cabeçalho do relatório de visita;
  3. primeira dobra do site, simplificada.
  - Depois monta as pranchas em 1080×1350, em linguagem simples e com opções numeradas:
    - `1-paletas.png`: "Paleta 1, 2 ou 3?"
    - `2-rotas.png`: "Rota A, B ou C?"
    - uma prancha de aplicação por rota.
  - O texto das pranchas usa a credencial e a frase de apoio do brief v2.
- **Seguir**: o fluxo HTML → PNG de `producao.py` + `renderizar-producao.js` (com `lista.json`).
- **Validar**: `NODE_PATH=$(npm root -g) node tia-clara/_fonte/renderizar-producao.js`, ou uma variante que aponte para `12-identidade-v2/03-apresentacao/`, gera todos os PNGs; nenhum texto abaixo de 28 px em 1080 (regra de `07-producao/producao.md`).

### Tarefa 7: checagem de distinção (depende de material externo)
- **Ação**: prancha lado a lado com a logo da colega e a identidade da Clínica Veterinária Itaguá, comparando as 2 ou 3 rotas.
- **Bloqueio**: precisa da foto ou do link da logo da colega e da identidade da clínica. Sem isso, a tarefa fica marcada como **pendente** nas pranchas e no PRD, e a Clara escolhe sabendo que a distinção ainda não foi verificada.
- **Validar**: a prancha existe, ou a pendência está registrada.

### Tarefa 8: registrar e entregar
- **Ação**:
  - atualizar o `tia-clara/README.md` e o PRD (marco 1 `in-progress`);
  - fazer commit e push;
  - enviar as pranchas por aqui para você repassar à Clara.
  - Quando ela responder, registrar a escolha em `12-identidade-v2/decisao.md` e marcar o marco 1 como `complete`.
- **Validar**: `git status` limpo depois do push; as pranchas abrem no celular.

## Validação
```bash
pip install fonttools uharfbuzz brotli
python3 tia-clara/_fonte/v2_paletas.py                  # sai com código 1 se algum par de texto reprovar no contraste
python3 tia-clara/_fonte/v2_rotas.py                    # "ok" por SVG
python3 tia-clara/_fonte/v2_apresentacao.py
NODE_PATH=$(npm root -g) node tia-clara/_fonte/render.js tia-clara/12-identidade-v2/02-rotas/teste-reducao.html tia-clara/12-identidade-v2/02-rotas/teste-reducao.png 1600 900
grep -rL "<text" tia-clara/12-identidade-v2/02-rotas/*/*.svg   # lista todos (nenhum usa <text>)
! grep -rqi "ato de amor" tia-clara/12-identidade-v2 --include=*.svg --include=*.html --include=*.json   # a frase da clínica não aparece nas peças (os .md a citam como proibida)
python3 -c "import json; json.load(open('tia-clara/00-brief/brief.json')); json.load(open('tia-clara/00-brief/brand-state.json'))"
```

## Riscos
| Risco | Probabilidade | Mitigação |
|---|---|---|
| **Ilustração feita por código fica aquém da referência** (a referência é xilogravura detalhada; o vetor gerado por script funciona bem para traço simples, não para ilustração rica) | Alta | Rotas com monoline e poucas formas. Se a Clara escolher uma rota que peça ilustração rica, o marco 2 recomenda um ilustrador ou uma ferramenta de geração de imagem para a arte final, com o sistema (cores, tipografia, redução) já decidido aqui |
| **A logo da colega não chegar**, e a distinção não poder ser verificada | Alta | Tarefa 7 com bloqueio explícito; rota B como a opção menos genérica; pedir a imagem antes de apresentar |
| Download da fonte cursiva bloqueado pela rede do ambiente | Média | Baixar do repositório `google/fonts` no GitHub, que o proxy libera. Se falhar, pedir o arquivo ou usar uma alternativa OFL já disponível |
| O verde de texto legível trazer de volta o "escuro" | Média | Limite medido: luminosidade ≥ 25 % e verde escuro só no texto, nunca como fundo dominante; o sálvia médio lidera a área |
| Cursiva e ilustração puxarem para o infantil | Média | Critério "não infantil" no scorecard da tarefa 5 e no teste de 5 segundos do marco 2 |
| Escolha ambígua da Clara pelo WhatsApp | Baixa | Opções numeradas e uma pergunta direta em cada prancha |
| Invadir o marco 2 (refinar a rota antes da escolha) | Média | Parar na escolha: sem versões finais, variações de cor da logo ou brand book |

## Aceite
- [x] Tarefas 1–6 e 8 completas; tarefa 7 **bloqueada** (falta a logo da colega), com a pendência registrada nas pranchas, em `rotas.md`, no `brand-state.json` e no PRD
- [x] `v2_paletas.py` passa: 3 paletas com sálvia médio dentro da faixa medida e todos os pares de texto AA (o sol virou só acento gráfico: verde sobre sol dava 3,1–4,3:1)
- [x] 3 rotas com símbolo, assinatura e versão reduzida: B ✅ a 32 px; C lida como ilhas e sol a 32 px (✅ a 48 px); A no limite a 32 px (registrado no scorecard)
- [x] Nenhum item da lista "não pode" (grep da frase e revisão visual)
- [x] Pranchas 1080×1350 prontas para enviar à Clara (sem texto < 28 px nem sobreposição, checado pelo `v2_renderizar.js`)
- [x] Padrões seguidos (`marca.py`, `render.js`, `teste-L1`), não reinventados. `marca.py` ganhou só a decomposição de glifos compostos, e a v1 regenerada saiu idêntica
- [ ] Escolha da Clara registrada, fechando o marco 1
