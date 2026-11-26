# T-020 — Revisão independente: legal/rules/depassement.yaml (categoria E)

Revisor: REV · Data: 2026-11-26 · Objeto: 63 regras (R-DEP-001 a 063), status `pendente`.
Fonte única: legal/sources/741.01.txt (LCR, État 2026-07-01), 741.11.txt (OCR, État 2026-10-01), 741.21.txt (OSR, État 2026-10-01). Nada da web.
Método: (1) script próprio (fora do repositório) que separa cada artigo em alíneas pela posição do parágrafo, conta "…" como alínea, ignora títulos marginais, linhas "(art. …)" e notas "* …", junta as letras a./b. ao parágrafo e compara o `trecho_literal_fr` (sem "*" e sem número de nota colado) com a alínea indicada; (2) conferência de que cada `termos_fr` aparece no trecho; (3) conferência de que cada id citado em `excecoes` aponta para o artigo/alínea dito; (4) leitura de cada regra contra o artigo inteiro e contra as remissões; (5) cruzamento com priorite.yaml e arret-stationnement.yaml; (6) busca de "dépass|devanc|croise|déboît|présélection|à la file|de front|rabatt|lents|allure trop" nos três arquivos para achar lacunas; (7) teste das funções `normalize`/`strip_notes` do scripts/check_quotes.py com o trecho proposto para R-DEP-052.

Resultado: **51 APROVAR · 12 CORRIGIR · 0 REMOVER**.
- 62 dos 62 trechos presentes são cópia exata da alínea indicada; R-DEP-028 termina antes do " …" final (correto). Todas as alíneas conferem com a contagem por posição. Todos os `termos_fr` aparecem no trecho. Todas as referências cruzadas apontam para o artigo/alínea certo.
- Nenhuma distância, velocidade ou prazo inventado. Os números que aparecem (100 m, 1 m, 30 km/h, 100 km/h, três/quatro faixas) estão no texto.
- Os problemas sérios são de leitura, não de cópia: (a) o "à droite de la ligne de sécurité" do OCR 11 al. 3 virou, em português, algo que pode ser lido como "ultrapassar pela direita"; (b) o fim da proibição de ultrapassar foi ensinado sem o limite "no máximo até o fim da próxima interseção" (OSR 16 al. 2), que está no arquivo e não está em nenhuma regra do projeto para o 2.44/2.45.

## 1. Veredito por regra

Gravidade: **A** = ensina errado ou omite algo de prova; **M** = contexto ou exceção que falta, justificativa falsa; **B** = forma, clareza, nota.

