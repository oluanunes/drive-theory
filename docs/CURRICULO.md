# CURRICULO.md — Currículo legal do exame teórico de base (cat. B) x categorias do app

Data da pesquisa: 2026-11-26 · Tarefa T-002 (PESQ) · Idioma: português

## 1. Fontes e vigência

| Código | Fonte | URL | Vigência mostrada | Natureza |
|---|---|---|---|---|
| S1 | OAC RS 741.51 (PDF oficial da Confédération, publicado em Bundespublikationen, mesmo conteúdo do Fedlex) | https://res.cloudinary.com/adminch/image/private/s--wy9yMja5--/v1752030461/Bundespublikationen/741-51f.pdf | "État le 1er janvier 2026" | Oficial (PDF federal) |
| S2 | OCR RS 741.11 (PDF oficial) | https://res.cloudinary.com/adminch/image/private/s--wlKhk8kZ--/v1752031602/Bundespublikationen/741-11f.pdf | "État le 1er octobre 2026" | Oficial (PDF federal) |
| S3 | OSR RS 741.21 (PDF oficial) | https://res.cloudinary.com/adminch/image/private/s--3YdiC6d9--/v1752031725/Bundespublikationen/741-21f.pdf | "État le 1er octobre 2026" | Oficial (PDF federal) |
| S4 | LCR RS 741.01 via lexfind.ch (reprodução da compilação oficial) | https://www.lexfind.ch/tolv/251630/fr (estado 1er avril 2025) e https://www.lexfind.ch/tolv/145993/fr (estado 1er janvier 2020) | 2025-04-01 e 2020-01-01 (DESATUALIZADO) | Reprodução secundária, marcada como tal |

Observações de método e limites:
- fedlex.admin.ch NÃO foi aberto (o WebFetch recusou a URL fora da lista permitida e a shell não tem acesso). Usei os PDFs oficiais federais (S1-S3), que trazem o mesmo texto consolidado do Fedlex. Não usei blog, fórum, site de quiz nem IA como base.
- Também apareceu em buscas o omnilex.ai (ferramenta comercial de IA jurídica). Foi aberto uma vez só para triangular e NÃO é usado como base de nenhum item.
- A ferramenta WebFetch devolve resumo do texto e limita citações literais a ~125 caracteres. Por isso, o "texto original em francês" abaixo são TRECHOS literais curtos (marcados "trecho"), não o texto integral. O texto completo deve ser lido em S1 (partir do caractere ~250000 do PDF, Annexe 11).
- O PDF da OAC mostra estado em 2026-01-01, enquanto OCR e OSR mostram 2026-10-01. Pode haver alteração na OAC/anexo 11 depois de 2026-01-01 que não verifiquei (a página da OFROU sobre modificações OAC/OCR falhou ao abrir). Isto é lacuna.
- Para a LCR só consegui fontes secundárias antigas (S4). Os títulos marginais da LCR vieram de texto "embaralhado" pelo extrator e dois snapshots concordam entre si, mas ficam como "PARCIAL / a confirmar no Fedlex".

## 2. Base legal confirmada

- OAC art. 13 "Examen théorique de base" (S1): al. 1 diz que o exame permite à autoridade competente verificar se o candidato tem os conhecimentos descritos em Annexe 11, ch. II.1 (trecho: "permet à l'autorité compétente de constater si le candidat dispose des connaissances"); al. 1bis permite fazer o exame até um mês antes da idade mínima; al. 2 diz que os cantões elaboram as perguntas com a OFROU e podem delegar a terceiros. Status: VERIFICADO (resumo do fetch, trecho literal curto).
- Título da annexe confirmado: "Annexe 11 (art. 13 et 21) Preuve de l'acquisition des connaissances théoriques". Seção "II Exigences minimales", ponto "1 Examen théorique de base (art. 13)". Seguinte: "2 Examen théorique complémentaire (art. 21)" (itens 2.1 a 2.14, fora do escopo cat. B). Status: VERIFICADO (S1). Nota: o extrator disse que o capítulo I se chama "Connaissances"; não conferi se isso é o título real do ch. I.
- Não existe item 1.7 em II.1 (S1, segundo o fetch).

## 3. Itens do anexo 11, ch. II.1, mapeados

