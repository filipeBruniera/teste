# Tia Clara — QA de Marca

> Fase 9 · QA Director. A nota é diagnóstica; as **falhas críticas** mandam mais que a nota.

## Condições de falha crítica

| Condição | Status | Evidência |
|---|---|---|
| Semelhança confusa com concorrente conhecido | ✅ Passa | Nenhum player da categoria usa plaquinha + serifa + paleta profunda. **Pendente:** busca no INPI (classes 45, 43, 44, 35) |
| Inutilizável em 1 cor | ✅ Passa | `04-logo/testes/teste-L1.png`: preto, branco, carimbo, latão |
| Ilegível em tamanho pequeno obrigatório | ✅ Passa | Símbolo compacto a 16 px; horizontal compacta a 24 px de altura |
| Par de cor/texto reprovado | ✅ Passa | Todos os pares de texto ≥ 4,5:1. Latão só sobre Pinho; Argila sobre Sálvia só em texto grande |
| Logo mestre só em raster/IA | ✅ Passa | SVG gerado por script, texto em curvas (`_fonte/marca.py`) |
| Sem regras para contextos comuns | ✅ Passa | Tamanhos mínimos, área de proteção, versões compactas, fundo carregado, avatar circular |
| Social com texto pequeno demais para celular | ✅ Passa | Mínimo de 28 px em 1080. A única exceção era a fonte da estatística, já corrigida para 28 px |

## Nota diagnóstica: 88/100

| Dimensão | Peso | Nota | Comentário |
|---|---|---|---|
| Relevância estratégica | 20 | 18 | Guardiã/Curadora/Cuidadora viram decisões visuais concretas. Risco: o nome "Tia" continua puxando para o registro de creche |
| Distinção | 20 | 16 | Espaço em branco real na categoria. Mas "monograma dentro de forma" é uma construção comum, e creme + serifa + terracota é um visual frequente em marcas DTC fora do setor. **Mitigação:** Pinho lidera (≥ 25%), Argila é tempero, e a plaquinha é objeto, não moldura decorativa |
| Reprodutibilidade | 15 | 14 | Forma cheia, sem efeito. As hairlines do logotipo pedem a versão compacta abaixo de 60 px |
| Escala entre canais | 15 | 14 | Testado em avatar, favicon, header, post, story, cartão, objeto físico, site desktop/celular |
| Legibilidade / acessibilidade | 10 | 9 | Contraste AA em todos os pares de texto. A argola do rótulo foi reduzida para não ser lida como a letra "O" |
| Coerência do sistema | 10 | 9 | Os modelos só usam tokens (Gate D1 ✅) |
| Movimento / digital | 10 | 8 | Assinatura animada com versão para "reduzir movimento". Falta testar com vídeo real do pet |

## Auditoria final

| Item | Status |
|---|---|
| Variantes do logo | ✅ 36 SVGs + 105 PNGs + favicon.ico |
| Hierarquia tipográfica | ✅ 2 famílias, 8 papéis, escala social separada |
| Contraste | ✅ Tabela em `05-design-system/design-system.md` |
| 3+ aplicações reais | ✅ Relatório de WhatsApp, posts, cartão, plaquinha/chaveiro, site |
| Legibilidade no celular | ✅ Mínimo de 28 px e zonas seguras nos stories |
| Claro / escuro | ✅ Tokens para modo escuro; favicon adapta sozinho |
| Continuidade do movimento | ✅ Fundo fixo, pivô no furo, sem salto de quadro |
| Nomes e editabilidade dos arquivos | ✅ Prefixo `tc-`, nomes em português sem acento; tudo regenerável por script |

## Riscos abertos (não bloqueiam)

1. **Nome.** "Tia Clara" lembra creche ("tia") e a personagem de *A Feiticeira* (adorável e desastrada). A identidade compensa, mas **a decisão sobre o nome é sua**: veja *Decisões* no brand book.
2. **INPI.** Fazer a busca de anterioridade antes de imprimir em escala.
3. **Fotos.** Os modelos usam marcadores. A marca só fica completa com fotografia real dentro das regras.
4. **Razões para acreditar.** Só comunicar os protocolos que a Clara de fato pratica (visita de apresentação, chaves codificadas, relatório, contrato, seguro).
5. **Estatística dos 83%.** Veio de resultado de busca (pesquisa Rover, maio/2026). Confirmar na fonte antes de publicar.
6. **Canva.** Recriar o relatório e 3–4 modelos no Canva para uso diário, herdando os tokens.
