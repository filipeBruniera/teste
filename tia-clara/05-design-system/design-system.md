# Tia Clara — Sistema de Design

> Fase 5 · Brand System Designer. Os tokens ficam em `tokens.json` (formato W3C) e `tokens.css`. **Gate D1: nenhuma peça pode criar cor, fonte ou raio que não esteja aqui.**

## 1. Cor

### Primitivos
| Nome | Hex | Papel | Pode ser texto sobre… |
|---|---|---|---|
| **Pinho** | `#1E3B33` | Guardiã. Cor-mãe: logo, títulos, fundos de autoridade | Linho 10,5 · Papel 11,5 · Sálvia 9,1 |
| **Pinho Profundo** | `#142A24` | Fundo escuro de alto contraste, modo escuro | n/a (fundo) |
| **Musgo** | `#56625A` | Texto secundário | Linho 5,5 · Papel 6,0 · Sálvia 4,8 |
| **Linho** | `#F4EEE3` | Fundo padrão | Pinho 10,5 · Argila 4,8 |
| **Papel** | `#FBF8F2` | Cartões e superfícies elevadas | n/a (fundo) |
| **Sálvia** | `#DDE1D4` | Blocos de apoio, fundo de relatório | Pinho 9,1 |
| **Latão** | `#C6A15E` | O metal da plaquinha: símbolo, rótulos e filetes sobre Pinho | **Só sobre Pinho** (5,0) e Pinho Profundo (6,3). Nunca sobre claro (2,1 ✗) |
| **Argila** | `#A94E2A` | Cuidadora: calor, botão, destaque | Linho 4,8 · Papel 5,2. Sobre Sálvia só em texto grande (4,2) |
| **Argila Clara** | `#E7B89A` | Argila legível sobre Pinho | Pinho 6,8 · Pinho Profundo 8,5 |
| **Tinta** | `#1B1D1A` | Produção em preto, texto longo opcional | Linho 14,7 |

### Proporção de uso
**60 Linho/Papel · 25 Pinho · 10 Sálvia · 5 acentos (Argila ou Latão).**

Os acentos são tempero. Uma peça tem **um** acento dominante: Argila (peças quentes, CTA) ou Latão (peças de protocolo e segurança). Os dois só aparecem juntos se um deles estiver pequeno.

### Modo escuro
- Fundo: Pinho Profundo.
- Superfície: Pinho.
- Texto: Linho; secundário, Sálvia.
- Destaque: Argila Clara.
- Metal: Latão.

### Proibido
- Vermelho de alarme, verde-menta, turquesa, azul-hospital (código de veterinária).
- Rosa, lilás, azul-bebê (código infantil/template).
- Gradientes, neon.
- Latão em texto sobre claro.

## 2. Tipografia

Duas famílias, dois papéis. As duas são **OFL**: livres para uso comercial e para embutir.

| Família | Papel | Uso |
|---|---|---|
| **Literata** (serifa) | **A voz** | Títulos, frases de marca, citações. O **itálico** é o afeto: só em frases da Cuidadora, no máximo **1 por peça** |
| **Instrument Sans** (grotesca) | **O método** | Texto corrido, rótulos, horários, interface, relatório |

### Escala (web)
| Papel | Estilo | Tamanho / entrelinha |
|---|---|---|
| Display | Literata 600 · opsz 72 · −0,01em | 56 / 1,05 |
| Título 1 | Literata 600 · opsz 48 | 40 / 1,1 |
| Título 2 | Literata 600 · opsz 36 | 30 / 1,15 |
| Título 3 | Literata 600 · opsz 24 | 22 / 1,25 |
| Afeto | Literata Itálico 400 | 22 / 1,4 |
| Corpo | Instrument Sans 400 | 17 / 1,55 (mínimo 16) |
| Rótulo | Instrument Sans 600, CAIXA-ALTA, +0,14em, com argola ◦ | 12 / 1,2 |
| Dado | Instrument Sans 500, algarismos tabulares | 14 / 1,4 |

### Escala social (tela de 1080 px de largura)
| Papel | Tamanho |
|---|---|
| Display | 112 |
| Título | 76 |
| Subtítulo | 48 |
| Corpo | 36 |
| Rótulo | 28 |

**Nada abaixo de 28 px** (≈ 9 pt no celular).

