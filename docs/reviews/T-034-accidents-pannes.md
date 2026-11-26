# T-034 — Revisão independente: legal/rules/accidents-pannes.yaml (categoria F)

Revisor: REV · Data: 2026-11-26 · Objeto: 37 regras (R-ACC-001 a 037), status `pendente`.
Fonte única: legal/sources/741.01.txt (LCR, État 2026-07-01), 741.11.txt (OCR), 741.21.txt (OSR), 741.41.txt (OETV), État 2026-10-01. Nada da web.
Método: (1) script próprio (fora do repositório) que separa cada artigo em parágrafos pela posição, conta "…" e "et …" como um parágrafo, ignora linhas "(art. …)" e junta listas a./b. ao parágrafo; confere se o `trecho_literal_fr` está no parágrafo indicado, se é o parágrafo inteiro e se cada `termos_fr` está no trecho; (2) busca, nos cinco arquivos, de remissões « art. N, al. X » a LCR 4/51/92, OCR 23/35/39/54-57, OETV 90, OSR 45/47/62/68/70; (3) leitura de cada regra contra o artigo inteiro; (4) cruzamento por id e por lei/artigo/alínea com priorite, depassement, arret-stationnement, comportement **e danger-securite.yaml (T-033, criado em paralelo)**; (5) leitura de T-032-notas, SPEC §5, CURRICULO (F e G).

Resultado: **22 APROVAR · 11 CORRIGIR · 4 REMOVER** (+ cabeçalho do YAML).
- 37/37 trechos são cópia literal do arquivo; todos os `termos_fr` estão no trecho. 36/37 estão no parágrafo indicado pela contagem simples; a exceção é R-ACC-025 (5.º parágrafo; a autora usou "6" por hipótese, ver §4).
- Nenhum valor inventado (1 m, 50 m, 1 a 1,5 m, três anos, CEE-ONU 150/27 estão no texto). Nenhuma regra fala de álcool, telefone, buzina, capacete ou condução ecológica.
- **Duplicatas não detectadas pelo T-032:** R-ACC-030, 031 e 032 têm a mesma lei/artigo/alínea e o mesmo trecho de R-DAN-013, R-DAN-006 e R-DAN-007 (danger-securite.yaml). O T-032-notas diz "sem colisão com os outros YAML": vale para os ids, não para o conteúdo.
- Os problemas sérios são de contexto: R-ACC-004 e 006, lidas sozinhas, ensinam que **todo** acidente exige avisar a polícia e esperar a autorização dela para sair. As duas frases estão na LCR 51 al. 2, que começa com « S'il y a des blessés »; o OCR 55 (cabeçalho « art. 51, al. 1 et 2 ») confirma que essa alínea é a dos acidentes com feridos.

## 1. Veredito por regra

Gravidade: **A** = ensina errado ou omite algo de prova; **M** = contexto ou exceção que falta, alínea errada; **B** = forma, clareza, nota.

