# Revisão de SEO local: landing page Tia Clara

> Passo 2 do pós-GAN. Auditoria feita pelo agente `seo-specialist` com o método da skill `seo`, sobre `tia-clara/10-site/`. O revisor só leu a página. O que foi aplicado está no fim do documento. O guia do Perfil de Empresa no Google está em [`perfil-de-empresa-google.md`](perfil-de-empresa-google.md).

**Estrutura encontrada:** não havia `robots.txt`, `sitemap.xml`, `manifest.json` nem `404.html`. Os favicons e a `og-capa.png` (1200×630) estão corretos.

## Prioridades

| Item | Impacto | Esforço |
|---|---|---|
| `og:image` com caminho relativo: quebra a prévia do link no WhatsApp, o canal principal | Alto | Baixo |
| `canonical` apontando para `https://example.org/` (domínio reservado, não é da marca) | Alto (bloqueia a publicação) | Baixo (depende do domínio) |
| Sem `robots.txt` e `sitemap.xml` | Alto | Baixo |
| JSON-LD incompleto: faltam `url`, `logo`, `image` e `hasOfferCatalog` | Alto | Baixo–médio |
| `<title>` e meta description sem bairro/cidade | Alto | Baixo |
| Faltam `og:url`, `og:image:width/height` e as tags `twitter:` | Médio-alto | Baixo |
| Perguntas do FAQ com estilo de título, mas marcadas como `<span>` e não como `<h3>` | Médio | Baixo |
| Grafia do nome diferente entre `brief.json` e o site (consistência de NAP) | Médio | Baixo |
| Estatística de 83% sem fonte verificável (risco de confiança se indexada) | Médio | Baixo |
| Links `wa.me/55XXXXXXXXXXX` fictícios | Alto para conversão (não é defeito técnico de SEO) | Depende do dado |
| Perfil de Empresa no Google inexistente | Alto | Médio |

## `<head>`

- **Title** (35 caracteres, sem localização) → `Tia Clara — Pet Sitter &amp; Dog Walker em [BAIRRO]`. O "&" segue a regra de grafia. A cidade fica na description e no JSON-LD para não estourar ~60 caracteres.
- **Meta description** → `Pet sitting em domicílio (cães e gatos) e passeios com cães em [BAIRRO], [CIDADE]. Relatório de cada visita, sempre a mesma cuidadora.` Conferir se fica entre 120 e 160 caracteres depois de preencher.
- **Canonical** → `https://[DOMINIO]/`.
- **Open Graph e Twitter**: `og:image` precisa de URL absoluta. Adicionar:
  - `og:url`;
  - `og:image:width` 1200, `og:image:height` 630, `og:image:type` e `og:image:alt`;
  - `twitter:title`, `twitter:description` e `twitter:image`.
- **Robots meta**: omitido está correto (o padrão é `index, follow`).
- **Favicons**: corretos.
- **Manifest**: opcional, não influi em SEO.

## JSON-LD

- **Tipo:** manter `LocalBusiness`. Não existe subtipo de pet sitting no schema.org. `VeterinaryCare` e `AnimalShelter` foram descartados de propósito, porque contrariam o "não parecer veterinária" da estratégia.
- **Especificidade:** entra por `serviceType` e `hasOfferCatalog` (pet sitting em domicílio; passeios com cães).
- **Endereço:** sem `address`, e isso é o correto para uma empresa de área de atendimento (privacidade). Usar `areaServed` estruturado (`City` / `Place`).
- **`logo`:** símbolo quadrado de 512 px (`04-logo/png/tc-simbolo-512px.png`, copiado para `10-site/assets/logo/`).
- **`image`:** `og-capa.png` até existir uma foto real, seguindo o protocolo de privacidade.
- **`sameAs`:** omitido até haver um @ real do Instagram.
- **`openingHoursSpecification`:** omitido. Não há horário real, e um marcador de texto invalida a estrutura.
- **`aggregateRating` / `review`:** **não adicionar** enquanto os depoimentos forem marcadores. Dado inventado viola as políticas do Google.
- **`FAQPage`:** prioridade baixa. O conteúdo bate com o FAQ visível, mas o revisor aponta que o Google deixou de exibir o rich result de FAQ em maio de 2026 (fontes: [inblog](https://inblog.ai/blog/google-faq-schema-rich-result-deprecation), [Passionfruit](https://www.getpassionfruit.com/blog/what-changed-with-google-drops-faq-rich-results-and-what-to-do-now)). Não foi adicionado.

## Conteúdo on-page

- **Hierarquia (manter):** um `h1` de marca ("Pode deixar comigo.") e um `h2` por seção. O rótulo acima do H1 já carrega "Pet sitter & dog walker · bairro, cidade", que é onde a palavra-chave local entra sem forçar.
- **FAQ:** as perguntas eram `<span class="tc-titulo-3">` dentro de `<summary>`. O HTML permite um título dentro de `<summary>`, então viraram `<h3>`.
- **Palavra-chave local:** hoje aparece só no rótulo do hero. Sugestões:
  - uma linha de área de atendimento no rodapé, com área e não endereço;
  - o bairro nos subtítulos de Serviços.
  - O revisor alerta: não repetir o termo além disso.
- **`alt`:** as fotos ainda são marcadores (sem `<img>`). Quando entrarem, precisam de `alt` descritivo, nunca vazio. Os `alt=""` dos ícones decorativos estão certos.
- **Texto âncora:** descritivo, sem "clique aqui". Manter.

## `robots.txt` e `sitemap.xml`

Site de uma página só, sem área privada: `Allow: /` e a indicação do sitemap. O sitemap tem uma URL, `lastmod` na data de publicação (AAAA-MM-DD) e `changefreq` mensal. A página `404.html` é opcional, porque o GitHub Pages e a Netlify já têm a sua.

## Pendências que dependem de dados reais

| Dado | O que bloqueia |
|---|---|
| Domínio `[DOMINIO]` | canonical, `og:url`, `og:image` absoluto, robots, sitemap e as URLs do JSON-LD |
| Bairro(s) e cidade | title, description, `areaServed`, rodapé e a área de atendimento no Google |
| Telefone / WhatsApp | links `wa.me`, rodapé e `telephone` no JSON-LD |
| Instagram | `sameAs` |
| Preço | `priceRange` e os marcadores de preço |
| Fotos reais | `<img>` com `alt` descritivo, dentro do protocolo de privacidade |
| Estatística de 83% | confirmar a fonte ou tirar |
| Depoimentos | só com autorização, e nunca em `aggregateRating` antes disso |
| Protocolos ⚑ | confirmar com a Clara antes de o Google indexá-los como fato |

## Aplicado nesta branch

_Preenchido depois da aplicação das correções._
