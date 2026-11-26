# T-005 — Revisão independente: legal/rules/priorite.yaml (categoria D)

Revisor: REV · Data: 2026-11-26 · Objeto: 46 regras (R-PRIO-001 a 046), status `pendente`.
Fonte única usada: legal/sources/741.01.txt (LCR, État 2026-07-01), 741.11.txt (OCR, État 2026-10-01), 741.21.txt (OSR, État 2026-10-01). Nada da web.
Método: cada regra conferida contra o artigo inteiro no arquivo-fonte (não só o trecho). A numeração das alíneas foi recontada por linha (os arquivos não trazem números de alínea; alíneas revogadas aparecem como "…").

Resultado: **35 OK · 10 CORRIGIR · 1 REMOVER (realocar)**.

## 1. Veredito por regra

| id | veredito | problema | correção proposta (com citação do texto) |
|---|---|---|---|
| R-PRIO-001 | CORRIGIR | `excecoes` incompletas. Faltam exceções de OUTROS artigos que mudam a resposta em perguntas clássicas de priorité de droite: o tram que vem da esquerda tem prioridade; o veículo prioritário passa por cima de tudo; o ciclista em piste cyclable a até 2 m da via segue as mesmas regras de prioridade da via. | Acrescentar em `excecoes`: (a) LCR 38 al. 1: « La voie ferrée doit être dégagée pour laisser passer les tramways ou chemins de fer routiers; la priorité leur sera accordée. » (ressalva: OCR 45 al. 2, ver R-PRIO-024). (b) OCR 16 al. 1: veículos com feu bleu + avertisseur à deux sons « ont la priorité sur tous les usagers de la route ». (c) OCR 40 al. 5: ciclistas em pista a ≤ 2 m « sont soumis, aux intersections aux mêmes règles de priorité que les conducteurs circulant sur la chaussée contiguë ». (d) OCR 41b al. 1 (rotatória: sinal 3.02 na entrada, não vale a direita). |
| R-PRIO-002 | OK | | |
| R-PRIO-003 | OK | | |
| R-PRIO-004 | OK | | |
| R-PRIO-005 | OK | | |
| R-PRIO-006 | OK | | |
| R-PRIO-007 | OK | | |
| R-PRIO-008 | OK | | |
| R-PRIO-009 | OK | | |
| R-PRIO-010 | OK | | |
| R-PRIO-011 | OK | | |
| R-PRIO-012 | OK | | |
| R-PRIO-013 | OK | | |
| R-PRIO-014 | OK | | |
| R-PRIO-015 | OK | | |
| R-PRIO-016 | OK | | |
| R-PRIO-017 | OK | | |
| R-PRIO-018 | OK | | |
| R-PRIO-019 | OK | | |
| R-PRIO-020 | CORRIGIR | `regra_pt` acrescenta exemplos "(patins, patinete, rollers etc.)" que não estão em OCR 6 al. 1. Vêm de OCR 1 al. 10, mas "patinete" em PT induz ao erro: patinete elétrico NÃO é engin assimilé (a definição exige força muscular). | Trocar por: "(patins, rollers, trotinete sem motor, bicicleta infantil — OCR 1 al. 10: « mus par la seule force musculaire des utilisateurs. Les vélos d'enfants sont considérés comme des engins assimilés »)". |
| R-PRIO-021 | OK | | |
| R-PRIO-022 | OK | | |
| R-PRIO-023 | OK | | |
| R-PRIO-024 | CORRIGIR | `excecoes: []`, mas o próprio corpus traz exceções que invertem a resposta: tram que desemboca de via secundária em via principal deve ceder; tram cede a veículos prioritários. Sem isso o aluno aprende "tram sempre tem prioridade", o que contradiz R-PRIO-025. | Acrescentar em `excecoes`: OCR 45 al. 2: « Ils céderont la priorité aux véhicules du service du feu, du service de santé, de la police et de la douane qui sont annoncés par des avertisseurs spéciaux. En débouchant d'une route secondaire sur une route principale, ils sont tenus d'accorder la priorité. » Acrescentar também (complemento, não exceção) que os sinais luminosos e a polícia continuam valendo (LCR 27 al. 1; OSR 68 al. 1). |
| R-PRIO-025 | OK | | |
| R-PRIO-026 | CORRIGIR | `nota` enganosa: "NÃO no LCR art. 36 al. 4". O OCR 17 indica como base justamente « (art. 36, al. 4, LCR) ». A regra do ônibus é uma exceção, no OCR, ao princípio do LCR 36 al. 4. | Reescrever a nota: "Base legal indicada no OCR 17: LCR 36 al. 4. A al. 5 é exceção a esse princípio (normalmente quem entra na circulação cede; aqui quem vem atrás deve deixar o ônibus sair). Ver R-PRIO-030." |
| R-PRIO-027 | OK | | |
| R-PRIO-028 | CORRIGIR | `regra_pt` sem contexto: lida isoladamente, parece regra geral de subir na calçada. No OCR 16 a al. 2 serve para liberar a pista para o veículo prioritário (dever do LCR 27 al. 2). | "Para liberar imediatamente a pista a um veículo prioritário (luz azul + avisador de dois sons), os condutores sobem na calçada com todas as precauções necessárias, quando isso for indispensável." Citar LCR 27 al. 2: « la chaussée doit être immédiatement dégagée ». |
| R-PRIO-029 | CORRIGIR | (1) A 2ª "exceção" (OSR 68 al. 3-4) não é exceção: confirma a regra (com verde, quem vira continua cedendo). (2) Falta a exceção real: seta verde SEM amarelo piscante. (3) A exceção OCR 15 al. 1 está certa, mas a redação não mostra o efeito prático. | Mover OSR 68 al. 3 e al. 4 (2ª frase) para `nota` como "confirmação". Nova exceção: "Seta verde sem amarelo piscante (OSR 68 al. 4: « Les flèches vertes permettent de circuler dans le sens indiqué »): o texto só exige ceder quando o amarelo pisca. Que não é preciso ceder sem o amarelo é inferência do texto, não frase expressa (para pedestres é expresso: OCR 6 al. 2, 2ª frase)". Reescrever a exceção OCR 15 al. 1: "Se você segue a via principal que dobra à esquerda, o veículo em sentido contrário que segue reto sai da via principal e deve ceder a você (OCR 15 al. 1; OSR 65 al. 1: « accorder la priorité aux véhicules circulant sur la route principale ou à ceux qui la quittent »)." |
| R-PRIO-030 | CORRIGIR | `excecoes: []`. Falta a exceção do ônibus de linha (OCR 17 al. 5), que inverte a resposta para "entrar na circulação". Nota "LCR 36 al. 4 NÃO trata de ônibus" é literal, mas induz ao erro (ver R-PRIO-026). | Acrescentar exceção: "Ônibus em tráfego de linha, dentro de localidade, em parada sinalizada, com pisca acionado: quem vem atrás deve, se necessário, reduzir ou parar para deixá-lo sair; não vale se a parada fica na borda esquerda; o ônibus espera se quem vem atrás não consegue parar a tempo (OCR 17 al. 5, R-PRIO-026)." Referências cruzadas: OCR 15 al. 3 (R-PRIO-017) e OCR 17 al. 1-4 (partida, marcha à ré, retorno). |
| R-PRIO-031 | OK | | |
| R-PRIO-032 | OK | | |
| R-PRIO-033 | OK | | |
| R-PRIO-034 | OK | | |
| R-PRIO-035 | OK | | |
| R-PRIO-036 | REMOVER (realocar) | Não é regra de prioridade: OCR 6 al. 5 regula ULTRAPASSAR um ônibus escolar parado (« ne les dépasseront qu'à une allure réduite »). Ninguém recebe prioridade. Ver Notas §4.3. Detalhe: "luzes intermitentes" = « feux clignotants avertisseurs » (OCR 23 al. 3 let. a), ou seja, o pisca-alerta. | Tirar da categoria D e mover para G (cuidado com crianças, currículo 1.4.1), com tag cruzada para E (ultrapassagem). Na regra_pt, trocar "luzes intermitentes" por "pisca-alerta (feux clignotants avertisseurs, OCR 23 al. 3 let. a: « pour laisser monter et descendre les écoliers »)". |
| R-PRIO-037 | OK | | |
| R-PRIO-038 | OK | | |
| R-PRIO-039 | OK | | |
| R-PRIO-040 | CORRIGIR | `nota` falsa: diz que o asterisco colado em "reculer." foi mantido no trecho, mas o `trecho_literal_fr` traz "devra reculer. Le croisement", sem asterisco. Passa no script só porque check_quotes.py apaga "*" (`text.replace("*", "")`). | Corrigir a nota: "O arquivo-fonte tem asterisco de nota após 'reculer.'; omitido no trecho (o script de checagem ignora '*')". Ou recolocar o asterisco, como foi feito em R-PRIO-045. Decidir um padrão único. |
| R-PRIO-041 | OK | | |
| R-PRIO-042 | CORRIGIR | OSR 67 al. 2 (sinais de qualquer pessoa que previnem perigo) está só na `nota`. Para a prova, isso conta mais que a lista a-i (ex.: pessoa que sinaliza um acidente). | Passar para `excecoes` (ou para um complemento na regra_pt): OSR 67 al. 2: « Les signes et instructions donnés par d'autres personnes doivent être observés lorsqu'ils sont destinés à prévenir un danger ou à régler la circulation dans une situation difficile. » |
| R-PRIO-043 | CORRIGIR | `excecoes: []`. Há duas coisas acima dos sinais luminosos, ambas cobradas em prova: ordens da polícia e veículos prioritários. | Acrescentar: (a) LCR 27 al. 1: « les ordres de la police ont le pas sur les règles générales, les signaux et les marques » (os sinais luminosos são "signaux"); (b) OCR 16 al. 1: prioridade « même aux endroits où la circulation est réglée par des signaux lumineux ». (c) Quando o semáforo está desligado ou com amarelo piscante, voltam a valer Stop, Cédez le passage e regra geral (OSR 36 al. 3; OSR 70 al. 1 let. b). |
| R-PRIO-044 | OK | | |
| R-PRIO-045 | OK | | |
| R-PRIO-046 | OK | | |

## 2. Lacunas (regras de prioridade relevantes para a prova que faltam)

Prioridade alta (pegadinhas frequentes na prova; texto já está no arquivo-fonte):
1. **Ciclistas e pistas/bandas cicláveis — OCR 40 al. 1, 4, 5.** Al. 1: ciclista que sai da pista/banda para a pista principal cede. Al. 4: quem atravessa pista/banda fora de interseção (ex.: para entrar numa propriedade) cede aos ciclistas. Al. 5: pista a ≤ 2 m segue as regras de prioridade da via contígua; « En obliquant, les conducteurs de véhicules automobiles circulant sur la chaussée contiguë doivent accorder la priorité aux cyclistes. » (o "gancho à direita").
2. **Inserção em autoestrada e fermeture éclair — OCR 36 al. 4** (« Les usagers des autoroutes et semi-autoroutes ont la priorité sur les véhicules venant d'une voie d'accès. L'art. 8, al. 5, s'applique en cas de ralentissements. ») **e OCR 8 al. 5** (alternância antes do estreitamento de faixas). Ver também OSR 75 al. 4 (sem linha de espera nas entradas de autoestrada).
3. **Via principal que muda de direção — OSR 65 al. 1** (placa 5.09 « Direction de la route principale »: quem perdeu a prioridade cede « aux véhicules circulant sur la route principale ou à ceux qui la quittent »). Par obrigatório de R-PRIO-015.
4. **Pedestres fora de faixa e zonas — OCR 47 al. 5** (« Hors des passages pour piétons, les piétons accorderont la priorité aux véhicules. »); **OSR 22b al. 1** (zone de rencontre: pedestres « bénéficient de la priorité mais ne doivent toutefois pas gêner inutilement les véhicules »; 20 km/h); **OSR 22c al. 1** (zone piétonne: veículos autorizados no máximo a passo; pedestres têm prioridade).
5. **Hierarquia completa (regra-síntese)**, montada só com citações e marcada como síntese: veículo prioritário (OCR 16 al. 1, vale até com semáforo) / ordens da polícia (LCR 27 al. 1; OSR 66 al. 1) > sinais luminosos (OSR 68 al. 1) > sinais e marcas (LCR 27 al. 1, 2ª frase) > regras gerais (LCR 36 al. 2), e o tram (LCR 38 al. 1) acima da regra geral. Polícia x veículo prioritário: o texto não ordena um em relação ao outro. Não inventar.

Prioridade média:
6. **Tram em parada sem ilha — OCR 25 al. 3** (parar até os passageiros saírem da pista); **LCR 33 al. 3** (cuidado com quem sobe/desce do transporte público); OCR 25 al. 4 (entrar nos trilhos para virar à esquerda só se nenhum tram se aproxima).
7. **Não passar pela direita veículos parados para pedestres — OCR 8 al. 3** (« sauf si ces véhicules s'arrêtent pour laisser la priorité à des piétons »).
8. **Calçada — OCR 41 al. 3**: quem precisa usar a calçada com o veículo « doit leur accorder la priorité » (complementa R-PRIO-017, "traversant un trottoir").
9. **Corredor de emergência — OCR 36 al. 7** (em autoestrada com 2+ faixas e trânsito parado, deixar corredor entre a faixa mais à esquerda e a seguinte). Completa R-PRIO-038.
10. **Vias de montanha — OCR 38 al. 1 e 3** (mesma categoria: quem desce recua, salvo se o outro está perto de um local de desvio; nas estradas postais de montanha, seguir os sinais do condutor do ônibus). R-PRIO-040 remete a isso, mas não há regra.
11. **Semáforo, outras cores — OSR 68 al. 2 e 5** (vermelho; amarelo depois do verde = parar se ainda possível; vermelho+amarelo = esperar o verde); **OSR 70 al. 1 let. b** (amarelo piscante com a instalação desligada → R-PRIO-007).
12. **Dois veículos virando à esquerda em sentidos opostos — OCR 13 al. 4** (« ils se croiseront à gauche »). Não é prioridade estrita, mas cai junto com R-PRIO-029.
13. **Linhas de parada e de espera — OSR 75 al. 1 e 3** (a frente do veículo não pode ultrapassar a linha; a linha de espera indica onde parar « le cas échéant »). Hoje só aparecem como referência em 005/006.

Prioridade baixa: OSR 1 al. 7-8 (definição de route principale e route secondaire; na secundária vale a regra geral); OSR 36 al. 6 (Stop/Cédez podem ser colocados em saídas de garagem, pátio etc.); OSR 109 al. 3-4 (como a autoridade resolve o encontro de vias principais); OSR 75 al. 7 (sas pour cyclistes).

## 3. Conflitos e duplicatas

- **R-PRIO-024 x R-PRIO-025 (conflito aparente):** 024 sem exceções ("tram tem prioridade") x 025 ("tram desembocando de via secundária cede"). Resolve com a correção de 024.
- **R-PRIO-030 x R-PRIO-026 (conflito aparente):** "quem entra na circulação cede" x "deixe o ônibus sair". Resolve com a exceção em 030 e a nota corrigida em 026.
- **R-PRIO-029 (incoerência interna):** uma "exceção" que é confirmação. Ver tabela.
- **Duplicatas (não remover, mas ligar entre si):** 020 (OCR 6 al. 1) x 023 (LCR 33 al. 2): mesmo dever; o OCR é mais amplo (inclui o pedestre que espera com intenção visível). Ao ensinar, use 020 como regra e 023 como base legal. 021 x 044: a al. 3-4 do OSR 68 repete OCR 6 al. 2. É coerente. 007 x 043: o OSR 36 al. 3 é um caso particular do OSR 68 al. 1. É coerente. 027 x 038: OCR 16 al. 1 (luz azul E avisador) x LCR 27 al. 2 ("avertisseurs spéciaux"). É coerente; nas perguntas, use as duas condições do OCR.
- **Exceções duplicadas em 001 e 017/015/016**: aceitável (referências cruzadas), sem contradição.
- **Padrão de asterisco**: 045 mantém "*", 040 omite e diz que mantém. Unificar (ver tabela).

## 4. Notas

### 4.1 OSR art. 41 e 43 (cabeçalho vazio)
O que o arquivo mostra:
- "## Art. 41" e "## Art. 43" aparecem sem título marginal e sem corpo. Todos os outros artigos do capítulo 4 têm título.
- Na OSR, o mesmo padrão aparece em outros artigos: art. 3, 60, 91, 94, 115a. Na OCR, também: art. 26, 44, 49, 62, 69 etc.
- Alíneas revogadas aparecem como "…" (ex.: OCR 24 al. 1 e 4; OCR 47 al. 4 e 6).
- As notas de rodapé foram descartadas na extração: sobram só marcadores "*" e linhas "* …". Por isso, nenhuma menção "abrogé" com data existe no arquivo. As 3 ocorrências de "abrog" na OSR não têm relação com isso.
- Há um buraco na numeração dos sinais: o art. 40 trata do 3.06 e o art. 42 do 3.09. Os números 3.07 e 3.08 não aparecem no capítulo.

O que dá para concluir: o padrão é compatível com artigos revogados (no Fedlex, o artigo revogado mostra só o número e uma nota "Abrogé par…"). docs/CURRICULO.md, a partir do índice do PDF oficial (S3), registra "41 abrogé; 43 abrogé", o que corrobora.

O que NÃO dá para concluir só pelo arquivo: a data e o ato de revogação, se algo substituiu esses artigos, e a exclusão total de uma perda na extração.

Recomendação: tratar como revogados (nenhuma regra) e deixar a confirmação para o PESQ no HTML do Fedlex (notas de rodapé). O risco para a prova é baixo: o capítulo vigente cobre 3.01 a 3.06, 3.09 e 3.10.

### 4.2 Artefato "sem espaço perto de aspas" (ex.: `Le signal"Laissez passer…"(3.09)`)
- No texto oficial há guillemets « » com espaços. Nos três arquivos não existe nenhum « ». A extração trocou as guillemets por `"` e comeu os espaços.
- O sentido não muda e nenhuma regra fica errada por causa disso. O efeito é de leitura (o aluno vê `signal"Stop"et"Cédez le passage"`) e de rigor: o `trecho_literal_fr` é literal da extração, não do Fedlex, embora a SPEC diga "copiado do Fedlex, sem alteração". O check_quotes.py já normaliza isso (linha 94) e apaga "*" (linha 106).
- Recomendação: guardar o trecho como está, para continuar batendo com o arquivo, e no app (build_data.py) exibir `"X"` como « X » com espaços. Na SPEC, registrar que "literal" = literal do texto extraído, com aspas normalizadas.
- Não confundir com erro de extração: "bénéfice" (OSR 35 e 39, no lugar de "bénéficie") está no próprio texto. Mantenha.

### 4.3 R-PRIO-036 (ônibus escolar): categoria
Pertence a outra categoria. OCR 6 al. 5 fica num artigo sobre pedestres, mas a regra é de comportamento ao ultrapassar um veículo parado (reduzir, prudência, parar se preciso), sem atribuir prioridade a ninguém. O melhor encaixe é G (usuários vulneráveis/crianças, currículo 1.4.1), com tag cruzada E (ultrapassagem). Manter o texto, mas tirar de D.

### 4.4 Numeração das alíneas
Os arquivos não numeram alíneas. A recontagem por linha, considerando as linhas "…" e as listas a./b., confere em todas as 46 regras. Exemplos checados: OCR 1 al. 8-9, 6 al. 1-5, 17 al. 5, 47 al. 2, OSR 66 al. 1, 67 al. 1, 68 al. 1/3/4. Ao criar regras novas, contar "…" como alínea. Nas citações de lacunas acima a contagem foi feita assim: OCR 40 al. 5, 36 al. 4/7, 47 al. 5, OSR 1 al. 7-8.

### 4.5 Fora do pedido, mas relevante
R-PRIO-019 (pisca na rotatória) e R-PRIO-037 (ciclista na rotatória) não são prioridade em sentido estrito. Mantê-los em D é razoável porque explicam a rotatória inteira, mas eles podem ganhar a tag C.