| id | veredito | grav. | problema | correção proposta (pronta para colar) |
|---|---|---|---|---|
| R-ACC-001 | APROVAR | | | |
| R-ACC-002 | APROVAR | | | |
| R-ACC-003 | APROVAR | | Distinção envolvidos × outras pessoas mantida. | |
| R-ACC-004 | CORRIGIR | M | A `regra_pt` sozinha diz "devem avisar a polícia" sem a condição « S'il y a des blessés » que abre a al. 2. A nota avisa, mas o gerador de perguntas lê a `regra_pt`. É pergunta clássica (dano só material → não é a polícia em primeiro lugar). | `regra_pt`: "Num acidente com feridos (LCR 51 al. 2, que começa com « S'il y a des blessés »), os envolvidos, mas em primeiro lugar os condutores de veículos, devem avisar a polícia. Acidente só com danos materiais: avisar o lesado e, se for impossível, a polícia (al. 3, R-ACC-007 e 008). Ferimentos leves em que não é preciso avisar a polícia: OCR 55 al. 2 (R-ACC-017 e 018)." |
| R-ACC-005 | CORRIGIR | B | Mesmo contexto da al. 2 (feridos) omitido. | `regra_pt`: "Num acidente com feridos (LCR 51 al. 2), todas as pessoas envolvidas, passageiros incluídos, devem colaborar na reconstituição dos fatos (« reconstitution des faits »)." `excecoes`: acrescentar "Regra de outra disposição (não consta desta alínea): se um lesado chama a polícia sem que haja obrigação de avisá-la, os demais envolvidos participam da constatação até serem liberados (OCR 56 al. 3, R-ACC-022)." |
| R-ACC-006 | CORRIGIR | M | Ver §4, ponto 1. A `regra_pt` sem contexto ensina que, em qualquer acidente, só se sai com autorização da polícia; e a ordem "só podem deixar … sem autorização … se" é menos clara que o texto (« ne pourront quitter … sauf si »). | `regra_pt`: "Num acidente com feridos (LCR 51 al. 2), as pessoas envolvidas, passageiros incluídos, não podem deixar o local sem autorização da polícia, salvo se precisarem de socorro, se tiverem de buscar socorro ou de ir chamar a polícia (« quérir la police »)." `nota`: "A frase está na al. 2, que começa com « S'il y a des blessés ». O acidente só com danos materiais é regido pela al. 3 (R-ACC-007, 008), que não contém essa exigência de autorização, mas obriga a avisar o lesado ou, se impossível, a polícia. Para os ferimentos leves do OCR 55 al. 2 (R-ACC-017, 018) o texto não diz como esta frase se aplica: nenhuma pergunta deve cobrar esse caso-limite. Se um lesado chamar a polícia, os demais ficam até serem liberados (OCR 56 al. 3, R-ACC-022)." |
| R-ACC-007 | APROVAR | | | (opcional) `excecoes`: "Violar esta obrigação é punido (LCR 92 al. 1, R-ACC-010)." |
| R-ACC-008 | CORRIGIR | B | Regra fiel. Risco didático: a situação "carro estacionado danificado, dono ausente" convida a alternativa "deixar um bilhete", que o texto não menciona. | Acrescentar à `nota`: "O texto não menciona bilhete ou recado deixado no veículo. Perguntas não devem apresentá-lo como forma de cumprir a al. 3 nem como substituto do aviso à polícia." |
| R-ACC-009 | APROVAR | | Alínea confirmada (OCR 54: « art. 51, al. 1 et 4 »). | |
| R-ACC-010 | APROVAR | | | |
| R-ACC-011 | APROVAR | | | |
| R-ACC-012 | APROVAR | | Manter (§4, ponto 3). | (opcional) `excecoes`: "O OSR 104 (741.21.txt l. 1126) liga esta alínea aos acidentes: « l'obligation des usagers de la route de signaler des obstacles sur la chaussée (art. 4, al. 1, LCR; art. 23 et 54, OCR) »." |
| R-ACC-013 | CORRIGIR | B | `excecoes` cita "OCR 23 al. 4 (R-ACC-025)", mas R-ACC-025 usa `alinea: "6"`. Falta a ligação às regras de pane em autoestrada. | 2.ª exceção: "Regra de outra disposição (não consta desta alínea): sinal de pane e pisca-alertas: OCR 23 al. 1 a 3 (R-ARR-025 a 027) e última alínea do OCR 23 (R-ACC-025). Autoestradas e semiautoestradas: faixa de emergência só em necessidade absoluta e ocupantes não entram na pista (OCR 36 al. 3, R-ARR-032); sinal de pane a 100 m nas « routes à trafic rapide » e na borda direita da faixa de emergência (R-ARR-026)." |
| R-ACC-014 | APROVAR | | | |
| R-ACC-015 | APROVAR | | | |
| R-ACC-016 | APROVAR | | | |
| R-ACC-017 | APROVAR | | | (opcional) `excecoes`: "Se o ferido quiser chamar a polícia: OCR 56 al. 3 (R-ACC-022)." |
| R-ACC-018 | APROVAR | | Condições cumulativas mantidas. | |
| R-ACC-019 | APROVAR | | | |
| R-ACC-020 | APROVAR | | « il convient » mantido como "convém". | |
| R-ACC-021 | APROVAR | | | |
| R-ACC-022 | APROVAR | | | |
| R-ACC-023 | APROVAR | | Não generaliza para civis. | |
| R-ACC-024 | APROVAR | | | |
| R-ACC-025 | CORRIGIR | B | Texto certo; número não confirmável (§3, item 1). | `nota`: "NUMERAÇÃO NÃO CONFIRMADA. Última alínea do OCR 23: 5.º parágrafo do arquivo, depois da linha « et … ». As al. 1 a 3 estão confirmadas (o OCR 6 al. 5 cita « art. 23, al. 3, let. a »). Se « et … » for « 4 et 5 … », esta é a al. 6 (hipótese usada); nenhuma remissão nas fontes decide. No app, mostrar 'OCR 23 (última alínea)' até conferir no HTML do Fedlex." |
| R-ACC-026 | CORRIGIR | B | Conteúdo fiel, mas a frase em PT tem o sujeito no fim e "bem como os reboques" fica ambíguo. A numeração "2" está confirmada pela própria OETV (§3, item 2), mais forte do que a nota diz. | `regra_pt`: "Um triângulo de pane (« triangle de panne ») homologado, com marca de identificação conforme o regulamento CEE-ONU n.º 150 ou 27, deve estar a bordo dos veículos a motor com mais de um metro de largura (exceto motocicletas, motocicletas com sidecar, carrinhos de mão com motor e veículos de esteiras) e nos reboques atrelados a monoeixos." `nota`: "Numeração: al. 2 confirmada pelas remissões internas da OETV: cales = « art. 90, al. 3 » (OETV 114 al. 1, l. 1688; l. 2558) e palette = « art. 90, al. 1 » (anexo, l. 3761). O OCR 23 al. 1 cita « art. 90, al. 3, OETV » para o sinal de pane; essa remissão não bate com a OETV (R-ARR-025 repete-a)." |
| R-ACC-027 | APROVAR | | | |
| R-ACC-028 | APROVAR | | Limite "peu graves" mantido. | |
| R-ACC-029 | APROVAR | | | |
| R-ACC-030 | REMOVER | | Duplicata de R-DAN-013 (OSR 47 al. 6, mesmo trecho). R-DAN-013 já tem a remissão extra à marca 6.36. | Remover; R-ACC-029 não cita 030. |
| R-ACC-031 | REMOVER | | Duplicata de R-DAN-006 (OCR 39 al. 1). O CURRICULO.md põe o OCR 39 em G. | Remover. |
| R-ACC-032 | REMOVER | | Duplicata de R-DAN-007 (OCR 39 al. 2). | Remover. |
| R-ACC-033 | CORRIGIR | B | `excecoes` aponta para 031/032, que saem. | `excecoes`: "Regra de outra disposição (não consta desta alínea): regras de túnel do OCR 39: R-DAN-006, R-DAN-007 e R-ARR-033." |
| R-ACC-034 | CORRIGIR | B | Texto certo; "7" é só posição e a contagem por posição falha no próprio OSR (§3, item 3). | `nota`: "NUMERAÇÃO NÃO CONFIRMADA: 7.º parágrafo do OSR 62 por posição. O anexo só diz « (art. 62) ». A contagem por posição falha no OSR 68 e no OSR 70 (remissões do próprio OSR), e o parágrafo depois de uma lista a./b. pode pertencer à alínea da lista. Confirmar no HTML do Fedlex; no app, mostrar 'OSR 62'. Os valores 50 m e 1 a 1,5 m estão no texto." |
| R-ACC-035 | CORRIGIR | B | Idem 034. | `nota`: a mesma de R-ACC-034, sem a última frase, mais: "« À proximité immédiate » não é traduzido em metros." |
| R-ACC-036 | CORRIGIR | B | Idem; aqui a dúvida é concreta: se « Le cas échéant, les symboles… » continua a al. 1 (depois da lista a.-j.), o 4.80 é a al. 2, não a 3. | `nota`: "NUMERAÇÃO NÃO CONFIRMADA: 3.º parágrafo do OSR 62 por posição; pode ser al. 2 se o parágrafo « Le cas échéant… » for continuação da al. 1 (depois da lista). Confirmar no HTML do Fedlex; no app, mostrar 'OSR 62'. O texto não traz número de telefone de emergência." |
| R-ACC-037 | REMOVER | | É regra para a autoridade que instala a luz, não de conduta; não ensina o que o condutor faz. Erro de concordância ("é autorizado"). Alínea e letra estão confirmadas (OSR 68: « Le feu jaune clignotant (art. 70, al. 1) »), mas o conteúdo útil para o aluno está no OSR 68 (ver Lacuna L-02). | Remover. |

