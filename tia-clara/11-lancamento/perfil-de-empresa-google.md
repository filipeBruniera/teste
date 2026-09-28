# Perfil de Empresa no Google: guia de configuração

> Preparado pelo agente `seo-specialist` na revisão de SEO local ([`revisao-seo.md`](revisao-seo.md)). Tudo aqui depende dos dados reais: bairros, cidade, telefone e fotos.

## Categorias
- **Principal:** `Pet Sitter`
- **Secundária:** `Dog Walker`
- **Não adicionar** o que não é praticado: "Pet Groomer", "Veterinary Care". A estratégia é explícita em "não parecer veterinária".

## Empresa de área de atendimento, com endereço oculto
A Clara atende na casa do cliente, e o protocolo de privacidade proíbe expor a fachada ou o endereço.

1. Perfil de Empresa → Editar perfil → Local → Editar.
2. Desativar "Mostrar endereço aos clientes".
3. Definir a área de atendimento por cidade ou CEP. O Google não aceita raio de distância.
4. Listar só os bairros de fato atendidos, provavelmente de 3 a 8. O máximo permitido é 20.

**Áreas:** `[BAIRRO_1]`, `[BAIRRO_2]`, … + `[CIDADE]`. Precisa ser a mesma lista do rodapé do site e do `areaServed` do JSON-LD.

## Descrição (limite de 750 caracteres)
Rascunho no tom da marca, com cerca de 640 caracteres com os marcadores. Depois de preencher, confirme a contagem no editor.

```
Pet sitting em domicílio e passeios com cães em [BAIRRO], [CIDADE]. A Tia Clara cuida do seu pet na casa dele, na rotina dele — cães e gatos no pet sitting, só cães nos passeios. Cada visita segue um protocolo: chaves codificadas sem o seu endereço, ficha do pet com alimentação, horários e medicação prescrita pelo veterinário de vocês, e um relatório ao final — horário, o que foi feito e uma foto. Nos passeios, peitoral ajustado, guia com trava e plaquinha de identificação. É sempre a mesma pessoa cuidando do seu pet, visita após visita. Tudo em ordem enquanto você não está. Marque uma visita de apresentação pelo WhatsApp: [TELEFONE].
```

> ⚑ A descrição repete promessas de protocolo que ainda são hipóteses. Veja a auditoria de promessas em [`revisao-texto.md`](revisao-texto.md). Corte o que a Clara não praticar antes de publicar.

## Serviços
- Pet sitting em domicílio (cães)
- Pet sitting em domicílio (gatos)
- Passeios com cães / dog walking

Cada serviço pode ter uma descrição curta. Dá para reaproveitar os textos da seção Serviços do site.

## Atributos
A lista disponível depende da categoria: confira no painel. Não marque nenhum atributo de identidade (ex.: "administrado por mulheres") sem confirmação explícita da Clara. Essa decisão é dela.

## Fotos (protocolo de privacidade do design system, seção 7)
- Fotografia documental real:
  - o pet na casa dele;
  - as mãos da Clara ajustando o peitoral ou enchendo o pote;
  - o chaveiro codificado e a plaquinha.
- Nunca banco de imagens.
- Nunca fachada, número da casa, portão, placa de rua ou vista de janela reconhecível.
- Publicar sempre **depois** do serviço, sem geolocalização.
- Autorização do tutor antes de qualquer foto com o pet.

## Avaliações
- Pedir pelo link direto do Google, enviado no WhatsApp depois de um serviço concluído.
- Nunca oferecer desconto ou brinde em troca de avaliação: é contra a política do Google.
- Nunca pedir avaliação só aos clientes satisfeitos (seleção de avaliações).
- Responder a todas, inclusive as negativas, no tom firme e gentil do banco de frases.

## Consistência de nome, área e telefone
- **Nome:** usar uma grafia única e exata no cadastro do Google, no Instagram e no WhatsApp Business. Recomendado: **Tia Clara Pet Sitter & Dog Walker**, sem travessão, porque o Google desaconselha pontuação extra no campo de nome. O travessão pode continuar no `<title>` do site.
- **Área:** os mesmos bairros e a mesma cidade no site, no Google e na bio do Instagram.
- **Telefone:** o mesmo número no site (`wa.me`, rodapé, JSON-LD), no Google e no Instagram.

## Fontes consultadas pelo revisor
- [Google Business Profile Help: service areas](https://support.google.com/business/answer/9157481)
- [Barketing: GBP tips for pet sitters and dog walkers (2026)](https://barketing.co/google-business-profile-tips-for-pet-sitters-and-dog-walkers-in-2026/)
- [Voxa Digital: GBP categories 2026](https://voxadigital.com/google-business-profile-categories/)
- [Local Falcon: when to hide your address](https://www.localfalcon.com/blog/when-should-you-hide-your-address-on-google-business-profile)
- [Whitespark: JSON-LD for local business](https://whitespark.ca/blog/the-json-ld-markup-guide-to-local-business-schema/)
