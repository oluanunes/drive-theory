# T-024 — Revisão independente: legal/rules/comportement.yaml (categoria C)

Revisor: REV · Data: 2026-11-26 · Objeto: 51 regras (R-COM-001 a 051), status `pendente`.
Fonte única: legal/sources/741.01.txt (LCR, État 2026-07-01), 741.11.txt (OCR, État 2026-10-01), 741.21.txt (OSR, État 2026-10-01), 741.51.txt (OAC, État 2026-01-01); 741.41.txt (OETV) só para remissões. Nada da web.
Método: (1) script próprio (fora do repositório) que separa cada artigo em alíneas pela posição do parágrafo, conta "…" como alínea, ignora títulos e linhas "(art. …)", junta as listas a./b. e 1./2. ao parágrafo, e confere se o `trecho_literal_fr` está na alínea indicada, se `trecho_completo: true` corresponde à alínea inteira e se cada `termos_fr` aparece no trecho; (2) busca, nos cinco arquivos, das remissões « art. N, al. Xbis » que mostram onde a contagem por posição falha; (3) leitura de cada regra contra o artigo inteiro e as remissões; (4) cruzamento com priorite.yaml (56), depassement.yaml (73) e arret-stationnement.yaml (88) por id e por lei/artigo/alínea; (5) busca de "0,5|0,8|0,25 mg|ébriété|pour mille" nas cinco fontes; (6) leitura do CURRICULO.md (categoria C e item 1.5.1) e do T-022-notas.md.

Resultado: **37 APROVAR · 14 CORRIGIR · 0 REMOVER** (+ cabeçalho do YAML).
- 51 de 51 trechos são cópia exata da alínea indicada (pela posição); os 33 marcados `trecho_completo: true` são a alínea inteira; nenhum `termos_fr` ausente do trecho.
- Nenhuma regra afirma o limite geral de 0,5 ‰. Nenhum valor inventado: todos os números (0,05 mg/l, 0,10 ‰, 12 anos, 150 cm, 4 e 7 anos, 25 km/h, 10 km/h, 50/80/100/120/30/20 km/h, 3,5 t, 1970) estão nas fontes.
- **LCR 31 al. 3 confere**: o 3.º parágrafo é a al. 2bis (a LCR cita « interdiction de conduire sous l'influence de l'alcool (art. 31, al. 2bis) », 741.01.txt l. 227 e 239; o OCR 2a cita « art. 31, al. 2bis et 2ter »), o 4.º é a 2ter, e o 5.º é a al. 3. A nota de R-COM-005 está certa.
- **Mas o LCR 41 tem o mesmo problema e passou**: os preâmbulos da OCR (« 41, al. 2bis ») e da OETV (« 41, al. 2bis et 3 ») mostram que o LCR 41 tem uma al. 2bis. O 3.º parágrafo (« Le Conseil fédéral peut prévoir … catadioptres ») é a 2bis, o 4.º é a al. 3 e o 5.º (« L'éclairage sera utilisé de manière à n'éblouir personne… ») é a **al. 4, não a 5** (R-COM-041).
- Os problemas sérios são de contexto: (a) as placas de velocidade máxima e mínima foram ensinadas sem o « au plus jusqu'à la fin de la prochaine intersection » do OSR 16 al. 2, e nenhuma regra do projeto diz isso para o 2.30/2.31 (R-ARR-039 omitiu de propósito); (b) os valores de 0,05 mg/l e 0,10 ‰, lidos sozinhos, não dizem que só valem para os grupos do OCR 2a al. 1.

## 1. Veredito por regra

Gravidade: **A** = ensina errado ou omite algo de prova; **M** = alínea errada, contexto ou exceção que falta, tradução que muda o sentido; **B** = forma, clareza, nota.

