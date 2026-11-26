# T-015 — Revisão independente: legal/rules/arret-stationnement.yaml (categoria B)

Revisor: REV · Data: 2026-11-26 · Objeto: 74 regras (R-ARR-001 a 074), status `pendente`.
Fonte única: legal/sources/741.01.txt (LCR, État 2026-07-01), 741.11.txt (OCR, État 2026-10-01), 741.21.txt (OSR, État 2026-10-01). Nada da web.
Método: (1) script próprio (fora do repositório) que separa cada artigo em alíneas por posição de parágrafo, conta "…" como alínea, junta as letras a./b. ao parágrafo e compara o `trecho_literal_fr` com a alínea indicada; (2) leitura de cada regra contra o artigo inteiro; (3) cruzamento com priorite.yaml (56 regras) e depassement.yaml (63 regras); (4) busca de "parqu|parcage|stationn|s'arrêter" nos três arquivos para achar lacunas.

Resultado: **57 APROVAR · 17 CORRIGIR · 0 REMOVER**.
- 73 dos 74 trechos são cópia exata da alínea inteira; R-ARR-027 é literal, mas para antes do marcador "et …" (correto).
- 3 regras citam a alínea errada (062, 063, 064).
- 1 afirmação falsa sobre as fontes: o anexo 3 da OSR (tabela do disco da zona azul) ESTÁ no 741.21.txt. O cabeçalho do YAML e a nota de R-ARR-055 dizem o contrário.

## 1. Veredito por regra

Gravidade: **A** = ensina errado ou omite algo de prova; **M** = citação errada, contexto que falta, exceção que falta; **B** = forma, termos, clareza.

