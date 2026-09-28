# Revisão de texto: landing page Tia Clara

> Passo 1 do pós-GAN. Modo *Copy Review* do `/ecc:marketing-campaign`, executado pelo agente `marketing-agent` sobre `tia-clara/10-site/index.html`, com o tom checado contra `01-estrategia/estrategia.md`, `07-producao/producao.md` e `00-brief/`. O revisor só leu a página. O que foi aplicado está no fim do documento.

## Resumo

| Dimensão | Nota (1–5) | Observação |
|---|---|---|
| Clareza (teste de 5 s) | 4 | O quê fica claro no hero. O "para quem" e o "por que agora" ficam implícitos |
| CTA | 3 | Vários rótulos e mensagens para a mesma ação. O CTA final era mais fraco que o do hero |
| Consistência de tom | 5 | Reaproveita o banco de frases quase à risca. Nenhum termo proibido |
| Promessas sustentáveis | 3 | Linguagem específica e correta, mas quase toda promessa de protocolo é hipótese ⚑ não confirmada |
| Adequação ao canal (site + WhatsApp) | 3 | Estrutura e links corretos, mas dados de produção vazam para o visitante (JSON-LD e seção Avaliações) |

**Veredito: forma e voz aprovadas. O conteúdo ainda não está pronto para publicar.**

O que bloqueia a publicação:
1. **Os três links de WhatsApp usam o número fictício `55XXXXXXXXXXX`** (cabeçalho, hero e contato). Enquanto ele não for trocado, nenhum CTA da página funciona.
2. **Cada promessa de protocolo** da tabela abaixo precisa ser confirmada com a Clara.
3. **A seção Avaliações** hoje avisa ao visitante que ainda não há prova social.

## Primeira dobra: teste de 5 segundos

Rótulo "Pet sitter & dog walker · [bairro, cidade]" → H1 **"Pode deixar comigo."** → texto de apoio "Visitas na sua casa e passeios com protocolo, relatório de cada visita e sempre a mesma pessoa cuidando do seu pet." → CTA "Agendar visita de apresentação".

- **O que faz:** claro. O H1 e o texto de apoio entregam o serviço, o mecanismo (protocolo, relatório) e o diferencial (a mesma pessoa).
- **Para quem é:** implícito. Nada diz "para quem viaja" ou "para quem trabalha o dia todo". Funciona para quem chega por indicação ou busca direta, e é mais fraco para tráfego frio de anúncio.
- **Por que agora:** ausente, o que está correto. A marca não usa urgência falsa.

## Achados

| # | Severidade | Seção | Texto atual | Problema | Proposta |
|---|---|---|---|---|---|
| 1 | Alta | Todos os CTAs | `https://wa.me/55XXXXXXXXXXX?text=…` | Número fictício: todo clique falha | Trocar pelo número real da Clara nos três links antes de publicar |
| 2 | Alta | Avaliações | "Esta seção vai reunir avaliações reais assim que os primeiros relatórios virarem histórico. Por enquanto, os espaços abaixo são marcadores — nada aqui foi escrito por um tutor de verdade." | Nota de produção exposta ao visitante; mostra a falta de prova social | "As primeiras avaliações chegam assim que os primeiros tutores contarem a experiência." Na publicação, tirar os 3 cartões até haver depoimento real autorizado |
| 3 | Alta | Avaliações: estatística | "Não confirmado" / "Estatística de terceiros, ainda não confirmada para uso na marca." | Publicar "não confirmado" ao lado de um número é pior do que não publicar | Tirar o bloco dos 83% da versão publicada até a fonte ser confirmada |
| 4 | Alta | JSON-LD | `areaServed`, `telephone` e `priceRange` com "a confirmar" | Buscadores podem indexar o texto provisório | Tirar essas chaves até haver dado real (ver revisão de SEO) |
| 5 | Média | Contato (CTA final) | "Chamar no WhatsApp" + "…quero saber mais sobre os serviços." | No momento de maior informação, o pedido recua para "saber mais" e vira um terceiro rótulo | "Agendar visita de apresentação" + "Olá, Tia Clara! Vi o site e quero agendar uma visita de apresentação." |
| 6 | Média | Hero: cartão de relatório | "Relatório · Thor" | A seção Relatório marca o mesmo cartão como exemplo; o do hero pode parecer um caso real | "Relatório · Thor (exemplo)" |
| 7 | Média | Como funciona | "conhecer a casa de vocês" | O hero diz "sua casa": muda o número para o mesmo referente | "conhecer a sua casa" |
| 8 | Média | FAQ | (não existe) | A objeção "hotelzinho não seria mais seguro?" da estratégia não é respondida | Nova pergunta: "Por que não um hotelzinho?" |
| 9 | Baixa/média | Passeio | (não existe) | A objeção "calor" não aparece | Só escrever depois que a Clara confirmar a prática (ex.: passeio em horário mais fresco) |
| 10 | Baixa | Cabeçalho | "Agendar apresentação" | Rótulo diferente do hero para a mesma ação | "Agendar visita" |
| 11 | Baixa | Serviços: pet sitting | "Visitas diárias, no horário combinado" | Fixa uma frequência que não está confirmada (gatos costumam ter outra) | "Visitas na frequência e no horário combinados" |
| 12 | Baixa | Preços | "investimento por visita" / "investimento por passeio" | Eufemismo de vendas, contra o pilar Clareza | "valor da visita" / "valor do passeio" |