| id | veredito | grav. | problema | correção proposta (pronta para colar) |
|---|---|---|---|---|
| R-DEP-001 | APROVAR | | | |
| R-DEP-002 | APROVAR | | | |
| R-DEP-003 | APROVAR | | | |
| R-DEP-004 | APROVAR | | Nota correta: o texto não fixa metros nem segundos. | |
| R-DEP-005 | CORRIGIR | **A** | A 4ª exceção lista "ultrapassar pela direita à direita da linha de segurança (OCR 11 al. 3)" como exceção a "ultrapassagens pela esquerda". O OCR 11 al. 3 não fala em ultrapassar pela direita do veículo: fala em ultrapassar ficando à direita da linha de segurança. Do jeito que está, ensina que existe ultrapassagem pela direita em curva. Além disso, "em filas paralelas e dentro das localidades" omite a condição "nas estradas com várias faixas marcadas para o mesmo sentido". | Trocar a 4ª exceção por: "Regra de outra disposição (não consta desta alínea): passar à frente (« devancer ») pela direita é permitido na circulação em filas paralelas e, dentro das localidades, nas estradas marcadas com várias faixas para o mesmo sentido, salvo se esses veículos param para dar prioridade a pedestres ou a usuários de engins assimilés; contornar veículos pela direita para ultrapassá-los continua proibido (OCR 8 al. 3, R-DEP-025). Autoestradas e semiautoestradas: OCR 36 al. 5 (R-DEP-047)." (O OCR 11 al. 3 sai desta lista.) |
| R-DEP-006 | APROVAR | | | (opcional) `excecoes`: "Ver R-PRIO-032 (OCR 9 al. 1): obstáculo na própria metade da pista → prioridade ao tráfego em sentido contrário." |
| R-DEP-007 | APROVAR | | | (opcional) `excecoes`: "Ver R-PRIO-036 (OCR 6 al. 5): ônibus escolar parado com pisca-alerta: só ultrapassar em velocidade reduzida e com prudência particular; se necessário, parar." |
| R-DEP-008 | APROVAR | | Nota honesta: não afirma conciliação e a regra não diz mais que o texto. Mas a conciliação está no próprio texto do OCR 11 al. 3 ("sans gêner ceux qui empruntent la même moitié de la chaussée"): ver §4, ponto 1, e a correção de R-DEP-032. | (opcional) trocar a `nota` por: "O OCR 11 al. 3 (R-DEP-032) só permite, em curva ou perto do topo de subida, a ultrapassagem feita à direita da linha de segurança, isto é, sem cruzá-la (LCR 34 al. 2; OSR 73 al. 7 let. a). Não autoriza usar a metade esquerda numa curva sem visibilidade. (Leitura combinada de textos; ver T-020 §4, ponto 1.)" |
| R-DEP-009 | CORRIGIR | B | A nota (al. 5 × al. 6) é honesta; não há contradição a esconder (§4, ponto 2). A 3ª exceção resume mal o OCR 8 al. 3 ("em filas paralelas ou dentro de localidades"). | 3ª exceção: trocar "passar à frente pela direita em filas paralelas ou dentro de localidades" por "passar à frente (« devancer ») pela direita na circulação em filas paralelas e, dentro das localidades, nas estradas com várias faixas marcadas para o mesmo sentido". |
| R-DEP-010 | APROVAR | | Ver §4, ponto 2. | |
| R-DEP-011 | APROVAR | | | |
| R-DEP-012 | APROVAR | | | |
| R-DEP-013 | APROVAR | | Nota honesta (§4, ponto 3). A regra não afirma mais que o texto. As condições do OCR 25 al. 1 estão na 1ª exceção. | |
| R-DEP-014 | APROVAR | | | |
| R-DEP-015 | APROVAR | | | |
| R-DEP-016 | APROVAR | | | |
| R-DEP-017 | APROVAR | | | |
| R-DEP-018 | APROVAR | | | |
| R-DEP-019 | CORRIGIR | B | "O mesmo princípio" fica sem referente quando a regra é lida sozinha (como o gerador de perguntas vai lê-la). | `regra_pt`: "O princípio da LCR 44 al. 1 (só passar de uma faixa a outra se disso não resultar perigo para os outros usuários) vale por analogia quando filas de veículos paralelas circulam na mesma direção em estradas largas cujas faixas não são marcadas." |
| R-DEP-020 | CORRIGIR | B | A exceção diz que o OCR 38 al. 1 "repete" esta regra. Não repete: vale só para veículos da mesma categoria e diz « près d'une place d'évitement », não « manifestement plus près ». | Trocar a exceção por: "Regra de outra disposição (não consta desta alínea): OCR 38 al. 1 (R-DEP-052) trata de veículos da mesma categoria, com redação própria (« sauf si l'autre véhicule se trouve près d'une place d'évitement », sem o « manifestement plus près » desta alínea); veículos de categorias diferentes: OCR 9 al. 2, primeira frase (R-PRIO-040)." |
| R-DEP-021 | CORRIGIR | B | Regra correta. A nota afirma que "a alínea 2 é « et … » e a al. 3 « … »". No Fedlex, « et … » isolado é tipicamente o resto de « 2 et 3 … » (duas alíneas revogadas, números perdidos na extração). Se for isso, « … » é a al. 4 e a frase da fluidez é a al. 5. A al. 1 não muda. | `nota`: "Regra geral de adaptação de velocidade (art. 32 al. 1 LCR, indicado no cabeçalho do OCR 4); incluída aqui só pela cláusula do cruzamento difícil. No arquivo, depois da al. 1 vêm as linhas « et … » e « … » e depois « Il est tenu de ne pas diminuer la fluidité du trafic… ». « et … » provavelmente corresponde a « 2 et 3 … » (duas alíneas revogadas); nesse caso a última alínea é a al. 5. Confirmar no HTML do Fedlex." |
| R-DEP-022 | APROVAR | | | (opcional) `excecoes`: "Regra de outra disposição (não consta desta alínea): OSR 24 al. 1 let. b: com os sinais « Obstacle à contourner par la droite » (2.34) e « Obstacle à contourner par la gauche » (2.35), « le conducteur doit contourner par la droite ou par la gauche l'obstacle devant lequel est placé le signal »." |
| R-DEP-023 | APROVAR | | | |
| R-DEP-024 | APROVAR | | | |
| R-DEP-025 | APROVAR | | Nota honesta. Risco didático: em PT "passar à frente" e "ultrapassar" são quase sinônimos (§4, ponto 4). | (opcional) acrescentar à `nota`: "Na explicação ao aluno, usar sempre 'passar à frente pela direita' para « devancer » (permitido nas condições da alínea) e 'contornar pela direita para ultrapassar' para a manobra proibida." |
| R-DEP-026 | APROVAR | | "voies multiples" (rodas lado a lado) e "voie" (faixa) na mesma frase. A tradução distingue ("várias vias" × "mesma faixa"), mas convém glossário (já pedido no T-015 §3). | |
| R-DEP-027 | APROVAR | | | |
| R-DEP-028 | APROVAR | | Trecho correto sem o " …" final. | |
| R-DEP-029 | APROVAR | | | |
| R-DEP-030 | APROVAR | | | |
| R-DEP-031 | APROVAR | | | |
| R-DEP-032 | CORRIGIR | **A** | "É permitido ultrapassar à direita da linha de segurança, mesmo numa curva" pode ser lido em PT como "ultrapassar pela direita" ou como licença para ultrapassar em curva. O texto só permite a manobra que fica à direita da linha (sem cruzá-la) e sem incomodar quem usa "a mesma metade da pista". A nota é honesta, mas a frase em PT, sozinha, ensina algo perigoso. | `regra_pt`: "É permitido ultrapassar à direita da linha de segurança (« à droite de la ligne de sécurité »), isto é, sem cruzar nem pisar essa linha (LCR 34 al. 2; OSR 73 al. 7 let. a), mesmo numa curva ou ao se aproximar do topo de uma subida, se a manobra puder ser feita sem incomodar quem usa a mesma metade da pista. Isso não autoriza ultrapassar pela direita do veículo ultrapassado nem usar a metade esquerda da pista. Nas passagens de nível sem barreiras, o condutor só pode ultrapassar ciclistas, usuários de engins assimilés à veículos e pedestres, desde que a visibilidade seja boa." `nota`: acrescentar "'Sem cruzar nem pisar a linha' vem da combinação com LCR 34 al. 2 e OSR 73 al. 7 let. a; não é frase expressa do OCR 11 al. 3 (ver T-020 §4, ponto 1)." |
| R-DEP-033 | APROVAR | | | |
| R-DEP-034 | APROVAR | | Nota correta: sem metros nem segundos no texto (§4, ponto 8). | |
| R-DEP-035 | APROVAR | | | |
| R-DEP-036 | CORRIGIR | B | "Numa parada da circulação" é ambíguo em PT (pode ser lido como parada voluntária). Falta a ligação com R-ARR-006, já pedida no T-015. | `regra_pt`: "Quando a circulação fica parada (« arrêt de la circulation »), o condutor não deve parar sobre uma passagem de pedestres nem bloquear, numa interseção, a via aos veículos que circulam no sentido transversal." `excecoes`: acrescentar "Ver R-ARR-006 (OCR 18 al. 2: parada voluntária)." |
| R-DEP-037 | APROVAR | | | |
| R-DEP-038 | APROVAR | | | |
| R-DEP-039 | APROVAR | | Coerente com OCR 36 al. 5 let. b (conceitos diferentes: trocar de faixa para ultrapassar × passar à frente na própria faixa). | |
| R-DEP-040 | APROVAR | | Tradução literal correta. "Se cruzam pela esquerda" é difícil de visualizar; não acrescentar desenho sem fonte (§4, ponto 10). | |
| R-DEP-041 | APROVAR | | | |
| R-DEP-042 | APROVAR | | | |
| R-DEP-043 | APROVAR | | Nota honesta (§4, ponto 3). | |
| R-DEP-044 | APROVAR | | | |
| R-DEP-045 | APROVAR | | Mesmo artigo que R-ARR-028 (OCR 25 al. 5), deveres diferentes. Sem duplicata. | |
| R-DEP-046 | APROVAR | | | |
| R-DEP-047 | APROVAR | | Nota honesta (§4, ponto 4). | |
| R-DEP-048 | APROVAR | | | |
| R-DEP-049 | APROVAR | | | |
| R-DEP-050 | APROVAR | | | |
| R-DEP-051 | APROVAR | | Nota honesta: a limitação à mão única vem do título do artigo. | |
| R-DEP-052 | CORRIGIR | M | A justificativa para omitir o trecho não se sustenta. O cabeçalho do próprio YAML manda copiar "sem asterisco de nota e sem número de nota colado", e todas as outras regras seguem essa convenção. Testei: o `check_quotes.py` aceita o trecho abaixo na variante `sem_notas` (`strip_notes` remove o "33" colado). Também é a única regra com `termos_fr` vazio. | `trecho_literal_fr`: "Lorsque, sur une route à forte déclivité ou sur une route de montagne, des véhicules de même catégorie ne peuvent pas se croiser, c'est le véhicule descendant qui doit reculer, sauf si l'autre véhicule se trouve près d'une place d'évitement. Le croisement de véhicules de catégories différentes est régi par l'art. 9, al. 2, première phrase." `trecho_completo`: true. `termos_fr`: ["de même catégorie", "véhicule descendant qui doit reculer", "près d'une place d'évitement", "catégories différentes"]. `nota`: "Marcador de nota « *3*3 » depois de « catégorie » retirado, conforme o cabeçalho; o check_quotes.py aceita o trecho na variante sem_notas (testado no T-020)." |
| R-DEP-053 | APROVAR | | | |
| R-DEP-054 | APROVAR | | | |
| R-DEP-055 | APROVAR | | | |
| R-DEP-056 | CORRIGIR | M | (1) Falta a duração do sinal: OSR 16 al. 2 manda observar o 2.44 "mais au plus jusqu'à la fin de la prochaine intersection". Nenhuma regra do projeto diz isso para o 2.44/2.45; R-ARR-039 (mesma alínea) só fala de 2.49/2.50. (2) A consequência prática da definição (o 2.44 não proíbe ultrapassar veículos de rodas uma atrás da outra) é o ponto de prova e não está dito. A nota diz que o termo é mantido em francês "porque o texto não explica", mas o próprio corpus usa a expressão oposta (OSR 42 al. 1: « véhicules dont les roues sont placées l'une derrière l'autre »). | Acrescentar à `regra_pt`: "Consequência da definição (leitura do texto, não frase expressa): o 2.44 não proíbe ultrapassar veículos de rodas uma atrás da outra (« roues … placées l'une derrière l'autre », expressão do OSR 42 al. 1), por exemplo bicicletas e motos." `excecoes`: acrescentar "Regra de outra disposição (não consta desta alínea): OSR 16 al. 2 (R-ARR-039): o 2.44 « doit être observé » até o sinal de fim (2.55 ou 2.58), « mais au plus jusqu'à la fin de la prochaine intersection »." (A citação literal da frase toda está em R-DEP-059.) |
| R-DEP-057 | APROVAR | | Mesma lacuna de duração de 056, coberta pela correção de 059. | (opcional) mesma exceção do OSR 16 al. 2 de R-DEP-056, trocando 2.44/2.55 por 2.45/2.56. |
| R-DEP-058 | CORRIGIR | B | "Esses dois sinais" fica sem referente quando a regra é lida sozinha. "Ultrapassados (« devancés »)" mistura os dois verbos que R-DEP-025 e 047 separam de propósito. | `regra_pt`: "Os sinais « Interdiction de dépasser » (2.44) e « Interdiction aux camions de dépasser » (2.45) não impedem os condutores de ultrapassar, se disso não resultar perigo, veículos cuja velocidade máxima é limitada a 30 km/h (monoeixos, carrinhos de mão equipados com motor, chariots à moteur, chariots de travail, veículos automotores agrícolas; art. 11 al. 2 let. g, 13 al. 3 let. b, 17 e 161 a 166 OETV). Os bondes e chemins de fer routiers em marcha podem ser passados à frente pela direita (« devancés par la droite »)." |
| R-DEP-059 | CORRIGIR | **A** | Sozinha, ensina que a proibição dura até o sinal 2.55/2.56. O OSR 16 al. 2 (no arquivo) limita: no máximo até o fim da próxima interseção, e inclui o 2.58 entre os sinais de fim. É pergunta clássica de prova. | Acrescentar à `regra_pt`: "Sem sinal de fim, a proibição vale no máximo até o fim da próxima interseção; o sinal « Libre circulation » (2.58) também a encerra (OSR 16 al. 2)." `excecoes`: acrescentar "Regra de outra disposição (não consta desta alínea): OSR 16 al. 2 (R-ARR-039): os sinais 2.44 e 2.45 « doivent être observés jusqu'au signal correspondant indiquant la fin de la prescription (2.53, 2.54, 2.55, 2.56, 2.58) mais au plus jusqu'à la fin de la prochaine intersection »." e "Ver R-DEP-060 (OSR 32 al. 1)." |
| R-DEP-060 | CORRIGIR | M | A nota diz que a al. 2 (2.58) não foi usada porque "não menciona a proibição de ultrapassar expressamente". É verdade para o OSR 32 al. 2, mas o OSR 16 al. 2 lista o 2.58 entre os sinais que encerram o 2.44/2.45. A nota leva a concluir que o 2.58 não encerra a proibição de ultrapassar. | `nota`: "Al. 2 do OSR 32 (« Libre circulation », 2.58) não menciona a proibição de ultrapassar, mas o OSR 16 al. 2 (R-ARR-039) lista o 2.58 entre os sinais de fim do 2.44/2.45 e limita a validade ao fim da próxima interseção (ver R-DEP-059). Al. 3 a 5 não tratam de ultrapassagem." `excecoes`: acrescentar "Ver R-DEP-059 (OSR 26 al. 4) e R-ARR-039 (OSR 16 al. 2)." |
| R-DEP-061 | APROVAR | | Let. c: não inferir em PT que o lado da linha descontínua "pode" cruzar; o texto não diz. Está correto como está. | |
| R-DEP-062 | APROVAR | | | |
| R-DEP-063 | APROVAR | | | |