| id | veredito | grav. | problema | correção proposta (pronta para colar) |
|---|---|---|---|---|
| R-ARR-001 | APROVAR | | | (opcional) `excecoes`: "Regra de outra disposição (não consta desta alínea): OCR 12 al. 2, cuja base indicada é LCR 37 al. 1: « Sauf nécessité, les coups de frein et arrêts brusques ne sont admis que si aucun véhicule ne suit. » (R-DEP-035)." |
| R-ARR-002 | APROVAR | | | |
| R-ARR-003 | APROVAR | | | |
| R-ARR-004 | APROVAR | | Termo "éclairage suffisant" não aparece literalmente. | (opcional) termo → "l'éclairage est suffisant". |
| R-ARR-005 | APROVAR | | O termo "s'arrêter hors de la chaussée" não é literal. A nota do art. 18 (25 al. 5, 39 al. 3) pende do asterisco da **al. 2** ("L'arrêt volontaire est interdit*"), não da al. 1. | (opcional) termo → "s'arrêteront si possible hors de la chaussée". Na 2ª exceção, trocar "(remissões da nota do art. 18)" por "(remissões da nota ligada à al. 2 do art. 18)". |
| R-ARR-006 | CORRIGIR | M | (1) A alínea proíbe só a parada **voluntária**. Falta a regra da parada involuntária (congestionamento): sem ela, o aluno conclui que parar sobre a faixa de pedestres num engarrafamento é permitido. (2) O termo "ligne de sécurité" não existe no texto (ele usa o plural). (3) A let. c é ambígua (ver §4, ponto 1). | Acrescentar em `excecoes`: "Regra de outra disposição (não consta desta alínea): esta alínea trata só da parada voluntária. Numa parada da circulação vale OCR 12 al. 3: « Lors d'un arrêt de la circulation, le conducteur ne doit ni s'arrêter sur un passage pour piétons ni barrer, à une intersection, la voie aux véhicules circulant dans le sens transversal. » (R-DEP-036)." Termo: "ligne de sécurité" → "lignes de sécurité". |
| R-ARR-007 | CORRIGIR | M | Tradução errada: "magasins du service du feu" quer dizer depósitos do corpo de bombeiros, não "lojas". O aluno pode imaginar uma loja comercial. O termo "monter dans le véhicule ou en descendre" não é literal. | `regra_pt`: trocar "diante dos locais e lojas do corpo de bombeiros" por "diante de instalações e depósitos do serviço de bombeiros (« locaux et magasins du service du feu »)". Termo → "monter dans le véhicule ou d'en descendre". |
| R-ARR-008 | APROVAR | | | |
| R-ARR-009 | CORRIGIR | B | "Parcar é um estacionamento que…" é circular em PT: a mesma palavra traduz *parcage* e *stationnement*. Em R-ARR-042 o autor já usa "permanência" para *stationnement*. Padronizar. | `regra_pt`: "Estacionar (« parcage ») é uma permanência do veículo (« stationnement ») que não serve unicamente para deixar subir ou descer passageiros ou para carregar ou descarregar mercadorias." |
| R-ARR-010 | APROVAR | | | |
| R-ARR-011 | APROVAR | | | |
| R-ARR-012 | APROVAR | | | |
| R-ARR-013 | APROVAR | | | |
| R-ARR-014 | APROVAR | | Nota correta (let. b ambígua, ver §4, ponto 5). | |
| R-ARR-015 | APROVAR | | | |
| R-ARR-016 | APROVAR | | | |
| R-ARR-017 | APROVAR | | | |
| R-ARR-018 | APROVAR | | | |
| R-ARR-019 | APROVAR | | Termo não literal (o texto conjuga: "montent … en descendent"). | (opcional) termo → "montent dans un véhicule ou en descendent". |
| R-ARR-020 | APROVAR | | Termo não literal. | (opcional) termo → "chargés et déchargés". |
| R-ARR-021 | APROVAR | | | |
| R-ARR-022 | APROVAR | | | |
| R-ARR-023 | APROVAR | | Termo não literal. | (opcional) termo → "serrera le frein". |
| R-ARR-024 | APROVAR | | | |
| R-ARR-025 | APROVAR | | Ver §5 (categoria F). | |
| R-ARR-026 | APROVAR | | Ver §5 (categoria F). | |
| R-ARR-027 | APROVAR | | Ver §3 (ligação com R-PRIO-036) e §5. | |
| R-ARR-028 | APROVAR | | | |
| R-ARR-029 | CORRIGIR | B | A 1ª exceção não é exceção na parte "dentro das localidades": a al. 1 já se limita a « en dehors des localités ». Só o limite de 1,00 m de largura é exceção. | Trocar a 1ª exceção por: "Exceção: em veículos com largura de no máximo 1,00 m, os catadióptricos bastam (OCR 31 al. 3, R-ARR-031). Dentro das localidades a al. 1 não se aplica; ali os catadióptricos bastam (OCR 31 al. 3)." |
| R-ARR-030 | CORRIGIR | M | Sem contexto. Lida sozinha (como o gerador de perguntas vai lê-la), parece regra de iluminação em movimento. O contexto "veículo estacionado" vem só do título do art. 31. | `regra_pt`: "Veículo estacionado (OCR 31, « Utilisation des feux en cas de parcage »): para os veículos de várias vias sem motor, basta uma luz amarela não ofuscante, colocada do lado da circulação e visível pela frente e por trás." |
| R-ARR-031 | CORRIGIR | M | Sem contexto, ensina algo perigoso: "os catadióptricos bastam dentro das localidades" pode ser lido como dispensa de luzes ao circular. | `regra_pt`: "Veículo estacionado (OCR 31, « Utilisation des feux en cas de parcage »): os catadióptricos bastam dentro das localidades e nos veículos cuja largura não excede 1,00 m. Ao circular vale o OCR 30 (luzes de cruzamento ou de circulação diurna)." |
| R-ARR-032 | CORRIGIR | M | A `regra_pt` não diz que vale só em autoestrada e semiautoestrada (está só na nota). Sozinha, sugere que fora da autoestrada só se pode parar em vagas sinalizadas, o que contradiz OCR 18 al. 1. | `regra_pt`: começar com "Nas autoestradas e semiautoestradas (OCR 36), o condutor só usará a faixa de emergência…" (resto igual). |
| R-ARR-033 | APROVAR | | | |
| R-ARR-034 | APROVAR | | | |
| R-ARR-035 | CORRIGIR | B | "dos outros veículos" fica sem referente quando a regra é lida sozinha. O termo "signaux ou marques" não é literal. | `regra_pt`: "O estacionamento dos outros veículos (isto é, os que não são ciclos; ver OCR 41 al. 1, R-ARR-034) na calçada é proibido…" (resto igual). Termo → "signaux ou des marques". |
| R-ARR-036 | CORRIGIR | B | Os termos "signalisation par zones" e "signal de zone" não estão na al. 1 (o primeiro está na al. 2 e na al. 3; a al. 1 diz "signaux de zone"). | `termos_fr`: ["signaux de zone", "ZONE", "Parcage autorisé (4.17)", "Parcage avec disque de stationnement (4.18)", "Parcage contre paiement (4.20)"]. |
| R-ARR-037 | APROVAR | | | |
| R-ARR-038 | APROVAR | | | |
| R-ARR-039 | CORRIGIR | M | (1) O termo "plaque de rappel" não está na al. 2 (está na al. 3 e na al. 4 do OSR 16). (2) A 1ª exceção para em "não diz qual sinal corresponde", mas o corpus responde: nenhum dos sinais listados termina a proibição de parar ou de estacionar. Sem isso, o aluno pode achar que o 2.58 « Libre circulation » encerra um 2.49. | Termos: remover "plaque de rappel". Trocar a 1ª exceção por: "Os sinais de fim listados (2.53, 2.54, 2.55, 2.56, 2.58) não encerram 2.49/2.50: OSR 32 al. 1 diz que 2.53 a 2.56 encerram limites de velocidade e proibições de ultrapassar; OSR 32 al. 2 diz que o 2.58 encerra restrições « imposées aux véhicules en mouvement ». Para 2.49/2.50, o fim é indicado pela « Plaque indiquant la fin d'une prescription » (5.06) (OSR 30 al. 3; OSR 64 al. 3) ou, no máximo, pelo fim da próxima interseção. (Combinação de textos; não é frase expressa.)" |
| R-ARR-040 | CORRIGIR | **A** | A `regra_pt` não diz que se trata da zona de encontro. Lida sozinha, ensina que "o estacionamento só é permitido nos locais designados por sinais ou marcas" em qualquer via, o que é falso (OCR 19). Além disso, é idêntica à de R-ARR-041, e o subtema "zonas-de-estacionamento" está errado. | `regra_pt`: "Na zona de encontro (« zone de rencontre », sinal 2.59.5), o estacionamento só é permitido nos locais designados por sinais ou marcas. Ao estacionamento de ciclos e ciclomotores aplicam-se as regras gerais de estacionamento." `subtema`: zona-de-encontro. `termos_fr`: acrescentar "Les règles régissant le parcage en général". `excecoes`: acrescentar "Ver R-PRIO-054 (OSR 22b al. 1: prioridade dos pedestres)." |
| R-ARR-041 | CORRIGIR | **A** | Mesmo problema, para a zona de pedestres. | `regra_pt`: "Na zona de pedestres (« zone piétonne », sinal 2.59.3), o estacionamento só é permitido nos locais designados por sinais ou marcas. Ao estacionamento de ciclos e ciclomotores aplicam-se as regras gerais de estacionamento." `subtema`: zona-de-pedestres. `excecoes`: acrescentar "Ver R-PRIO-055 (OSR 22c al. 1: veículos autorizados no máximo a passo)." |
| R-ARR-042 | CORRIGIR | M | (1) A 1ª exceção ("cartão: até 3 h em locais com proibição de estacionar") colocada num item sobre 2.49 E 2.50 sugere que o cartão também vale sob o 2.49. OCR 20a al. 1 let. a manda respeitar o art. 19 al. 2, cuja let. a proíbe estacionar « partout où l'arrêt n'est pas permis ». (2) A diferença prática entre 2.49 e 2.50, ponto clássico de prova, está escondida na nota. | Trocar a 1ª exceção por: "OCR 20a al. 1 let. a: com o cartão de estacionamento para pessoas com deficiência, até 3 h em locais com proibição de ESTACIONAR (2.50), respeitando sempre o art. 19 al. 2 a 4. Como o art. 19 al. 2 let. a proíbe estacionar « partout où l'arrêt n'est pas permis », a facilidade não vale sob o 2.49 (inferência; ver §4, ponto 6)." Acrescentar à `regra_pt`: "Consequência da definição: com o 2.50 continua permitido parar só para deixar subir ou descer passageiros ou para carregar ou descarregar; com o 2.49, nenhuma parada voluntária é permitida." |
| R-ARR-043 | APROVAR | | | |
| R-ARR-044 | APROVAR | | Conteúdo repetido em R-ARR-060 sem referência cruzada (§3). | |
| R-ARR-045 | APROVAR | | | |
| R-ARR-046 | APROVAR | | | |
| R-ARR-047 | APROVAR | | | |
| R-ARR-048 | APROVAR | | | |
| R-ARR-049 | APROVAR | | | |
| R-ARR-050 | APROVAR | | | |
| R-ARR-051 | APROVAR | | | |
| R-ARR-052 | APROVAR | | Termo não literal. | (opcional) termo → "le stationnement est limité dans le temps". |
| R-ARR-053 | APROVAR | | | |
| R-ARR-054 | APROVAR | | | |
| R-ARR-055 | CORRIGIR | **A** | (1) **A nota é falsa em relação à fonte.** Ela diz que o texto não fixa a duração na zona azul, mas o 741.21.txt traz o anexo 3, ch. 1 (linhas 3856-3897), com a tabela de horários e a dispensa do disco entre 19h00 e 07h59. Esse é o dado mais cobrado do tema. (2) "dias úteis": em PT-BR isso costuma significar segunda a sexta. O texto diz « jours ouvrables » e não define o termo (ver §4, ponto 2). (3) Termo "dimanche et jours fériés" não literal. | Trocar a `nota` por: "A duração na zona azul está regulada no disco do anexo 3, ch. 1, da OSR, que está no arquivo-fonte (seção 'Annexe 3' / '1 Disque de stationnement (art. 48a)'). Ver as regras novas da lacuna L-01. 'jours ouvrables' não é definido no texto: não traduzir como 'segunda a sexta'." Na `regra_pt`, trocar "nos dias úteis" por "nos dias úteis (« jours ouvrables »; o texto não define se o sábado está incluído)". Acrescentar em `excecoes`: "Anexo 3, ch. 1, OSR: « Entre 19.00 et 07.59, il n'est pas nécessaire d'apposer le disque de stationnement, pour autant que le véhicule soit de nouveau engagé dans la circulation avant 08.00. »" Termo → "le dimanche et les jours fériés". |
| R-ARR-056 | APROVAR | | Confere com o anexo 3 (« sur le trait qui suit celui de l'heure d'arrivée effective »). | |
| R-ARR-057 | APROVAR | | | |
| R-ARR-058 | APROVAR | | | |
| R-ARR-059 | APROVAR | | | |
| R-ARR-060 | APROVAR | | Duplica R-ARR-044 (§3). Termo "arrêt ou parcage" não literal. | (opcional) termo → "l'arrêt ou le parcage"; referência cruzada com R-ARR-044. |
| R-ARR-061 | APROVAR | | | |
| R-ARR-062 | CORRIGIR | M | **Alínea errada.** No OSR 65 o texto "Station de recharge (5.42)" é o 14º parágrafo. Contando a linha "…" (al. 8 revogada) como uma alínea, como no resto do projeto (T-005 §4.4), é a **al. 13**. A al. 12 é o "Téléphone de secours/Extincteur" (5.57/5.59). | `fonte.alinea`: "13". `nota`: "Contagem por posição, com a linha '…' contada como al. 8." |
| R-ARR-063 | CORRIGIR | M | Alínea errada: é a **al. 14** (a al. 13 é a da regra 062). | `fonte.alinea`: "14". |
| R-ARR-064 | CORRIGIR | M | Alínea errada: é a **al. 16**. A al. 15 é outra regra: covoiturage « Excepté » nos sinais 2.01/2.03/2.64, sobre circulação, não estacionamento. | `fonte.alinea`: "16". |
| R-ARR-065 | APROVAR | | A nota (10 m é regra de marcação, 5 m é a distância para o condutor) está correta e é importante. | |
| R-ARR-066 | APROVAR | | | |
| R-ARR-067 | APROVAR | | O termo "marques blanches" não existe no texto ("Les marques sont blanches"). | (opcional) termo → "Les marques sont blanches". |
| R-ARR-068 | APROVAR | | | |
| R-ARR-069 | APROVAR | | | |
| R-ARR-070 | APROVAR | | | |
| R-ARR-071 | APROVAR | | | |
| R-ARR-072 | APROVAR | | | (opcional) `nota`: "Sem inscrição ou símbolo, 6.22/6.23 proíbem só estacionar; parar para passageiros ou mercadorias decorre da definição de parcage (OCR 19 al. 1; OSR 30 al. 1)." |
| R-ARR-073 | APROVAR | | | |
| R-ARR-074 | APROVAR | | Termo não literal. | (opcional) termo → "monter dans le véhicule ou d'en descendre". |

