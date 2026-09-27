# Tia Clara — Sistema de Logo

> Fase 4 · Logo Designer. Fonte única da verdade: `_fonte/marca.py`. **Todo texto está em curvas.** Nenhum arquivo final depende de fonte instalada.

## Funil de exploração
- **12 rotas** → `exploracao/01-doze-rotas.png`
- **6 pré-selecionadas**: 1 plaquinha+C, 2 plaquinha+tc, 6 guia-em-C, 7 C-check, 8 porta, 10 arco com orelhas
- **3 famílias**: Plaquinha (A), C-check (B), Guia (C)
- **1 mestre**: Plaquinha. Refinamento em `exploracao/02-familia-plaquinha.png` e `03-logotipo-variacoes.png`

Descartadas e por quê:

| Rota | Motivo |
|---|---|
| 3 · redonda | "C" em círculo lê como © |
| 4 · casa | Código de imobiliária |
| 5 · chave | Código de chaveiro/imobiliária; chave+patinha já virou template |
| 9 · colo | Genérico |
| 10 · orelhas | Fofo e só de gato |
| 11 · brasão | Parece segurança privada |
| 12 · argola | Lê como "D" |

## Construção

**Símbolo:**
- Plaquinha de 100 × 112 u: topo em semicírculo (r 50), cantos inferiores r 22.
- Furo: r 7,5 em (50, 19).
- C em Literata (opsz 36, peso 690), centralizado opticamente: +1 u abaixo do centro da área útil e +2,6 u à direita, porque o C é aberto à direita e pesa à esquerda.
- A **versão compacta** (≤ 32 px) usa furo maior (r 9,5) e C mais pesado (opsz 14, peso 790).

**Dupla leitura, intencional:** o furo e o C também formam uma figura, com cabeça e braços que envolvem. É a Guardiã dentro da plaquinha.

**Logotipo:**
- "*Tia*" em Literata Itálico 500: o gesto, o afeto.
- "**Clara**" em Literata 680: a firmeza.
- O pingo do i vira **argola**, o mesmo anel do furo da plaquinha. É o único detalhe customizado: sutil de propósito.

**Descritor:** PET SITTER & DOG WALKER em Instrument Sans 560, caixa-alta, espaçamento +150.

## Arquivos (`master/`)

| Peça | Arquivo |
|---|---|
| Assinatura horizontal (principal) | `tc-assinatura-horizontal.svg` + `-preto` `-branco` `-linho` |
| Assinatura horizontal compacta (sem descritor) | `tc-assinatura-horizontal-compacta*.svg` |
| Assinatura vertical | `tc-assinatura-vertical*.svg` |
| Assinatura vertical compacta | `tc-assinatura-vertical-compacta*.svg` |
| Assinaturas com fundo Pinho | `tc-assinatura-*-sobre-pinho.svg` |
| Logotipo (com e sem descritor) | `tc-logotipo*.svg` |
| Símbolo | `tc-simbolo.svg` + `-preto` `-branco` `-linho` `-latao` `-argila` |
| Símbolo compacto (16–32 px) | `tc-simbolo-compacto*.svg` |
| Avatar (Instagram/WhatsApp) | `tc-avatar.svg`, `tc-avatar-linho.svg` |
| Favicon (adapta ao modo escuro) | `tc-favicon.svg`, `png/favicon.ico` |
| Ícone de app / apple-touch | `tc-app-icon.svg` |

Os PNGs com fundo transparente ficam em `png/`. Para regenerar:

```
python3 tia-clara/_fonte/marca.py && NODE_PATH=$(npm root -g) node tia-clara/_fonte/exportar.js
```

## Regras

**Área de proteção:** **x = ¼ da largura da plaquinha** na peça em uso. Deixe no mínimo 1x livre em todos os lados.

**Tamanho mínimo:**

| Peça | Digital | Impresso |
|---|---|---|
| Horizontal com descritor | 60 px de altura | 18 mm de altura |
| Horizontal compacta | 24 px de altura | 8 mm |
| Vertical com descritor | 140 px de largura | 35 mm |
| Vertical compacta | 64 px de largura | 18 mm |
| Símbolo | 32 px (abaixo: compacto) | 8 mm |
| Símbolo compacto | 16 px | 5 mm |

**Cores permitidas do logo:**
- Pinho sobre Linho/Papel/branco
- Linho sobre Pinho
- Latão sobre Pinho (só o símbolo, ou peças especiais)
- Preto ou branco para produção em 1 cor

**Não fazer:**
- esticar, inclinar, girar;
- trocar a fonte;
- deixar "Tia" e "Clara" no mesmo estilo;
- trocar a argola por patinha ou coração;
- usar a plaquinha sem o furo;
- colocar contorno, sombra, gradiente ou brilho;
- usar sobre foto ou textura sem placa de proteção;
- usar Argila no logo sobre Pinho (contraste baixo e vibração);
- aplicar Latão sobre fundo claro;
- recriar o logo com texto digitado.

## Gate L1 — ✅ aprovado (`testes/teste-L1.png`)

- ✅ 16/24/32 px
- ✅ preto/branco
- ✅ escala de cinza
- ✅ 1 cor impressa
- ✅ tela ruim
- ✅ recorte circular
- ✅ cabeçalho horizontal
- ✅ coluna vertical
- ✅ fundo carregado com proteção
- ✅ revisão de semelhança: sem conflito conhecido. **Pendente: busca no INPI, classes 45, 43, 44 e 35**