**Cabeçalho do YAML (linha 6): CORRIGIR (B).** A remissão do OSR 47 a « art. 10, al. 3, OCR » não confirma a contagem de "…": o OCR 10 não tem alínea revogada. As remissões que confirmam são OSR 45 → « art. 38, al. 3, OCR » (OCR 38 tem "…" como al. 2) e OCR 8 al. 4 → « art. 74a, al. 7, let. e, OSR » (OSR 74a tem "…" como al. 3). Texto proposto: "(confere com as remissões: OSR 45 cita « art. 38, al. 3, OCR » e OCR 8 al. 4 cita « art. 74a, al. 7, let. e, OSR »). Atenção: « et … » isolado pode representar DUAS alíneas (« 2 et 3 … »); ver R-DEP-021."

## 2. Lacunas (só com base nos textos disponíveis)

Prioridade alta:
1. **L-01: OSR 16 al. 2 para o 2.44/2.45** (741.21.txt, linha 137): « Les signaux "Vitesse maximale" (2.30), "Vitesse minimale" (2.31), "Interdiction de dépasser" (2.44), "Interdiction aux camions de dépasser" (2.45), "Interdiction de s'arrêter" (2.49) et "Interdiction de parquer" (2.50) doivent être observés jusqu'au signal correspondant indiquant la fin de la prescription (2.53, 2.54, 2.55, 2.56, 2.58) mais au plus jusqu'à la fin de la prochaine intersection. » R-ARR-039 tem essa alínea como fonte, mas a `regra_pt` dela cita só 2.49/2.50. Resolver de um destes jeitos (decisão do Luan, §4 ponto 5): (a) ampliar a `regra_pt` de R-ARR-039 para listar todos os sinais da frase; ou (b) criar R-DEP-064 com a mesma fonte e foco em 2.44/2.45. As correções de 056/059/060 já fazem a ligação.
2. **L-02: OSR 74 al. 3, faixas de présélection** (linha 782): « Le conducteur ne peut traverser les intersections que dans la direction des flèches de présélection marquées sur sa voie de circulation. Les flèches jaunes sont destinées exclusivement aux conducteurs des bus publics en trafic de ligne; elles les autorisent à circuler dans la direction indiquée. » Nenhum dos três YAML cobre o OSR 74. É o comportamento central das « voies de présélection ».