**Cabeçalho do YAML (linhas 8-10): CORRIGIR (A).** O texto afirma: "Fora do escopo por falta de texto no arquivo: anexos da OSR (… modelo do disco de estacionamento, anexo 3 ch. 1 …)" e "Duração máxima da zona azul sem placa … não constam do texto". É falso para o anexo 3, ch. 1. Para o anexo 2 é verdade: os sinais 2.49, 2.50, 4.17, 4.18 e 4.20 aparecem só com número, nome e artigo. Texto proposto: "Anexo 2 da OSR: os sinais aparecem só com número e nome (sem descrição). Anexo 3, ch. 1 (disco): o texto e a tabela de horários ESTÃO no arquivo e geram as regras da lacuna L-01 do T-015. Anexo 3, ch. 2 (cartão): só dimensões e cores."

## 2. Lacunas (com base só nos textos disponíveis)

Prioridade alta:
1. **L-01: disco e duração na zona azul, OSR anexo 3, ch. 1** (741.21.txt, linhas 3856-3897). Falta por completo, e é o item do tema que mais cai em prova. Texto disponível:
   - « La flèche doit être placée sur le trait qui suit celui de l'heure d'arrivée effective. » (repete o OSR 48a al. 3)
   - « Les jours ouvrables - ainsi que les dimanches et jours fériés, pour autant que cela soit expressément indiqué - les véhicules ne peuvent être parqués que comme suit: »
   - Tabela (chegada efetiva → hora a indicar → hora de saída), lida da extração: 08.00-08.29 → 08.30 → 09.30; 08.30-08.59 → 09.00 → 10.00; "etc."; 11.00-11.29 → 11.30 → 12.30; **11.30-13.29 → « sur le trait suivant A » → 14.30**; 13.30-13.59 → 14.00 → 15.00; "etc."; 17.30-17.59 → 18.00 → 19.00; **18.00-07.59 → « sur le trait suivant A » → 09.00**.
   - « Entre 19.00 et 07.59, il n'est pas nécessaire d'apposer le disque de stationnement, pour autant que le véhicule soit de nouveau engagé dans la circulation avant 08.00. »

   Regras sugeridas: R-ARR-075 (como regular o disco), R-ARR-076 (tabela: saída 1 h depois da hora indicada, pausa do almoço até 14h30, noite até 09h00), R-ARR-077 (dispensa do disco entre 19h00 e 07h59). Cuidados: (a) "1 h" é leitura da tabela, não frase do texto, e precisa ser marcada assim; (b) a tabela foi linearizada na extração, então é preciso confirmar o alinhamento das colunas no HTML do Fedlex antes de validar (§4, ponto 3); (c) o check_quotes.py pode não achar trechos da tabela (células HTML). Citar só as frases corridas como `trecho_literal_fr`.

