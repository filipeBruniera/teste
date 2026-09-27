# Site da Tia Clara — `tia-clara/10-site/`

Landing page one-page, estática (HTML + CSS, um pouco de JS vanilla e opcional). Sem build, sem dependências externas obrigatórias. Segue à risca `tia-clara/05-design-system/tokens.css` e `design-system.md` — nenhuma cor, fonte, raio ou sombra fora dos tokens.

## Como publicar

O site é autocontido: basta subir a pasta `tia-clara/10-site/` inteira para qualquer hospedagem estática.

- **GitHub Pages**: publique esta pasta como raiz do Pages (ou copie o conteúdo para `docs/`/`gh-pages`).
- **Netlify / Vercel**: aponte o "publish directory" para `tia-clara/10-site`. Não há comando de build.
- **Localmente**: `python3 -m http.server 3000 --directory tia-clara/10-site` e abra `http://localhost:3000/`.

Antes de publicar de verdade, resolva a lista de marcadores abaixo — todos vêm marcados em amarelo/tracejado no próprio layout (`data-marcador="…"` no código, estilo `.tc-marcador`), então dá para achá-los buscando por `data-marcador=` no `index.html`.

## Marcadores — dados pendentes (não inventados)

| `data-marcador` | Onde aparece | O que falta |
|---|---|---|
| `bairro-cidade` | Rótulo do herói | Bairro e cidade reais de atuação |
| `preco-pet-sitting` | Serviços · Pet sitting | Valor por visita — **nunca foi inventado um número** |
| `preco-passeio` | Serviços · Passeios | Valor por passeio — **nunca foi inventado um número** |
| `foto-hero` | Herói | Foto real do pet em casa, altura dos olhos, luz natural (ver regras de fotografia do design system) |
| `foto-relatorio` | Relatório de visita | Foto real do passeio/visita |
| `estatistica-83` | Avaliações | "83% dos tutores prefeririam pet sitting a domicílio" — pesquisa Rover 2026, **não confirmada**; confirmar a fonte antes de publicar como fato, ou remover |
| `depoimento-1`, `depoimento-2`, `depoimento-3` | Avaliações | Depoimentos reais, com autorização do tutor — os textos atuais são só placeholders explícitos, não citações reais |
| `whatsapp-numero` | CTA final | Número de WhatsApp visível junto ao botão |
| `telefone` | Rodapé | Telefone/WhatsApp para contato |
| `area-atendimento` | Rodapé | Bairros e cidade atendidos (área, nunca endereço), iguais aos do Perfil de Empresa no Google |
| `instagram` | Rodapé | @ do Instagram |

Além dos marcadores visíveis, há marcadores **de código** que precisam ser trocados antes de publicar:

| Marcador | Onde | O que vai no lugar |
|---|---|---|
| `55XXXXXXXXXXX` | os três links `wa.me` (cabeçalho, herói, CTA final) | número real do WhatsApp, com DDI e DDD |
| `[DOMINIO]` | `canonical`, `og:url`, `og:image`, `twitter:image`, JSON-LD, `robots.txt`, `sitemap.xml` | domínio do site, sem barra final (ex.: `tiaclara.com.br`) |
| `[BAIRRO]`, `[CIDADE]` | `<title>`, meta description, JSON-LD `areaServed` | bairro principal e cidade |
| `[TELEFONE]` | JSON-LD `telephone` | telefone no formato `+55 11 91234-5678` |
| `[FAIXA_DE_PRECO]` | JSON-LD `priceRange` | faixa de preço (ex.: `R$ 60–120`) ou remova a chave |
| `[DATA_DE_PUBLICACAO]` | `sitemap.xml` | data de publicação, `AAAA-MM-DD` |