Legenda de status: VERIFICADO = li o item na fonte oficial (S1) e confirmei o conteúdo por trechos literais; resumo PT é minha paráfrase. Mapeamento para categorias A-H é PROPOSTA minha (a lei não conhece as categorias do app). Leis "a confirmar" = não abri o artigo.

### 1.1 "Les prescriptions en matière de circulation routière:" (título literal)
- Trechos FR: « Notamment les signaux, y compris les marques routières et les signaux lumineux » ... « les règles de priorité et les prescriptions régissant les vitesses maximales »
- PT: regras de trânsito, em especial sinais (incluindo marcações no solo e semáforos/sinais luminosos), regras de prioridade e velocidades máximas. A palavra "notamment" indica que a lista não é exaustiva.
- Categorias: A (sinais, marcações, sinais luminosos), D (prioridade), C ou G (velocidades máximas; atribuição por decisão do produto). B (parada/estacionamento) e E (ultrapassagem) NÃO são nomeados aqui; cabem só por "notamment"/regras gerais (ver lacunas).
- Leis prováveis: OSR (confirmado, seção 4), OCR art. 4a e 5 (velocidade, confirmados por título, seção 4), OCR art. 14-16 (prioridade, confirmados). LCR art. 27, 32, 36 (a confirmar, títulos via S4).
- Status: VERIFICADO.

### 1.2 "Le conducteur:" (título literal)
- 1.2.1 Trechos: « l'importance de l'attention et des règles de comportement à observer à l'égard » ... « des autres usagers de la route ». PT: importância da atenção e das regras de comportamento perante os outros usuários da via. Categorias: C. Leis: OCR art. 2, 3 (títulos confirmados "État du conducteur", "Conduite du véhicule"); LCR art. 26, 31 (a confirmar). Status: VERIFICADO.
- 1.2.2 Trechos: « la perception et l'appréciation des situations du trafic et les décisions à prendre » ... « de l'alcool, de stupéfiants et de produits pharmaceutiques ». PT: percepção e avaliação de situações de trânsito, decisões a tomar, tempo de reação e efeitos de álcool, drogas, medicamentos, emoção e cansaço (a lista de emoção/cansaço vem do resumo do extrator, não de trecho literal que eu tenha visto; tratar como VERIFICADO PARCIAL nesse detalhe). Categorias: C, G. Leis: OCR art. 2 e 2a ("Interdiction de conduire sous l'influence de l'alcool"), LCR art. 31 (a confirmar), LCR art. 55 (título "Constat de l'incapacité de conduire", confirmado via S4 parcial). Status: VERIFICADO (detalhe de emoção/cansaço parcial).
- 1.2.3 Trechos: « les règles régissant l'usage écologique du véhicule (conduire en ménageant l'environnement » ... « connaître le principe du roulement en poussée (en coupant les gaz) ». PT: condução ecológica (marcha mais alta possível, trocar cedo, desligar o motor parado, usar a inércia/roulement en poussée). Categorias: C (melhor encaixe; não há categoria "eco"). Leis: OCR art. 33-34 (incommodités/bruit, títulos confirmados, relação provável) e OCR art. 3 (a confirmar). Status: VERIFICADO (conteúdo); relação com OCR a confirmar.
- 1.2.4 Trechos: « les connaissances sur les systèmes d'aide à la conduite et d'automatisation visant à accroître » ... « les principales fonctions des systèmes d'aide à la conduite et d'automatisation ». PT: conhecer sistemas de assistência à condução e automação, seus modos (especialmente assistência permanente), funções, limites e riscos, e a necessidade de ficar atento e pronto para retomar o controle. Categorias: H. Leis: OETV 741.41 (requisitos técnicos, a confirmar), OCR art. 3 (a confirmar), e possivelmente a ordonnance sur la conduite automatisée (RS 741.59, só vista como título de PDF em busca, NÃO aberta). Status: VERIFICADO (conteúdo); leis NÃO VERIFICADO.

