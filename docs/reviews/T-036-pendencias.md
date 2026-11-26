# T-036: pendências de accidents-pannes.yaml (decisão do Luan e numeração incerta)

Base: docs/reviews/T-034-accidents-pannes.md. Todos os status continuam `pendente`.

## Pontos de decisão do Luan (T-034 §5)

| # | Ponto | Leitura conservadora aplicada |
|---|---|---|
| 1 | Duplicatas | Removidas R-ACC-030, 031, 032 (ficam R-DAN-013, 006, 007). Ids não reutilizados. |
| 2 | R-ACC-037 | Removida. A lacuna L-02 (OSR 68, « feu jaune clignotant ») já existe como R-PAN-044 (panneaux.yaml, OSR 68 al. 6, mesmo trecho); nenhuma regra nova foi criada aqui para não duplicar. |
| 3 | R-ACC-012 | Mantida. |
| 4 | Caso-limite R-ACC-006 x 017/018 | R-ACC-006 passou a valer só para acidente com feridos (LCR 51 al. 2); nota proíbe pergunta sobre o caso-limite (ferimentos leves do OCR 55 al. 2) até haver fonte. |
| 5 | Numeração a conferir no HTML do Fedlex antes de `validado` | Ver tabela abaixo. |
| 6 | R-ARR-025 (OETV 90 al. 3) | Fora do escopo deste arquivo. Falta nota em arret-stationnement.yaml igual à de R-ACC-026: a OETV 90 al. 3 são as cales; o triângulo é a al. 2. |
| 7 | Primeiros socorros e números 144/117/118/112 | Fora do app (não constam de legal/sources). Só entram com fonte não legal rotulada, se o Luan quiser. |

## Numerações incertas

| Regra | Citação usada | Dúvida | Leitura conservadora |
|---|---|---|---|
| R-ACC-025 | OCR 23 al. 6 | Última alínea do art. 23, depois da linha « et … »; número não decidível pelas fontes. | Nota diz "NUMERAÇÃO NÃO CONFIRMADA"; app deve mostrar "OCR 23 (última alínea)". |
| R-ACC-034, 035 | OSR 62 al. 7 | Contagem por posição; parágrafo após lista a./b. pode pertencer à alínea da lista. | App deve mostrar "OSR 62". |
| R-ACC-036 | OSR 62 al. 3 | Pode ser al. 2 se « Le cas échéant… » continuar a al. 1. | App deve mostrar "OSR 62". |
| R-DAN-013 (outro YAML) | OSR 47 al. 6 | Nenhuma remissão confirma; coerente com R-ARR-048/049. | Dúvida passa a ser só de R-DAN-013 (não editado aqui). |

Confirmadas: OETV 90 al. 2 (R-ACC-026), LCR 51 al. 1 a 4, OCR 54 a 56.

## Itens opcionais do T-034 não aplicados (fora das 11 correções pedidas)

- R-ACC-007: `excecoes` com a sanção da LCR 92 al. 1 (R-ACC-010).
- R-ACC-012: `excecoes` com a remissão do OSR 104 (741.21.txt l. 1126).
- R-ACC-017: `excecoes` com OCR 56 al. 3 (R-ACC-022).
- R-ACC-029: `excecoes` com R-DAN-045 e R-DAN-046 (reboque, OCR 72; L-05).

## Outras lacunas do T-034 sem regra nova

- L-01: sem fonte. L-03: está em arret-stationnement.yaml (não editável aqui). L-04 e L-05: já cobertas por regras existentes.
