# BOARD — quadro de tarefas

Orquestrador: Claude (conversa principal). Máx. 3 subagentes simultâneos, sem subagente criando subagente.
Papéis: PESQ (pesquisa legal), DEV (desenvolvimento e testes), REV (revisor independente).
Modelos: Haiku = mecânico · Sonnet = pesquisa, redação, código · Opus = revisão e casos com exceções · Fable = só com aprovação.
Prioridade: P0 base legal · P1 perguntas · P2 interface · P3 extras.
Status: TODO · DOING · BLOCKED · REVIEW · WAITING-LUAN · DONE
Regra de bloqueio: 2 falhas na mesma tarefa → para e vai para o Luan com a causa.

## Calendário-alvo (exame até 31/12, escopo completo — D-006)
| Período | Marco |
|---|---|
| 26-28/11 | Fase 0 + currículo oficial mapeado (T-002) + checagem no Actions (T-004) |
| 28/11-03/12 | Priorité completa (regras + perguntas) e PWA mínimo em paralelo |
| 04-20/12 | Esteira: as outras 9 categorias, 2 em paralelo, ~3-4 dias cada par. Fase 4 (Erros, revisão espaçada, simulado) entra no meio |
| 21/12-exame | Congelamento: só correções. Estudo e simulados |

Gargalo previsto: validação do Luan (H-02/H-03 de cada tema), ~30-45 min por tema.

## Tarefas

| ID | Tarefa | P | Papel/Modelo | Depende | Arquivos permitidos | Aceite | Status |
|---|---|---|---|---|---|---|---|
| T-001 | Estrutura, SPEC, BOARD, DECISIONS, SOURCES | P0 | Orquestrador | — | docs/* | Docs existem e Luan aprova | DONE |
| T-002 | Ler OAC art. 13 + anexo 11 ch. II.1 no Fedlex e mapear competências → categorias A-J | P0 | PESQ/Sonnet | T-001 | docs/CURRICULO.md | Cada competência com link Fedlex | DONE parcial: 15/15 itens; lacunas em H, 1.5.1, LCR, OETV |
| T-003 | Mapear regras de Priorité (OCR, OSR) com trecho literal | P0 | PESQ/Sonnet | T-002 | legal/rules/priorite.yaml | Schema SPEC §5 completo | REVIEW (32 regras; corrigir R-PRIO-013/016/019/020/021) |
| T-004 | Script + workflow GitHub Actions que baixa o Fedlex e confere se cada `trecho_literal_fr` existe no texto | P0 | DEV/Haiku | T-001, H-04 | scripts/check_quotes.*, .github/workflows/* | Falha se algum trecho não bater | DONE (Actions: 27 OK, 3 FALHA, 2 sem trecho) |
| H-04 | Luan cria o repo vazio oluanunes/drive-theory (a integração do GitHub não tem permissão para criar) | P0 | Luan | — | — | Repo existe e Claude consegue fazer push | DONE |
| T-005 | Revisão independente das regras de Priorité (exceções, omissões) | P0 | REV/Opus | T-003, T-004 | só comentários em docs/reviews/ | Relatório com veredito por regra | TODO |
| H-02 | Luan valida as regras de Priorité | P0 | Luan | T-005 | — | status → validado | TODO |
| T-006 | ~20 perguntas originais de Priorité (múltipla resposta, níveis 1-4) | P1 | DEV/Sonnet | H-02 | questions/priorite.json | Schema SPEC §5, cada alternativa justificada | TODO |
| T-007 | Revisão independente das perguntas | P1 | REV/Opus | T-006 | docs/reviews/ | Sem ambiguidade nem contradição com regra | TODO |
| H-03 | Luan aprova amostra de perguntas | P1 | Luan | T-007 | — | status → aprovado | TODO |
| T-008 | PWA mínimo: Aprender / Praticar / Erros, offline, progresso local | P2 | DEV/Sonnet | T-001 | app/* | Roda no iPhone; testes passam | TODO |
| H-01 | Luan confirma formato da prova em asa.ch ou no OCN Friburgo | P0 | Luan | — | — | SPEC §3 → confirmado | TODO (não bloqueia até o simulador) |

## Bloqueios abertos
- Trechos literais: WebFetch e shell não leem o Fedlex completo; conferência real só via Actions (T-004, depende de H-04).
- Categoria H sem artigos confirmados: precisa de pesquisa dedicada (T-009, a criar).
- Anexo 11 OAC: confirmar se mudou após 01/01/2026.

## Conflitos abertos
- Nenhum.
