# BOARD — quadro de tarefas

Orquestrador: Claude (conversa principal). Máx. 3 subagentes simultâneos, sem subagente criando subagente.
Papéis: PESQ (pesquisa legal), DEV (desenvolvimento e testes), REV (revisor independente).
Modelos: Haiku = mecânico · Sonnet = pesquisa, redação, código · Opus = revisão e casos com exceções · Fable = só com aprovação.
Prioridade: P0 base legal · P1 perguntas · P2 interface · P3 extras.
Status: TODO · DOING · BLOCKED · REVIEW · WAITING-LUAN · DONE
Regra de bloqueio: 2 falhas na mesma tarefa → para e vai para o Luan com a causa.

## Calendário-alvo (exame até 31/12)
| Período | Marco |
|---|---|
| 26-27/11 | Fase 0: fundação |
| 28/11-03/12 | Fases 1+2: base legal e ~20 perguntas de Priorité |
| 04-07/12 | Fase 3: PWA mínimo no iPhone |
| 08-21/12 | Fase 5 reduzida: +1 tema a cada ~3 dias (ordem pelas dificuldades do Luan) e Fase 4 (Erros + revisão espaçada) |
| 22/12-exame | Só revisão. Nada de funcionalidade nova. Simulados no iTheorie |

## Tarefas

| ID | Tarefa | P | Papel/Modelo | Depende | Arquivos permitidos | Aceite | Status |
|---|---|---|---|---|---|---|---|
| T-001 | Estrutura, SPEC, BOARD, DECISIONS, SOURCES | P0 | Orquestrador | — | docs/* | Docs existem e Luan aprova | WAITING-LUAN |
| T-002 | Ler OAC art. 13 + anexo 11 ch. II.1 no Fedlex e mapear competências → categorias A-J | P0 | PESQ/Sonnet | T-001 | docs/CURRICULO.md | Cada competência com link Fedlex | TODO |
| T-003 | Mapear regras de Priorité (OCR, OSR) com trecho literal | P0 | PESQ/Sonnet | T-002 | legal/rules/priorite.yaml | Schema SPEC §5 completo | TODO |
| T-004 | Script que confere se cada `trecho_literal_fr` existe no texto Fedlex baixado | P0 | DEV/Haiku | T-001 | scripts/check_quotes.* | Falha se algum trecho não bater | TODO |
| T-005 | Revisão independente das regras de Priorité (exceções, omissões) | P0 | REV/Opus | T-003, T-004 | só comentários em docs/reviews/ | Relatório com veredito por regra | TODO |
| H-02 | Luan valida as regras de Priorité | P0 | Luan | T-005 | — | status → validado | TODO |
| T-006 | ~20 perguntas originais de Priorité (múltipla resposta, níveis 1-4) | P1 | DEV/Sonnet | H-02 | questions/priorite.json | Schema SPEC §5, cada alternativa justificada | TODO |
| T-007 | Revisão independente das perguntas | P1 | REV/Opus | T-006 | docs/reviews/ | Sem ambiguidade nem contradição com regra | TODO |
| H-03 | Luan aprova amostra de perguntas | P1 | Luan | T-007 | — | status → aprovado | TODO |
| T-008 | PWA mínimo: Aprender / Praticar / Erros, offline, progresso local | P2 | DEV/Sonnet | T-001 | app/* | Roda no iPhone; testes passam | TODO |
| H-01 | Luan confirma formato da prova em asa.ch ou no OCN Friburgo | P0 | Luan | — | — | SPEC §3 → confirmado | TODO |

## Bloqueios abertos
- Nenhum.

## Conflitos abertos
- Nenhum.
