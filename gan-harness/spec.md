# Spec — Landing page da Tia Clara (modo gan-design)

## Brief (do usuário, literal)

> Landing page one-page da Tia Clara Pet Sitter & Dog Walker, HTML/CSS estático em tia-clara/10-site/. Seguir à risca tia-clara/08-brand-book/index.html, 05-design-system/tokens.css e design-system.md. Partir da primeira dobra em 07-producao/modelos/site-home-desktop.html e site-home-celular.html. Seções: hero, serviços, como funciona, relatório de visita, protocolos, avaliações, FAQ, CTA para WhatsApp, rodapé. Textos do banco de frases em 07-producao/producao.md. Originalidade = fidelidade à marca, não efeitos: um acento por seção, itálico só em frase de afeto, sem patinhas nem mascote. Responsivo de 390 a 1440 px, WCAG AA. Dados pendentes (bairro, telefone, fotos, estatística de 83%) como marcadores visíveis.

## Fontes da verdade (ler antes de construir)

| Arquivo | O que manda |
|---|---|
| `tia-clara/05-design-system/design-system.md` | Cor, proporção 60/25/10/5, tipografia web, grid, raios, dispositivos gráficos, ícones, fotografia, privacidade |
| `tia-clara/05-design-system/tokens.css` | **Único** vocabulário de cor, fonte, raio, espaço e movimento (Gate D1: nada fora dele) |
| `tia-clara/01-estrategia/estrategia.md` | Posicionamento, público, razões para acreditar (⚑ hipóteses), pilares, princípios verbais, anti-posicionamento |
| `tia-clara/07-producao/producao.md` | Banco de frases, palavras proibidas, regras de produção |
| `tia-clara/07-producao/modelos/site-home-desktop.html` e `site-home-celular.html` (+ PNGs em `07-producao/png/`) | Primeira dobra aprovada: ponto de partida do hero |
| `tia-clara/08-brand-book/index.html` | Referência visual geral (grande; use `grep` por seção) |
| `tia-clara/04-logo/master/*.svg` | Logos. Não redesenhar |

## Entregável

Site estático **autocontido** em `tia-clara/10-site/`, publicável sozinho (GitHub Pages / Netlify), sem build:

```
tia-clara/10-site/
  index.html
  css/tokens.css      # cópia de 05-design-system/tokens.css, só com os caminhos das fontes ajustados
  css/site.css
  js/site.js          # opcional, mínimo, vanilla (menu no celular). Nada de framework
  assets/logo/…       # SVGs copiados de 04-logo/master (os que forem usados)
  assets/fontes/…     # Literata e Instrument Sans (OFL) + as licenças
  favicon.svg / favicon.ico / apple-touch-icon
  README.md           # como publicar e lista de marcadores a substituir
```

Servido em `http://localhost:3000/` (a raiz do servidor é `tia-clara/10-site/`).

## Seções (nesta ordem)

1. **Cabeçalho**: assinatura horizontal compacta, navegação por âncoras, botão "Agendar apresentação". No celular: menu acessível.
2. **Hero**: partir da primeira dobra aprovada ("Pode deixar comigo.", rótulo com bairro/cidade como marcador, subtítulo, 2 CTAs, 3 provas com ícones, foto em moldura-plaquinha, cartão de relatório "Tudo certo por aqui.").
3. **Serviços**: pet sitting em domicílio (cães e gatos) e passeios (só cães). O que inclui. Preço: marcador ("a confirmar"), nunca inventar valores.
4. **Como funciona**: visita de apresentação → ficha do pet → visitas/passeios com relatório. Passos claros.
5. **Relatório de visita**: a peça-assinatura da marca (linha de registro `08:02 ✓ Entrada`, foto, observação, fecho "Tudo certo por aqui.").
6. **Protocolos**: chaves codificadas, equipamento de passeio (peitoral, guia com trava, plaquinha), emergência (autorização + veterinário do tutor), contrato, continuidade (sempre a mesma pessoa). Peça de protocolo: fundo Pinho com Latão.
7. **Avaliações**: depoimentos como **marcadores visíveis** (não inventar nomes nem citações apresentadas como reais).
8. **FAQ**: perguntas reais do público (objeções da estratégia: chave, "e se acontecer algo?", gatos, medicação, passeio em grupo). `<details>` nativo é bem-vindo.
9. **CTA para WhatsApp**: link `https://wa.me/55XXXXXXXXXXX` com marcador visível do telefone e mensagem pré-preenchida.
10. **Rodapé**: assinatura, contatos (marcadores), Instagram (marcador), privacidade da marca em uma linha, OFL/créditos se necessário.

