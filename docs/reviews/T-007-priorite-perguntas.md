# T-007 REV — Revisão independente de questions/priorite.json (24 perguntas)

Revisor: agente REV (não escreveu as perguntas). Data: 2026-11-26.
Fontes usadas: só legal/sources/741.01.txt (LCR), 741.11.txt (OCR), 741.21.txt (OSR) e legal/rules/priorite.yaml.
Método: cada pergunta foi resolvida a partir do texto oficial antes de olhar o gabarito; depois foram conferidos gabarito, justificativas, explicação, regra_ids e palavras_fr.

**Resultado geral: nenhum gabarito está errado segundo o texto oficial.** Os problemas são: falta de dados no enunciado (2), uma alternativa correta perigosa do jeito que está escrita (Q-020), generalizações nas justificativas e explicações, metadados, termos em francês e um vazamento sistemático da resposta (ver Riscos).

## 1. Tabela por pergunta

| id | veredito | problema | correção proposta (com texto oficial) |
|---|---|---|---|
| Q-PRIO-001 | CORRIGIR | Justificativa da alt. B: "A esquerda só ganha se a via for sinalizada como principal" é falso como regra geral: o tram (LCR 38 al. 1), o veículo prioritário (OCR 16 al. 1), sinais e polícia (LCR 36 al. 2, 3ª frase) também dão prioridade a quem vem da esquerda. `regra_simples` "Sem sinais, quem vem da direita passa primeiro" também é ampla demais (saída de garagem/estacionamento não é interseção, OCR 1 al. 8). | B: "Errada. LCR 36 al. 2 dá a prioridade a quem vem da direita; nada no enunciado dá prioridade ao carro da esquerda." `regra_simples`: "Em interseção sem sinais, quem vem da direita passa primeiro." `excecao`: acrescentar tram (LCR 38 al. 1) e veículo prioritário (OCR 16 al. 1). |
| Q-PRIO-002 | CORRIGIR | Gabarito certo. `regra_simples` "3.03 = você tem prioridade" e `excecao` "Nenhuma exceção" escondem os dois casos que o exame cobra: na via principal, quem vira à esquerda continua cedendo a quem vem em sentido contrário (LCR 36 al. 3: « Avant d'obliquer à gauche, le conducteur accordera la priorité aux véhicules qui viennent en sens inverse ») e quem sai de via principal que muda de direção cede ao sentido contrário (OCR 15 al. 1). | `regra_simples`: "3.03 = a priorité de droite deixa de valer contra você nas próximas interseções. 3.04 = ela volta." `excecao`: "Mesmo na via principal, ao virar à esquerda você cede a quem vem em sentido contrário (LCR 36 al. 3); tram e veículos prioritários seguem regras próprias." |
| Q-PRIO-003 | APROVAR | — (nota menor: o enunciado diz "passam carros" e a alt. B supõe "via livre"; funciona como hipótese, mas pode-se tirar "Na via que você vai cruzar passam carros"). | — |
| Q-PRIO-004 | APROVAR | — | — |
| Q-PRIO-005 | APROVAR | — | — |
| Q-PRIO-006 | CORRIGIR | Enunciado contraditório: "Você está **parado** em um semáforo que está **verde**", e a alt. A manda "se necessário, parar o veículo". | Enunciado: "Você se aproxima de um cruzamento com o semáforo verde para você. Uma ambulância se aproxima com luz azul e avisador de dois sons alternados." Resto igual (LCR 27 al. 2; OCR 16 al. 1 « même aux endroits où la circulation est réglée par des signaux lumineux »). |
| Q-PRIO-007 | APROVAR | — (cosmético: em `como_identificar`, "O sinal de que..." pode ser lido como placa de trânsito; trocar por "O indício de que..."). | — |
| Q-PRIO-008 | APROVAR | — | — |
| Q-PRIO-009 | CORRIGIR | Falta dado que muda a resposta. O enunciado exclui semáforo e polícia, mas não exclui sinal de prioridade nem diz qual via é principal. Se o tram vem de uma via secundária para a principal em que você está, ele é que cede (OCR 45 al. 2: « En débouchant d'une route secondaire sur une route principale, ils sont tenus d'accorder la priorité »), e a alt. A fica errada. A própria Q-013 ensina esse caso, então as duas se contradizem para o aluno. | Enunciado: "Numa interseção sem semáforo, sem policial e sem sinais de prioridade (nenhuma via é sinalizada como principal), os trilhos de um tram cruzam a pista. O tram vem pela sua esquerda..." Em `excecao`, manter a remissão para a Q-013. |
| Q-PRIO-010 | CORRIGIR | Falta dado: se você segue uma via principal que dobra à esquerda (placa 5.09), o carro em sentido contrário que segue reto sai da via principal e é ele que cede (OCR 15 al. 1; OSR 65 al. 1). Com seta verde sem amarelo piscante (OSR 68 al. 4) o caso também muda. O enunciado não exclui nenhum dos dois. `palavras_fr` "virer à gauche" não está no texto legal. | Enunciado: "Numa interseção sem semáforo, sem policial e sem placa 'Direction de la route principale' (5.09), você vai virar à esquerda..." `palavras_fr`: "obliquer à gauche — virar à esquerda" (LCR 36 al. 3). |
| Q-PRIO-011 | APROVAR | — (sugestão: em `excecao`, acrescentar que com semáforo desligado ou amarelo piscante o 3.02 volta a valer, OSR 36 al. 3, como já está em R-PRIO-043). | — |
| Q-PRIO-012 | APROVAR | — | — |
| Q-PRIO-013 | CORRIGIR | "Você segue numa via principal" pode ser lido como "rua maior". OCR 45 al. 2 depende de a via ser principal no sentido legal. | Enunciado: "Você segue numa via sinalizada como principal (sinal 3.03)..." |
| Q-PRIO-014 | CORRIGIR | Gabarito certo (OCR 15 al. 2). Metadados: a justificativa D cita OCR 14 al. 5 e regra_ids não tem R-PRIO-014. O enunciado não dá geometria: se as duas vias secundárias ficam frente a frente, nenhuma vem "da direita" da outra e o conflito real é resolvido pelo LCR 36 al. 3 (quem vira à esquerda cede). A alternativa A continua correta porque é abstrata. | regra_ids += R-PRIO-014. Enunciado: "...cada um por uma dessas vias secundárias; a via do outro carro fica à sua direita." (Isso também permite uma alternativa aplicada: "O outro carro passa antes de você.") `excecao` não é exceção: renomear o conteúdo ("Ambos cedem à via prioritária"). |
| Q-PRIO-015 | CORRIGIR | Terminologia em português confusa: no projeto, "pista" traduz *chaussée*, e a pergunta usa "pista ciclável" e "pista contígua" na mesma frase (alt. B). `palavras_fr` traduz *piste cyclable* por "ciclovia" e *bande cyclable* por "faixa ciclável", enquanto o enunciado e o YAML usam "pista/banda ciclável". O aluno vê três nomes para a mesma coisa. | Escolher um padrão único no projeto (sugestão: "ciclovia (piste cyclable)", "faixa ciclável (bande cyclable)", "pista (chaussée)") e aplicar no enunciado, nas alternativas e em palavras_fr. Gabarito sem mudança (OCR 40 al. 1 e 4). |
| Q-PRIO-016 | CORRIGIR | Gabarito certo (OSR 42 al. 1-2). `subtema` "inversao-de-prioridade" não bate com o R-PRIO-010 ("sinal-estreitamento"). `palavras_fr` "chaussée rétrécie" é o nome de outro sinal (sinal de perigo 1.07, OSR 65 al. 6); o art. 42 diz « là où la chaussée se rétrécit » / « passage rétréci ». | subtema = "sinal-estreitamento". palavras_fr: "là où la chaussée se rétrécit — onde a pista estreita" ou "passage rétréci — passagem estreitada". |
| Q-PRIO-017 | APROVAR | — | — |
| Q-PRIO-018 | APROVAR | — | — |
| Q-PRIO-019 | APROVAR | — | — |
| Q-PRIO-020 | CORRIGIR (prioridade alta) | Alt. B ("Com seta verde sem amarelo piscante, quem vira **não precisa dar prioridade aos pedestres**") está literalmente certa (OCR 6 al. 2, 2ª frase), mas o enunciado diz que **há pedestres atravessando** a via em que você entra. Junto, isso ensina "posso seguir mesmo com pedestres na faixa". O texto só tira a regra especial de prioridade; continuam valendo LCR 26 al. 1 (« ne pas gêner ni mettre en danger ») e LCR 26 al. 2 (prudência particular « s'il apparaît qu'un usager de la route va se comporter de manière incorrecte »). Risco de ensinar comportamento perigoso. | Enunciado: "Você vai virar numa interseção regulada por semáforo; há uma faixa de pedestres na via transversal em que você vai entrar." Alt. B: "Com seta verde sem amarelo piscante, a regra que obriga quem vira a ceder aos pedestres da via transversal (OCR 6 al. 2) não se aplica." `excecao`/`erro_comum`: "Mesmo com seta verde, se um pedestre ainda estiver na faixa, você não pode colocá-lo em perigo (LCR 26 al. 1-2)." |
| Q-PRIO-021 | CORRIGIR | Gabarito certo (OSR 65 al. 1). A justificativa C fundamenta mal: diz que a priorité de droite "foi suprimida nos sinais de via principal (OSR 37 al. 1)", mas o enunciado não tem 3.03 para você. Quem tira a priorité de droite é o Stop da sua via (OSR 36 al. 1) e a regra de que sinais prevalecem sobre regras gerais (LCR 27 al. 1). R-PRIO-002 em regra_ids é pouco pertinente e falta R-PRIO-005. | Justificativa C: "Errada. Você tem um Stop: deve parar e ceder aos veículos da via da qual se aproxima (OSR 36 al. 1); a placa 5.09 inclui quem sai da via principal (OSR 65 al. 1). Sinais prevalecem sobre as regras gerais (LCR 27 al. 1)." regra_ids: trocar R-PRIO-002 por R-PRIO-005 (ou acrescentá-lo). |
| Q-PRIO-022 | CORRIGIR | Gabarito certo (OCR 40 al. 5). `palavras_fr` "obliquer — virar/inflectir": "inflectir" não é português corrente. Mesmo problema de "pista ciclável" e "pista" da Q-015. O enunciado não diz o sentido da curva nem o do ciclista; a alternativa A é abstrata e continua certa, mas fica pouco aplicada. | palavras_fr: "obliquer — virar (mudar de direção)". Enunciado: "...vai virar à direita numa interseção. Um ciclista vem atrás de você, pela ciclovia, seguindo em frente." Terminologia igual à da Q-015. |
| Q-PRIO-023 | APROVAR | — | — |
| Q-PRIO-024 | CORRIGIR | Alt. B diz "os condutores **podem** subir na calçada". O texto é um dever: « Les conducteurs **empiéteront** sur le trottoir avec toutes les précautions nécessaires lorsqu'il est indispensable de dégager immédiatement la chaussée » (OCR 16 al. 2), e R-PRIO-028 diz "sobem". "Podem" não é falso, mas ensina como faculdade o que a lei impõe. `explicacao.por_que` cita OCR 16 al. 1 e LCR 27 al. 2, mas regra_ids não tem R-PRIO-027 nem R-PRIO-038. | B: "Quando for indispensável para liberar imediatamente a pista a um veículo prioritário, os condutores devem subir na calçada, com todas as precauções necessárias." regra_ids += R-PRIO-027, R-PRIO-038. |

Contagem: **APROVAR 11 · CORRIGIR 13 · REESCREVER 0 · REMOVER 0**.

## 2. palavras_fr duvidosas

| pergunta | termo | problema | sugestão |
|---|---|---|---|
| Q-010 | virer à gauche | não aparece no texto; a lei usa « obliquer à gauche » (LCR 36 al. 3) | obliquer à gauche — virar à esquerda |
| Q-016 | chaussée rétrécie | é o nome do sinal de perigo 1.07, não o termo do art. 42 | là où la chaussée se rétrécit / passage rétréci |
| Q-022 | obliquer — "virar/inflectir" | "inflectir" não é português corrente | virar (mudar de direção) |
| Q-015, Q-022 | piste cyclable — ciclovia; bande cyclable — faixa ciclável | termo FR certo, mas a tradução difere da usada no enunciado e no YAML ("pista/banda ciclável") | padronizar (ver Q-015) |
| Q-004 | ralentir | existe no OCR 41b, mas os artigos citados (OSR 36 al. 2, OCR 14 al. 1) dizem « réduira sa vitesse » | réduire sa vitesse — reduzir a velocidade |
| Q-020 | jaune clignotant | derivação aceitável; o texto diz « feu jaune clignote » | feu jaune clignotant (opcional) |

Os demais termos aparecem no texto oficial ou são derivação direta.

## 3. Resumo de riscos

1. **Vazamento sistemático da resposta (risco alto para o treino).** (a) Em todas as 24 perguntas, as alternativas corretas são as primeiras da lista. (b) Todas as perguntas com "Qual afirmação está correta?" (singular) têm exatamente 1 correta, e todas com "Quais afirmações..." têm 2 ou 3. O aluno aprende o padrão em vez da regra. Correção: o app deve embaralhar as alternativas, e o enunciado deve ser sempre "Quais afirmações estão corretas?". Não é erro de lei, mas invalida o treino no formato do exame (só pontua se todas as marcações estiverem certas).
2. **Q-020**: a alternativa correta, junto com o enunciado, pode ensinar a avançar sobre pedestres na faixa.
3. **Q-009 x Q-013**: sem o dado "nenhuma via é principal", as duas ensinam respostas que se contradizem.
4. **Q-010**: o caso da placa 5.09, que inverte a resposta, não é excluído pelo enunciado.
5. **Generalizações nas explicações** ("só ganha se", "3.03 = você tem prioridade", "excecao: nenhuma"): o aluno vai decorar justamente as frases curtas.
6. **Distratores fracos**: vários são absurdos e ninguém marcaria ("maior velocidade" na Q-001, "ninguém precisa dar prioridade" na Q-010, "ambos têm prioridade sobre a via prioritária" na Q-014, "só os trens rodoviários" na Q-009). Quase toda alternativa correta é paráfrase literal do artigo, o que treina reconhecimento de texto e não aplicação em situação.

## 4. Perguntas que dependem de interpretação

- **Q-020 B**: a lei afasta só a regra especial do OCR 6 al. 2; o dever geral do LCR 26 continua. A alternativa deve ser formulada como "a regra do OCR 6 al. 2 não se aplica", não como "não precisa ceder".
- **Q-014**: OCR 15 al. 2 manda aplicar a priorité de droite, mas se as duas vias ficam frente a frente nenhuma vem da direita; aí decide o LCR 36 al. 3. A pergunta precisa de geometria.
- **Q-022**: OCR 40 al. 5 não diz a direção da curva (o YAML já registra isso em nota). A pergunta deve fixar a direita e um ciclista seguindo reto. O caso de ciclovia a mais de 2 m numa interseção não está resolvido no texto: evitar.
- **Q-024**: se só a luz azul, de noite, obriga os outros a liberar a pista não está claro (o LCR 27 al. 2 fala de « avertisseurs spéciaux »). A pergunta não entra nisso e não deve entrar.

## 5. Lacunas de cobertura (regras validadas sem pergunta)

- **Ordem de passagem com 3 ou 4 usuários** (o tipo mais típico do exame suíço de Priorité, com imagem): por exemplo priorité de droite + virar à esquerda + tram, ou via principal com 5.09 + veículo que sai dela.
- Via principal + virar à esquerda (LCR 36 al. 3 dentro do 3.03).
- Sinais 3.05 e 3.06 (R-PRIO-008, 009) e o sinal de prioridade em geral (R-PRIO-004).
- OCR 14 al. 2 (consideração por quem chegou sem ver você, R-PRIO-012); al. 3 (filas paralelas, R-PRIO-013); al. 4 (cavaleiros, R-PRIO-033); al. 5 como resposta correta (todas as direções ao mesmo tempo, R-PRIO-014).
- Cruzamento com obstáculo na sua metade (OCR 9 al. 1, R-PRIO-032) e via estreita por categorias / montanha (OCR 9 al. 2, R-PRIO-040).
- Entrar na circulação, marcha à ré, retorno (LCR 36 al. 4, R-PRIO-030), sem ser pelo caso do ônibus.
- Pedestres: cego com bengala branca (R-PRIO-035), fora da faixa (R-PRIO-053), coluna sem faixa (R-PRIO-034), faixa com refúgio (OCR 47 al. 3).
- Semáforo desligado ou com amarelo piscante: os sinais voltam a valer (R-PRIO-043, exceções).
- Instruções de outras pessoas (OSR 67, R-PRIO-042: patrulheiros escolares, canteiro de obras).
- Hierarquia completa (R-PRIO-056): polícia > semáforo > sinais > regra geral, numa única situação.

## 6. Sugestões para as próximas perguntas

1. Enunciado padrão "Quais afirmações estão corretas?" e embaralhamento das alternativas no app (ou variar a posição no JSON).
2. Todo enunciado deve fixar explicitamente: sinais presentes/ausentes, semáforo, polícia, via principal sim/não, tram, veículo prioritário. É a checklist das variáveis que invertem a resposta.
3. Pelo menos 1 distrator plausível por pergunta (um que um aluno mediano marcaria), de preferência baseado numa exceção real de outro artigo.
4. Mais perguntas aplicadas ("Quem passa primeiro?", "Em que ordem?") com diagrama SVG, e menos paráfrase literal do artigo.
5. Nas explicações, nunca escrever "só", "sempre" ou "nenhuma exceção" sem conferir LCR 38 (tram), OCR 16 (prioritários), LCR 27 (polícia/sinais) e LCR 36 al. 3 (virar à esquerda).
6. Fixar no projeto um glossário PT único (chaussée = pista; piste cyclable / bande cyclable = ?) e validar palavras_fr contra o texto com grep antes de entregar.
