# DECISIONS — registro de decisões

| ID | Data | Decisão | Por quê | Quem |
|---|---|---|---|---|
| D-001 | 2026-11-26 | Opção C: construir o DRIVE THEORY direto, sem NEXUS como software. As funções de orquestração ficam com o Claude na conversa principal, com o estado em docs/ e Git | Avaliação /CONSTRAINTS + /RISK + /FAILURE + /DECISION: o NEXUS duplicaria o que o Claude Code já faz e atrasaria o app; o uso programático por assinatura é incerto | Luan |
| D-002 | 2026-11-26 | Máx. 3 subagentes simultâneos, 3 papéis (PESQ, DEV, REV), sem subagente criando subagente; modelo escolhido por tarefa | Limitar custo e contradições | Luan |
| D-003 | 2026-11-26 | Revisor sempre diferente do autor; "validado" só com OK do Luan | PDF NEXUS regra 11; PDF PROJETO §2 | Luan |
| D-004 | 2026-11-26 | PWA + GitHub Pages, custo zero, repositório público oluanunes/drive-theory (Pages gratuito exige repo público) | Funciona no iPhone sem App Store nem conta paga | Luan |
| D-005 | 2026-11-26 | ~~Escopo reduzido até o exame~~ REJEITADA | — | Luan |
| D-006 | 2026-11-26 | Escopo completo (categorias A-J) até o exame. A regra de qualidade não muda: só entra no treino o que tiver fonte conferida e o OK do Luan; o resto fica visível como "pendente" | Pedido do Luan; precisão jurídica continua prioridade 1 | Luan |
| D-007 | 2026-11-26 | A checagem de citações (T-004) roda no GitHub Actions, que baixa o texto do Fedlex. O workspace do Claude não acessa fedlex.admin.ch | Proxy recusou fedlex.admin.ch e fedlex.data.admin.ch (403); Actions é gratuito em repo público | Orquestrador |