Prioridade média:
2. **L-02: OCR 30 al. 5**, « En cas d'arrêt prolongé, il est autorisé de passer aux feux de position. » Fecha o tema das luzes do veículo parado (R-ARR-004, 029-031).
3. **L-03: OCR 12 al. 3** (parada involuntária: não parar sobre a faixa nem bloquear interseção). Já existe como R-DEP-036. Basta a referência cruzada em R-ARR-006 (ver tabela); não criar duplicata.
4. **L-04: manobras de estacionamento.** OCR 37 al. 3: « Sur une chaussée à sens unique, le conducteur ne fera pas marche arrière sauf en parquant son véhicule, en y attelant une remorque, etc. »; OCR 17 al. 1-3 (antes de sair com o carro, garantir que nenhuma criança ou outro usuário corre perigo; marcha à ré só a passo; ajuda de terceiro se a vista para trás está tapada). Nenhum dos 3 arquivos cobre o OCR 17 al. 1-4 (priorite.yaml tem só a al. 5). Pode ficar em C, com tag B.
5. **L-05: OCR 3 al. 4**, sistema de ajuda ao estacionamento: « le conducteur peut lâcher l'appareil de direction durant le parcage et même quitter le véhicule si le système le permet. Il est tenu de surveiller la manœuvre et de l'interrompre au besoin. » Categoria H, com tag B. É norma recente e provável em prova.
6. **L-06: placas complementares de estacionamento, OSR 64.** Al. 4 let. b (« Plaque de direction » 5.07 sob 2.50 e 4.17: « pour indiquer dans quelle direction s'étend une place interdite ou réservée au stationnement »). Al. 5 let. b (« le mot "Excepté" ou "Autorisé" … signifie que le signal … ne s'applique pas au genre de transport correspondant »). Explica placas do tipo "excepté riverains" sob o 2.50.
7. **L-07: OCR 41 al. 3** (quem usa a calçada com o veículo deve dar prioridade aos pedestres). Completa R-ARR-035 (parar na calçada). Já tinha sido apontada no T-005 (lacuna 8) e ainda não está em priorite.yaml.