| id | veredito | grav. | problema | correção proposta (pronta para colar) |
|---|---|---|---|---|
| R-COM-001 | APROVAR | | | |
| R-COM-002 | APROVAR | | Tradução de « infirmes » correta. | |
| R-COM-003 | APROVAR | | | |
| R-COM-004 | APROVAR | | Quase o mesmo conteúdo de R-COM-007 (OCR 2 al. 1); as duas já se citam. | |
| R-COM-005 | APROVAR | | Alínea confere (ver Resultado). A nota está correta. | (opcional) acrescentar à `nota`: "Também confirmado pela própria LCR: « interdiction de conduire sous l'influence de l'alcool (art. 31, al. 2bis) » (741.01.txt, l. 227 e 239)." |
| R-COM-006 | APROVAR | | | |
| R-COM-007 | APROVAR | | | |
| R-COM-008 | APROVAR | | Lista let. a a g fiel; nenhuma concentração inventada; nota correta sobre o al. 3 (diretivas do OFROU). | |
| R-COM-009 | CORRIGIR | B | Lida sozinha, pode passar a ideia de que "com receita, pode dirigir". O dever de se abster está só em `excecoes`. | `regra_pt`: "A presença atestada de uma das substâncias do al. 2 (cannabis, morfina livre, cocaína, anfetamina, metanfetamina, MDEA, MDMA) não basta, por si só, para estabelecer a incapacidade de conduzir de uma pessoa que consiga provar que consome uma ou mais delas sob prescrição médica. Isso não autoriza a conduzir: quem não é capaz de conduzir, inclusive sob efeito de medicamento, deve se abster (OCR 2 al. 1, R-COM-007; LCR 31 al. 2, R-COM-004)." |
| R-COM-010 | APROVAR | | | |
| R-COM-011 | CORRIGIR | M | « courses d'apprentissage » / « courses d'exercice » viraram "cursos de aprendizagem e de exercício". « Course » aqui é trajeto/viagem ao volante, não curso; "curso de exercício" não faz sentido e "curso" sugere matrícula em autoescola. É justamente a let. que cobre o Luan agora (f, g) e depois do exame prático (h). `termos_fr` ["interdite"] é fraco. | Na `regra_pt`, trocar "f) para condutores de veículos em cursos de aprendizagem (« courses d'apprentissage ») e de exercício; g) para acompanhantes em cursos de aprendizagem;" por "f) para condutores de veículos em trajetos de aprendizagem (« courses d'apprentissage ») e trajetos de exercício (« courses d'exercice »); g) para acompanhantes em trajetos de aprendizagem;". `termos_fr`: ["La conduite sous l'influence de l'alcool est interdite"]. Acrescentar à `nota`: "A definição de « influence de l'alcool » está no al. 3 (R-COM-012 a 014) e vale para esta proibição." |
| R-COM-012 | CORRIGIR | M | Lida sozinha, a `regra_pt` diz que "há influência do álcool" a partir de 0,05 mg/l, sem dizer a quem isso se aplica. O aviso está só na `nota`. O gerador de perguntas e o aluno podem generalizar para todos os condutores. | `regra_pt`: "Para a proibição do OCR 2a al. 1 (R-COM-011: entre outros, quem conduz ou acompanha em trajetos de aprendizagem e o titular de permis de conduire à l'essai), há influência do álcool quando o condutor apresenta, entre outros casos, uma concentração de álcool no ar expirado de 0,05 mg/l ou mais. O OCR 2a não diz que este valor vale para os demais condutores." `nota`: "O limite dos demais condutores (« état d'ébriété ») é fixado por ordonnance da Assemblée fédérale (LCR 55 al. 6), que não está em legal/sources. Não usar o « 0,50 pour mille » nem o « 0,25 mg/l » do OAC 36 al. 4: tratam de advertência a quem conduz veículo para o qual não se exige permis de conduire." |
| R-COM-013 | CORRIGIR | M | Mesmo problema de 012, com o valor (0,10 ‰) que mais vai cair em pergunta. | `regra_pt`: "Para a proibição do OCR 2a al. 1 (R-COM-011: entre outros, quem conduz ou acompanha em trajetos de aprendizagem e o titular de permis de conduire à l'essai), há influência do álcool quando o condutor apresenta, entre outros casos, uma taxa de álcool no sangue de 0,10 por mil ou mais. O OCR 2a não diz que este valor vale para os demais condutores." `nota`: a mesma de R-COM-012. |
| R-COM-014 | CORRIGIR | M | Mesmo problema de 012. Falta a `nota` que 012 e 013 têm. | `regra_pt`: "Para a proibição do OCR 2a al. 1 (R-COM-011), há influência do álcool quando o condutor apresenta, entre outros casos, uma quantidade de álcool no organismo que leva a uma taxa de álcool no sangue como a da let. b (0,10 por mil ou mais). O OCR 2a não diz que este valor vale para os demais condutores." `nota`: a mesma de R-COM-012. |
| R-COM-015 | APROVAR | | Fiel. A nota (o texto não diz « téléphone ») é exatamente o que a regra pode afirmar. Perguntas sobre celular só podem usar « système d'information ou de communication » e o dever de atenção; nada de "viva-voz permitido" nem multa. | |
| R-COM-016 | APROVAR | | Ver §4, ponto 4 (numeração do OCR 3 al. 4 citada em `excecoes`). | |
| R-COM-017 | APROVAR | | | |
| R-COM-018 | APROVAR | | Let. a a g fiéis, condições de 25 km/h mantidas em b, c e g. A nota contra generalizar a let. d está correta. | |
| R-COM-019 | APROVAR | | Alínea confirmada pela OETV (« art. 3a, al. 3, OCR », painéis do cinto obrigatório, 741.41.txt l. 3770). | |
| R-COM-020 | APROVAR | | | |
| R-COM-021 | CORRIGIR | B | A nota está certa (o texto não dispensa do cinto), mas a `regra_pt` sozinha permite ler "criança com 150 cm: nada é obrigatório". | Acrescentar à `regra_pt`: "Essas exceções dispensam só o dispositivo de retenção; o OCR 3a al. 1 continua exigindo que o condutor se assegure de que crianças com menos de doze anos estão corretamente presas (R-COM-017)." |
| R-COM-022 | APROVAR | | Condição « favorables » mantida. Ver §4, ponto 3 (numeração do OCR 4a). | |
| R-COM-023 | APROVAR | | | |
| R-COM-024 | APROVAR | | | |
| R-COM-025 | APROVAR | | | |
| R-COM-026 | APROVAR | | | |
| R-COM-027 | APROVAR | | | |
| R-COM-028 | APROVAR | | Nota honesta: o 100 km/h vem da frase de abertura do al. 2. | |
| R-COM-029 | APROVAR | | | |
| R-COM-030 | APROVAR | | | |
| R-COM-031 | CORRIGIR | **A** | Ensina que a velocidade máxima sinalizada só termina no 2.53/2.53.1. O OSR 16 al. 2 (no arquivo, 741.21.txt l. 137) limita: « doivent être observés jusqu'au signal correspondant indiquant la fin de la prescription (2.53, 2.54, 2.55, 2.56, 2.58) mais au plus jusqu'à la fin de la prochaine intersection », com exceção expressa do 2.30.1 (toda a zona construída). Nenhuma regra do projeto ensina isso para o 2.30: R-ARR-039 (mesma alínea) omitiu 2.30/2.31 "por estarem fora do tema" (nota dela). É pergunta clássica de prova. | Acrescentar à `regra_pt`: "Sem sinal de fim, o « Vitesse maximale » (2.30) vale no máximo até o fim da próxima interseção (onde o sinal é repetido se a validade deve continuar); o OSR 16 al. 2 inclui o « Libre circulation » (2.58) entre os sinais de fim. Exceção: o 2.30.1 vale em toda a zona construída de forma compacta da localidade (OSR 16 al. 2; R-COM-023)." `excecoes`: acrescentar "Regra de outra disposição (não consta desta alínea): OSR 16 al. 2 (R-ARR-039): « Les signaux "Vitesse maximale" (2.30), "Vitesse minimale" (2.31) […] doivent être observés jusqu'au signal correspondant indiquant la fin de la prescription (2.53, 2.54, 2.55, 2.56, 2.58) mais au plus jusqu'à la fin de la prochaine intersection. Le signal "Vitesse maximale 50, Limite générale" (2.30.1) s'applique dans toute la zone bâtie de façon compacte à l'intérieur des localités »." e "Ver R-DEP-060 (OSR 32 al. 1: sinais de fim)." |
| R-COM-032 | APROVAR | | Artigo de um só parágrafo citado como al. 1 (ver §5). | |
| R-COM-033 | APROVAR | | Coerente com a nota de R-PRIO-054 (20 km/h). | |
| R-COM-034 | CORRIGIR | M | Mesma omissão de 031 para o 2.31. | Acrescentar à `regra_pt`: "Sem sinal de fim, a velocidade mínima sinalizada vale no máximo até o fim da próxima interseção; o OSR 16 al. 2 inclui o « Libre circulation » (2.58) entre os sinais de fim." `excecoes`: acrescentar a mesma citação do OSR 16 al. 2 proposta em R-COM-031. |
| R-COM-035 | APROVAR | | "meia-volta" aqui × "retorno" em R-ARR-082 para o mesmo « faire demi-tour »: padronizar (glossário). | (opcional) `excecoes`: acrescentar "Regra de outra disposição (não consta desta alínea): OCR 27 al. 5: nos trajetos de aprendizagem, nas « chaussées fortement fréquentées », « il est interdit […] de faire demi-tour sur la chaussée » (ver Lacuna L-01)." |
| R-COM-036 | APROVAR | | | |
| R-COM-037 | CORRIGIR | B | "Quanto ao resto" fica sem referente quando a regra é lida sozinha. | Trocar o início da `regra_pt` por: "Fora dos casos do al. 1 (do anoitecer ao amanhecer, com má visibilidade e nos túneis: faróis baixos, R-COM-036), o uso das luzes de circulação diurna ou dos faróis baixos é obrigatório para os veículos a motor; …" (resto igual). |
| R-COM-038 | CORRIGIR | B | `excecoes` cita "LCR 41 al. 5"; é a al. 4 (ver R-COM-041). | `excecoes`: "Regra de outra disposição (não consta desta alínea): LCR 41 al. 4 (R-COM-041): a iluminação deve ser usada de modo a não ofuscar ninguém sem necessidade." |
| R-COM-039 | APROVAR | | Corretamente sem metros de visibilidade (o texto não fixa). | |
| R-COM-040 | APROVAR | | | |
| R-COM-041 | CORRIGIR | M | Alínea errada: é o 5.º parágrafo, mas o LCR 41 tem al. 2bis (preâmbulo da OCR: « 41, al. 2bis »; preâmbulo da OETV: « 41, al. 2bis et 3 »). O 3.º e o 4.º parágrafos são as duas delegações ao Conselho Federal (catadióptricos; cores das luzes), ou seja, 2bis e 3. Logo, « n'éblouir personne » é a al. 4. | `fonte.alinea`: "4". `nota`: "Numeração: 5.º parágrafo do arquivo; no texto legal é a al. 4, porque o 3.º parágrafo (« Le Conseil fédéral peut prévoir … catadioptres ») é a al. 2bis (remissões « 41, al. 2bis » no preâmbulo da OCR e « 41, al. 2bis et 3 » no da OETV). Confirmar no HTML do Fedlex." |
| R-COM-042 | APROVAR | | Let. a a h fiéis. | |
| R-COM-043 | APROVAR | | | |
| R-COM-044 | APROVAR | | | |
| R-COM-045 | APROVAR | | | |
| R-COM-046 | APROVAR | | | |
| R-COM-047 | APROVAR | | | |
| R-COM-048 | CORRIGIR | B | « course d'apprentissage » traduzido como "curso de aprendizagem" (ver R-COM-011). | `regra_pt`: "Ninguém pode conduzir um veículo a motor sem ser titular de um permis de conduire ou, se faz um trajeto de aprendizagem (« course d'apprentissage »), de um permis d'élève conducteur." |
| R-COM-049 | APROVAR | | Alínea 4 confirmada pela própria LCR (« Art. 10, al. 1, 2 et 4 … », l. 1598). Exceção do OAC 24g confere com o texto. | |
| R-COM-050 | CORRIGIR | B | « lieu de stationnement » virou "local de estacionamento". No projeto, "estacionar" traduz « parquer » (categoria B), e a frase sugere vaga de estacionamento. A alínea não define o termo. | `regra_pt`: "Deve-se pedir um novo permis de circulation quando o veículo muda de « lieu de stationnement » de um cantão para outro ou passa a outro detentor." `nota`: "« lieu de stationnement » não é definido nesta alínea; não traduzir como 'vaga' ou 'local de estacionamento'." |
| R-COM-051 | CORRIGIR | B | Regra e alínea corretas (item 1.5.1). A `excecao` restringe o LCR 10 al. 4 a "(permis de conduire)"; o texto diz « leurs permis », sem especificar. | `excecoes`: "Regra de outra disposição (não consta desta alínea): LCR 10 al. 4 (R-COM-049): os condutores devem sempre portar « leurs permis » e apresentá-los, quando solicitado, aos órgãos de controle." |

