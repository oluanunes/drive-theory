# DRIVE THEORY SWITZERLAND — SPEC v0.1

Fonte: PDFs "PROJETO" e "NEURAL ORCHESTRATOR" (Luan, 2026-11-26). Abordagem: opção C (ver DECISIONS.md D-001).

## 1. Objetivo
Ajudar o Luan a passar no exame teórico de base, categoria B, até o fim de dezembro de 2026, entendendo as regras em vez de decorar respostas.

Ordem de prioridade (do PDF): precisão jurídica > cobertura do currículo > clareza didática > qualidade das perguntas > diagnóstico de dificuldades > aprendizagem efetiva > simulação realista > interface.

## 2. Prazo e escopo real
- Hoje: 2026-11-26. Exame: até 2026-12-31. São cerca de 5 semanas.
- Até o exame NÃO é possível cobrir as 10 categorias com base legal validada. Escopo até o exame:
  - Temas priorizados pelas dificuldades do Luan (Priorité primeiro).
  - O iTheorie continua sendo usado para simulados com as perguntas oficiais da ASA e para cobrir o que o app ainda não tem.
- Depois do exame, a expansão (Fase 5) continua só se o Luan quiser.

## 3. Formato da prova (para o simulador)
| Item | Valor | Status |
|---|---|---|
| Perguntas | 50, resposta múltipla (mais de uma alternativa pode estar certa) | Fontes secundárias (comparis.ch e outras). Confirmar em asa.ch: PORTÃO H-01 |
| Pontos | 3 por resposta totalmente correta, máximo 150 | idem |
| Reprovação | mais de 15 pontos de erro | idem |
| Tempo | 45 min | idem |
| Base legal do conteúdo | OAC (RS 741.51) art. 13 e anexo 11, ch. II.1 | Ler no Fedlex (tarefa T-002) |

## 4. Fontes (hierarquia do PDF)
1. Fedlex: LCR (RS 741.01), OCR (RS 741.11), OSR (RS 741.21), OAC (RS 741.51), OETV (RS 741.41)
2. OFROU/ASTRA  3. asa  4. Serviços cantonais (OCN Friburgo)  5. Material oficial de formação
6. Escolas de condução reconhecidas: só complementar  7. Outras: só como secundárias, identificadas
Proibido como base legal: blogs, fóruns, Reddit, sites de quiz, conteúdo gerado por IA.

## 5. Modelo de dados

### Regra (`legal/rules/<tema>.yaml`)
```yaml
id: R-PRIO-001
categoria: D-Priorite
subtema: priorite-de-droite
regra_pt: "Texto simples em português"
termos_fr: ["priorité de droite"]
fonte: { lei: OCR, rs: "741.11", artigo: "36", alinea: "2", url: "https://www.fedlex.admin.ch/..." }
trecho_literal_fr: "copiado do Fedlex, sem alteração"
excecoes: []
versao_lei_em_vigor_desde: "AAAA-MM-DD"
verificado_em: "AAAA-MM-DD"
status: pendente | revisado_ia | validado   # 'validado' só com OK do Luan
```

### Pergunta (`questions/<tema>.json`)
- id, regra_ids[], categoria, subtema, competencia, nivel (1-5)
- enunciado, imagem (opcional, diagrama SVG próprio)
- alternativas[] com {texto, correta: bool, justificativa}
- explicacao: {regra_simples, por_que, como_identificar, erro_comum, excecao, palavras_fr}
- etiqueta: legislacao_verificada | questao_original | cenario_pratico | verificacao_pendente
- status: rascunho | revisado_ia | aprovado
- Nunca rotular como "Pergunta oficial ASA". Nunca copiar o catálogo da ASA nem o do iTheorie.

Regra de ouro: uma pergunta só entra no treino se todas as regras dela estiverem `validado` e a pergunta estiver `aprovado`.

## 6. App (stack)
- PWA (HTML, CSS e JS sem framework pesado), instalável no iPhone pelo Safari ("Adicionar à Tela de Início"), funciona offline.
- Dados: JSON gerado a partir das regras e perguntas validadas. Progresso no IndexedDB do aparelho.
- Hospedagem: GitHub Pages (gratuito). Custo total: CHF 0. Sem App Store, sem conta Apple de desenvolvedor.
- Dark mode padrão, interface em português, termos em francês entre parênteses.

## 7. Modos (por fase)
Fase 3: Aprender, Praticar, Erros.  Fase 4: Revisão espaçada, Simulado (formato da seção 3).  Depois: Desafios, Professor de IA (só com base validada; se não souber: "Não tenho fonte verificada para confirmar essa regra. Não vou inventar.").

## 8. Fora do escopo até o exame
NEXUS como software, dashboard de agentes, app nativo, sincronização entre aparelhos, imagens geradas por IA.
