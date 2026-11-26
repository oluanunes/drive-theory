# T-021 — Pendências do depassement.yaml (após aplicar o T-020)

Agente: DEV · Data: 2026-11-26. Todas as 73 regras (R-DEP-001 a 073) continuam `status: pendente`. Nada aqui foi decidido pelo Luan.

## 1. O que foi feito (resumo)
- Corrigidas (conferidas no texto de legal/sources/): 005, 009, 019, 020, 021, 032, 036, 052, 056, 058, 059, 060 + cabeçalho. Opcionais do relatório também aplicados: 006, 007, 008, 022, 025, 057 (e uma remissão em 061).
- Novas regras (trecho literal conferido com `normalize` do check_quotes.py): R-DEP-064 (OSR 74 al. 3, présélection), 065 (OSR 74 al. 4, rabattement), 066 (OCR 25 al. 4), 067 (OSR 25 al. 1, 2.42/2.43), 068 (OSR 27 al. 1, 2.46), 069 (OCR 28 al. 2), 070 (OCR 28 al. 3), 071 (OSR 73 al. 1), 072 (OSR 73 al. 6), 073 (OSR 24 al. 1, 2.32 a 2.36).

## 2. Decisões que dependem do Luan
1. **Leitura combinada LCR 35 al. 4 × OCR 11 al. 3 (R-DEP-008, 032).** Aplicada como "leitura marcada" (LCR 34 al. 2 + OSR 73 al. 7 let. a), com frase explícita na `nota`. Aceitar ou retirar a frase "Isso não autoriza ultrapassar pela direita do veículo ultrapassado nem usar a metade esquerda da pista" de R-DEP-032.
2. **LCR 35 al. 5 × al. 6 (R-DEP-009, 010):** nota continua só descrevendo os dois textos. Decidir se a explicação das perguntas pode afirmar a articulação.
3. **LCR 38 al. 2 × OCR 25 al. 1 (R-DEP-013, 043):** relação ambígua; notas mantidas. Decidir qual leitura ensinar (recomendada no T-020: regra geral pela direita; pela esquerda só nas condições do OCR 25 al. 1).
4. **Vocabulário fixo em PT** para « devancer » ("passar à frente pela direita") × "ultrapassar/contornar pela direita" (R-DEP-025, 047). Registrado só em R-DEP-025; falta decidir para as perguntas.
5. **R-DEP-056, consequência para bicicletas e motos:** o texto da `regra_pt` está marcado "leitura do texto, não frase expressa" (definição do 2.44 + OSR 42 al. 1). "Por exemplo bicicletas e motos" é o exemplo do relatório; os arquivos-fonte não nomeiam esses veículos nesse contexto. Aceitar ou retirar.
6. **Onde fica o OSR 16 al. 2 para o 2.44/2.45 (L-01):** ampliar R-ARR-039 (recomendado no T-020, mas é outro YAML, fora do meu escopo) ou criar regra nova aqui (seria R-DEP-074, não 064, que foi usado). Por ora 056, 057, 059 e 060 citam o OSR 16 al. 2 em `excecoes`.
7. **« et … » no OCR 4 (R-DEP-021)**: uma ou duas alíneas revogadas? Só o HTML do Fedlex confirma. Afeta o número da alínea de L-04 (abaixo).
8. **Números práticos** (segundos, metros, distância lateral a ciclistas): sem fonte nos arquivos; nenhuma pergunta deve cobrar valor. Se o Luan quiser, precisa de fonte secundária oficial (OFROU/asa).
9. **R-DEP-040 (OCR 13 al. 4, « se croiseront à gauche »):** sem diagrama, sem fonte oficial com figura.
10. **Glossário "veículo de várias vias" (rodas lado a lado) × "faixa"** (R-DEP-026; T-015 §3).

## 3. Lacunas NÃO criadas
- **L-04 (OCR 4, última alínea, « Il est tenu de ne pas diminuer la fluidité du trafic… »):** texto claro, mas o número da alínea (4 ou 5) depende do item 7. Não criei para não registrar alínea errada.
- **L-01:** ver item 6.
- Prioridade baixa do T-020 (sem texto problemático, mas fora do foco cat. B ou de outra categoria): OCR 36 al. 1 e 2 (autoestrada), OSR 28 al. 1 (2.47), OCR 43 al. 2 e LCR 46 al. 2 (ciclos lado a lado), OSR 1.07-1.09 e 1.31, OCR 53 (cavaleiros e rebanhos). Decidir se entram e em qual categoria.
- OSR 25 al. 2 (quando colocar 2.42/2.43) e OSR 24 al. 2 a 6: regras para quem sinaliza ou sinais fora de ultrapassagem; não incluídas.

## 4. Remissões a fazer nos outros YAML (fora do meu escopo)
- R-ARR-006: apontar para R-DEP-036 (parada involuntária × voluntária).
- R-ARR-039: citar 2.44/2.45 (ou ampliar, ver item 6) e apontar para R-DEP-056, 057, 059, 060.
- R-PRIO-032 e R-PRIO-036: apontar para R-DEP-006 e R-DEP-007.
- R-ARR-028: sem mudança (OCR 25 al. 5, sem duplicata com R-DEP-045; R-DEP-066 cita-o em `excecoes`).

## 5. Ajustes meus em relação ao texto proposto no T-020
- R-DEP-056/057 `excecoes`: o relatório citava « doit être observé »; o texto do OSR 16 al. 2 diz « doivent être observés ». Usei a forma literal.
- R-DEP-056 `nota`: a frase "mantido em francês porque o texto não explica o termo" foi trocada por "nenhum artigo define o termo; o OSR 42 al. 1 usa a expressão oposta" (o relatório apontou a inconsistência, mas não propôs texto).
- R-DEP-032 `nota`: a frase antiga "nenhuma interpretação adicional foi acrescentada" ficou falsa depois da correção; foi removida e substituída pela leitura marcada, como no relatório.
- Cabeçalho: acrescentei uma linha sobre R-DEP-052 (sem número de nota) e troquei "OSR 73 al. 1-6" fora de escopo por "al. 2-5", já que al. 1 e 6 viraram R-DEP-071 e 072. O Luan pode preferir manter o escopo antigo (então remover 071 e 072).
- R-DEP-073 copia a alínea inteira do OSR 24 al. 1 (inclui 2.32, 2.33 e 2.36, não só 2.34/2.35), porque o trecho tem de ser a alínea completa.
- Contagem das alíneas de OCR 25 al. 4 e OCR 28 al. 2 e 3 é por posição no arquivo (como o resto); o OCR 25 e o OCR 28 não têm linhas « … », então o risco do item 7 não os afeta.