**Cabeçalho do YAML: CORRIGIR (B).** Em 15 regras (001-008, 014, 015, 017-020, 034, 035) `trecho_completo: true` com o trecho sendo só uma frase de uma alínea de várias frases; em 021, 033, 036 é `false` porque a outra frase não está em nenhuma regra. A convenção é coerente, mas não é a que o cabeçalho descreve. Trocar a definição por: "trecho_completo: true quando o trecho é a alínea inteira ou quando as demais frases da alínea estão em regras irmãs citadas em `excecoes`; false quando parte da alínea não está em nenhuma regra." E "NÃO duplicadas" deve acrescentar: "OCR 39 al. 1 e 2 (R-DAN-006, 007) e OSR 47 al. 6 (R-DAN-013)".

## 2. Lacunas (só com base nos textos disponíveis)

1. **L-01 (alta): primeiros socorros e números de emergência.** Concordo com o T-032: não estão em legal/sources (busquei 144/117/118/112; ausentes). O app não pode ensiná-los como regra legal. Se o Luan quiser, precisa de outra fonte, rotulada como conteúdo não legal.
2. **L-02 (média): OSR 68, « Le feu jaune clignotant (art. 70, al. 1) incite les conducteurs à faire preuve d'une prudence particulière »** (741.21.txt l. 664). É a regra de conduta que R-ACC-037 não dá. Categoria A. Numeração: o OSR 70 cita « art. 68, al. 6 »; por posição é o 7.º parágrafo. Usar "6" (remissão).
3. **L-03 (média): R-ARR-025** (fora deste arquivo) repete a remissão « art. 90 al. 3 OETV » do OCR 23. Merece nota igual à de R-ACC-026; sem ela, o aluno associa "OETV 90 al. 3" ao triângulo, e a OETV diz que a al. 3 são as cales.
4. **L-04 (baixa): pane em autoestrada.** O que as fontes trazem já está coberto: R-ARR-026 (100 m, borda direita da faixa de emergência), R-ARR-027 (pisca-alertas), R-ARR-032 (necessidade absoluta; ocupantes não entram na pista), R-ARR-049 (4.16), R-ACC-029 (rebocar só até a saída). Não há nas fontes regra sobre sair pelo lado direito, ficar atrás da barreira ou usar colete. Não inventar; a correção de R-ACC-013 liga F a essas regras.
5. **L-05 (baixa): reboque de veículo em pane** (OCR 72: barra 5 m, corda 8 m). Está em G (R-DAN-045, 046). R-ACC-029 poderia citá-las em `excecoes`.

