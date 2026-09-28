# Rubrica de avaliação — modo design (gan-design)

**Nota ponderada** = Design × 0,35 + Originalidade × 0,30 + Acabamento × 0,25 + Funcionalidade × 0,10
**Aprovação:** ≥ 7,5. Escala 1–10 por critério, com a calibragem do avaliador (7 = sólido, 8 = profissional, 9 = sênior, 10 = entregável como produto real).

> Por pedido do usuário, **Originalidade = fidelidade à marca, não efeitos.** A pergunta não é "ganharia um prêmio por ousadia?", e sim "um diretor de arte da marca aprovaria isso como a Tia Clara, e ela não se confunde com nenhum template de pet shop?".

### Design Quality (weight: 0.35)
Hierarquia, composição, ritmo entre seções, tipografia, uso de cor e espaço. É um todo coerente?
- 1–3: template genérico, blocos iguais empilhados, "AI slop".
- 4–6: correto mas previsível; hierarquia fraca; seções com o mesmo layout.
- 7–8: composição própria por seção, alternância Linho/Papel/Pinho/Sálvia com propósito, ritmo claro, primeira dobra fiel ao modelo aprovado.
- 9–10: parece feito pelo estúdio que criou o brand book.

### Originality — brand fidelity (weight: 0.30)
Distinção **dentro** do sistema: usa os dispositivos próprios (plaquinha, argola ◦, linha de registro, filete de latão) para dizer coisas, não para enfeitar.
- **Penalizar forte (nota ≤ 4 se ocorrer)**: cor/fonte/raio/sombra fora dos tokens; gradiente (exceto a hachura do marcador de foto); patinha, osso, coração, cruz, escudo, mascote; Latão em texto sobre claro; mais de um acento dominante por seção; itálico fora de frase de afeto ou mais de um por seção; moldura-plaquinha em botão/campo; texto proibido (ver spec).
- 1–3: poderia ser qualquer pet shop; viola regras de marca.
- 4–6: segue os tokens, mas os dispositivos da marca são decoração ou estão ausentes.
- 7–8: a página só poderia ser da Tia Clara; relatório e protocolo são protagonistas; tom "Pode deixar comigo." do começo ao fim.
- 9–10: cada seção tem um momento memorável que nasce do sistema, não de efeitos.

### Craft (weight: 0.25)
Acabamento, responsividade, acessibilidade, estados.
- 1–3: quebra no celular, rolagem horizontal, contraste reprovado, sem foco visível.
- 4–6: funciona, mas espaçamentos inconsistentes, textos mal quebrados, alvos pequenos, fontes caindo para fallback.
- 7–8: 390/768/1024/1440 sem defeitos; foco visível; contraste AA; hover/focus/active consistentes; movimento com tokens e reduzido quando pedido.
- 9–10: pixel-perfect, micro-detalhes (quebras de título, alinhamento de linhas de base, números tabulares).

### Functionality (weight: 0.10)
- 1–3: seções faltando, âncoras quebradas, links mortos, erros no console.
- 4–6: tudo presente, mas menu do celular/FAQ/âncoras com falhas, marcadores confusos.
- 7–8: todas as seções do spec; âncoras, menu, FAQ e link do WhatsApp funcionam; marcadores visíveis e listados no README; JSON-LD válido.
- 9–10: impecável também em teclado, leitor de tela e sem JS.

## Falhas críticas (limitam a nota ponderada a 6,0 até serem corrigidas)
1. Rolagem horizontal em qualquer largura de 390 a 1440.
2. Par de texto/fundo abaixo de 4,5:1 (ou 3:1 para texto grande ≥ 24 px / 18,66 px negrito).
3. Uso de motivo proibido (patinha, osso, coração, cruz, escudo, mascote) ou dado inventado apresentado como real (preço, depoimento, telefone, estatística sem marcador).
4. Seção obrigatória ausente.