## Regras de marca (não negociáveis)

- **Só tokens** de `tokens.css`. Nenhuma cor, fonte, raio ou sombra nova. **Sem sombras** (elevação vem da cor: Papel sobre Linho). **Sem gradientes** (a única exceção é a hachura do marcador de foto, já definida nos modelos).
- Proporção aproximada na página: 60 Linho/Papel · 25 Pinho · 10 Sálvia · 5 acentos. **Pinho lidera.**
- **Um acento dominante por seção**: Argila (seções quentes e CTA) **ou** Latão (protocolo, só sobre Pinho). Latão nunca como texto sobre fundo claro.
- **Itálico da Literata só em frase de afeto**, no máximo **um por seção** ("Tudo certo por aqui.", "Pode deixar comigo." quando usada como afeto…).
- Literata = voz (títulos). Instrument Sans = método (corpo, rótulos, horários). Rótulo em caixa-alta com a **argola ◦** (`.tc-rotulo`). Horários com algarismos tabulares.
- Moldura-plaquinha (`--tc-raio-plaquinha`) **só** em foto de pet, selo e destaque. Nunca em botão ou campo.
- Ícones lineares 1,5 px, grade 24, máx. 3 formas, do vocabulário do design system (chave, guia, relógio, prancheta com check, calendário, câmera, casa, plaquinha, telefone). **Proibidos**: patinha, osso, coração, cruz, estetoscópio, pílula, seringa, escudo.
- **Sem mascote, sem ilustração**: fotos documentais. Como ainda não há fotos, usar o **marcador de foto** dos modelos (hachura Sálvia + descrição da foto segundo as regras de fotografia).
- Texto: banco de frases e princípios verbais. **Evitar**: "aumigos", "filho de quatro patas", "mãe de pet", "fofurices", "risco zero", "100% seguro", "cuido como se fosse meu", termos clínicos (diagnóstico, tratamento, consulta, saúde). Medicação: "Administro a medicação prescrita pelo veterinário de vocês."
- Grafia: "Tia Clara"; descritor "Pet Sitter & Dog Walker" (com &).
- Privacidade: nada de fachada, endereço ou geolocalização.

## Dados pendentes → marcadores visíveis

Bairro/cidade, telefone/WhatsApp, @ do Instagram, preços, fotos, depoimentos e a **estatística de 83%** (pesquisa Rover 2026, não confirmada). Cada marcador deve ser **visível e inconfundível** na página (estilo consistente, ex. rótulo "A CONFIRMAR"), listado no `README.md` do site e fácil de achar no código (ex. `data-marcador`). Os protocolos da estratégia são hipóteses ⚑: podem aparecer, mas o README deve dizer que precisam ser confirmados com a Clara.

## Requisitos técnicos

- HTML semântico, `lang="pt-BR"`, um `h1`, hierarquia de títulos correta, landmarks, link "pular para o conteúdo".
- **WCAG 2.2 AA**: contraste (usar os pares aprovados do design system), foco visível em tudo que é clicável, navegação por teclado, alvos ≥ 24 px (ideal 44 px no celular), `prefers-reduced-motion` respeitado.
- **Responsivo de 390 a 1440 px** sem rolagem horizontal. Grid web: 12 colunas, máx. 1200, calha 24, margem 16 (celular) / 32 (tablet). Corpo ≥ 16 px.
- Movimento: pouco e com propósito, usando os tokens de duração/curva. Nada de animação decorativa.
- Modo escuro via tokens (`prefers-color-scheme`) é desejável, não obrigatório. Se fizer, tem de passar no contraste.
- SEO local básico: `<title>`, meta description, Open Graph, `LocalBusiness` em JSON-LD com marcadores, favicon.
- Desempenho: sem dependências externas obrigatórias; fontes com `font-display: swap`; imagens SVG.