Para conferir que não sobrou nenhum: `grep -rnE "\[[A-Z_]+\]|55X{5,}" tia-clara/10-site --include=*.html --include=*.txt --include=*.xml` não pode retornar nada. O JSON-LD não tem `sameAs` (Instagram) de propósito, até haver um @ real: adicione `"sameAs": ["https://instagram.com/SEU_USUARIO"]` quando existir. Não adicione `aggregateRating` nem `review` enquanto os depoimentos forem marcadores.

A lista completa do que falta para publicar, incluindo as promessas a confirmar com a Clara, está em [`../11-lancamento/checklist-pre-lancamento.md`](../11-lancamento/checklist-pre-lancamento.md).

Nenhum preço, telefone, @ de Instagram, nome de cliente, depoimento ou estatística foi inventado como se fosse real: tudo isso está marcado.

## Hipóteses de estratégia (⚑) usadas no texto

A `01-estrategia/estrategia.md` marca alguns protocolos e diferenciais como hipóteses (⚑), não confirmados com a Clara. Eles aparecem no site porque a especificação permite ("podem aparecer, mas o README deve dizer que precisam ser confirmados"). Confirmar antes de publicar:

- **Passeio em grupo pequeno** (seção Serviços e FAQ): o site descreve o padrão como individual, com grupo pequeno "a combinar" — confirmar se a Clara realmente oferece essa opção.
- **Protocolo completo** (visita de apresentação, ficha do pet, chaves codificadas, equipamento com trava, autorização de emergência, contrato, continuidade): a seção Protocolos apresenta esses itens como prática já estabelecida. Confirmar item a item que é o que a Clara de fato faz antes de publicar — a marca só pode prometer o que é verdade.
- O relatório de "Thor" (seção Relatório de visita) é um **exemplo ilustrativo** do formato — igual ao usado nas peças oficiais de produção (`relatorio-whatsapp.png`) — e está identificado como exemplo no próprio texto. Não é um depoimento nem um caso real.

## Estrutura

```
10-site/
  index.html          um h1, uma seção por bloco do briefing, JSON-LD LocalBusiness (área de atendimento, sem endereço)
  css/tokens.css       cópia de 05-design-system/tokens.css (só caminho das fontes mudou)
  css/site.css         estilos do site, só com var(--tc-…)
  js/site.js           opcional: sincroniza aria-expanded do menu, Esc fecha, funciona sem JS
  assets/logo/…         SVGs copiados de 04-logo/master
  assets/fontes/…       Literata e Instrument Sans (OFL) — WOFF2 com subconjunto, ver "Fontes" abaixo
  assets/og-capa.png    imagem de compartilhamento (Open Graph), gerada no estilo das peças de autoridade — não é fotografia, é tipografia da marca
  favicon.svg / favicon.ico / apple-touch-icon.png
  robots.txt / sitemap.xml   com o marcador [DOMINIO]
```

## Fontes

`assets/fontes/` guarda só as versões **web** (WOFF2, com subconjunto) de Literata e Instrument Sans — as origens completas (TTF variável) continuam em `05-design-system/fontes/`, a fonte da verdade. Quem gera as versões web é `tia-clara/_fonte/fontes-web.py` (`pip install fonttools brotli`; depois `python3 tia-clara/_fonte/fontes-web.py`), que:

