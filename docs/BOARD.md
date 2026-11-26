# BOARD — quadro de tarefas

Orquestrador: Claude (conversa principal). Máx. 3 subagentes simultâneos, sem subagente criando subagente.
Papéis: PESQ (pesquisa legal), DEV (desenvolvimento e testes), REV (revisor independente).
Modelos: Haiku = mecânico · Sonnet = pesquisa, redação, código · Opus = revisão e casos com exceções · Fable = só com aprovação.
Prioridade: P0 base legal · P1 perguntas · P2 interface · P3 extras.
Status: TODO · DOING · BLOCKED · REVIEW · WAITING-LUAN · DONE
Regra de bloqueio: 2 falhas na mesma tarefa → para e vai para o Luan com a causa.

## Calendário-alvo (PROVA: 20/12/2026 em Fribourg; escopo completo — D-006)
| Período | Marco |
|---|---|
| 26-27/11 | Fundação, currículo, checagem automática, textos legais no repo |
| 27/11-01/12 | Priorité validada + perguntas + PWA mínimo no iPhone |
| 02/12-15/12 | Esteira: categorias A, B, C, E, F, G, H em pares (~3 dias por par) + Erros/revisão espaçada/simulado |
| 16-17/12 | Últimas correções |
| 17/12 (noite) | CONGELAMENTO: nada novo, só estudo |
| 18-19/12 | Simulados (app + iTheorie) |
| 20/12 | Prova |

Gargalo previsto: validação do Luan (~30-45 min por tema, ~5-6 h no total até 15/12).

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
| T-008 | PWA mínimo: Aprender / Praticar / Erros, offline, progresso local | P2 | DEV/Sonnet | T-001 | app/*, scripts/build_data.py | Roda no iPhone; testes passam | DONE no código (17 testes; Chromium). Falta: H-05 (ativar Pages) e teste no iPhone |
| T-011 | Corrigir/completar regras de Priorité com o texto completo de legal/sources/ | P0 | PESQ/Sonnet | H-05 | Luan ativa o GitHub Pages: repo → Settings → Pages → Source: GitHub Actions | P2 | Luan | T-008 | — | App abre em https://oluanunes.github.io/drive-theory/ | WAITING-LUAN |
| T-005b | T-005 retomada após limite de uso (Opus) | P0 | REV/Opus | T-011 | docs/reviews/T-005-priorite.md | Relatório completo | DOING |
| T-010 | legal/rules/priorite.yaml | 0 trechos não encontrados | DONE (46 regras, 46 OK no Actions) |
| T-010 | Workflow fetch-laws: textos completos LCR/OCR/OSR/OAC/OETV em legal/sources/ | P0 | Orquestrador | T-004 | scripts/fetch_laws.py, .github/workflows/fetch-laws.yml | 5 leis salvas com versão e URL | DONE |
| H-01 | Luan confirma formato da prova em asa.ch ou no OCN Friburgo | P0 | Luan | — | — | SPEC §3 → confirmado | TODO (não bloqueia até o simulador) |

## Bloqueios abertos
- (resolvido) Trechos literais: leis completas agora em legal/sources/ via Actions (T-010).
- Categoria H sem artigos confirmados: precisa de pesquisa dedicada (T-009, a criar).
- Anexo 11 OAC: confirmar se mudou após 01/01/2026.

## Conflitos abertos
- Nenhum.
