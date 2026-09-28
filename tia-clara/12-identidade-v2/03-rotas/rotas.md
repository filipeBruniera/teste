# Tia Clara · Identidade v2: rotas de logo

> **Marco 1 do [plano](../../../.claude/plans/tia-clara-nova-identidade.plan.md).** Estas são propostas de direção para a Clara escolher, não a logo final. Três lógicas visuais diferentes, não três variações de cor. Todo o texto está em curvas, gerado por [`_fonte/v2_rotas.py`](../../_fonte/v2_rotas.py).

| | **A · Com eles** | **B · Assinatura** | **C · As ilhas** |
|---|---|---|---|
| Ideia | A Clara de costas, sentada com o cão e o gato, olhando a serra e o mar de Ubatuba | O nome dela, escrito à mão: o pingo do "i" é o sol e uma onda sublinha "Clara" | No horizonte de Ubatuba, as ilhas são a cabeça de um gato e a de um cão; o sol nasce entre elas |
| De onde vem | É a referência de que ela mais gosta (a silhueta dela com os bichos) | A cursiva da referência | O litoral e os bichos da referência, num desenho que só a Tia Clara tem |
| Símbolo | Selo circular com a cena | Monograma "Tc" com o sol | Selo circular com as ilhas-bichos |
| Nome | TIA CLARA em caixa-alta (Figtree) | Tia Clara em cursiva (Norican) | Tia Clara em semicursiva (Courgette) |
| Paleta mostrada | 1 · Sálvia da serra | 2 · Sálvia oliva | 3 · Sálvia do mar |
| O que distingue | Ela aparece na marca | A assinatura é dela; o sol e a onda são detalhes próprios | O conceito é próprio: bicho que vira paisagem |
| O que pode dar errado | É a composição mais comum entre pet sitters, e o maior risco de ficar "igual à colega" | Assinatura em cursiva é comum; depende dos detalhes para ser dela | Precisa de uma segunda olhada para ver os bichos; a 32 px vira "duas ilhas e o sol" |

Qualquer rota funciona com qualquer paleta.

## Scorecard: critérios do [diagnóstico](../01-diagnostico.md)

| Critério | A | B | C |
|---|---|---|---|
| 1. Claridade: sálvia lidera, sem área escura dominante | ✅ | ✅ | ✅ |
| 2. Redução: reconhecível a 32 px e em 1 cor ([teste](teste-reducao.png)) | ⚠️ Bom a 48 px; a 32 px as três figuras viram mancha | ✅ "Tc" legível até 16 px | ⚠️ A 32 px é lida como ilhas e sol, e as orelhas somem; a 48 px, ✅ |
| 3. Distinção: não é o selo genérico nem a silhueta no pôr do sol | ❌ É a composição genérica da referência | ⚠️ Cursiva é comum; o sol no "i" e a onda são próprios | ✅ Conceito próprio |
| — comparação com a logo da colega | pendente | pendente | pendente |
| 4. Sem gótico nem clínica | ✅ | ✅ | ✅ |
| 5. Adulta, não infantil | ✅ | ✅ | ✅ |
| 6. Lugar: Ubatuba sem virar cartão-postal | ✅ Serra, mar e nome | ⚠️ Só a onda e o nome | ✅ Ilhas, mar e sol nascendo |
| 7. Nome legível a 24 px | ✅ | ✅ | ✅ |

**Recomendação do estúdio:** **C** como principal, por ser a única com ✅ em distinção. **B** é a alternativa mais segura, a que melhor aguenta tamanho pequeno. **A** entra porque a Clara gostou da referência, mas é a mais parecida com o que já existe no mercado e o maior risco de repetir o problema da colega.

## O que ainda não está resolvido (vai para o marco 2)
- **Comparação com a logo da colega:** só dá para confirmar a distinção depois de ver a logo dela.
- **Ilustração:** as figuras foram desenhadas em vetor, com traço simples e silhueta. Na rota escolhida, o marco 2 refina o desenho. Se a Clara quiser o nível de detalhe da referência (xilogravura), a arte final pede um ilustrador; cores, tipografia e regras de redução já ficam decididas aqui.
- **1 cor da rota C:** o recorte do sol entre as ilhas precisa de ajuste fino.
- **Rota B:** o "Tc" é a versão reduzida; resta decidir se a assinatura completa ganha também um símbolo ao lado.

## Arquivos
- `rota-{a,b,c}/tc-{rota}-assinatura.svg`: assinatura completa (símbolo, nome, "PET SITTER & DOG WALKER" e "UBATUBA")
- `rota-{a,c}/tc-{rota}-simbolo.svg`: símbolo sozinho
- `rota-{a,b,c}/tc-{rota}-reduzida.svg`: versão para avatar (A e C com zoom na parte central)
- `rota-{a,b,c}/tc-{rota}-1cor.svg` e `-1cor-branco.svg`: uma cor sobre claro e sobre escuro
- `teste-reducao.html` e `.png`: prancha de redução (16, 32, 48 e 120 px, 1 cor, avatar)
- `especime-cursivas.png`: as 15 cursivas testadas antes da escolha de Norican e Courgette
