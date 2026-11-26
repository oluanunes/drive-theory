# T-032 — Notas do PESQ: legal/rules/accidents-pannes.yaml (categoria F)

Data: 2026-11-26 · 37 regras (R-ACC-001 a 037), todas `pendente`. Fonte única: legal/sources/*.txt (LCR 741.01, OCR 741.11, OSR 741.21, OETV 741.41). Nada da web.
Verificação local: yaml.safe_load OK, ids únicos e sem colisão com os outros YAML; os 37 trechos foram extraídos do texto do artigo indicado e conferidos com a `normalize` de scripts/check_quotes.py (todos "literal"); todo `termos_fr` está no trecho; todo id citado em `excecoes` existe.

## 1. Artigos cobertos

- LCR 51 al. 1 a 4 (R-ACC-001 a 009): parar, segurança da circulação, socorro, polícia, colaboração, não sair do local, danos só materiais, passagem de nível. LCR 92 al. 1 e 2 (010, 011): multa e fuga. LCR 4 al. 1 (012): obstáculos.
- OCR 54 al. 1 e 2 (013 a 015), OCR 55 al. 1 e 2 (016 a 018), OCR 56 al. 1 a 5 (019 a 024). OCR 54 al. 1 era o ponto deixado para F pela nota de arret-stationnement.
- Pane: OCR 23 última alínea (025), OETV 90 al. 2 (026), OCR 57 al. 1 e 3 (027, 028), OCR 35 al. 3 (029), OSR 47 al. 6 (030).
- Túneis e emergência: OCR 39 al. 1 e 2 (031, 032), OSR 45 al. 3 (033), OSR 62 (034 a 036: 4.94, 4.95, 4.80), OSR 70 al. 1 let. f (037).
- Não duplicados, só citados em `excecoes`: OCR 21 al. 3, OCR 22, OCR 23 al. 1 a 3, OCR 36 al. 3, OCR 39 al. 3, OSR 47 al. 5 (R-ARR); LCR 27 al. 2, OCR 16 (R-PRIO); OCR 30 al. 1 (R-COM).

## 2. Numeração de alíneas incerta (conferir no HTML do Fedlex antes de validar)

1. **R-ACC-025 (OCR 23, última alínea).** No arquivo é o 5.º parágrafo, depois de uma linha « et … ». Essa linha costuma ser « N et N+1 … » (duas alíneas revogadas); usei `alinea: "6"` como hipótese. Pode ser outra combinação. O texto da regra está certo; só o número pode mudar.
2. **R-ACC-026 (OETV 90).** O OCR 23 al. 1 manda ver « art. 90, al. 3, OETV » para o sinal de pane, mas no arquivo o triângulo é o 2.º parágrafo e as cales o 3.º (o OETV 114 al. 1 cita « art. 90, al. 3 » para as cales). Usei "2" (posição). A remissão do OCR 23 parece desatualizada. Decidir se R-ARR-025 deve ganhar uma nota.
3. **R-ACC-034, 035 (OSR 62, 4.94/4.95) e R-ACC-036 (OSR 62, 4.80).** Usei "7" e "3" por posição (a lista de símbolos da al. 1 conta como um parágrafo). Nenhuma remissão nas fontes confirma; pode haver alínea bis/ter intermediária.
4. **R-ACC-030 (OSR 47 al. 6, 4.24).** "6" por posição; o 4.15 como al. 4 e o 4.16 como al. 5 já são usados em R-ARR-048 e 049, então a sequência é coerente. Sem confirmação independente.
5. **R-ACC-027, 028 (OCR 57 al. 1, 3) e R-ACC-029 (OCR 35 al. 3).** Posição simples, sem "…" antes; sem remissão que confirme. Risco baixo.
6. **LCR 51 e LCR 92.** Confirmadas: as remissões do OCR 54 a 56 (« 51, al. 1 et 4 », « al. 1 et 2 », « al. 2 et 3 ») batem com os 4 parágrafos. LCR 4 al. 1 confirmada pelo cabeçalho do OCR 23 (« art. 4, al. 1, LCR »).

## 3. Lacunas (o que as fontes NÃO trazem; nada foi inventado)

- **Primeiros socorros.** Nenhuma norma de COMO socorrer (ordem de ações, reanimação, posição lateral de segurança, proteger o local além do OCR 54 al. 1) consta de legal/sources. Em LCR 51 al. 2 só há o dever de socorrer; as técnicas do curso de socorristas do Luan não têm base legal nas fontes. Se o app for ensinar isso, precisa de outra fonte (fora do escopo do legal/sources) e deve ser marcado como conteúdo não legal.
- **Números de emergência (144, 117, 118, 112).** Não aparecem nas fontes (busca nos cinco arquivos). Nenhuma regra os cita. O OSR 62 (4.80) só diz que o poste de chamada é ligado « aux services d'appel d'urgence ».
- **Colete refletivo, kit de primeiros socorros.** Não há obrigação para carros de passeio nas fontes (o OETV só exige « pharmacie de bord » para autocarros). Nenhuma regra de colete ou kit.
- **Sinal de pane: distâncias.** 50 m e 100 m (routes à trafic rapide) estão em R-ARR-026; não repeti. Sobre « routes à trafic rapide » o OCR 23 não define o termo.
- **SDR (art. 13 al. 3)** é citada pelo OSR 45 al. 3 para túneis, mas não está em legal/sources; não afirmei o conteúdo (R-ACC-033). Também ausentes: regras de túnel sobre incêndio e distância entre veículos (nem OCR 39 nem OSR trazem comportamento em incêndio além do que está nas regras).
- **Fogo / extintor.** OETV 114 al. 2 (extintor) vale só para « voitures automobiles lourdes de transport »; não é cat. B, deixei de fora. OETV 114 al. 1 (cale) idem.

## 4. Pontos de tensão e decisões de leitura

1. **LCR 51 al. 2, 4.ª frase × OCR 55 al. 2 / LCR 51 al. 3.** A frase « ne pourront quitter les lieux sans l'autorisation de la police » (R-ACC-006) está na alínea dos feridos; nos casos em que a polícia nem precisa ser avisada (R-ACC-017, 018, 007, 008) o texto não diz como isso se combina. As regras não afirmam nada além do texto; perguntas devem evitar o cenário limite. O OCR 56 al. 3 (R-ACC-022) fecha parte do caso (lesado que quer chamar a polícia).
2. **LCR 51 al. 2, 2.ª frase (R-ACC-004).** « avertiront la police » está no parágrafo que começa com « S'il y a des blessés ». Não ensinar "todo acidente exige polícia"; para danos só materiais, R-ACC-007/008.
3. **R-ACC-020 (OCR 56 al. 1, 2.ª frase).** O texto diz « il convient » (convém), não « doit ». Mantido como "convém".
4. **R-ACC-023 (OCR 56 al. 4).** Vale só para os veículos listados em corrida urgente e transporte público com horário, e só « si des mesures sont prises ». Não generalizar para civis.
5. **R-ACC-028 (OCR 57 al. 3).** Só « défectuosités peu graves ». O texto não diz o que fazer com defeito grave; não preencher a lacuna com regra de pane na pista (isso está em OCR 23 e 54).
6. **R-ACC-037 (OSR 70 al. 1 let. f).** É regra de sinalização (luz amarela intermitente de advertência), não de conduta; incluída porque cita acidentes em autoestradas. Candidata a remoção se o Luan achar que não cai na prova. A letra f foi identificada por posição (a lista é a.–g., g revogada).
7. **R-ACC-012 (LCR 4 al. 1).** Regra geral sobre obstáculos; incluída por ser a base legal do OCR 23. Mesma observação: candidata a remoção.
8. **Trechos `trecho_completo: false`:** R-ACC-021 (2.ª frase « La poursuite pénale est réservée. » não copiada), R-ACC-033 (2.ª frase sobre colocação do sinal), R-ACC-036 (2.ª frase sobre o símbolo extintor) e R-ACC-037 (só a let. f; a lista está em linhas separadas).

## 5. Fora de escopo por decisão do Luan (não criado)

- Álcool/drogas: inclui LCR 55 al. 1 (alcootest após acidente), LCR 91a (recusar teste) e OCR 2a. Telefone, buzina, capacete, condução ecológica: nenhuma regra. O limite geral de alcoolemia não foi tocado.

## 6. Terminologia para o glossário

- « signal de panne » = "sinal de pane" (OETV 90: « triangle de panne » = triângulo de pane); « feux clignotants avertisseurs » = pisca-alertas (R-ARR-027).
- « lésé » = lesado; « éraflures » = arranhões; « course urgente » = corrida urgente (não "curso"); « remorquer » = rebocar um veículo, não puxar um reboque; « demi-tour » = meia-volta (arret-stationnement usa "retorno").

## 7. Sugestões para o REV

- Conferir no HTML do Fedlex as numerações da seção 2 (itens 1 a 5).
- Decidir sobre R-ACC-012 e R-ACC-037 (seção 4, itens 6 e 7).
- Cruzamento sugerido: R-ARR-025 poderia receber uma nota sobre a discrepância OETV 90 (seção 2, item 2).