Prioridade média:
3. **L-03: OSR 74 al. 4**: « Les flèches de rabattement (blanches, placées de biais; 6.07) annoncent au conducteur qu'il doit quitter la voie de circulation dans la direction indiquée. »
4. **L-04: OCR 4, última alínea** (al. 4 ou 5, ver R-DEP-021): « Il est tenu de ne pas diminuer la fluidité du trafic en circulant, sans raison impérieuse, à une allure trop réduite. » É a regra de « véhicules lents » do lado de quem anda devagar demais. Confirmar o número da alínea antes de criar.
5. **L-05: OCR 25 al. 4**: « Lorsque aucun tramway ou chemin de fer routier ne s'approche, les conducteurs qui obliquent à gauche peuvent s'engager sur les rails pour se mettre en ordre de présélection. » Fecha o bloco do bonde (013-015, 043-045) e da présélection.
6. **L-06: OSR 24 al. 1 let. b** (sinais 2.34/2.35, contornar obstáculo pela direita/esquerda). Complementa R-DEP-022. Ver correção opcional de 022.
7. **L-07: OSR 25 (2.42/2.43, proibição de virar) e OSR 27 al. 1 (2.46, proibição de meia-volta)**: o CURRICULO.md põe os dois na categoria E e nenhum YAML os cobre.
8. **L-08: OCR 28 al. 2 e 3** (interromper o sinal de direção depois da manobra; braço estendido se não houver indicadores ou se não estiverem visíveis). Completa R-DEP-016/046.
9. **L-09: OSR 73 al. 1 e al. 6** (a linha de segurança marca o meio da pista ou delimita as faixas; as linhas de aviso anunciam linhas de segurança e linhas duplas, obrigatórias fora das localidades). O cabeçalho as excluiu por "não serem comportamento", mas são necessárias para entender 002, 032 e 061 e costumam cair em prova.

