# Tia Clara: checklist antes de publicar o site

> Consolida as pendências da [revisão de texto](revisao-texto.md), da [revisão de SEO](revisao-seo.md), do [QA da marca](../09-qa/qa.md) e do `brand-state.json`. O site (`10-site/`) está pronto em forma, mas **não pode ir ao ar** antes dos itens bloqueadores.

## 1. Bloqueadores: dados reais

- [ ] **Número do WhatsApp**: trocar `55XXXXXXXXXXX` nos três links `wa.me` e preencher o marcador `whatsapp-numero`.
- [ ] **Domínio**: trocar `[DOMINIO]` no `index.html`, no `robots.txt` e no `sitemap.xml`.
- [ ] **Bairro(s), cidade e estado**: `[BAIRRO]`, `[CIDADE]`, `[UF]` e os marcadores `bairro-cidade` e `area-atendimento`. Precisam ser os mesmos bairros no site, no Google e no Instagram.
- [ ] **Telefone**: marcador `telefone` e `[TELEFONE]` no JSON-LD.
- [ ] **Preços**: marcadores `preco-pet-sitting` e `preco-passeio`, e `[FAIXA_DE_PRECO]` no JSON-LD (ou remover a chave).
- [ ] **Data de publicação**: `[DATA_DE_PUBLICACAO]` no `sitemap.xml`.
- [ ] Conferência final: `grep -rnE "\[[A-Z_]+\]|55X{5,}" tia-clara/10-site --include=*.html --include=*.txt --include=*.xml` não retorna nada.

## 2. Bloqueadores: promessas a confirmar com a Clara

A marca só pode prometer o que a Clara faz. Para cada item, **manter** se for verdade hoje, **ajustar o texto** se for parcial ou **tirar** se não for.

- [ ] **"Sempre a mesma pessoa"** (hero, relatório, protocolos, JSON-LD). O que acontece em viagem, doença ou férias da Clara?
- [ ] **Emergência**: existe autorização assinada, com o veterinário de referência registrado? Ela liga para o tutor quando algo sai do previsto?
- [ ] **Chaves codificadas**: o chaveiro com código e o registro de entrega e devolução já existem ou são meta?
- [ ] **Visita de apresentação** antes de todo primeiro serviço, sem exceção?
- [ ] **Ficha do pet** por escrito para cada pet?
- [ ] **Relatório com foto** em 100% das visitas e passeios?
- [ ] **Equipamento de passeio**: peitoral ajustado, guia com trava e plaquinha de identificação em todo passeio?
- [ ] **Contrato** ou termo por escrito antes da primeira visita?
- [ ] **Passeio**: individual como padrão? Qual o tamanho máximo do "grupo pequeno" e o critério?
- [ ] **Calor**: há horário ou cuidado específico? Se sim, vale acrescentar ao passeio (a objeção ainda não é respondida na página).

## 3. Prova social e estatística

- [ ] **Depoimentos**: trocar os 3 marcadores por depoimentos reais **com autorização**. Se não houver na publicação, **tirar os três cartões** e deixar só a frase de introdução.
- [ ] **Estatística de 83%** (pesquisa Rover 2026): confirmar na fonte e citar com link, ou **tirar o bloco** da versão publicada.
- [ ] Não adicionar `aggregateRating` / `review` no JSON-LD até haver avaliações reais.

## 4. Fotos

- [ ] Foto do hero: pet em casa, altura dos olhos, luz natural.
- [ ] Foto do relatório: passeio ou visita.
- [ ] Seguir o protocolo de privacidade: sem fachada, número da casa ou geolocalização, publicar depois do serviço e ter autorização do tutor.
- [ ] Trocar os marcadores `foto-hero` e `foto-relatorio` por `<img>` com `alt` descritivo.
- [ ] Quando houver foto, trocar o `image` do JSON-LD pela foto (hoje aponta para a `og-capa.png`).

## 5. Marca e registro

- [ ] **Decisão sobre o nome** (manter "Tia Clara" ou dar protagonismo a "Clara"). Ver *Decisões* no brand book.
- [ ] **Busca no INPI** (classes 45, 43, 44 e 35) antes de imprimir em escala.
- [ ] **Grafia única do nome** no Google, no Instagram e no WhatsApp Business: *Tia Clara Pet Sitter & Dog Walker*.

## 6. Depois de publicar

- [ ] Criar o Perfil de Empresa no Google seguindo [`perfil-de-empresa-google.md`](perfil-de-empresa-google.md) (área de atendimento com endereço oculto).
- [ ] Enviar o `sitemap.xml` no Google Search Console.
- [ ] Testar a prévia do link no WhatsApp (imagem `og-capa.png` e título).
- [ ] Verificar a URL publicada com a skill `canary-watch` ou `browser-qa` do ECC.
