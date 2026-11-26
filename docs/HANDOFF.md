# HANDOFF — DRIVE THEORY SWITZERLAND

Para continuar o projeto em outra ferramenta (ex.: Craft Anything). Atualizado em 2026-11-26.

## Objetivo
PWA em português (termos em francês entre parênteses) para o Luan passar na prova teórica suíça categoria B, em **20/12/2026, Fribourg**. Ensina as regras a partir das fontes oficiais (Fedlex) e treina com perguntas originais (nunca copiadas de ASA/iTheorie).

## Onde está
- Repositório público: https://github.com/oluanunes/drive-theory (branch `main`)
- App publicado (GitHub Pages): publicado a partir de `app/`
- Stack: HTML/CSS/JS puro, service worker, IndexedDB. Sem build, sem dependências. Custo zero.

## Estrutura
- `app/` — o PWA. `app/data/content.json` é GERADO; não editar à mão.
- `legal/sources/` — texto das leis (gerado por GitHub Actions; não editar).
- `legal/rules/*.yaml` — regras (uma por unidade de norma), com trecho literal em francês e fonte.
- `questions/*.json` — perguntas de múltipla resposta.
- `scripts/` — `build_data.py` (gera content.json), `check_questions.py`, `check_quotes.py`, testes.
- `docs/` — SPEC, BOARD (estado das tarefas), DECISIONS, SOURCES, GLOSSARIO, `reviews/` (revisões independentes).
- `.github/workflows/` — check-quotes (confere trechos contra o Fedlex), fetch-laws, pages.

## Regras do projeto (não quebrar)
1. Todo `trecho_literal_fr` tem de bater com o texto oficial (o workflow check-quotes confere).
2. Só entram no app regras `validado` e perguntas `aprovado` cujas regras estejam todas validadas.
3. Autor ≠ revisor: cada bloco passou por revisão independente antes da validação.
4. A validação e a aprovação atuais foram **delegadas pelo Luan a Claude** (campos `validado_por` / `aprovado_por`); o Luan confere pelo app (aba "Revisão" → "Copiar lista") e manda os erros.
5. Perguntas: múltipla resposta, enunciado "Quais afirmações estão corretas?", sem vazar quantas marcar, correta nem sempre a primeira nem a mais longa, justificativa por alternativa com artigo/alínea.
6. Fora do escopo (decisão do Luan): álcool/drogas, telefone, buzina, capacete, condução ecológica.

## Estado (resumo)
- Regras validadas: Priorité 56, Arrêt & stationnement 87/88 (R-ARR-076 pendente: tabela da zona azul, confirmar no Fedlex), Dépassement 73, Comportement 57.
- Perguntas aprovadas: 108 (Priorité 36, Arrêt 24, Dépassement 24, Comportement 24).
- Em andamento: categorias A (Panneaux), F (Accidents & pannes), G (Danger/sécurité); H (sistemas de assistência) ainda sem pesquisa.
- Aberto: formato da prova (Luan confirma com o OCN Fribourg; provisório: 50 perguntas, 45 min, reprova com >15 pontos de erro); simulador e repetição espaçada.

## Atenção
- A ferramenta nova provavelmente não executa os agentes/revisores nem os workflows daqui. Sem eles, a conferência dos trechos legais (item 1) e a revisão independente (item 3) precisam ser refeitas à mão ou por outro meio.
- Numeração de alíneas com al. bis/ter e linhas « et … » nas fontes precisa de conferência no HTML do Fedlex.