**Cabeçalho do YAML (linha 7): CORRIGIR (B).** Trocar "Única exceção: LCR 31, alinea "3" …" por: "Exceções: LCR 31 al. 3 (5.º parágrafo; os 3.º e 4.º são as al. 2bis e 2ter, ver R-COM-005) e LCR 41 al. 4 (5.º parágrafo; o 3.º é a al. 2bis, ver R-COM-041). Atenção: a contagem por posição falha sempre que o artigo tem alínea bis/ter; também acontece no LCR 55 (a LCR cita « art. 55, al. 6 » e a OCR « 55, al. 7, let. a » para os 7.º e 9.º parágrafos do arquivo)."

## 2. Lacunas (só com base nos textos disponíveis)

Prioridade alta:
1. **L-01: OCR 27, « Courses d'apprentissage »** (741.11.txt, l. 394-405). O CURRICULO.md põe o OCR 27 na categoria C, e nenhum YAML o cobre. É a situação atual do Luan: placa « L blanc sur fond bleu », visível de trás e retirada fora dos trajetos de aprendizagem (al. 1); acompanhante sentado ao lado e alcançando ao menos o freio de mão (al. 2); autoestradas e semiautoestradas só quando pronto para o exame (al. 4); proibido arrancar em subida, fazer meia-volta e marcha à ré nas « chaussées fortement fréquentées » (al. 5). Confirmar a numeração (6 parágrafos, sem "…") antes de criar.
2. **L-02: OSR 16 al. 2 para 2.30/2.31.** Resolvido pelas correções de R-COM-031 e 034. Alternativa: ampliar a `regra_pt` de R-ARR-039 (já pedido no T-020, L-01, para 2.44/2.45). Sem uma das duas, o projeto não ensina a validade das placas de velocidade.

