# T-033 — Notas da PESQ (categoria G, legal/rules/danger-securite.yaml)

51 regras (R-DAN-001 a 051), todas `pendente`. Fonte única: legal/sources/*.txt. Validado com yaml.safe_load (ids únicos), `normalize` de scripts/check_quotes.py (51 de 51 trechos presentes, todos os `termos_fr` dentro do trecho) e conferência das alíneas por posição.

## 1. Alíneas incertas (número legal usado, a confirmar no HTML do Fedlex)
- **OCR 41, R-DAN-020 e R-DAN-021.** Por posição, as bandes longitudinales pour piétons são o 4.º parágrafo e a regra das crianças de 12 anos é o 5.º. O OSR 77 al. 3 cita « art. 41, al. 3, OCR » para as bandes, e o OSR 33 cita « art. 41, al. 4 » para o chemin pour piétons. Citei as al. 3 e 4. Isso indica que o 3.º parágrafo (« Le conducteur qui doit emprunter le trottoir… ») é a al. 2bis. Esse parágrafo já está em R-ARR-086 com alinea "3". Ação sugerida: conferir e, se confirmar, corrigir R-ARR-086 para "2bis".
- **OETV 58.** As remissões internas (« al. 6 » para a marque d'identification, « al. 7 » para a marque de réception) ficam uma posição abaixo da contagem por posição. Provavelmente há uma al. 5bis, o parágrafo « La charge nominale… ». O al. 4 (perfil de 1,6 mm, R-DAN-049) não é afetado, e a OETV 119 let. d o confirma.
- **LCR 9.** O preâmbulo da OCR cita « art. 9, al. 1bis, 2 et 3 », então a numeração por posição não é segura além da al. 1. Não criei regra da LCR 9. Os máximos (2,55 m, 4 m) estão em OCR 64 al. 1 e OCR 66 al. 1.
- **OCR 24, 47, 48, 60 e OSR 93.** Têm parágrafos « … » (revogados), contados na posição. Os al. 3 e 4 de OSR 93 e o al. 1 de OCR 60 dependem disso.

## 2. Dúvidas de conteúdo
- **R-DAN-010 (OCR 35 al. 2).** O arquivo diz « 50 cm » (cm³ perdido na extração). Conferir antes de usar o número em perguntas.
- **R-DAN-035 (OCR 73 al. 2).** A lista de exceções a. a d. está em linhas separadas. O trecho é só a primeira frase (`trecho_completo: false`) e a lista está em `regra_pt`.
- **R-DAN-005 (OSR 93 al. 4).** Mesma situação: trecho é a frase de abertura e a lista a. a c. está em `regra_pt`.
- **R-DAN-042 (OCR 66 al. 1).** O fim da linha é « …. » (frase revogada), deixado de fora. O trecho é a primeira frase.
- **R-DAN-041 (OCR 64 al. 1).** O trecho é a primeira frase, porque a segunda é só remissão ao OCR 73 al. 2.
- **R-DAN-014, 023, 025 e 026 (sinais).** São sinais de perigo (OSR 11, 12, 47). Se existir ou for criado um YAML da categoria A com o OSR 4 a 15, pode haver sobreposição. Cruzar antes de validar.
- **OSR 5 e 8 e OSR 21 al. 2.** Na categoria G, só usei OSR 5 al. 1 e OSR 8 al. 1 e 3. OSR 5 al. 2, 8 al. 2 e 21 al. 2 aparecem só como exceções cruzadas.

## 3. Lacunas e itens não criados
- **Fora do escopo por decisão do Luan:** álcool e drogas, telefone, buzina, capacete e condução ecológica.
- **Categoria F:** acidente e pane (OCR 54 a 56, LCR 51, OETV 90 triângulo de pane).
- **Sem regra própria, só citados em exceções:** OCR 32 (luzes de reboque), OCR 43 e 42 al. 1 e 2 (ciclos e motos), LCR 46 e 47, OCR 45 e 48 al. 1 (bonde, carrinhos), OCR 50, 50a e 51 a 53 (cavaleiros e animais conduzidos), OCR 57 a 59, OCR 61 e 63 (transporte de pessoas em veículos de carga e motos), OCR 65, 67, 68, 71, 74, OCR 58 al. 2 e 6, LCR 30 al. 4 e 5 (animais e mercadorias perigosas), OETV 61 al. 2 a 4 e 63. Motivo: o limite de ~50 regras e a baixa relevância para a categoria B.
- **Ônibus escolar:** a única regra é a OCR 6 al. 5 (R-PRIO-036). A OCR 23 al. 3 let. a (pisca-alerta) está em arret-stationnement.yaml.
- **Pneus de inverno:** a OETV 59 al. 3 e 4 só trata de exceção de velocidade. Nenhuma norma das fontes obriga pneus de inverno, e não criei regra sobre isso.
- **Visibilidade e neblina:** o que o texto dá já está em R-COM-036 a 039, R-COM-006 e R-DEP-021. Nada novo.
- **OCR 5 al. 1 let. a ch. 4** (80 km/h com pneus com cravos). A lista é multinível, então só cito em exceção de R-DAN-051.
- **Portarias fora das fontes** (sem inventar): dimensões de veículos específicos, mercadorias perigosas (ADR/SDR), tacógrafo e requisitos de extintor ou triângulo além do OETV 90.
- **Distância de segurança (curr. 1.3.1)** e velocidades máximas já estão em R-DEP-034 a 036 e R-COM. Nada novo na G.