### 1.3 "La route:" (título literal)
- 1.3.1 Trechos: « les principes essentiels concernant le respect des distances de sécurité aux autres véhicules » ... « la distance de freinage et la tenue de route du véhicule ». PT: distância de segurança, distância de frenagem, aderência/comportamento do veículo em condições meteorológicas e de pista diferentes. Categorias: G (e C). Leis: OCR art. 12 "Véhicules qui se suivent", OCR art. 4 "Adaptation de la vitesse" (títulos confirmados), OSR art. 28 (distância mínima entre pesados, título confirmado, pouco relevante para cat. B). Status: VERIFICADO.
- 1.3.2 Trechos: « les dangers inhérents aux différents états de la route, notamment en fonction des conditions atmosphériques ». PT: perigos ligados ao estado da pista, clima e hora do dia/noite. Categorias: G. Leis: OCR art. 4, 30 ("Utilisation des feux lors de la marche"); OSR art. 4-9 (sinais de perigo). Status: VERIFICADO.
- 1.3.3 Trecho: « les particularités des différents genres de routes et des prescriptions légales topiques. » PT: particularidades dos tipos de via (autoestrada, via de montanha, túnel, sentido único, rotatória, zonas residenciais etc.) e regras legais aplicáveis. Categorias: A, C, D (rotatórias/prioridade), G. Leis: OCR art. 35-41b (títulos confirmados), OSR art. 22a-22c (zonas) . Status: VERIFICADO.

### 1.4 "Les autres usagers de la route:" (título literal)
- 1.4.1 Trecho: « les dangers spécifiques liés à l'inexpérience des autres usagers de la route ». PT: riscos por inexperiência de outros usuários e grupos vulneráveis (crianças, pedestres, ciclistas, pessoas com mobilidade reduzida). Categorias: G, D (pedestres). Leis: OCR art. 6, 40, 41, 46-48 (títulos confirmados; art. 6 e 47 abertos e conferidos), LCR art. 33 (a confirmar). Status: VERIFICADO.
- 1.4.2 Trechos: « les dangers inhérents à la présence, sur la route, de divers genres de véhicules » ... « la vision différente qu'en ont les conducteurs ». PT: riscos de tipos diferentes de veículos, que se comportam e são vistos de forma diferente pelos condutores. Categorias: G. Leis: OCR art. 42-43a (motos, ciclos), OCR art. 45 (tram); OETV a confirmar. Status: VERIFICADO.

### 1.5 "Les prescriptions générales et règles diverses:" (título literal)
- 1.5.1 Trecho: « les prescriptions régissant les documents officiels requis pour faire usage d'un véhicule; ». PT: documentos oficiais exigidos para usar um veículo (permis de conduire, permis de circulation etc.). Categorias: NENHUMA de A-H (ver seção 6). Leis: OAC (a confirmar), OETV (a confirmar), LCR art. 10-11 (a confirmar, não abertos). Status: VERIFICADO (conteúdo); leis NÃO VERIFICADO.
- 1.5.2 Trecho: « les règles générales sur le comportement du conducteur en cas d'accident ». PT: comportamento geral do condutor em acidente: medidas de segurança, alertar a polícia, socorro. Categorias: F. Leis: OCR art. 54 "Mesures de sécurité sur les lieux d'un accident", 55 "Accidents ayant causé des dommages corporels", 56 "Constatation des faits" (títulos confirmados); LCR art. 51 (a confirmar, não aberto). Status: VERIFICADO.
- 1.5.3 Trecho: « les facteurs qui influent sur la sécurité du chargement et celle des personnes transportées. » PT: fatores que afetam a segurança da carga e dos passageiros. Categorias: G (parcial; carga e passageiros não têm categoria própria). Leis: OCR art. 3a (cinto) e 3b (capacete) (títulos confirmados), LCR art. 30 "Passagers, chargement, remorques" (título via S4, a confirmar), OETV a confirmar. Status: VERIFICADO.

