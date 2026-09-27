# Tia Clara — Identidade em Movimento

> Fase 6 · Motion Director. Arquivos:
> - `logo-reveal.html`: animação em vetor, respeita "reduzir movimento"
> - `logo-reveal.webm`: vídeo
> - `storyboard-logo.png`: quadros-chave
>
> Tokens de tempo e curva estão em `05-design-system/tokens.json` → `movimento`.

## Personalidade
**Firme · calma · precisa · acolhedora.**

Nada pula, nada gira à toa. O movimento resolve uma inquietação e termina em repouso: é o que o tutor sente quando chega o relatório.

## Primitivos
| Token | Valor | Uso |
|---|---|---|
| micro | 160 ms | Estados de interface, checks |
| padrão | 320 ms | Entrada de texto e blocos |
| ênfase | 720 ms | Título principal, logotipo |
| assentar | 1400 ms | **Só a plaquinha**: balanço até parar |
| curva firme | `cubic-bezier(.2, 0, 0, 1)` | Padrão: sai decidida, chega suave |
| curva de saída | `cubic-bezier(.4, 0, 1, 1)` | Saídas, sempre mais curtas que a entrada |
| curva assentar | `cubic-bezier(.34, 1.2, .64, 1)` | Pequeno excesso, depois calma |

**Limites:**
- Deslocamento máximo de 32 px (em 1080).
- Escala só de 0,96 a 1.
- Sem desfoque, brilho, partículas ou 3D.
- Escalonamento entre linhas: 80 ms.

## Assinatura animada: "o balanço que assenta"
1. **0–250 ms** · a plaquinha desce 26 px e aparece. O pivô é o **furo**, como se estivesse pendurada.
2. **250–1650 ms** · ela balança −9° → +6° → −3° → +1,2° → 0°, com amortecimento. **Inquietação → calma.**
3. **1050 ms** · "**Clara**" sobe 14 px, firme.
4. **1250 ms** · "*Tia*" chega pela esquerda, gesto.
5. **1550 ms** · o descritor fecha o espaçamento de 0,30 em para 0,15 em.
6. **2400 ms** · repouso. Segure 1 s antes de cortar.

**Som (opcional):** um "tlim" metálico curto e seco, de latão na argola, no instante em que a plaquinha para. Sem latido, sem efeito cartoon, sem trilha infantil.

## Texto
- O título lidera: sobe 12–16 px, 720 ms, curva firme.
- O texto de apoio entra 160 ms depois, só com opacidade, e fica **parado e legível** por pelo menos 2 s por linha.
- **Linha de registro** (relatório em vídeo): cada linha entra com 80 ms de escalonamento. O check ✓ aparece 120 ms depois da linha, com escala 0,96 → 1.

## Transições
| Nome | Como é | Quando usar |
|---|---|---|
| **Plaquinha** | Máscara em arco (proporção 100×112) cresce do centro e revela a próxima cena | Abertura e fecho, troca de assunto |
| **Registro** | Painel Sálvia ou Pinho sobe 100% com curva firme; as linhas de texto entram escalonadas | Relatórios, passo a passo |
| **Corte seco** | — | Entre planos de vídeo do pet (preferir sempre a efeitos) |

## Loop
Para avatar animado ou fundo de story: a plaquinha oscila ±1,5° num ciclo de 4 s (seno). O fundo nunca se mexe.

## Regras para social e vídeo
- **O primeiro 1–2 s estabelece uma âncora estável:** logo ou título parado, fundo fixo. Nada de "pulo de tela" entre quadros.
- Enquadramento seguro 9:16: zona útil entre 250 px (topo) e 340 px (base) em 1080×1920.
- Legendas: Instrument Sans 600, 44–52 px, em Linho sobre faixa Pinho a 88%, no máximo 2 linhas.
- Fecho padrão: 1,5 s da assinatura assentada + "Pode deixar comigo." em Literata.

## QA de movimento
- ✅ Alternativa com movimento reduzido: `prefers-reduced-motion` desliga tudo e mostra o logo estático.
- ✅ Sem salto de quadro: o fundo é fixo e só o objeto se move.
- ✅ Pivô no furo: a física é coerente com o objeto real.
- ✅ Duração total de 2,4 s: cabe no primeiro segundo e meio do reel sem atrasar a mensagem.
