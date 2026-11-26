# T-022 PESQ — notas da categoria C (legal/rules/comportement.yaml)

51 regras (R-COM-001 a 051), todas `pendente`. Fonte única: legal/sources/*.txt. Nada da web.

## Artigos cobertos
LCR 10 (al. 1, 2, 4), 11 (al. 3), 26 (al. 1, 2), 31 (al. 1, 2, 3), 32 (al. 1), 41 (al. 1, 5), 42 (al. 1). OCR 2 (al. 1, 2, 4, 5), 2a (al. 1, 3 let. a, b, c), 3 (al. 1, 3), 3a (al. 1 a 4), 4a (al. 1 a 6), 5 (al. 2 let. c, 4, 5), 17 (al. 4), 30 (al. 1 a 4), 33 (al. 1), 34 (al. 1 a 3). OSR 22 (al. 1), 22a, 22b (al. 2), 23 (al. 1). OAC 71 (al. 5).

## Decisões de método
- Listas a./b. em linhas separadas: copiada só a frase de abertura (ou uma linha da lista), `trecho_completo: false`; os itens vão em `regra_pt`, na ordem do texto.
- Alíneas por posição no arquivo, com uma exceção: LCR 31 "al. 3" é o 5.º parágrafo (os 3.º e 4.º são as al. 2bis e 2ter, confirmado pela remissão no cabeçalho do OCR 2a). Usei o número legal e expliquei na `nota` de R-COM-005. Um revisor que conte só por posição vai achar "5"; peço que confira com o HTML do Fedlex.
- Não dupliquei: OCR 4 al. 1 e OCR 12 (R-DEP-021, 034 a 036), OCR 28, LCR 27, LCR 33 al. 2, OCR 3 al. 4, OCR 17 al. 1 a 3 e 5, OCR 30 al. 5, OCR 31, LCR 41 al. 2, OSR 22b al. 1. Citados por id em `excecoes`.

## Lacunas e dúvidas
1. **Limite geral de álcool (outros condutores).** O OCR 2a só define "influência do álcool" (0,05 mg/l; 0,10 por mil) dentro do artigo que proíbe o álcool para certos grupos (inclui cursos de aprendizagem e permis à l'essai). O LCR 31 al. 2ter e o LCR 55 al. 6 remetem a uma ordonnance da Assemblée fédérale para os limites gerais (estado de ébriété); esse texto (RS 741.13) não está em legal/sources. Não escrevi regra do limite geral nem do "0,5 por mil". Precisa de nova fonte.
2. **Drogas.** OCR 2 al. 2 lista as substâncias (let. a a g) sem concentração; remete a diretivas do OFROU (al. 3, não incluída). Nenhum valor numérico incluído.
3. **Telefone.** Nenhum artigo carregado diz "téléphone" ou "mains libres". O que existe é o OCR 3 al. 1 (« système d'information ou de communication », « appareil reproducteur de son »). Perguntas sobre celular no volante só podem se apoiar nessa frase, sem acrescentar proibição ou multa. A OETV (741.41) não foi pesquisada a fundo (571 KB) para dispositivos viva-voz.
4. **OCR 4 al. 5 (allure trop réduite).** A frase "Il est tenu de ne pas diminuer la fluidité du trafic en circulant, sans raison impérieuse, à une allure trop réduite" é a última do OCR 4, mas a numeração (« et … » / « … » antes dela) é incerta (T-020 já levantou). Não criei regra; confirmar a numeração no Fedlex antes. R-DEP-021 cobre só a al. 1.
5. **OCR 5 al. 1 e al. 2 let. a e b.** Listas multinível (80/60/40/30 km/h por tipo de veículo, pneus com pregos, reboques) com subitens numerados em linhas separadas. Só entrou a let. c do al. 2 (automóvel ligeiro com reboque até 3,5 t, 100 km/h em autoestradas/semiautoestradas). Os 80 km/h para veículos com pneus com pregos (OCR 5 al. 1 let. a ch. 4) e os 40 km/h de reboque (let. c ch. 1) podem aparecer em prova de cat. B e ficaram de fora por não haver trecho de uma só linha com o limite junto. Sugestão: tarefa específica.
6. **Sinais de aviso e luzes de aviso.** OCR 29 e LCR 40 (buzina, sinais óticos) e o uso de luzes de emergência: o CURRICULO.md põe OCR 28 a 32 na categoria A. Não incluí OCR 29/LCR 40. Decidir quem cobre.
7. **Capacete (OCR 3b)** e ônibus (OCR 3 al. 2): fora do escopo cat. B; omitidos. OCR 3a al. 3 (ônibus/minibus) foi incluído por mencionar o cinto.
8. **Condução ecológica (item 1.2.3).** O texto das fontes só dá OCR 33 e 34 (ruído, motor parado, fumaça, aceleração e rotação). Não há « roulement en poussée » nem « marche la plus haute possible » nas fontes; não inventei. Item 1.2.3 do currículo fica parcialmente coberto.
9. **Distância de segurança.** Só o OCR 12 al. 1 (« distance suffisante ») e o OCR 4 al. 1 (parar na distância visível), ambos já em R-DEP. O texto não fixa metros nem segundos; nenhuma regra dos « 2 segundos » foi escrita.
10. **Item 1.5.1 (documentos).** Coberto por LCR 10 al. 1, 2, 4, LCR 11 al. 3 e OAC 71 al. 5 (portar o original do permis de circulation). Não li o OAC 5 (exceções à obrigação de ter permis) nem o OAC 24g além do primeiro parágrafo; ficam citados como "outra disposição". As condições para emitir o permis de circulation (OAC 71 al. 1, LCR 11 al. 1 e 2) não entraram: não são regra de conduta do condutor.
11. **Ebriedade para o aluno de cat. B em curso de aprendizagem.** O OCR 2a al. 1 let. f e g cobrem condutores e acompanhantes em cursos de aprendizagem, e let. h o permis à l'essai (com exceção das categorias especiais F, G e M). Pode haver outras regras sobre o permis à l'essai na OAC (não lidas).
12. **OSR 22b al. 2 (20 km/h).** Relacionada ao R-PRIO-054 (OSR 22b al. 1), que está em prioridade; mantida em C por ser velocidade.
13. **Traduções a conferir.** « infirmes » (pessoas inválidas/com deficiência), « chariots à moteur » (carros a motor), « permis de conduire à l'essai » (carta à prova), « allure du pas » (velocidade de passo). Sugiro entrada no GLOSSARIO.md.