### 1.6 "Les mesures de sécurité à prendre en quittant le véhicule:" (título literal)
- ATENÇÃO, discrepância: o título do ponto 1.6 fala em medidas de segurança ao SAIR do veículo, mas os subitens 1.6.1 e 1.6.2 (pelo fetch) tratam de componentes e equipamento de segurança. Não consegui ler se há texto introdutório que explique isso. Tratar o título e o corpo como não plenamente conciliados.
- 1.6.1 Trechos: « les composants qui jouent un rôle déterminant pour la sécurité routière » ... « les ceintures de sécurité et les avertisseurs acoustiques ». PT: componentes decisivos para a segurança (direção, suspensão, freios, pneus, luzes, piscas, refletores, retrovisores, limpadores, escape, cintos, buzina). Categorias: G (parcial); F (panes) quando for falha de componente. Leis: OETV 741.41 (a confirmar), OCR art. 22 "Manière d'immobiliser les véhicules" e art. 3a. Status: VERIFICADO (conteúdo); lista de componentes é do resumo do extrator, não de trechos literais.
- 1.6.2 Trecho: « l'équipement de sécurité des véhicules, notamment l'utilisation des ceintures de sécurité ». PT: equipamento de segurança (cinto, apoio de cabeça, sistemas de retenção para crianças) e seu uso. Categorias: G. Leis: OCR art. 3a "Port de la ceinture de sécurité" (título confirmado), OETV a confirmar. Status: VERIFICADO.

Total: 6 pontos principais (1.1 a 1.6) e 14 subitens folha no anexo (1.1; 1.2.1-1.2.4; 1.3.1-1.3.3; 1.4.1-1.4.2; 1.5.1-1.5.3; 1.6.1-1.6.2) = 15 itens folha contando 1.1.

## 4. Artigos confirmados por categoria (A-H)

Convenção: "ABERTO" = li o conteúdo do artigo; "TÍTULO" = só vi o título no índice do texto oficial. Todos de S2/S3 (vigência 2026-10-01) salvo LCR (S4, desatualizada).