## Promessas: auditoria

**Classificação:** (a) segura como está · (b) confirmar com a Clara antes de publicar · (c) arriscada, reescrever ou tirar.

| Promessa | Seção | Classe | Ação |
|---|---|---|---|
| "Pode deixar comigo." / "Tudo certo por aqui." / "Tudo em ordem enquanto você não está." | Várias | a | Frases de tom, não afirmações verificáveis |
| "O pet fica no território dele, do jeito dele…" | Serviços | a | Decorre do próprio modelo de serviço |
| Visita de apresentação antes do primeiro serviço | Como funciona / CTAs | b | Confirmar que toda primeira contratação inclui a visita, sem exceção |
| Ficha do pet por escrito | Como funciona | b | Confirmar que a ficha é preenchida e usada para cada pet |
| Chaves codificadas, guarda segura, entrega e devolução registradas | Protocolos / FAQ | b | Confirmar se o sistema já existe hoje ou é meta |
| Relatório no WhatsApp com horários, o que foi feito, foto e observação | Relatório / FAQ | b | Confirmar que é viável em 100% das visitas |
| Peitoral ajustado, guia com trava e plaquinha de identificação | Protocolos | b | Confirmar que é o equipamento padrão de todo passeio |
| Autorização assinada + veterinário de referência + aviso por telefone | Protocolos / FAQ | b (prioridade alta) | Confirmar o documento e o compromisso de ligar |
| Contrato por escrito antes da primeira visita | Protocolos | b | Confirmar que existe um termo por escrito, mesmo simples |
| "Sempre a mesma pessoa" (aparece 4 vezes, incluindo o JSON-LD) | Hero, Relatório, Protocolos | b (prioridade máxima) | Confirmar o que acontece em viagem, doença ou férias da Clara. Com substituta, comunicar um plano de continuidade ou suavizar a frase |
| Passeio individual; grupo pequeno a combinar | Serviços / FAQ | b | Confirmar o tamanho máximo e o critério |
| 83% dos tutores preferem pet sitting (pesquisa Rover 2026) | Avaliações | c | Tirar até confirmar a fonte |
| 3 cartões "espaço reservado para um depoimento real" | Avaliações | c | O formato imita uma citação real: tirar até haver depoimentos autorizados |

## CTAs

- Os três CTAs levam ao WhatsApp, mas o do contato tinha rótulo e mensagem mais fracos. Recomendação: unificar em "Agendar visita de apresentação" (achados 5 e 10).
- "Ver como funciona" é uma âncora interna e não compete com a conversão.
- As mensagens pré-preenchidas estão bem escritas: em primeira pessoa, naturais e específicas. O problema é só o número.

