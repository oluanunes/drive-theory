# T-018 — Pendências de arret-stationnement.yaml (para decisão do Luan)

Base: T-015 §4 e §2. Nada abaixo foi decidido pelo DEV. Todas as regras seguem `pendente`.

## A. Decisões do Luan (T-015 §4)

1. R-ARR-006 let. c (OCR 18 al. 2): a condição de 3 m vale também para a pré-seleção ou só para as linhas? Sugestão do revisor: ensinar a leitura mais segura e marcar como interpretação. Texto da regra não alterado.
2. "jours ouvrables" (R-ARR-055, R-ARR-076): o texto não define. Aplicado só o mínimo seguro (manter o termo francês, sem afirmar nada sobre o sábado). Decidir se busca definição oficial.
3. Tabela do anexo 3 (R-ARR-076): conferir alinhamento das colunas no HTML/PDF do Fedlex. A regra tem `nota` explícita, `trecho_completo: false`, e as linhas « etc. » não foram preenchidas. O significado de « A » em « sur le trait suivant A » não é explicado na extração.
4. Numeração das alíneas do OSR 65 (R-ARR-062/063/064 = al. 13/14/16): conferido contra 741.21.txt (contando « … » como al. 8, convenção T-005 §4.4). Confirmar no Fedlex.
5. OCR 20a al. 1 let. b ("durée illimitée" em places de parc): inclui vagas com disco ou pagas? Sem fonte; nenhuma pergunta deve cobrar isso.
6. R-ARR-042: aceitar como inferência que o cartão de deficiente não vale sob o 2.49 (aplicado com a marca "inferência" no texto).
7. R-ARR-039: aceitar como inferência que 2.53 a 2.58 não encerram o 2.49/2.50 (aplicado com a marca "Combinação de textos; não é frase expressa").
8. OSR 22b al. 3 / 22c al. 2, 2ª frase (R-ARR-040/041): se as regras gerais de parcage dispensam ciclos e ciclomotores do local sinalizado. Texto não diz; a regra_pt repete só o literal.
9. OCR 31 al. 2 (R-ARR-030): vale só fora das localidades? E de dia? O texto não diz; a regra_pt só afirma o contexto "veículo estacionado".
10. OCR 23, última alínea (« Le signal de panne doit aussi être placé à l'arrière des véhicules remorqués »): numeração incerta por causa de « et … » (arquivo, linha 378). Regra não criada.
11. R-ARR-006 let. f ("passages sous voies"): manter só o termo francês? Não alterado.
12. Categoria de R-ARR-083 (OCR 3 al. 4, sistema de ajuda ao estacionamento): o CURRICULO sugere H; ficou em B neste arquivo, com nota.

## B. Lacunas do T-015 §2 NÃO criadas

- L-03: só referência cruzada (feita em R-ARR-006 -> R-DEP-036); sem duplicata.
- OCR 54 al. 1 (medidas de segurança em pane): categoria F, outro tema.
- OSR 48 al. 5-7 (P+R 4.25, parking coberto 4.21), OSR 54 (4.46), OSR 62 (4.83): texto disponível, baixa prioridade, não incluídos.

## C. Ajustes opcionais do T-015 (APROVAR) NÃO aplicados

Termos não literais (004, 005, 019, 020, 023, 052, 060, 067, 074), nota de 072, nota de 005, e referências cruzadas 001 -> R-DEP-035, 027 -> R-PRIO-036, 028 -> R-DEP-045, 044 <-> 060. Fora do escopo das 17 correções.

## D. Verificação de trechos

`scripts/check_quotes.py` só roda contra a rede ou contra `DIR/<rs>.html`; não aceita os .txt. Foi feita verificação local equivalente (mesma `normalize` do script) de todos os `trecho_literal_fr` contra legal/sources/*.txt: 88/88 encontrados. O check_quotes oficial (Fedlex) deve rodar no CI; o trecho de R-ARR-075/077 atravessa quebra de linha da extração e R-ARR-076 cita só a frase introdutória.