### A — Panneaux, feux & signes
- OSR (S3): Ch. 2 Signaux de danger, art. 4-15 (TÍTULO; ex.: art. 4 Tournants, 10 Passages à niveau/voies de tram, 11 Passages pour piétons, enfants, cyclistes); Ch. 3 Signaux de prescription, art. 16-34 (TÍTULO; ex.: art. 22 Vitesse maximale, 22a Zone 30, 22b Zone de rencontre, 22c Zone piétonne, 24 Sens obligatoire, 26 Interdictions de dépasser, 30 Interdiction de s'arrêter, de parquer); Ch. 4 Signaux de priorité art. 35-43 (ver D); Ch. 5 Signaux d'indication art. 44-56 (TÍTULO; ex.: art. 46 Sens unique, impasse; 47 Autres signaux impliquant des règles de comportement). Observação: numeração e títulos conferem com o índice do PDF; o texto de cada signal (numeração 1.xx, 2.xx) está nos anexos da OSR, NÃO abertos.
- OCR art. 1a "Numéros utilisés pour la désignation de signaux et de marques" (TÍTULO), art. 28 "Signes" (TÍTULO), art. 29 "Signaux avertisseurs" (TÍTULO), art. 30 "Utilisation des feux lors de la marche" (TÍTULO), art. 31 "Utilisation des feux en cas de parcage" (TÍTULO), art. 32 "Éclairage de remorques..." (TÍTULO), art. 23 "Utilisation du signal de panne et des feux clignotants" (TÍTULO).
- LCR art. 27 "Signaux, marques et ordres à observer", 39 "Signes", 40 "Signaux avertisseurs", 41 "Éclairage des véhicules" (títulos via S4; PARCIAL, a confirmar).
- URLs: S3, S2, S4.

### B — Arrêt & stationnement
- OCR art. 18 "Arrêt", 19 "Parcage en général", 20 "Parcage dans des cas particuliers", 20a "Facilités de parcage pour les personnes à mobilité réduite", 21 "Monter dans le véhicule et en descendre, charger et décharger des marchandises", 22 "Manière d'immobiliser les véhicules", 31 "Utilisation des feux en cas de parcage" (todos TÍTULO). OCR art. 25 al. 5 (ABERTO): não parar sobre as vias de tram nem a menos de 1,5 m do trilho mais próximo.
- OSR art. 30 "Interdiction de s'arrêter, de parquer", 31, 48 "Signalisation des parkings", 48a "Parcage avec disque de stationnement", 48b "Parcage contre paiement" (TÍTULO).
- LCR art. 37 "Arrêt, parcage" (título via S4, a confirmar).
- URLs: S2, S3, S4.

### C — Comportement au volant
- OCR art. 2 "État du conducteur", 2a "Interdiction de conduire sous l'influence de l'alcool", 3 "Conduite du véhicule", 3a "Port de la ceinture de sécurité", 3b "Port du casque", 4 "Adaptation de la vitesse", 4a "Limitations générales de vitesse; règle fondamentale", 5 "Vitesse maximale pour certains genres de véhicules", 17 "Démarrage, marche arrière, demi-tour", 27 "Courses d'apprentissage" (todos TÍTULO), 33 "Bruit à éviter", 34 "Autres incommodités à éviter".
- LCR art. 26 "Règle fondamentale", 31 "Maîtrise du véhicule", 32 "Vitesse", 55 "Constat de l'incapacité de conduire" (títulos via S4, PARCIAL).
- URLs: S2, S4.

### D — Priorité (mais completo; ver seção 5)

### E — Dépassement
- OCR art. 7 "Circulation à droite", 8 "Routes à plusieurs voies, circulation à la file, circulation selon le principe de la fermeture éclair", 9 "Croisement", 10 "Dépassement en général", 11 "Dépassement dans des cas particuliers", 12 "Véhicules qui se suivent", 13 "Présélection, changement de direction" (todos TÍTULO). OCR art. 25 al. 1 (ABERTO): tram/chemin de fer routier fora do meio-fio pode ser ultrapassado pela esquerda só onde não há interseção e sem bloquear o tráfego em sentido contrário.
- OSR art. 26 "Interdictions de dépasser", 25 "Interdiction d'obliquer", 27 "Interdiction de faire demi-tour" (TÍTULO).
- LCR art. 34 "Circulation à droite", 35 "Croisement et dépassement" (títulos via S4, PARCIAL).
- URLs: S2, S3, S4.

### F — Accidents & pannes
- OCR art. 54 "Mesures de sécurité sur les lieux d'un accident", 55 "Accidents ayant causé des dommages corporels", 56 "Constatation des faits" (TÍTULO); art. 23 "Utilisation du signal de panne et des feux clignotants" (TÍTULO); art. 22 "Manière d'immobiliser les véhicules" (TÍTULO).
- LCR: art. sobre obligações em caso de acidente (provável art. 51) NÃO VERIFICADO, não abri.
- URL: S2.

### G — Danger, sécurité & prudence
- OCR art. 3 "Conduite du véhicule", 4 "Adaptation de la vitesse", 12 "Véhicules qui se suivent", 24 "Règles à observer aux passages à niveau et devant les barrières" (ABERTO: não se demorar, não abrir cancelas, não contorná-las), 36 "Règles particulières de circulation sur les autoroutes et semi-autoroutes", 37 "Chaussées à sens unique", 38 "Routes à forte déclivité et routes de montagne", 39 "Tunnels", 40 "Pistes et bandes cyclables", 41 "Chemins réservés aux piétons et trottoirs", 41a "Quartiers d'habitation...", 42-43a (motos, ciclos, cadeiras de rodas), 46-48 (pedestres), 50-52 (via/cavaleiros/animais) (todos TÍTULO salvo art. 24).
- OSR art. 4-15 sinais de perigo (TÍTULO).
- LCR art. 26, 33 "Obligations à l'égard des piétons", 30 "Passagers, chargement, remorques" (via S4, PARCIAL).
- URLs: S2, S3, S4.

### H — Systèmes d'aide à la conduite
- Nenhum artigo da OCR/OSR/LCR foi confirmado por mim como regra detalhada. O currículo (1.2.4) é confirmado, mas a regra detalhada provavelmente está na OETV 741.41 e/ou em norma de condução automatizada (RS 741.59, só visto como título de PDF). NÃO VERIFICADO. Recomenda-se nova pesquisa dedicada (T-002b).

## 5. Categoria D — Priorité (detalhe)

Todos abertos em S2 (OCR, vigência 2026-10-01) salvo indicação. Descrição é paráfrase minha; trecho literal curto entre aspas.

| Tema | Artigo | Título | Conteúdo confirmado | Status |
|---|---|---|---|---|
| Exercício da prioridade (geral) | OCR art. 14 | Exercice du droit de priorité | al. 1: quem deve ceder não deve atrapalhar, reduzir a tempo, parar antes do cruzamento se preciso (« Celui qui est tenu d'accorder la priorité ne doit pas gêner »); al. 2: quem tem prioridade deve considerar quem chegou antes de ele ver o veículo; al. 3: prioridade vale também em faixas paralelas mesmo com a faixa próxima parada; al. 4: cavaleiros/condutores de animais grandes equiparados; al. 5: situações sem regra (ex.: chegada simultânea de todas as direções) exigem atenção e entendimento | VERIFICADO |
| Priorité de droite (regra de direita) | OCR art. 15 al. 2 | Priorité dans des cas particuliers | Onde duas ou mais vias com sinal Stop/Cédez le passage encontram uma via com prioridade no mesmo ponto, os usuários aplicam a regra da direita entre si. A regra geral de priorité de droite é provavelmente LCR art. 36 al. 2 (NÃO ABERTO, a confirmar). OCR art. 14 NÃO menciona a priorité de droite explicitamente | VERIFICADO (art. 15); LCR 36 a confirmar |
| Priorité de droite (sinal) | OSR art. 40 | Intersection comportant la priorité de droite | Só título visto (S3) | TÍTULO |
| Casos especiais | OCR art. 15 al. 1 | idem | Via principal que muda de direção: quem sai dela só cede ao tráfego em sentido contrário da via principal | VERIFICADO |
| Saídas (garagem, pátio, ciclovia, estacionamento, posto, calçada) | OCR art. 15 al. 3 | idem | Quem sai desses locais deve ceder à via; se visibilidade ruim, parar e talvez usar ajudante (trecho: « Celui qui, sortant d'une fabrique, d'une cour, d'un garage ») | VERIFICADO |
| Rotatórias | OCR art. 41b | Carrefours à sens giratoire | al. 1: reduzir e ceder a veículos vindos da esquerda dentro da rotatória (« Avant d'entrer dans un carrefour à sens giratoire »); al. 2: sem sinalizar para entrar nem para seguir na faixa, mas sinalizar a saída; al. 3: ciclistas podem se afastar da regra de ficar à direita | VERIFICADO |
| Sinais de prioridade (capítulo) | OSR art. 35-43 | Cap. 4 "Signaux de priorité": 35 Principes; 36 Signaux «Stop» et «Cédez le passage»; 37 Route principale; 38 Fin de la route principale; 39 Intersection avec une route sans priorité; 40 Intersection comportant la priorité de droite; 41 abrogé; 42 Priorité dans les cas où la chaussée se rétrécit; 43 abrogé | Só títulos conferidos no índice oficial; texto dos artigos NÃO aberto | TÍTULO |
| Pedestres | OCR art. 6 | Comportement à l'égard des piétons et des utilisateurs d'engins assimilés à des véhicules | al. 1: ceder a pedestre que está na faixa não regulada ou espera visivelmente (« Avant d'atteindre un passage pour piétons où le trafic n'est pas réglé »); al. 2: em cruzamentos regulados, quem vira cede a quem atravessa a via em que entra, salvo seta verde sem amarelo piscante; al. 3: em fila sem faixa, parar se há pedestre esperando; al. 4: cego não acompanhado com bengala branca levantada sempre tem prioridade; al. 5: ônibus escolar parado com pisca-alerta, passar devagar e parar se preciso | VERIFICADO |
| Pedestres (obrigações do pedestre) | OCR art. 47 | Traversée de la chaussée | al. 2: em travessia não regulada o pedestre tem prioridade, exceto sobre tram e veículos sobre trilhos, e não pode reivindicá-la se o veículo está perto demais para parar; al. 3: ilha de refúgio divide em duas travessias; al. 5: fora de travessias o pedestre cede | VERIFICADO |
| Pedestres (outros) | OCR art. 46, 48, 41 | Usage de la chaussée; Cas particuliers; Chemins réservés aux piétons et trottoirs | Só título | TÍTULO |
| Pedestres (lei) | LCR art. 33 | Obligations à l'égard des piétons | Só título via S4 | PARCIAL |
| Tram / bonde | OCR art. 25 | Règles à observer à l'égard des tramways et chemins de fer routiers | al. 1 ultrapassagem pela esquerda; al. 2 tram à esquerda, deixar espaço; al. 3 paradas sem ilha, parar até passageiros liberarem; al. 4 virar à esquerda pode entrar nos trilhos; al. 5 não parar nos trilhos nem a < 1,5 m | VERIFICADO |
| Tram (condutores do tram) | OCR art. 45 | Tramways et chemins de fer routiers | al. 2: devem ceder a veículos prioritários e ceder ao entrar em via principal vindo de via secundária; art. 15 NÃO trata de tram | VERIFICADO |
| Tram (lei) | LCR art. 38 | Règles à observer envers les tramways et chemins de fer routiers | Só título via S4 | PARCIAL |
| Ônibus (bus) | OSR art. 34 | Chaussées et voies réservées aux bus | Só título. Regras de prioridade específicas de ônibus saindo de parada (provável OCR/LCR) NÃO ENCONTRADAS/NÃO VERIFICADAS | TÍTULO / NÃO VERIFICADO |
| Veículos prioritários | OCR art. 16 | Véhicules prioritaires | al. 1: bombeiros, saúde, polícia, alfândega com luz azul e sirene bitonal têm prioridade sobre todos, mesmo em semáforo (« ont la priorité sur tous les usagers de la route, même aux endroits où »); al. 2: pode usar calçada com cuidado para liberar a pista; al. 3-4: uso restrito a viagens oficiais urgentes; à noite pode só a luz azul | VERIFICADO |
| Passagem de nível | OCR art. 24 | Règles à observer aux passages à niveau et devant les barrières | al. 2 não se demorar, veículos com esteira/correntes e cavaleiros a passo; al. 3 não abrir nem contornar cancelas; al. 1 e 4 abrogados | VERIFICADO |
| Prioridade (lei base) | LCR art. 36 | Présélection, priorité | Só título via S4; conteúdo NÃO ABERTO | PARCIAL / a confirmar |
| Cruzamento com veículo em obra/estreitamento | OSR art. 42 | Priorité dans les cas où la chaussée se rétrécit | Só título | TÍTULO |

Lacunas D: texto de OSR art. 35-42 (que sinal vale o quê), LCR art. 36 (regra geral priorité de droite), prioridade de ônibus saindo de parada, prioridade em semáforo/agente de trânsito (OCR art. 1 ou LCR art. 27, NÃO VERIFICADO).

## 6. Itens do currículo que NÃO cabem em A-H

- 1.5.1 Documentos oficiais para usar um veículo: nenhuma categoria. Sugestão: nova categoria "K Documentos e obrigações" ou anexar a G. Decisão do Luan/produto.
- 1.5.3 Carga e passageiros: encaixe só parcial em G.
- 1.2.3 Condução ecológica: encaixe só parcial em C.
- 1.6 (medidas ao sair do veículo/componentes e equipamento): encaixe só parcial em G; aguardar leitura do texto exato.
- Cobertura inversa: B (parada/estacionamento) e E (ultrapassagem) não são nomeados no anexo 11 ch. II.1 (só em "notamment" do 1.1). As categorias do app existem na prática (perguntas oficiais cobrem), mas não derivam de item explícito do currículo. Itens I (Outils/Entraîneur) e J (Casse-têtes) ignorados conforme pedido.

## 7. Resumo de verificação

- Itens folha do currículo mapeados: 15 (1.1; 1.2.1-1.2.4; 1.3.1-1.3.3; 1.4.1-1.4.2; 1.5.1-1.5.3; 1.6.1-1.6.2), todos com conteúdo VERIFICADO em S1 por trechos literais curtos.
- Itens NÃO VERIFICADOS na parte "leis prováveis": 1.2.4 (H), 1.5.1, e a LCR em geral (apenas títulos via fonte secundária); OETV 741.41 NÃO aberta em nenhum item.
- Pendências: (1) abrir texto integral do anexo 11 II.1 no Fedlex (WebFetch recusou fedlex.admin.ch; a leitura foi por resumo do extrator, não literal); (2) conferir se houve alteração do anexo 11 após 2026-01-01; (3) confirmar LCR no Fedlex; (4) pesquisar OETV e norma de condução automatizada para categoria H; (5) abrir texto de OSR art. 35-42 e LCR art. 36.