- Recorta o glyph set para Latin básico + Latin-1 Supplement inteiro (todos os acentos do português: á à â ã é ê í ó ô õ ú ü ç, maiúsculas incluídas) + a pontuação tipográfica usada ou prevista no site (– — “ ” ‘ ’ • …), preservando `kern`, `liga`, `ccmp`, `locl`, `calt`, `mark`, `mkmk` e os recursos de algarismo (`tnum`, `onum`, `lnum`, `pnum` — `tnum` é o que os horários de `.tc-dado` e os números de `.tc-protocolo__numero` realmente usam).
- Restringe (`fontTools.varLib.instancer`) só os eixos variáveis que o CSS deste site **não** varia: o peso da Literata itálica (só usada em `--tc-afeto`, sempre 400) fica fixo; a largura (`wdth`) da Instrument Sans (nunca acionada — nada usa `font-stretch` nem `font-variation-settings: 'wdth'`) fica fixa em 100 (normal). Os eixos que o CSS de fato varia continuam variáveis: peso da Literata normal (400–600, títulos e corpo de depoimento), peso da Instrument Sans (400–700) e `opsz` da Literata (7–72, intocado) — o navegador ajusta o `opsz` sozinho por tamanho (`font-optical-sizing: auto`, padrão do CSS), do afeto pequeno ao display grande, então o eixo precisa continuar variável mesmo sem nenhum `font-variation-settings` explícito no CSS.
- Não gera `InstrumentSans-Italic.woff2`: nenhum elemento do site pede itálico nesta família (o único itálico do site é a voz, em Literata) — carregar esse arquivo seria puro desperdício. Se um itálico de Instrument Sans passar a ser necessário, gere-o a partir de `05-design-system/fontes/InstrumentSans-Italic[wdth,wght].ttf` do mesmo jeito.
- Compila direto em WOFF2 (usa o pacote `brotli`) — os `@font-face` de `css/tokens.css` já apontam pros arquivos `.woff2`, com `font-display: swap` e `unicode-range` batendo com o subconjunto.

Resultado: as 4 fontes TTF (~2,2 MB juntas, sendo ~1,8 MB só de Literata) viraram 3 WOFF2 (~150 KB juntos) sem trocar peso, tamanho, itálico ou glifo nenhum do que a página realmente usa. Os `.txt` de licença (`*-OFL.txt`) continuam junto dos arquivos, como a OFL exige.

Sem `<link rel="preload">` para as fontes: `css/tokens.css` já é o primeiro `<link rel="stylesheet">` do `<head>`, então o navegador descobre os `@font-face` cedo mesmo sem preload, e cada arquivo WOFF2 já é pequeno (27–76 KB). Testado sem preload e não há ganho perceptível — e um preload mal calibrado (sem `crossorigin`, ou de um arquivo que a página não acaba usando naquela largura) baixa o arquivo duas vezes ou dispara aviso de "preload não usado" no console, então foi uma troca consciente, não esquecimento.

## Acessibilidade e responsivo

- `lang="pt-BR"`, um único `h1`, hierarquia de títulos em ordem, landmarks (`header`, `nav`, `main`, `footer`), link "Pular para o conteúdo" como primeiro elemento focável.
- Contraste: só usa os pares aprovados no design system (ex. Argila sobre Papel/Linho, nunca Argila sobre Sálvia em texto pequeno — por isso o rótulo "A peça-assinatura", que cai sobre o fundo Sálvia da seção Relatório, usa Musgo em vez de Argila; Latão só sobre Pinho).
- Menu do celular é um `<nav>` sempre presente no DOM: **sem JavaScript**, a lista de links fica visível e empilhada logo abaixo do cabeçalho — a navegação funciona inteira sem JS. Com JavaScript, um script mínimo inline liga a classe `tc-js` ao `<html>`; ela ativa o botão hambúrguer, e o `site.js` alterna a exibição da lista (painel flutuante com um véu Pinho semitransparente atrás, para separar do conteúdo por baixo), sincroniza `aria-expanded`, fecha com Esc, ao clicar fora (inclusive no véu) e ao clicar num link.
- Modo escuro fica travado no claro: `data-tema="claro"` no `<html>` neutraliza `prefers-color-scheme: dark` de propósito. É uma decisão consciente de escopo, não um esquecimento — ativar o modo escuro de verdade exigiria trocar os usos diretos de `--tc-papel`/`--tc-pinho` nos componentes customizados (marcadores, cartões, cabeçalho) pelas variáveis semânticas (`--tc-fundo-elevado`/`--tc-fundo-inverso`) e reauditar o contraste de cada um antes de reativar.
- Testado sem rolagem horizontal de 390 a 1440 px. `prefers-reduced-motion` zera as transições via tokens.