## 3. Numeração (o que as fontes permitem confirmar)

1. **OCR 23, última alínea (R-ACC-025):** confirmadas só as al. 1 a 3 (OCR 6 al. 5 cita « art. 23, al. 3, let. a »). « et … » é uma linha; quantas alíneas revogadas ela representa e qual é o número da última só o HTML do Fedlex mostra. O problema « et … » é o mesmo do OCR 4 (T-020 R-DEP-021; T-024 L-04).
2. **OETV 90 (R-ACC-026): al. 2 confirmada.** A OETV cita « art. 90, al. 3 » duas vezes para as cales (l. 1688, 2558) e « art. 90, al. 1 » para a palette (l. 3761). A remissão do OCR 23 al. 1 é a discordante. O HTML do Fedlex serviria só para ver se há nota de rodapé explicando a remissão do OCR.
3. **OSR 62 (R-ACC-034 a 036): não confirmada.** Nenhuma remissão a « 62, al. » do OSR nas fontes (as de 741.41.txt l. 3695/3698 são da OETV). O anexo só diz « (art. 62) ». A contagem por posição falha perto daqui: no OSR 68 as remissões do OSR 70 (« 68, al. 3 », « al. 6 », « al. 7 », « al. 8 ») caem nos parágrafos 4, 7, 8 e 9; e o OSR 70 tem « al. 4 et 4bis ». Exige o HTML.
4. **OSR 47 al. 6 (R-ACC-030):** nenhuma remissão confirma; coerente com R-ARR-048/049 e R-DAN-013. Se R-ACC-030 sair, a dúvida fica com R-DAN-013.
5. **OSR 70 al. 1 let. f (R-ACC-037):** confirmada (OSR 68: « art. 70, al. 1 »). Irrelevante se a regra sair.
6. **LCR 51, LCR 92, LCR 4 al. 1, OCR 54-56:** confirmadas (cabeçalhos do OCR 23, 54, 55, 56). **OCR 35 al. 3, OCR 57 al. 1/3:** sem remissão, sem "…" antes; risco baixo.