Prioridade baixa:
8. OCR 23, última alínea: « Le signal de panne doit aussi être placé à l'arrière des véhicules remorqués. » A numeração é incerta por causa da linha "et …" (§4, ponto 10). Categoria F.
9. OCR 54 al. 1 (medidas de segurança imediatas em caso de pane, « passagers compris »). Categoria F, tag B.
10. LCR 43 al. 2: « Le trottoir est réservé aux piétons, la piste cyclable aux cyclistes. » É a base legal de OCR 41 (R-ARR-034/035).
11. OSR 2a al. 5: « Un signal de zone peut indiquer tout au plus trois réglementations du trafic. »
12. OSR 48 al. 5-7 (P+R 4.25, distância e direção de um parking, parking coberto 4.21); OSR 54 (indicador « Place de stationnement » 4.46); OSR 62 (4.83, parcage automatisé).

Nenhuma multa, nenhum valor de OAO e nenhum dado de dimensão de vaga está nos arquivos-fonte. O autor fez bem em não inventar.

## 3. Duplicatas e referências cruzadas

Dentro do arquivo:
- **040 x 041:** `regra_pt` idênticas (resolvido com a correção A).
- **044 (OSR 30 al. 3) x 060 (OSR 64 al. 3):** mesmas placas 5.04/5.05/5.06, sem referência cruzada entre si. Manter as duas e ligar uma à outra.
- **009 x 042** (definição de parcage), **017 x 061** (cartão atrás do para-brisa), **052 x 058** (nova taxa), **007 x 074** (paradas de transporte público), **006 let. e x 065** (faixa de pedestres), **036 x 050**: repetições coerentes, já ligadas por referência.

