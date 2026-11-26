# T-029 REV — Revisão independente de questions/arret-stationnement.json, depassement.json e comportement.json (72 perguntas)

Revisor: agente REV (não escreveu as perguntas). Data: 2026-11-26.
Fontes usadas: só legal/sources/741.01.txt (LCR), 741.11.txt (OCR), 741.21.txt (OSR), 741.51.txt (OAC) e legal/rules/{arret-stationnement,depassement,comportement,priorite}.yaml. Sem web.
Método: cada pergunta foi resolvida a partir do texto oficial (artigos extraídos do .txt) antes de olhar o gabarito. Depois foram conferidos: gabarito de cada alternativa, artigo/alínea da justificativa, enunciado, vazamento, distratores, francês/português, segurança, regra_ids, dependência de números ausentes e de interpretação. Formato e critérios: T-017.

**Resultado geral: nenhum gabarito está errado segundo o texto oficial.** Nenhuma pergunta toca álcool, telefone, buzina, capacete ou condução ecológica (0 REMOVER). Os problemas são: uma alternativa correta com sentido trocado (Q-DEP-004 D), duas alternativas corretas que só valem com um dado que o enunciado não fixa (Q-DEP-009 C, lado da faixa; Q-COM-007 D, tipo de estrada de entrada), um enunciado que contradiz duas alternativas (Q-DEP-018), seis pares "espelho" (uma alternativa é a negação literal de outra), duas perguntas com só 3 alternativas e viés de comprimento.

Convenção: "texto exato" substitui o campo inteiro indicado. Justificativas não citadas ficam iguais.

## 1. Tabela por pergunta

### 1.1 questions/arret-stationnement.json

