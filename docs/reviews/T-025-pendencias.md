# T-025 — Pendências (legal/rules/comportement.yaml, categoria C)

DEV · 2026-11-26 · Base: docs/reviews/T-024-comportement.md. Todas as regras seguem `status: pendente`. Para cada ponto, a leitura conservadora aplicada no YAML.

## 1. Pontos que dependem do Luan

| # | Ponto | Leitura conservadora aplicada | O que falta |
|---|---|---|---|
| 1 | Numeração do LCR 41 al. 4 (R-COM-041, citada em R-COM-038) | `alinea: "4"` deduzida das remissões « 41, al. 2bis » (preâmbulo da OCR) e « 41, al. 2bis et 3 » (OETV). A `nota` diz "confirmar no HTML do Fedlex". Cabeçalho do YAML atualizado. | Confirmar no HTML do Fedlex, ou aceitar a dedução. |
| 2 | Numeração do OCR 4a (R-COM-022 a 027) e do OCR 5 al. 4/5 (R-COM-029, 030) | Mantida a contagem por posição, sem alteração. Trechos conferem; só o número pode mudar (ex.: al. « 3bis »). | Confirmar no HTML do Fedlex. |
| 3 | Numeração do OCR 3 al. 4 (sistema de ajuda ao estacionamento; R-ARR-083, citado em R-COM-016) | Mantida a posição. Pode ser « 3bis ». | Confirmar no HTML do Fedlex. |
| 4 | Numeração do OCR 27 (R-COM-052 a 057, novas) | Contagem por posição: 6 parágrafos, sem « … » nem bis; a lista a./b. pertence ao 3.º (R-COM-054). Nenhuma remissão nas fontes confirma. Cada `nota` diz isso. | Confirmar no HTML do Fedlex antes do exame de 20/12. |
| 5 | Validade das placas 2.30/2.31 (OSR 16 al. 2) | Ensinada em R-COM-031 e R-COM-034 (com a citação do OSR 16 al. 2 em `excecoes`). R-ARR-039 não foi alterada (outro YAML, fora do escopo desta tarefa). | Decidir se R-ARR-039 também recebe a regra (já pedido no T-020 para 2.44/2.45). Sem isso, as duas YAML ficam coerentes por remissão, não por repetição. |
| 6 | Item 1.5.1 (R-COM-047 a 051) | Mantido na categoria C. | Manter em C ou criar categoria própria. Não afeta o conteúdo. |
| 7 | Glossário (docs/GLOSSARIO.md, não editado) | No YAML: « course d'apprentissage » = "trajeto de aprendizagem"; « lieu de stationnement » sem tradução (entre aspas francesas); « faire demi-tour » = "meia-volta" (R-ARR-082 usa "retorno"). | Registrar no glossário e padronizar R-ARR-082. |
| 8 | Artigos de um só parágrafo (OSR 22a em R-COM-032; OCR 33 em R-COM-042) | Mantido `alinea: "1"` (convenção do projeto). | Decidir se o app mostra só "OSR 22a" quando o artigo tem um só parágrafo. |
| 9 | Contexto do álcool (R-COM-012 a 014) | Valores 0,05 mg/l e 0,10 ‰ apresentados só para a proibição do OCR 2a al. 1; o texto do OCR 2a al. 3 não os restringe expressamente, mas nenhuma outra fonte carregada diz que valem para os demais condutores. Nenhum limite geral é afirmado. | Nada a fazer agora; qualquer pergunta de prova sobre esses valores deve manter a restrição aos grupos do OCR 2a al. 1. |

## 2. Lacunas não criadas (texto disponível, fora da prioridade alta)

| Lacuna | Fonte | Por que não foi criada | Leitura conservadora |
|---|---|---|---|
| L-04 | OCR 4, última alínea (« ne pas diminuer la fluidité du trafic … à une allure trop réduite ») | Numeração incerta (pode ser « 2 et 3 … »), já apontada no T-020 (R-DEP-021). | Não ensinar; nenhuma regra afirma o conteúdo. |
| L-05 | OCR 5 al. 1 let. a ch. 4 (80 km/h, « pneus à clous ») e let. c ch. 1 (40 km/h) | Lista multinível; prioridade média. | Não ensinar. Atenção ao traduzir: « remorquage » é rebocar um veículo (inclusive avariado), não puxar um reboque (corrige o T-022-notas, item 5). |
| L-06 | LCR 15a al. 1 (permis à l'essai; período probatório de três anos) | Prioridade média. | R-COM-011 let. h cita o « permis de conduire à l'essai » sem definir o período; não afirmar duração nas perguntas até existir a regra. |
| L-07 | LCR 63 al. 1 (seguro de responsabilidade civil obrigatório) | Prioridade média. | Não ensinar; ao lado de R-COM-047 só vale o que ela já diz. |
| baixa | OAC 5 (exceções à obrigação de permis); OSR 22 al. 3 e 4 (onde se colocam 2.30.1/2.53.1); OSR 27 al. 1 (2.46, proibição de meia-volta); OCR 36 al. 1 (meia-volta em autoestrada) | Prioridade baixa. | R-COM-048 continua dizendo que o OAC 5 não foi lido. Meia-volta: só o que R-COM-035 e R-COM-056 afirmam. |

## 3. Fora de escopo por decisão do Luan

Álcool/drogas (novas regras além das já existentes), telefone, buzina, capacete e condução ecológica: nenhuma regra nova criada e nenhuma lacuna desses temas registrada. Apenas foram corrigidas as regras de álcool que já existiam (R-COM-009, 011 a 014).

## 4. Discordâncias com o T-024

Nenhuma. Os 14 itens (A, M, B), o cabeçalho e os dois ajustes opcionais (R-COM-005, 035) foram conferidos nos arquivos de legal/sources e aplicados. Dois pequenos ajustes de redação:
- R-COM-012 a 014, `nota`: o T-024 afirma que o LCR 55 al. 6 remete à Assemblée fédérale; a nota diz "LCR 55, remetida como « art. 55, al. 6 » na própria LCR" (741.01.txt l. 225, 237, 263) para não depender da contagem por posição.
- R-COM-035: a `excecoes` opcional aponta para R-COM-056 (nova), que cobre o OCR 27 al. 5.