Com outras categorias:
- **R-ARR-027 x R-PRIO-036:** as duas tratam do ônibus escolar com pisca-alerta (OCR 23 al. 3 let. a; OCR 6 al. 5). Sem contradição. Acrescentar "ver R-PRIO-036" em 027.
- **R-ARR-006 x R-DEP-036** (OCR 12 al. 3): complementares (voluntária x involuntária). Ligar (correção acima).
- **R-ARR-001 x R-DEP-035** (OCR 12 al. 2, base LCR 37 al. 1): ligar (opcional na tabela).
- **R-ARR-028 x R-DEP-045** (OCR 25 al. 3, parar atrás do tram para os passageiros): mesmo artigo, deveres diferentes. Ligar.
- **R-ARR-032 x R-DEP-049** (corredor de emergência, OCR 36 al. 7): mesmo artigo. Sem conflito.
- **R-ARR-040/041 x R-PRIO-054/055:** mesma zona, alíneas diferentes. Ligar (correção acima).
- **R-ARR-010 x R-PRIO-002** (OSR 37 al. 1 cita o OCR 19): coerentes.
- **"várias vias" (« voies multiples »)**: 029/030 usam a mesma tradução que R-DEP-026. Está coerente no projeto, mas convém um glossário: "veículo de várias vias = com rodas lado a lado (ex.: automóvel)". Hoje "vias" pode ser lido como "faixas da estrada".