Prioridade média:
3. **L-03: limite geral de álcool.** Não está nas fontes (ordonnance da Assemblée fédérale, LCR 55 al. 6; RS 741.13 não baixada). **Armadilha:** uma busca por "0,50 pour mille" acha o OAC 36 al. 4 (741.51.txt, l. 811), mas ele trata de advertência a quem conduz « un véhicule automobile pour lequel le permis de conduire n'est pas nécessaire ». Não serve de fonte para o limite dos condutores de cat. B. O mesmo vale para o 1,6 ‰ do LCR 15d (inquérito de aptidão). Correção ao T-022-notas, item 1: o LCR 31 al. 2ter remete ao Conselho Federal (os valores do OCR 2a al. 3), não à Assemblée fédérale; só o LCR 55 al. 6 remete à Assemblée fédérale.
4. **L-04: OCR 4, última alínea** (« ne pas diminuer la fluidité du trafic … à une allure trop réduite »). Numeração incerta (« et … » pode ser « 2 et 3 … »), já apontado no T-020 (R-DEP-021, L-04).
5. **L-05: OCR 5 al. 1** let. a ch. 4 (80 km/h com « pneus à clous ») e let. c ch. 1 (40 km/h). **Tradução:** T-022-notas item 5 chama a let. c ch. 1 de "reboque"; « remorquage » é rebocar um veículo (inclusive avariado, « chariot de dépannage »), não puxar um reboque.
6. **L-06: LCR 15a al. 1** (« Le permis de conduire obtenu pour la première fois … est délivré à l'essai. La période probatoire est de trois ans. »). Dá o contexto da let. h de R-COM-011 (álcool proibido no permis à l'essai).
7. **L-07: LCR 63 al. 1** (nenhum veículo a motor « ne peut être mis en circulation » sem seguro de responsabilidade civil). Encaixa no item 1.5.1 ao lado de R-COM-047.