Prioridade baixa:
10. OCR 36 al. 1 (autoestrada: virar só onde sinalizado; proibido meia-volta e marcha à ré) e al. 2 (berme centrale). Talvez categoria G.
11. OSR 28 al. 1 (2.47, distância mínima entre automotores pesados). Fora do foco cat. B.
12. OCR 43 al. 2 (motociclistas não circulam lado a lado nem ao lado de ciclos); LCR 46 al. 2 (ciclistas não circulam lado a lado).
13. OSR 1.07-1.09 (« Chaussée rétrécie »: croisements difficiles) e 1.31 (« Bouchon »: files à l'arrêt ou circulant lentement). Categoria G.
14. OCR 53 (colunas de cavaleiros e rebanhos divididas para facilitar a ultrapassagem).

Não estão nos arquivos-fonte e não devem ser inventados: distância em segundos ou "metade do velocímetro" entre veículos; distância lateral mínima para ultrapassar ciclistas; lista de veículos autorizados a mais de 100 km/h. O autor fez bem em não acrescentar nada disso.

## 3. Duplicatas e referências cruzadas

Dentro do arquivo:
- **020 (LCR 45 al. 1) × 052 (OCR 38 al. 1):** quase a mesma regra, com redações diferentes ("manifestement plus près" × "près"). Manter as duas, já ligadas (corrigir a palavra "repete" em 020).
- **059 (OSR 26 al. 4) × 060 (OSR 32 al. 1):** os dois dizem que 2.55/2.56 encerram a proibição. Manter, ligar uma à outra (correções acima).
- **012 × 037**, **016 × 046**, **018 × 023**, **004 × 034**, **013 × 043 × 058 × 051**: repetições coerentes, já ligadas.

Com outros arquivos:
- **R-DEP-056/057/059/060 × R-ARR-039 (OSR 16 al. 2):** ligação que falta e que importa (lacuna L-01).
- **R-DEP-036 × R-ARR-006** (parada involuntária × voluntária): ligar dos dois lados (T-015 já pediu o lado de R-ARR-006).
- **R-DEP-035 × R-ARR-001**: já ligadas pelo T-015.
- **R-DEP-045 × R-ARR-028**: mesmo artigo (OCR 25 al. 3 e al. 5), deveres diferentes. Sem duplicata.
- **R-DEP-029/011 × R-ARR-048** (sinal 4.15): ligadas.
- **R-DEP-020/052 × R-PRIO-040** (OCR 9 al. 2): ligadas.
- **R-DEP-007/027 × R-PRIO-036** (ônibus escolar; R-PRIO-036 tem `categoria_cruzada: E-Depassement`): não há referência em depassement.yaml. Ligar (opcional em 007).
- **R-DEP-006 × R-PRIO-032** (OCR 9 al. 1, obstáculo na própria metade): ligar (opcional).
- **R-DEP-054 × R-PRIO-047/048** (bandas cicláveis): ligadas.
- **R-DEP-047 × R-PRIO-050/051** (entrada de autoestrada, zíper): ligadas.

Nenhuma duplicata a remover. O cabeçalho lista corretamente o que já estava em priorite.yaml e arret-stationnement.yaml.

## 4. Pontos que exigem decisão do Luan

1. **LCR 35 al. 4 × OCR 11 al. 3 (R-DEP-008, 032).** A nota é honesta: não afirma conciliação, e as regras não dizem mais que o texto. Mas o texto já contém a conciliação. O OCR 11 al. 3 fala em ultrapassar "à droite de la ligne de sécurité" e "sans gêner ceux qui empruntent la même moitié de la chaussée". Com LCR 34 al. 2 (circular sempre à direita das linhas de segurança) e OSR 73 al. 7 let. a (proibido cruzar ou pisar nelas), a leitura é: em curva ou perto do topo, só é permitida a ultrapassagem feita dentro da própria metade, sem cruzar a linha. A proibição da LCR (usar a metade esquerda em curva sem visibilidade) continua inteira. Recomendo aceitar essa leitura, marcada como combinação de textos (correção de 032). Sem ela, as duas regras parecem se contradizer e uma pergunta mal feita pode ensinar a ultrapassar em curva.
2. **LCR 35 al. 5 × al. 6 (R-DEP-009, 010).** Nota honesta. Não há contradição: a al. 1 define que a ultrapassagem se faz pela esquerda. A al. 5 proíbe essa ultrapassagem quando o da frente sinaliza que vai virar à esquerda. A al. 6 diz que, uma vez em présélection à esquerda, ele só pode ser ultrapassado pela direita. O OCR 10 al. 1 vai no mesmo sentido. É leitura sólida, mas é inferência. Decidir se a explicação das perguntas pode dizer isso.
3. **LCR 38 al. 2 × OCR 25 al. 1 (R-DEP-013, 043).** Nota honesta e prudente, porque a relação é mesmo ambígua. O OCR 25 al. 1 vale só para bonde "ne circulant pas au bord de la chaussée" e pode ser lido de dois jeitos: (a) como condição da 2ª frase da LCR ("si cela n'est pas possible"); ou (b) como permissão própria para bonde no meio da pista. Recomendo ensinar a leitura mais segura: regra geral pela direita; pela esquerda só se pela direita não for possível E não houver interseção E sem estorvar o tráfego em sentido contrário. Marcar como interpretação.
4. **OCR 8 al. 3 × OCR 36 al. 5 (R-DEP-025, 047).** Notas honestas. Os dois textos usam o mesmo par de verbos: « devancer » (permitido) × « dépasser … en déboîtant puis en se rabattant » / « contourner … pour les dépasser » (proibido). A relação entre os dois artigos na autoestrada (o 36 al. 5 substitui o 8 al. 3 ou soma-se a ele?) não está escrita. Na prática os dois apontam para o mesmo comportamento. Decidir o vocabulário fixo em PT ("passar à frente pela direita" × "ultrapassar pela direita") e usá-lo em todas as perguntas.
5. **Onde pôr o OSR 16 al. 2 para o 2.44/2.45 (L-01):** ampliar R-ARR-039 ou criar R-DEP-064. Recomendo ampliar R-ARR-039 (uma alínea, uma regra) e manter as referências em 056/059/060.
6. **« et … » vale uma ou duas alíneas?** (OCR 4, R-DEP-021; também OCR 23, T-015 §4 ponto 10). Não afeta nenhuma alínea citada neste arquivo, mas afeta as lacunas L-04 e L-08 do T-015. Confirmar no HTML do Fedlex.
7. **2.44 e veículos de duas rodas (R-DEP-056).** A conclusão de que o 2.44 não proíbe ultrapassar bicicletas e motos vem da definição (« roues placées l'une à côté de l'autre ») e do contraste com o OSR 42 al. 1. É inferência forte, mas não é frase expressa. Aceitar ou não.
8. **Distância entre veículos e distância lateral (R-DEP-004, 034).** O texto só diz « distance suffisante ». Se o Luan quiser a regra prática (segundos, metros, distância a ciclistas), é preciso fonte oficial secundária (OFROU/asa, tarefa PESQ). Até lá, nenhuma pergunta deve cobrar número.
9. **R-DEP-052:** aceitar o trecho sem o marcador "*3*3", como no resto do projeto (recomendado; testado no check_quotes).
10. **OCR 13 al. 4 (R-DEP-040), "ils se croiseront à gauche":** a tradução literal está certa, mas a manobra é difícil de visualizar. Um diagrama exigiria interpretar (cruzar-se "à esquerda" = cada um passa pela frente do outro?). Não desenhar sem fonte oficial com figura.
11. **Glossário "várias vias" × "faixa"** (R-DEP-026; também T-015 §3): fixar "veículo de várias vias = rodas lado a lado" para não confundir com "faixas da estrada".

## 5. Notas

- **Qualidade geral:** cópia literal perfeita, alíneas certas, nenhum número inventado e notas que dizem quando o texto não esclarece algo. É o arquivo mais limpo até agora. Os erros reais são três: (a) um resumo em exceção que transforma "à direita da linha" em "pela direita" (005); (b) uma frase em PT ambígua num ponto de segurança (032); (c) a falta do limite "até a próxima interseção", que está numa alínea que o projeto já tinha, mas resumida só para parar e estacionar (059/R-ARR-039).
- **Categoria:** R-DEP-021 (OCR 4), 034-036 (OCR 12) e 049 (corredor de emergência) também cabem em G. Sugiro tag cruzada, sem mover.
- **R-DEP-055 e 063, 3ª frase:** são regras para ciclistas ou para a autoridade que marca a via. O autor marcou isso nas notas. Perguntas para cat. B devem usá-las só do ponto de vista do motorista (esperar ciclistas passando à frente pela direita; não cruzar a linha amarela contínua).

## 6. Resumo

| | quantidade |
|---|---|
| Regras revisadas | 63 |
| APROVAR | 51 (6 delas com ajuste opcional: 006, 007, 008, 022, 025, 057) |
| CORRIGIR | 12 (A: 3 · M: 3 · B: 6) + cabeçalho do YAML (B) |
| REMOVER | 0 |
| Trechos literais exatos | 62/62 presentes (028 termina antes do " …", correto); 052 sem trecho → corrigir |
| Alíneas erradas | 0 |
| termos_fr ausentes do trecho | 0 (052 tem lista vazia) |
| Lacunas | 14 (alta: 2 · média: 7 · baixa: 5) |
| Pontos para decisão do Luan | 11 |

CORRIGIR por gravidade:
- A: 005, 032, 059
- M: 052, 056, 060
- B: 009, 019, 020, 021, 036, 058 (+ cabeçalho)