Não há duplicata a remover.

## 4. Pontos que exigem decisão do Luan (ambiguidades)

1. **OCR 18 al. 2 let. c (R-ARR-006):** « sur les tronçons servant à la présélection ainsi qu'à côté des lignes de sécurité … lorsqu'il ne reste pas un passage d'une largeur de 3 m au moins ». A condição dos 3 m vale também para a pré-seleção, ou só para as linhas? A gramática permite as duas leituras. Recomendo ensinar a leitura mais segura (pré-seleção: nunca parar; linhas: só se restarem menos de 3 m) e marcar a regra como interpretação.
2. **« jours ouvrables » (R-ARR-055 e L-01):** o texto não define. Em PT-BR, "dias úteis" sugere segunda a sexta. Decidir: manter o termo francês e não afirmar nada sobre o sábado (recomendado), ou buscar a definição numa fonte oficial (PESQ).
3. **Tabela do anexo 3 (L-01):** a extração juntou as colunas num texto linear. A leitura acima (chegada → hora a indicar → saída) é consistente linha a linha, mas confirme no HTML ou PDF do Fedlex antes de validar números.
4. **Numeração do OSR 65 (062-064):** contei "…" como uma alínea (al. 8), seguindo T-005 §4.4. Se o Fedlex numerar diferente, os números mudam, mas os do YAML (12/13/15) não batem com nenhuma contagem coerente. Confirmar no HTML (o check_quotes.py confere o trecho, não o número da alínea).
5. **OCR 20a al. 1 let. b:** « stationner sur les places de parc pendant une durée illimitée ». Isso inclui vagas com disco ou pagas? O texto não diz (a nota do autor está correta). Não criar pergunta sobre isso até haver fonte.
6. **Cartão de deficiente sob o 2.49 (R-ARR-042):** a conclusão de que não vale vem de combinar OCR 20a let. a com OCR 19 al. 2 let. a e OSR 30 al. 1. É sólida, mas é inferência. Aceitar como tal ou pedir confirmação.
7. **Fim de 2.49/2.50 (R-ARR-039):** o OSR 16 al. 2 manda observar até o "signal correspondant" (2.53-2.58), mas nenhum deles serve para parar ou estacionar (OSR 32). Na prática, o fim é a placa 5.06 ou a próxima interseção. É inferência de texto; aceitar ou não.
8. **OSR 22b al. 3 / 22c al. 2, 2ª frase:** « Les règles régissant le parcage en général s'appliquent au stationnement des cycles et des cyclomoteurs ». Isso dispensa ciclos e ciclomotores da exigência de local sinalizado? A leitura é plausível, mas o texto não diz expressamente. Recomendo não ensinar além do literal.
9. **OCR 31 al. 2 (R-ARR-030):** vale só fora das localidades, como a al. 1? A al. 3 cobre o interior das localidades, o que sugere que sim, mas o texto da al. 2 não diz. E vale de dia? LCR 41 al. 2 só exige luz da tombée de la nuit ao lever du jour ou com visibilidade ruim. As notas do autor estão corretas; decidir se a pergunta pode cobrar isso.
10. **OCR 23, última alínea:** o arquivo mostra "et …" depois da let. b da al. 3. Não dá para saber se "Le signal de panne doit aussi être placé à l'arrière des véhicules remorqués" é a al. 4 ou outra. Confirmar no Fedlex antes de criar a regra (L-08).
11. **"passages sous voies" (R-ARR-006 let. f):** "passagens sob vias" em PT é vago. Pelo contexto (junto de "passages à niveau"), o sentido provável é passagem inferior sob a via férrea, mas isso não está escrito. Decidir se mantém só o termo francês.