## Objeções do público: cobertura

| Público | Objeção | Coberta? |
|---|---|---|
| Tutor que viaja | Entregar a chave a uma estranha | Sim (Protocolos, FAQ) |
| Tutor que viaja | "E se acontecer algo?" | Sim (Protocolos, FAQ) |
| Tutor que viaja | "Hotelzinho não seria mais seguro?" | Só indiretamente → achado 8 |
| Tutor que viaja | Gatos | Sim (FAQ) |
| Rotina intensa | Fuga | Sim (Protocolos, Serviços) |
| Rotina intensa | Brigas com outros cães | Parcial (implícito no passeio individual) |
| Rotina intensa | Calor | Não → achado 9 |
| Rotina intensa | Passeio "em bando" | Sim (Serviços, FAQ) |
| Necessidade específica | Medicação | Sim, sempre "prescrita pelo veterinário de vocês" |
| Necessidade específica | "Será que ela dá conta?" | Parcial (depende de prova social, ainda ausente) |

## Marcadores de dados pendentes

Os marcadores seguem um padrão visual consistente (`data-marcador` + etiqueta "a confirmar"), o que facilita o preenchimento. **A página convence enquanto eles não são preenchidos?** Em parte:
- **O que já funciona:** o ângulo "processo como prova" se sustenta sem fotos nem depoimentos.
- **Por que ainda não está pronta para tráfego real:**
  - o WhatsApp não funciona;
  - a seção Avaliações expõe a falta de prova social;
  - sem bairro, o visitante não sabe se é atendido.

## O que está bom e deve ficar

- "Pode deixar comigo." como H1 e de novo no fecho de Protocolos, sem excesso.
- "Tudo certo por aqui." como ritual do relatório.
- Reaproveitamento fiel do banco de frases, com a mesma voz do início ao fim.
- Nenhum termo clínico e nenhum exagero proibido.
- A linha de privacidade no rodapé: um diferencial real da categoria.
- A observação do relatório de exemplo ("Encontrou outro cão na praça e brincou um pouco. Voltou tranquilo e foi direto para a caminha.") é o melhor exemplo de afeto pelo detalhe da página e serve de modelo para relatórios reais.

## Aplicado nesta branch

| Achado | Situação |
|---|---|
| 1. Número do WhatsApp | **Pendente**: depende do número real (checklist, bloqueador) |
| 2. Nota de produção em Avaliações | **Aplicado**: nova frase de introdução. Os 3 cartões continuam como marcadores visíveis (pedido do spec); o checklist manda tirá-los se não houver depoimento real na publicação |
| 3. Rótulo "Não confirmado" dos 83% | **Pendente**: o marcador continua visível; o checklist manda confirmar a fonte ou tirar o bloco |
| 4. "A confirmar" dentro do JSON-LD | **Aplicado**: o JSON-LD foi refeito com marcadores de código (`[TELEFONE]`, `[FAIXA_DE_PRECO]`…) que o checklist obriga a trocar antes de publicar |
| 5. CTA final | **Aplicado**: "Agendar visita de apresentação" e a mensagem de agendamento |
| 6. Cartão do hero | **Aplicado**: "Relatório · Thor (exemplo)" |
| 7. "de vocês" / "sua" | **Aplicado** em "conhecer a sua casa" e "Eu visito a sua casa". "Veterinário de vocês" ficou, porque é a frase do banco de frases |
| 8. Objeção "hotelzinho" | **Aplicado**: nova pergunta no FAQ, "Por que não um hotelzinho?" |
| 9. Objeção "calor" | **Pendente**: só entra depois que a Clara confirmar a prática |
| 10. CTA do cabeçalho | **Aplicado**: "Agendar visita" |
| 11. "Visitas diárias" | **Aplicado**: "Visitas na frequência e no horário combinados" |
| 12. "investimento" | **Aplicado**: "valor da visita" / "valor do passeio" |
| Promessas classe (b) | **Pendente**: lista de confirmação com a Clara em [`checklist-pre-lancamento.md`](checklist-pre-lancamento.md) |