Prioridade baixa:
8. OAC 5 (« Exceptions à l'obligation de posséder un permis », 741.51.txt l. 147) está no arquivo e não foi lido (R-COM-048 diz isso honestamente).
9. OSR 22 al. 3 e 4 (onde se colocam os 2.30.1/2.53.1). Coerentes com R-COM-023.
10. OSR 27 al. 1 (2.46, proibição de meia-volta) e OCR 36 al. 1 (meia-volta proibida em autoestrada): já no T-020 (L-07, item 10).
11. Condução ecológica (1.2.3): só OCR 33/34 nas fontes; « roulement en poussée » não está nelas. Não inventar.

Não estão nos arquivos-fonte e não devem ser inventados: limite geral de 0,5 ‰ / 0,25 mg/l para condutores com permis definitivo; concentrações de drogas; proibição expressa do telefone ou regra do viva-voz; metros de visibilidade para o farol de neblina traseiro; multas.

## 3. Duplicatas e referências cruzadas

Todas as referências cruzadas do YAML apontam para o artigo/alínea dito (conferido id por id: R-DEP-021, 034-036, 046, 069, 070; R-PRIO-023, 026, 031, 038, 054; R-ARR-004, 029-031, 078, 080-083). Nenhuma regra repete lei/artigo/alínea de outro YAML.

- **R-COM-031/034 × R-ARR-039 (OSR 16 al. 2) × R-DEP-060 (OSR 32 al. 1):** complementares; hoje ninguém ensina a validade do 2.30/2.31 (correção A acima).
- **R-COM-033 × R-PRIO-054:** mesma zona de encontro, alíneas diferentes; coerentes.
- **R-COM-016 × R-ARR-083; R-COM-035 × R-ARR-080 a 082; R-COM-036 × R-ARR-078; R-COM-040 × R-ARR-004; R-COM-006 × R-DEP-021; R-COM-002 × R-PRIO-023:** mesmo artigo, deveres diferentes, já ligados.
- **Internas:** 004 × 007 (LCR 31 al. 2 × OCR 2 al. 1, quase o mesmo dever) e 022 × 023-026 (lista × início/fim de cada limite): repetições coerentes, já ligadas.
- Terminologia: « faire demi-tour » = "meia-volta" (R-COM-035) × "retorno" (R-ARR-082). Padronizar no GLOSSARIO.md.

Não há duplicata a remover.

## 4. Pontos que exigem decisão do Luan

1. **Limite geral de álcool (L-03):** (a) pedir ao PESQ que baixe a RS 741.13 e crie a regra; ou (b) seguir sem ela e não gerar pergunta sobre permis definitivo. Recomendo (a): é pergunta frequente de prova. Em nenhum caso usar o 0,50 ‰ do OAC 36 al. 4.
2. **LCR 41 al. 4 (R-COM-041):** aceitar a numeração deduzida das remissões (sólida: dois preâmbulos citam a 2bis) ou confirmar no HTML do Fedlex antes de validar.
3. **OCR 4a (R-COM-022 a 027) e OCR 5 al. 4/5 (029, 030):** nenhuma remissão nas fontes confirma as al. 3 a 6 do OCR 4a nem as al. 4/5 do OCR 5. O limite de 100 km/h nas semiautoestradas pode ter entrado depois, como « al. 3bis »; nesse caso as al. 4, 5 e 6 passariam a 3bis, 4 e 5. Não consigo decidir sem o HTML. Os trechos estão certos; só os números podem mudar.
4. **OCR 3 al. 4 (R-ARR-083, citado em R-COM-016 e no cabeçalho):** o « système d'aide au stationnement » parece inserção recente e pode ser « al. 3bis ». Nenhuma remissão nas fontes decide. Confirmar no HTML.
5. **Validade das placas 2.30/2.31 (L-02):** corrigir em R-COM-031/034 (recomendado, é velocidade) ou ampliar R-ARR-039.
6. **OCR 27 (L-01):** abrir tarefa PESQ curta antes do exame (20/12). É o artigo mais ligado à situação atual do Luan e não está em nenhum YAML.
7. **Item 1.5.1:** o CURRICULO.md diz "nenhuma categoria"; aqui ficou em C (047 a 051). Manter em C ou criar categoria própria. Não afeta o conteúdo.
8. **Glossário:** "trajeto de aprendizagem" para « course d'apprentissage », « lieu de stationnement » sem tradução, "meia-volta" para « demi-tour ».

## 5. Notas

- **Artigos de um só parágrafo** (OSR 22a em R-COM-032; OCR 33 em R-COM-042 é parágrafo único com lista) estão como `alinea: "1"`. No Fedlex esses artigos não têm número de alínea. Nenhum YAML do projeto usa `alinea: ""`; manter a convenção, mas uma citação "OSR 22a al. 1" mostrada ao aluno não existe formalmente. Sugestão: o app mostrar só "OSR 22a" quando o artigo tem um só parágrafo.
- **Exceções do OCR 2a al. 2 (R-COM-011):** a let. b só vale para quem é mobilizado « ni en service ni de permanence ». O resumo "nas condições do texto" basta; não detalhar em pergunta de cat. B.
- **Qualidade geral:** cópia 100% literal, notas honestas sobre o que o texto não diz (telefone, drogas, álcool, cinto × dispositivo), nenhum valor inventado. Os erros reais são de numeração bis (LCR 41), de validade de sinal (OSR 16 al. 2) e de contexto do álcool.

## 6. Resumo

| | quantidade |
|---|---|
| Regras revisadas | 51 |
| APROVAR | 37 (2 com ajuste opcional: 005, 035) |
| CORRIGIR | 14 (A: 1 · M: 6 · B: 7) + cabeçalho do YAML |
| REMOVER | 0 |
| Trechos literais exatos | 51/51 |
| Alíneas erradas | 1 confirmada (041); 2 grupos a confirmar no HTML (OCR 4a/5; OCR 3 al. 4) |
| Lacunas | 11 (alta: 2 · média: 5 · baixa: 4) |
| Pontos para decisão do Luan | 8 |

CORRIGIR por gravidade:
- A: 031
- M: 011, 012, 013, 014, 034, 041
- B: 009, 021, 037, 038, 048, 050, 051 (+ cabeçalho)
