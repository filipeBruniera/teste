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
| `instagram` | Rodapé | @ do Instagram |

Além dos marcadores visíveis, os três links `https://wa.me/55XXXXXXXXXXX` (cabeçalho, herói e CTA final) usam um número de exemplo óbvio (puro `X`) — troque pelo número real nos três lugares (buscar por `wa.me/55XXXXXXXXXXX`) antes de publicar. O JSON-LD (`<script type="application/ld+json">` no `<head>`) também tem `telephone`, `areaServed` e `sameAs` com o mesmo tipo de placeholder — ajuste junto.

Nenhum preço, telefone, @ de Instagram, nome de cliente, depoimento ou estatística foi inventado como se fosse real: tudo isso está marcado.

## Hipóteses de estratégia (⚑) usadas no texto

A `01-estrategia/estrategia.md` marca alguns protocolos e diferenciais como hipóteses (⚑), não confirmados com a Clara. Eles aparecem no site porque a especificação permite ("podem aparecer, mas o README deve dizer que precisam ser confirmados"). Confirmar antes de publicar:

- **Passeio em grupo pequeno** (seção Serviços e FAQ): o site descreve o padrão como individual, com grupo pequeno "a combinar" — confirmar se a Clara realmente oferece essa opção.
- **Protocolo completo** (visita de apresentação, ficha do pet, chaves codificadas, equipamento com trava, autorização de emergência, contrato, continuidade): a seção Protocolos apresenta esses itens como prática já estabelecida. Confirmar item a item que é o que a Clara de fato faz antes de publicar — a marca só pode prometer o que é verdade.
- O relatório de "Thor" (seção Relatório de visita) é um **exemplo ilustrativo** do formato — igual ao usado nas peças oficiais de produção (`relatorio-whatsapp.png`) — e está identificado como exemplo no próprio texto. Não é um depoimento nem um caso real.

## Estrutura

```
10-site/
  index.html          um h1, uma seção por bloco do briefing, JSON-LD LocalBusiness
  css/tokens.css       cópia de 05-design-system/tokens.css (só caminho das fontes mudou)
  css/site.css         estilos do site, só com var(--tc-…)
  js/site.js           opcional: sincroniza aria-expanded do menu, Esc fecha, funciona sem JS
  assets/logo/…         SVGs copiados de 04-logo/master
  assets/fontes/…       Literata e Instrument Sans (OFL) + licenças
  assets/og-capa.png    imagem de compartilhamento (Open Graph), gerada no estilo das peças de autoridade — não é fotografia, é tipografia da marca
  favicon.svg / favicon.ico / apple-touch-icon.png
```

## Acessibilidade e responsivo

- `lang="pt-BR"`, um único `h1`, hierarquia de títulos em ordem, landmarks (`header`, `nav`, `main`, `footer`), link "Pular para o conteúdo" como primeiro elemento focável.
- Contraste: só usa os pares aprovados no design system (ex. Argila sobre Papel/Linho, nunca Argila sobre Sálvia em texto pequeno; Latão só sobre Pinho).
- Menu do celular é um `<details>/<summary>` nativo — funciona **sem JavaScript**; o `site.js` só sincroniza `aria-expanded` e fecha com Esc.
- Testado sem rolagem horizontal de 390 a 1440 px. `prefers-reduced-motion` zera as transições via tokens.