## 4. Pontos de tensão

1. **R-ACC-006 × 007/008/017/018.** Leitura que as fontes sustentam: (a) a obrigação de não sair sem autorização da polícia está na al. 2 (feridos); a al. 3 (só danos materiais) tem outro dever (avisar o lesado; se impossível, a polícia) e não contém essa frase, então 006 não se aplica a 007/008; (b) para 017/018 (feridos leves, polícia dispensada) há tensão real: a al. 2 da LCR fala de « blessés » sem gradação e o OCR 55 al. 2 dispensa o aviso, mas nenhum texto diz se ainda é preciso autorização para sair. O OCR 56 al. 3 resolve só o caso em que um lesado chama a polícia. Recomendação: as correções de 004/006 e nenhuma pergunta sobre o caso (b).
2. **Duplicatas com danger-securite.yaml.** T-032 e T-033 rodaram em paralelo. Proponho remover as de F (030-032) porque o CURRICULO.md põe o OCR 39 em G e as R-DAN já estão escritas. A alternativa (remover as R-DAN) também é válida; o que não pode é manter as duas.
3. **R-ACC-012: manter.** É o dever geral de sinalizar obstáculos, e o OSR 104 o liga expressamente aos OCR 23 e 54. Útil para "carga caída na pista". **R-ACC-037: remover** (regra para a autoridade; substituir pela L-02).

## 5. Pontos que exigem decisão do Luan

1. Duplicatas: remover R-ACC-030/031/032 (recomendado) ou as R-DAN-013/006/007.
2. R-ACC-037: remover (recomendado) e abrir a L-02 (OSR 68, feu jaune clignotant) em A.
3. R-ACC-012: manter (recomendado) ou remover.
4. Caso-limite 006 × 017/018: aceitar que fique sem pergunta até haver fonte.
5. Numeração: conferir no HTML do Fedlex OCR 23 (última alínea) e OSR 62 (4.80, 4.94, 4.95) antes de `validado`, ou aceitar que o app mostre só "OCR 23 (última alínea)" / "OSR 62".
6. R-ARR-025: acrescentar nota sobre a remissão OETV 90 al. 3 (L-03).
7. Primeiros socorros e números 144/117/118/112: fora do app ou com fonte não legal rotulada (L-01).

## 6. Resumo

| | quantidade |
|---|---|
| Regras revisadas | 37 |
| APROVAR | 22 (4 com ajuste opcional: 007, 012, 017; e 029 via L-05) |
| CORRIGIR | 11 (A: 0 · M: 2 · B: 9) + cabeçalho do YAML (B) |
| REMOVER | 4 (030, 031, 032 duplicatas; 037) |
| Trechos literais exatos | 37/37 |
| Alíneas erradas | 0 confirmadas; não confirmáveis pelas fontes: OCR 23 última, OSR 62 (3 regras), OSR 47 al. 6. OETV 90 al. 2 confirmada |
| Duplicatas com outros YAML | 3 (R-DAN-013, 006, 007) |
| Lacunas | 5 (alta: 1 · média: 2 · baixa: 2) |
| Pontos para decisão do Luan | 7 |

CORRIGIR por gravidade:
- M: 004, 006
- B: 005, 008, 013, 025, 026, 033, 034, 035, 036 (+ cabeçalho)