### Regras
- Medida máxima: 68 caracteres.
- Títulos em caixa alta e baixa, nunca TUDO MAIÚSCULO em serifa. Caixa-alta só no rótulo.
- Números de horário sempre tabulares ("08:02", não "8h2").
- Contingência sem as fontes: Georgia + Arial.

## 3. Espaço, grid e composição

**Escala de espaço (base 4):** 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128.

| Formato | Grid |
|---|---|
| Instagram 1080×1350 | Margem 72 · 6 colunas · calha 24 |
| Stories/Reels 1080×1920 | Margem lateral 72 · zona segura: 250 px no topo e 340 px na base |
| Web | 12 colunas · máx. 1200 · calha 24 · margem 16 (celular) / 32 (tablet) |
| Impresso | Margem mínima de 5 mm + 3 mm de sangria |

**Comportamento:**
- **Uma mensagem por peça.**
- Alinhamento à esquerda para leitura.
- Centralizado só em selos, capas e assinatura vertical.
- Densidade média: respiro sim, vazio decorativo não.
- Contraste alto entre título e corpo.
- Assimetria permitida: foto sangrada + bloco de texto em cor sólida.

## 4. Raio, traço e elevação

- **Raios:** sm 6 (campos), md 12 (cartões), lg 20 (painéis), pílula (botões e selos de status).
- **Moldura-plaquinha:** arco 100×112 (`--tc-raio-plaquinha`). **Só** para foto de pet, selo e destaque. Nunca em botão ou campo.
- **Traço:** bordas de 1 px em Pinho 16%. Ícones com 1,5 px em grade de 24.
- **Sombra:** não há. A elevação vem da cor (Papel sobre Linho).

## 5. Dispositivos gráficos

1. **A plaquinha**: símbolo, moldura de foto, selo, etiqueta física.
2. **A argola ◦**: anel que abre rótulos, marca itens de lista, é o pingo do i e o furo da plaquinha. **Substitui a patinha em todas as funções** em que o mercado usaria uma.
3. **A linha de registro**: `08:02 ✓ entrada`, horário tabular + check + ação. Vem do Território B e aparece em relatórios e provas de processo.
4. **O filete de latão**: linha fina de 1–2 px em Latão sobre Pinho. Separa blocos em peças de protocolo.

## 6. Iconografia

- Linear, 1,5 px, grade 24, terminais e cantos arredondados (raio 2).
- Perspectiva frontal, sem preenchimento. A exceção é o ponto de status.
- **Complexidade máxima:** 3 formas por ícone.
- Base recomendada: **Phosphor (Regular)** ou **Lucide**, ajustada para 1,5 px.

**Vocabulário:**

| Ícone | Uso |
|---|---|
| chave | pet sitting |
| guia | passeio |
| relógio | rotina |
| prancheta com check | relatório |
| calendário | agenda |
| câmera | fotos |
| casa | domicílio |
| plaquinha | identificação |
| telefone | emergência |

**Proibidos:**
- patinha, osso, coração;
- cruz, estetoscópio, pílula, seringa (código de veterinária);
- escudo (código de segurança privada).

## 7. Fotografia

**A lógica dominante é fotografia documental. Não há ilustração nem mascote.**

| Faça | Não faça |
|---|---|
| Pet na **casa dele**, na rotina dele | Banco de imagem de "cão pulando feliz" |
| Altura dos olhos do pet, luz natural de janela | Flash, filtro pesado, vinheta |
| **Mãos da Clara** fazendo certo: ajustar peitoral, encher o pote, segurar a guia | Pet fantasiado, antropomorfizado |
| Detalhes de rotina: pote, guia no gancho, chaveiro codificado | Ambiente de clínica, jaleco, maca |
| Cor neutra-quente, verdes levemente dessaturados | Fotos escuras, tortas, com o rosto do tutor sem autorização |
| Passeio em lugar genérico (praça, calçada arborizada) | **Fachada, número da casa, portão, placa de rua** |

### Protocolo de privacidade (a Guardiã também está no conteúdo)
1. Nunca postar em tempo real que o tutor está fora. Publique **depois** do serviço.
2. Nunca mostrar fachada, número, portão, placa de rua ou vista da janela reconhecível.
3. Nunca geolocalizar o post durante o serviço.
4. Chaves só aparecem em chaveiro codificado, sem endereço.
5. Autorização de imagem do tutor antes de postar o pet.