| id | veredito | problema | correção (texto exato) |
|---|---|---|---|
| Q-ARR-001 | APROVAR | Gabarito certo (OCR 19 al. 1). Distratores A e C bons. | — |
| Q-ARR-002 | APROVAR | Gabarito certo (OCR 18 al. 2 let. a, e, f, g). Cosmético: "Também é sempre proibido" soa estranho. | (opcional) D: "É proibido parar voluntariamente diante de um sinal que o veículo poderia encobrir." |
| Q-ARR-003 | CORRIGIR (só justificativa) | Gabarito certo (LCR 37 al. 1-2). Justificativa A diz que o pisca-alerta parado "só é permitido como complemento do sinal de pane": o OCR 23 al. 3 let. a também prevê o ônibus escolar sinalizado. Frase absoluta mais estreita que a lei. | Justificativa A: "Errada. LCR art. 37 al. 2 não prevê exceção por duração: não se para onde se possa atrapalhar ou pôr em perigo a circulação. Num veículo parado, o pisca-alerta só serve como complemento do sinal de pane ou, em ônibus escolar sinalizado, para embarque e desembarque de alunos (OCR art. 23 al. 3 let. a); ele não autoriza a parada." |
| Q-ARR-004 | APROVAR | Gabarito certo (OCR 18 al. 1, « n'est autorisé que »). Lista fechada bem explorada. | — |
| Q-ARR-005 | APROVAR | Gabarito certo (OCR 18 al. 3). Única correta (D) é a mais longa: ver §3. | — |
| Q-ARR-006 | APROVAR | Gabarito certo (OCR 18 al. 4; 21 al. 2-3). Alt. D muda o cenário do enunciado (rua com carros estacionados → estrada de montanha), mas é inequívoca. | (opcional) Enunciado: "Um entregador precisa carregar e descarregar mercadorias na via, em lugares diferentes. Quais afirmações estão corretas?" |
| Q-ARR-007 | CORRIGIR | B, C, D certas (OCR 19 al. 2 let. c, d, g). Alt. A (correta) "é **sempre** proibido": a let. f não tem condição, mas o texto não diz se sinais ou marcas locais podem autorizar; "sempre" depende de interpretação e não é necessário. | Alt. A: "Estacionar sobre uma ponte é proibido." |
| Q-ARR-008 | APROVAR | Gabarito certo (OCR 18 al. 2 let. d; 19 al. 2 let. a, e, f). Números (5 m, 20 m) estão no texto. | — |
| Q-ARR-009 | CORRIGIR (justificativa + regra_ids) | **Atenção especial.** Gabarito certo: OSR 30 al. 1 — 2.49 proíbe o « arrêt volontaire », 2.50 o « parcage », e a própria al. 1 (2ª frase) define parcage como permanência que não serve só a passageiros ou carga. B e D certas, A e C erradas, sem interpretação. Problema: justificativa A tem raciocínio torto ("como estacionar é a permanência que não serve só a carga..., com o 2.49 nenhuma parada voluntária é permitida"). B usa a definição de parcage: falta R-ARR-009. | Justificativa A: "Errada. OSR art. 30 al. 1: o 2.49 proíbe a parada voluntária (« arrêt volontaire »). Parar para carregar mercadorias é parada voluntária. A exceção de carga e descarga só existe no conceito de « parcage », que é o que o 2.50 proíbe." regra_ids += "R-ARR-009". |
| Q-ARR-010 | APROVAR | Gabarito certo (OSR 30 al. 3; 64 al. 3). | (opcional) regra_ids += "R-ARR-084" (5.07, OSR 64 al. 4) |
| Q-ARR-011 | APROVAR | Gabarito certo (OSR 30 al. 4; 64 al. 5 let. a-b). Única correta (C) é a mais longa: ver §3. | — |
| Q-ARR-012 | CORRIGIR | Gabarito certo (OSR 31 al. 1-2). B é a negação literal de D (par espelho): quem não sabe nada acerta que exatamente uma das duas vale. | Alt. B: "O sinal «Police» (2.52) pode ser colocado por qualquer pessoa que precise controlar o trânsito." Justificativa B: "Errada. OSR art. 31 al. 2: o sinal é colocado pela polícia." |
| Q-ARR-013 | APROVAR | Gabarito certo (OSR 2a al. 2, 3, 5). Única correta (B) é a mais longa: ver §3. | — |
| Q-ARR-014 | APROVAR | Gabarito certo (OSR 48 al. 1-4). | — |
| Q-ARR-015 | APROVAR | Gabarito certo (OCR 25 al. 5; 21 al. 1). | — |
| Q-ARR-016 | APROVAR | Gabarito certo (OSR 65 al. 5). O cartão atrás do para-brisa também está no OCR 20a al. 4. | (opcional) regra_ids += "R-ARR-017" |
| Q-ARR-017 | CORRIGIR | **Atenção especial (cor sem imagem).** As cores estão descritas no texto (OSR 79 al. 2: « Les marques sont blanches »; al. 5: « marquées en jaune »), então a pergunta não depende de imagem. Problemas: (1) alt. C (correta) acrescenta "sempre", que o al. 5 não diz; a restrição a grupos também pode vir só no sinal ou placa (OSR 48 al. 4; 65 al. 5). (2) "pátio" pode ser área privada, fora da via pública. | Enunciado: "Um motorista estaciona num estacionamento público com vagas marcadas no chão. Quais afirmações estão corretas?" Alt. C: "As vagas reservadas a certos grupos de usuários são marcadas em amarelo." |
| Q-ARR-018 | CORRIGIR | Gabarito certo (OSR 77 al. 2). (1) Alt. B "é traçada na borda direita" não é falsa: em sentido único ela é traçada na direita **e** na esquerda. (2) O enunciado chama a linha de "linha que proíbe parar", o que entrega a alt. A. | Enunciado: "Antes de uma faixa de pedestres há uma linha amarela contínua (6.18), paralela à borda da pista. Quais afirmações estão corretas?" Alt. B: "Em vias de sentido único, ela é traçada só na borda direita da pista." |
| Q-ARR-019 | CORRIGIR | **Atenção especial (forma sem imagem).** Zigue-zague e "duas diagonais que se cruzam" são descrições do próprio OSR 79a al. 1 e 3: não dependem de imagem (um SVG ajudaria, mas não bloqueia). Gabarito certo. Problema: A é a negação literal de B (par espelho). | Alt. A: "Na vaga 6.23 sem nenhuma inscrição, estacionar é permitido se for por pouco tempo." Justificativa A: "Errada. OSR art. 79a al. 1: a vaga 6.23 proíbe estacionar no local marcado; a duração não muda isso, porque estacionar se define pela finalidade (OCR art. 19 al. 1)." |
| Q-ARR-020 | APROVAR | Gabarito certo (OCR 41 al. 1-3). | — |
| Q-ARR-021 | APROVAR | Gabarito certo (OCR 19 al. 3-4). | — |
| Q-ARR-022 | APROVAR | Gabarito certo (OCR 22 al. 1-3; « notamment » respeitado). Cosmético: D diz "o condutor" num enunciado com "a condutora". | (opcional) D: "Ao partir, ela deve tirar da pista os objetos que usou como calços." |
| Q-ARR-023 | APROVAR | Gabarito certo (OCR 23 al. 1-2). Não cobra as distâncias (50/100 m), coerente com a falta de definição de « routes à trafic rapide ». | — |
| Q-ARR-024 | CORRIGIR | Gabarito certo (OCR 36 al. 3; 39 al. 3; OSR 47 al. 5). Alt. A ("pode estacionar por um tempo se o problema for demorado") é discutível: com pane demorada o carro fica ali sem ser parada voluntária. Ortografia: "pára" (pré-Acordo). | Alt. A: "Num local sinalizado 4.16, o condutor pode deixar o carro estacionado para descansar, mesmo sem pane." Justificativa A: "Errada. OSR art. 47 al. 5: no 4.16 a parada voluntária e o estacionamento são proibidos; o local serve às paradas impostas pelas circunstâncias (OCR art. 36 al. 3)." Alt. D: "Em túnel, só se para em caso de necessidade, e o motor deve ser desligado imediatamente." |

### 1.2 questions/depassement.json

| id | veredito | problema | correção (texto exato) |
|---|---|---|---|
| Q-DEP-001 | APROVAR | Gabarito certo (LCR 35 al. 1). Enunciado exclui bonde, ilhas e mão única. | — |
| Q-DEP-002 | APROVAR | Gabarito certo (LCR 35 al. 2). Única correta (C) é a mais longa: ver §3. | — |
| Q-DEP-003 | APROVAR | Gabarito certo (LCR 35 al. 2, 2ª frase; OCR 10 al. 2). | — |
| Q-DEP-004 | CORRIGIR | A, B, C erradas, certo. Alt. D (correta) diz "consideração especial... em especial **por quem quer ultrapassar**". A LCR 35 al. 3 diz « notamment à ceux qu'il veut dépasser » = aqueles que **ele** quer ultrapassar. Em português a frase passa a falar de quem quer ultrapassar você: sentido trocado. Também é a única correta e a mais longa. | Alt. D: "Você anuncia a ultrapassagem a tempo e tem consideração especial pelo caminhão que vai ultrapassar." |
| Q-DEP-005 | CORRIGIR | **Atenção especial.** Gabarito certo e literal (LCR 35 al. 5, 2ª parte; « afin de permettre à ceux-ci de traverser »): a proibição depende da finalidade da parada, não de haver alguém na faixa. Problemas: (1) a única correta (B) repete o enunciado e é a mais longa: o aluno acerta por eco; (2) "pára" (pré-Acordo); (3) "passagem de pedestres" aqui e "faixa de pedestres" no resto do projeto; (4) a justificativa D cita OCR 10 al. 1 (pedestres atravessando), que não se aplica ao caso de D (faixa vazia). | Enunciado: "Na sua frente, um carro para diante de uma faixa de pedestres para deixar uma pessoa atravessar a via. Há espaço livre à esquerda e boa visibilidade. Quais afirmações estão corretas?" Alt. B: "Você deve ficar atrás do carro parado, mesmo com espaço livre à esquerda e boa visibilidade." Justificativa B: "Correta. LCR art. 35 al. 5, segunda parte: é proibido ultrapassar o veículo que parou diante da faixa de pedestres para permitir a travessia." Justificativa D: "Errada. LCR art. 35 al. 5 proíbe ultrapassar o veículo que parou para permitir a travessia; a regra não depende de já haver alguém na faixa." Em todos os campos: "pára" → "para"; "passagem de pedestres" → "faixa de pedestres". |
| Q-DEP-006 | APROVAR | Gabarito certo (LCR 35 al. 4, 1ª parte). Enunciado exclui linha de segurança (OCR 11 al. 3). | — |
| Q-DEP-007 | CORRIGIR | **Atenção especial (OCR 11 al. 4 × LCR 35 al. 4).** No cenário, as duas normas proíbem a ultrapassagem (LCR: falta boa visibilidade; OCR: sem via prioritária, polícia ou semáforo). Por isso o gabarito vale qualquer que seja a relação entre elas. Problemas: (1) "via sem sinal de prioridade a seu favor" não fecha o termo « route prioritaire » do OCR 11 al. 4; (2) alt. B ("sinalizou que vai seguir em frente") descreve um sinal que não existe; (3) a `excecao` afirma o que valeria **com** via prioritária ("deixaria de se aplicar, mas o LCR continuaria exigindo..."). Isso resolve por interpretação a tensão entre as duas normas, e a pergunta não precisa disso. | Enunciado: "Você segue atrás de um carro lento e se aproxima de uma interseção em que não vê o suficiente das desembocaduras das outras vias. Sua via não é principal: nenhum sinal lhe dá prioridade. Não há semáforo nem policial regulando a circulação. Quais afirmações estão corretas?" Alt. B: "Se o carro da frente estiver muito lento, a ultrapassagem nessa interseção passa a ser permitida." Justificativa B: "Errada. A velocidade do veículo da frente não está entre as condições do OCR art. 11 al. 4 nem do LCR art. 35 al. 4." `excecao`: "O enunciado exclui via prioritária, polícia e semáforo. Esta pergunta não trata do caso em que uma dessas condições existe. Nas interseções, o LCR art. 35 al. 4 exige boa visibilidade e nenhuma ofensa ao direito de prioridade dos outros." |
| Q-DEP-008 | APROVAR | Gabarito certo (LCR 36 al. 1; OCR 13 al. 1-2). Bom: corretas curtas, distrator longo. | — |
| Q-DEP-009 | CORRIGIR | **Atenção especial ("destinos indicados").** OCR 13 al. 3: a exceção exige que os destinos indicados nas duas faixas « soient les mêmes ». Alt. C (correta) diz "faixa vizinha que **também** indica a cidade A": uma faixa "A e B" também indica A, mas o destino não é o mesmo. Além disso, C não diz o lado. Se a faixa vizinha estiver à direita, passar por ela é ultrapassar pela direita (LCR 35 al. 1; OCR 8 al. 3, 2ª frase). Fora de autoestrada isso é proibido. Com o enunciado atual, C pode ser falsa. | Enunciado: "Você está numa faixa de um trecho de présélection, fora de autoestrada, cuja indicação de destino é só a cidade A. Um veículo lento circula à sua frente nessa faixa. Quais afirmações estão corretas?" Alt. C: "Se a faixa vizinha da esquerda indica só a cidade A, você pode passar para ela e ultrapassar, sem perigo." Justificativa C: "Correta. OCR art. 13 al. 3: a proibição não vale se os destinos indicados nas faixas do ultrapassado e de quem ultrapassa são os mesmos. A mudança continua sujeita a não criar perigo (LCR art. 44 al. 1), e a ultrapassagem se faz pela esquerda (LCR art. 35 al. 1)." |
| Q-DEP-010 | APROVAR | Gabarito certo (LCR 38 al. 3; OCR 25 al. 3). | — |
| Q-DEP-011 | APROVAR | Gabarito certo (LCR 38 al. 4; OCR 25 al. 2). Alt. B muda o cenário (bonde no mesmo sentido), mas é inequívoca. | — |
| Q-DEP-012 | APROVAR | Gabarito certo (LCR 34 al. 2, « toujours »; OSR 73 al. 1, al. 7 let. a). | — |
| Q-DEP-013 | APROVAR | Gabarito certo (LCR 34 al. 4; OCR 12 al. 1-3). | — |
| Q-DEP-014 | CORRIGIR (justificativa + regra_ids) | Gabarito certo. A justificativa D cita "OSR art. 26 al. 4 (remissão ao OSR art. 16 al. 2)", mas o 26 al. 4 não cita o 2.58 nem remete ao 16. A base real é OSR 16 al. 2 (lista 2.53-2.58) + OSR 32 al. 2. A alt. A também depende do OSR 16 al. 2, e falta R-ARR-039. | Justificativa D: "Correta. OSR art. 16 al. 2: o 2.58 está na lista de sinais de fim que encerram o 2.44. OSR art. 32 al. 2: o 2.58 indica que várias restrições impostas aos veículos em movimento terminam." regra_ids += "R-ARR-039". |
| Q-DEP-015 | APROVAR | Gabarito certo (OSR 26 al. 2-4). Alt. C (165 car.) é a mais longa: ver §3. | — |
| Q-DEP-016 | APROVAR | Gabarito certo (OCR 10 al. 3; LCR 35 al. 7). | — |
| Q-DEP-017 | CORRIGIR | Gabarito certo (LCR 45 al. 1). B é a negação literal de D (par espelho). | Alt. B: "Se é impossível cruzar, quem deve recuar é sempre o veículo que sobe." Justificativa B: "Errada. LCR art. 45 al. 1: se é impossível cruzar, recua o veículo que desce, salvo se o outro está manifestamente mais perto de um local de desvio." |
| Q-DEP-018 | CORRIGIR (enunciado) | Gabarito certo (OCR 40 al. 3; OSR 74a al. 1). O enunciado fixa "uma faixa delimitada por uma linha amarela (6.09)", e as alternativas A e D tratam de linha contínua: o aluno não sabe qual linha existe. O número 6.09 vale para as duas (OSR 74a al. 1, « discontinue ou continue (6.09) »). | Enunciado: "Uma estrada tem faixas cicláveis delimitadas por linha amarela (6.09): em alguns trechos a linha é contínua, em outros é descontínua. Quais afirmações estão corretas?" |
| Q-DEP-019 | APROVAR | Gabarito certo (OCR 7). Distrator D (estender a exceção) é ótimo. | — |
| Q-DEP-020 | APROVAR | Gabarito certo (OSR 24 al. 1 let. a-c). | — |
| Q-DEP-021 | APROVAR | Gabarito certo (OCR 36 al. 6-7). Alt. A com 218 car.: ver §3. | — |
| Q-DEP-022 | APROVAR | Gabarito certo (OSR 74 al. 3-4). Cores e números das flechas estão no texto. | — |
| Q-DEP-023 | CORRIGIR | Gabarito certo (OCR 28 al. 1-3). B é a negação literal de A (par espelho). | Alt. B: "Basta ligar o pisca no momento em que você começa a virar." Justificativa B: "Errada. LCR art. 39 al. 1: a intenção deve ser manifestada a tempo, antes de mudar de direção." regra_ids += "R-DEP-016". |
| Q-DEP-024 | APROVAR | Gabarito certo (OCR 8 al. 1; LCR 44 al. 1). "Fora de localidade" fecha a exceção do OCR 8 al. 1. | — |

### 1.3 questions/comportement.json

| id | veredito | problema | correção (texto exato) |
|---|---|---|---|
| Q-COM-001 | APROVAR | Gabarito certo (LCR 26 al. 1). A correta fala de "quem usa a via de acordo com as regras": não repete o erro do Q-PRIO-020. | — |
| Q-COM-002 | APROVAR | Gabarito certo (LCR 26 al. 2). | — |
| Q-COM-003 | APROVAR | Gabarito certo (LCR 31 al. 1 e al. 3; numeração "al. 3" certa por causa de 2bis/2ter). Não usa a al. 2 (álcool): dentro do escopo. | — |
| Q-COM-004 | CORRIGIR (só explicação) | **Atenção especial.** Gabarito certo (OCR 17 al. 4; OCR 3 al. 3). Única correta é a mais curta: bom. A justificativa D está certa: a exceção do auxílio ao estacionamento é só « durant le parcage » (OCR 3 al. 4). A `excecao` diz "durante a manobra", e numa pergunta sobre meia-volta isso sugere que a exceção valeria para a meia-volta. Não toca telefone (OCR 3 al. 1 não é usado). | `excecao`: "Com sistema de auxílio ao estacionamento, o condutor pode soltar o volante durante o estacionamento (« parcage »), não em outras manobras (OCR art. 3 al. 4; R-ARR-083). Este enunciado exclui esse sistema." |
| Q-COM-005 | APROVAR | Gabarito certo (LCR 32 al. 1). | — |
| Q-COM-006 | APROVAR | Gabarito certo (OCR 4a al. 1). | — |
| Q-COM-007 | CORRIGIR | Gabarito certo (OCR 4a al. 2, 3ª frase; OSR 22 al. 4). Alt. D (correta), lida sozinha, generaliza: "também vale sem sinalização, assim que exista zona compacta" vale só para quem entra por estrada secundária pouco importante, e C acabou de negar o "seja qual for a estrada". A `excecao` manda "usar o bom senso" (interpretação). | Alt. D: "Entrando por essa estrada agrícola, o limite de 50 km/h vale mesmo sem sinal, porque já existe zona construída de forma compacta." `excecao`: "O texto não define critério numérico para « zone bâtie de façon compacte ». Nesta pergunta, o enunciado já diz que ela existe." |
| Q-COM-008 | APROVAR | Gabarito certo (OCR 4a al. 3-5). | — |
| Q-COM-009 | CORRIGIR | Gabarito certo (OCR 4a al. 6; OCR 5 al. 4; OSR 22 al. 1). B é a negação literal de D (par espelho). | Alt. B: "A obrigação desse sinal só é suprimida pelo sinal 2.53.1 «Fin de la vitesse maximale 50, Limite générale»." Justificativa B: "Errada. OSR art. 22 al. 1: a obrigação do 2.30 é suprimida pelo sinal 2.53 « Fin de la vitesse maximale »; o 2.53.1 encerra o limite geral de 50 km/h." |
| Q-COM-010 | CORRIGIR | Gabarito certo (OCR 5 al. 2 let. c). (1) Só 3 alternativas: é a única forma do arquivo fora do padrão de 4, junto com Q-COM-022. (2) "automóvel ligeiro com reboque, cujo peso total é de 3,0 t" deixa ambíguo de quem é o peso (o gabarito não muda, mas a lei fala do peso do reboque). (3) "ligeiro" é PT-PT. | Enunciado: "Você conduz um automóvel leve com um reboque cujo peso total é de 3,0 t, numa autoestrada, com boas condições e sem sinais de velocidade. Quais afirmações estão corretas?" Nova alt. D: `{"texto": "Se um sinal indicar 120 km/h, você pode rodar a 120 km/h com esse reboque.", "correta": false, "justificativa": "Errada. OCR art. 5 al. 4: os limites do art. 5 também devem ser respeitados onde sinais indicam um limite superior."}` regra_ids += "R-COM-029". |
| Q-COM-011 | CORRIGIR | Gabarito certo (OSR 22 al. 1). Alt. C diz que "um pequeno excesso... é aceito... **pelos controles**": isso remete a tolerâncias de medição, que estão fora das fontes e podem ser verdadeiras na prática. O distrator não fica inequivocamente errado pelas fontes. | Alt. C: "Com condições tão boas, o valor do sinal funciona como recomendação e pode ser um pouco excedido." |
| Q-COM-012 | APROVAR | Gabarito certo (OSR 16 al. 2). Cosmético: a justificativa D diz "lista de sinais de fim do 2.30 e do 2.31", mas a lista é comum aos seis sinais. | (opcional) Justificativa D: "Correta. OSR art. 16 al. 2: o 2.58 está na lista de sinais de fim que encerram o 2.30; OSR art. 32 al. 2: o 2.58 indica o fim de várias restrições impostas aos veículos em movimento." |
| Q-COM-013 | CORRIGIR | Gabarito certo (OSR 22a; 22b al. 2). B, C e D testam o mesmo fato (20 × 30 km/h). B e C formam par espelho. | Alt. B: `{"texto": "Na zona de encontro, os pedestres podem usar toda a área de circulação e têm prioridade.", "correta": true, "justificativa": "Correta. OSR art. 22b al. 1."}` regra_ids += "R-PRIO-054". |
| Q-COM-014 | APROVAR | Gabarito certo (OSR 23 al. 1; 16 al. 2). "não é possível nem permitido" é tradução literal de « pas possible ni permis ». | — |
| Q-COM-015 | APROVAR | Gabarito certo (OCR 3a al. 1 e 3). Cinto não está no escopo excluído (capacete está; aqui não há capacete). | — |
| Q-COM-016 | CORRIGIR | Gabarito certo (OCR 3a al. 2). A alt. A se contradiz: a 1ª metade é verdadeira (atestado médico) e a 2ª falsa. O aluno fica sem saber o que está sendo avaliado. | Alt. A: "Quem declara por conta própria que o cinto lhe faz mal à saúde está dispensado, mesmo sem atestado médico." |
| Q-COM-017 | APROVAR | **Atenção especial.** Gabarito certo e literal (OCR 3a al. 4 let. a-d; al. 1). Idade, altura e tipo de assento estão todos fechados no enunciado: 6 anos/125 cm não cabe em nenhuma letra (b e c excluídas, d exige 7 anos); 11 anos/155 cm cabe na let. a. D separa bem "dispensa do dispositivo" de "dispensa de ir preso". Os números (150 cm, 4, 7, 12 anos) estão no texto. | — |
| Q-COM-018 | APROVAR | Gabarito certo (LCR 41 al. 1; OCR 30 al. 1). | — |
| Q-COM-019 | APROVAR | Gabarito certo (OCR 30 al. 2 let. a-c). | — |
| Q-COM-020 | APROVAR | Gabarito certo (OCR 30 al. 3-4; LCR 41). | — |
| Q-COM-021 | APROVAR | Gabarito certo (OCR 33 al. 1 let. f, g; LCR 42 al. 1). Escopo: não toca buzina (as letras usadas são portas e carga). "Ruído, poeira, fumaça ou odores" é regra de incomodidade, não de condução ecológica. Fica para decisão do Luan se quiser excluir também esse tema. | — |
| Q-COM-022 | CORRIGIR | Gabarito certo (LCR 10 al. 1, 4; OAC 71 al. 5). Só 3 alternativas. `palavras_fr` usa "carta de condução" (PT-PT). | Nova alt. D: `{"texto": "Quando os órgãos de controle pedirem, você deve apresentar os seus permis.", "correta": true, "justificativa": "Correta. LCR art. 10 al. 4: os condutores devem sempre portar os seus permis e apresentá-los, quando solicitado, aos órgãos de controle."}` `palavras_fr`: "permis de conduire — carteira de motorista". |
| Q-COM-023 | APROVAR | Gabarito certo (LCR 10 al. 2; 11 al. 3). | — |
| Q-COM-024 | CORRIGIR (terminologia) | **Atenção especial.** Gabarito certo (OCR 27 al. 1, 2, 4, 5). Exceção da cat. C excluída no enunciado. Não toca álcool (LCR 31 al. 2bis let. d-e não é usado). Problema: « chaussées fortement fréquentées » virou "vias de tráfego intenso", o mesmo nome dado a « trafic intense » no Q-COM-004 (OCR 17 al. 4). São termos legais diferentes com o mesmo nome em português (mesmo risco do Q-PRIO-032). A al. 5 não nomeia o sujeito; atribuir a proibição ao aluno é leitura do contexto do art. 27, e a nova redação fica mais literal. | Alt. D: "Num trajeto de aprendizagem, nas vias muito movimentadas, é proibido arrancar em subida, fazer meia-volta na pista e fazer marcha à ré." Justificativa D: "Correta. OCR art. 27: nas « chaussées fortement fréquentées » (vias muito movimentadas), é proibido, nos trajetos de aprendizagem, arrancar em subida, fazer meia-volta na pista, fazer marcha à ré e exercícios semelhantes." `palavras_fr`: "chaussées fortement fréquentées — vias muito movimentadas (não confundir com « trafic intense », OCR art. 17 al. 4)". |

## 2. Contagens

| arquivo | APROVAR | CORRIGIR | REMOVER |
|---|---|---|---|
| arret-stationnement.json | 16 | 8 (003, 007, 009, 012, 017, 018, 019, 024) | 0 |
| depassement.json | 16 | 8 (004, 005, 007, 009, 014, 017, 018, 023) | 0 |
| comportement.json | 15 | 9 (004, 007, 009, 010, 011, 013, 016, 022, 024) | 0 |
| **total (72)** | **47** | **25** | **0** |

Das 25 CORRIGIR, só mexem em alternativa **correta**: Q-ARR-007, Q-ARR-017, Q-DEP-004, Q-DEP-005, Q-DEP-009, Q-COM-007 e Q-COM-024 (redação). Só explicação/justificativa: Q-ARR-003, Q-ARR-009, Q-DEP-014, Q-COM-004. O resto mexe em distrator, enunciado ou número de alternativas.

## 3. Viés de forma: reescritas para equilibrar

Medido no arquivo atual: a alternativa mais longa é correta em **16/24 (ARR)**, **13/24 (DEP)** e 6/24 (COM). As de correta única e mais longa: ARR-005, 008, 011, 013; DEP-002, 004, 005. Com as correções da §1 **e** as reescritas abaixo (simulado com script), o número cai para **11/24 (ARR), 8/24 (DEP), 8/24 (COM)**, e nenhuma pergunta de correta única fica com a correta mais longa.

Reescritas só de forma. O sentido jurídico não muda e as justificativas continuam valendo:

| id | alt. | texto novo |
|---|---|---|
| Q-ARR-005 | D (V) | "A menos de 10 m da placa de parada, só se para para embarque ou desembarque de passageiros." |
| Q-ARR-005 | B (F) | "Diante das instalações do serviço de bombeiros, é proibido parar, mesmo que seja só para um passageiro descer do carro." |
| Q-ARR-008 | C (V) | "Estacionar a 3 m da pista transversal de uma interseção é proibido." |
| Q-ARR-011 | C (V) | "Com «Excepté» ou «Autorisé» junto a um símbolo, o sinal não vale para esse tipo de transporte." |
| Q-ARR-013 | B (V) | "O sinal de zona vale até o sinal de fim de zona, que restabelece as regras gerais." |
| Q-ARR-014 | D (V) | "Com tempo limitado, deve-se sair até o fim do tempo autorizado, salvo se o parquímetro permitir pagar de novo antes." |
| Q-ARR-015 | C (V) | "Antes de abrir a porta, quem desce deve olhar com atenção os veículos que vêm por trás." |
| Q-ARR-020 | C (V) | "Sem sinal ou marca, outros veículos só param na calçada para carga, descarga ou passageiros." |
| Q-ARR-022 | C (V) | "Num declive, além do freio, ela toma uma segunda medida, como engatar uma marcha inferior." |
| Q-DEP-002 | C (V) | "Só se ultrapassa com espaço livre e bem visível e sem incomodar quem vem de frente." |
| Q-DEP-010 | D (V) | "Sem refúgio, se os passageiros descem do lado da circulação, você para até eles saírem da pista." |
| Q-DEP-015 | C (V) | "Mesmo com o 2.45, o caminhão pode ultrapassar um automotor agrícola limitado a 30 km/h, se não houver perigo." |
| Q-DEP-021 | A (V) | "Com o trânsito a passo ou parado, deixa-se um corredor livre entre a faixa mais à esquerda e a vizinha." |
| Q-DEP-023 | C (V) | "Sem pisca, ou com o pisca invisível, o condutor ou um passageiro estende o braço para o lado em que vai." |

Regra para as próximas levas: escrever primeiro a correta com o mínimo de palavras e depois dar aos distratores **a mesma estrutura e o mesmo comprimento** (±15 car.). Não pôr o porquê ("porque...", "pois...") só nos distratores: hoje 20 distratores e só 4 corretas dos três arquivos trazem "porque/pois" no texto, o que também é um padrão reconhecível.

## 4. Pontos com atenção especial (resumo)

- **Q-ARR-009 (2.49 × 2.50):** gabarito literal. A definição de parcage está no próprio OSR 30 al. 1 (2ª frase), não só no OCR 19 al. 1. Corrigir só a justificativa A e o regra_ids.
- **Q-ARR-017/019 (cor/forma sem imagem):** as cores e formas são descritas em palavras no OSR 79 e 79a; nenhuma alternativa exige reconhecer desenho. Corrigir "sempre" (017) e o par espelho (019). Um SVG ajudaria, mas não bloqueia.
- **Q-DEP-005:** literal (finalidade da parada, não presença do pedestre). Corrigir forma (eco do enunciado), ortografia e termo.
- **Q-DEP-007 (OCR 11 al. 4 × LCR 35 al. 4):** no cenário, as duas normas levam ao mesmo resultado, então o gabarito não depende de hierarquia entre elas. A `excecao` atual resolve a tensão por interpretação (o caso **com** via prioritária): tirar.
- **Q-DEP-009 ("destinos indicados"):** "também indica" ≠ « soient les mêmes ». Falta o lado da faixa (ultrapassar pela direita seria proibido). É o único caso em que uma alternativa marcada correta pode ser falsa com o enunciado atual.
- **Q-COM-004:** gabarito certo; só a `excecao` amplia a exceção do auxílio ao estacionamento.
- **Q-COM-017:** a mais bem fechada do lote. APROVAR.
- **Q-COM-024:** certo; colisão de tradução "tráfego intenso" com o Q-COM-004.
- **Escopo do Luan:** nenhuma das 72 toca álcool, telefone, buzina, capacete ou condução ecológica. Únicos pontos vizinhos: Q-COM-003 e Q-COM-024, cujos artigos têm alíneas de álcool que não são usadas, e Q-COM-021 (incomodidades), mantida.

## 5. Problemas recorrentes

1. **Viés de comprimento** (§3): 16/24 ARR, 13/24 DEP. Correção proposta → 11, 8, 8.
2. **Pares espelho** (uma alternativa é a negação literal de outra, o que entrega que exatamente uma das duas é certa): Q-ARR-012, Q-ARR-019, Q-DEP-017, Q-DEP-023, Q-COM-009, Q-COM-013. Nas próximas levas, cada distrator deve errar num ponto **diferente** da correta.
3. **Absolutos em corretas além do texto:** "sempre" em Q-ARR-007 A e Q-ARR-017 C. (Absolutos literais, como « toujours » em Q-DEP-012 B e Q-COM-017 B, estão certos e devem ficar.) Nos distratores: 10/49 ARR, 14/48 DEP, 11/46 COM ainda usam só/sempre/basta/nunca/qualquer.
4. **Enunciado que não fecha a variável decisiva:** Q-DEP-009 (lado e destino idêntico), Q-DEP-018 (tipo de linha), Q-DEP-007 (via prioritária), Q-COM-010 (peso de quê), Q-ARR-018 (nome da linha entrega a resposta).
5. **Justificativa com artigo ou raciocínio errado:** Q-ARR-003 A, Q-ARR-009 A, Q-DEP-014 D (cita 26 al. 4 para o 2.58).
6. **Terminologia inconsistente entre arquivos** (fixar no GLOSSARIO.md): tramway = "tramway" (ARR, 13×) / "bonde" (DEP, 28×) / "tram" (PRIO, glossário). Faixa de pedestres = "faixa de pedestres" (maioria) / "passagem de pedestres" (DEP, 8×) / "passagens para pedestres" (COM-002). « trafic intense » e « chaussées fortement fréquentées » têm o mesmo PT. PT-PT misturado ao PT-BR: "ligeiro" (COM, 7×), "carta de condução", "camiões" (DEP-015 `como_identificar`). Ortografia pré-Acordo: "pára" (ARR 1×, DEP 5×).
7. **Formato:** Q-COM-010 e Q-COM-022 com 3 alternativas (as outras 70 têm 4).
8. **Alternativas fora do cenário do enunciado** (não bloqueia, mas confunde): Q-ARR-006 D, Q-ARR-023 D, Q-DEP-011 B, Q-COM-015 D, Q-COM-018 D.

## 6. Aprovar primeiro (as 10 mais seguras, temas variados)

1. Q-COM-017: dispositivo de retenção para crianças (OCR 3a al. 1 e 4, todas as variáveis fechadas)
2. Q-ARR-008: onde parar é proibido, estacionar também (OCR 18 al. 2 let. d; 19 al. 2 let. a, e, f)
3. Q-ARR-004: parar na borda esquerda, lista fechada (OCR 18 al. 1)
4. Q-DEP-001: cruzar pela direita, ultrapassar pela esquerda (LCR 35 al. 1)
5. Q-DEP-006: curva sem visibilidade, topo de subida, passagem de nível sem barreiras (LCR 35 al. 4)
6. Q-DEP-019: ilhas e obstáculos no meio da pista (OCR 7)
7. Q-DEP-013: distância e fila parada (OCR 12 al. 1-3)
8. Q-ARR-023: sinal de pane (OCR 23 al. 1-2)
9. Q-COM-008: limites gerais e sinais 4.01/4.02 (OCR 4a al. 3-5)
10. Q-COM-019: luzes de dia e exceções (OCR 30 al. 2)