## 5. Notas

- **Categoria F:** R-ARR-025, 026 e 027 (sinal de pane e pisca-alerta) estão listados no CURRICULO.md em F (Accidents & pannes: OCR 23). R-ARR-022 a 024 (OCR 22) aparecem em B e F. Recomendo manter em B com tag F, ou mover 025-027 para F. Não afeta o conteúdo.
- **Termos com número entre parênteses** (ex.: "Interdiction de s'arrêter (2.49)"): no arquivo-fonte fica `"Interdiction de s'arrêter"(2.49)`. É a mesma convenção de priorite.yaml (rótulo, não citação). Os termos_fr não são conferidos por script (build_data.py só os copia). Aceitável. Só marquei como problema os termos ausentes da alínea (036, 039) ou com palavra diferente (007, 035, os opcionais).
- **Qualidade geral:** trechos 100% literais e completos, notas honestas sobre o que o texto não diz, nenhuma distância, prazo ou valor inventado. Os erros reais são de contexto (regras que perdem o sentido fora do artigo), de numeração (OSR 65) e um erro de leitura da fonte (anexo 3).

## 6. Resumo

| | quantidade |
|---|---|
| Regras revisadas | 74 |
| APROVAR | 57 (12 delas com ajuste opcional de termo ou nota) |
| CORRIGIR | 17 (A: 3 · M: 10 · B: 4) + cabeçalho do YAML |
| REMOVER | 0 |
| Trechos literais exatos | 74/74 (027 termina antes do "et …", correto) |
| Alíneas erradas | 3 (062, 063, 064) |
| Lacunas | 12 (alta: 1 · média: 6 · baixa: 5) |
| Pontos para decisão do Luan | 11 |

CORRIGIR por gravidade:
- A: 040, 041, 055 (+ cabeçalho)
- M: 006, 007, 030, 031, 032, 039, 042, 062, 063, 064
- B: 009, 029, 035, 036
