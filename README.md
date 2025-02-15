# Sistema para imobiliária, um estudo sobre sistemas

Estou trabalhando neste projeto com o objetivo de facilitar o dia-a-dia no trabalho de uma imobiliária. Mas não apenas isso, por enquanto na fase do protótipo eu devo aprender mais sobre Python e algumas bibliotecas (FastAPI, SQLAlchemy, Pydantic, Streamlit e mais), Banco de Dados (PostgreSQL), SQL, Docker (Compose), Git e GitHub (CLI, versionamento, Pull Requests, Issues) e Servidores em rede local (Chaves SSH e Deploy).

O processo deve ser lento, pois este projeto não é prioridade no momento, mas pretendo entregar um protótipo de alta fidelidade e completamente funcional ainda neste trimestre. Para que sejam realizados alguns testes e ajustes.

Novas idéias para funcionalidades vão surgindo de conversas com responsáveis por administração de imóveis. Não tenho um projeto bem elaborado ainda, porém pretendo praticar esta disciplina antes de dart início a primeira versão.

## Problema

A imobiliária deseja um sistema que permita:

- Cadastrar imóvel, o número do apartamento e edifício, incluir se possível o código da celesc, do gás, da internet, Wifi - ID e Senha, senha da fechadura
- Cadastrar proprietário/responsável do imóvel, Nome, CPF, telefone (whatsapp) e e-mail
- Registrar os gastos variáveis e despesas fixas, detalhados, com data e com a nota (se aplicável)
- Registrar aluguel/reserva em um calendário, com valor da diária, valor da taxa de limpeza, valor da taxa de administração/comissão (calculado automaticamente)
- Gerar o relatório descritivo da contabilidade para cada apto, com as datas relacionadas
- Registrar o valor acumulado de cada apto
- Registrar saque dos valores de cada apto (com data, descrição e recibo)

Bônus:

- Integrar com AI para consultar datas disponíveis dos apartamentos, via chat com voz
- Integrar com AI para marcar reservas, via chat com voz
- Registrar as vagas de garagens, vinculadas ao número do apartamento
- Registrar aluguel das vagas de garagem, com o preço por dia, e qual apto ocupará

Mais informações:

- Deve permitir a alteração dos dados, editar ou excluir
- Deve ser possível cancelar reservas
- Não devem haver custos adicionais
- Deve ser compatível com windows 10, fedora41 (linux), iOS 18.1.1 e android 14

## Objetivos

### Protótipo

- [x] A princípio, desenvolver um sistema em rede local para os computadores da imobiliária, utilizando a linguagem Python 3.13
- [x] Configurar o banco de dados PostgreSQL utilizando SQLAlchemy
- [x] Verificar/Validar dados com Pydantic
- [x] Backend com FastAPI (inserir, editar, apagar)
- [x] Frontend com Streamlit. Integração com as funções do fastAPI
- [x] Gerador de PDF com os dados preenchidos para impressão de fichas dos inquilinos, no mesmo modelo que o exigido pelo condomínio
- [x] Importar dados do Google Forms e/ou .csv
- [x] Exibir tabelas (de reservas) mensais com dias como colunas, aptos como linhas, campos preenchidos terão diferença visual para checkin, checkout e dias ocupados. Mais informações, como Contato, valor total e valor já depositado são muito importantes.
- [x] Configurar uma maquina-servidor em rede local e passar o sistema para este servidor.
- [x] Implantar em contêineres utilizando Docker

### Primeira versão

- [ ]Refatorar o código, para melhorar a qualidade.
  - [ ] Legibilidade
  - [ ] Complexidade
  - [ ] Modularidade
  - [ ] Teste
  - [ ] Extensibilidade
- [ ] Revisar:
  - [ ] Confiabilidade
  - [ ] Desempenho
  - [ ] Escalabilidade
  - [ ] Usabilidade
  - [ ] Portabilidade
- [ ] Configurar backup automático do banco de dados
- [ ] Salvar imagem/pdf de recibos ou semelhantes, armazenando os links no banco de dados em uma nova tabela para relacionar com as outras tabelas do banco de dados
- [ ] Permitir alterações com tipo de requisição PATCH diretamente nos DataFrames (Estudar a necessidade)
- [ ] Fazer uma boa documentação

#### Estudos extras

- [ ] (Opcional) Criar banco de dados MongoDB para testar
- [ ] Documentar e orquestrar SQL com o DBT-core
- [ ] Utilizar o briefer

### Segunda versão

- ?? Criar banco de dados vetorial para o funcionamento da IA (ChromeDB?)
- Implementar IA (Groq?)
- Integrar com whatsapp (EvolutionAPI?)

## Tasks do protótipo

1. [x] Adicionar colunas para data de criação e data de modificação.
2. [ ] Criar checks e validations em `models.py`.
3. [x] Criar um `README.md`.
4. [x] Criar um módulo que permita preencher e exportar em PDF a 'ficha de controle de inquilino' requisitada pelo condomínio. E assim associar estes dados ao seu respectivo aluguel. Acredito que uma nova tabela seja necessária, seriam os dados do inquilino, acompanhantes, veículo, etc.
5. [x] Verificar se realmente há necessidade do offset e limit nas funções de `read_<all>` em `crud.py` ou se fica melhor diretamente no **frontend**.
6. [x] Renomear routes para router e checar os schemas de response.
7. [x] Adicionar tratamento de erros.
8. [x] Adicionar logs.
9. [ ] Verificação de CEP, CPF, RG, Telefone...
10. [x] Formato de apresentação e input para Apto, CEP, CPF, RG, Telefone...
11. [x] Importar csv para ficha de inquilino.
12. [x] Refazer os models/schemas/crud: Fix nos tipos de dados que estão int para str (cep, cpf, telefone, rg...)
13. [x] Criar todas as páginas.
14. [ ] Valores default no banco de dados.
15. [ ] Ver como é a configuração para aplicar offset e limit das querys no frontend.
16. [x] Fazer o login direito.
17. [x] Revisar os dfs, dicts, responses, keys e importações no frontend, paginas 1 a 6.
18. [x] Marcar campos Obrigatórios com um '*'.
19. [x] Tentar recriar as páginas que fazem cálculos para exibição instantânea do resultado, aprendi que não pode ser dentro de um `st.form()`.
20. [x] Melhor aquele esquema do if update_id... etc
21. [x] A tabela fichas tera um campo para RG ou CPF em vez de dois campos para cada acompanhante (no front pelo menos ta certo).
22. [x] Na visualização de DataFrames, colocar a coluna id na primeira posição.
23. [x] Reescrever o modo como os 'acompanhantes' são armazenados, array ou json (dict).
24. [ ] Descobrir um jeito de verificar a nível do banco de dados os JSON dos acompanhantes.
25. [x] Descobrir um jeito de reduzir o número de linhas que ocupa o formulário de acompanhantes.
26. [x] Na Page Fichas colocar botão para obter o PDF.
27. [x] Pedir confirmação antes de deletar um registro.
28. [x] Incluir categorias nos modelos para o banco de dados.
29. [x] Alterar a forma que o modificar funciona. Atualmente está utilizando os schemas de update, onde todos os campos são opcionais, mas como são enviados com put e não com patch, todos os campos devem ser enviados (incluindo nulos), o que pode atrapalhar a verificação do schema, ficando por conta do banco de dados e não é o ideal.
30. [ ] Adicionar com cuidado um st.rerun(), somente se um registro for efetuado com sucesso no banco de dados, a intenção é limpar os campos de entrada.
31. [x] Incluir ao sistema o valor já depositado (de uma reserva/aluguel), assim também mostrando o quanto falta (para o valor total). Adicionar para garagens também.
32. [x] Adicionar a página para visualização das tabelas de reservas.
33. [x] Marcar campos obrigatórios. E resaltalos no caso de ausência ao enviar um registro.
34. [x] Incluir ao sistema tabela de registros de pagamentos recebidos referentes aos alugueis.
35. [x] Utilizar variáveis de ambiente (.env) para valores que desejo aplicar automáticamente ao sistema, sem subir para o GitHub.
36. [x] Criar função que sera utilizadas para gerar a planilha com as reservas.
37. [x] Criar trigger para bloquear alugueis de um mesmo apto com datas conflitantes.
38. [x] Usar como primary-key o próprio nome do apartamento, na table apartamentos. E fazer as devidas alterações no restante do projeto.
39. [x] Alterar pagamentos, alugueis e garagens para atender melhor a necessidade de registros precisos.
40. [ ] Placeholders e help no front.
41. [x] Mostrar uma identificação mais amigável ao inserir IDs.
42. [x] Incluir DIC, RIP, Inscrição Imobiliária e Matrícula como colunas dos apartamentos.
43. [x] Utilizar o apto+checkin para encontrar uma ficha.
44. [x] Por conveniência, colunas com nome e contato devem estar na table de alugueis.
45. [x] Consulta de disponibilidade
46. [x] Bloquear overbooking
47. [x] Separar em duas planilhas, para os dois tipos de aptos, conforme as regras de negócio.
48. [x] Adicionar a data na tabela de pagamentos e no restante do sistema.
49. [x] Criar a página para gerar os relatórios.
50. [x] Definir relationships de back_populates em `models.py`, para facilitar as querys.
51. [x] Mostrar se há pagamentos para um aluguel/reserva, qual é o total, quanto foi depositado, quanto falta, se está paga.
52. [x] Configurar Docker para instalar locale e setar com pt-br
53. [ ] Manipular os inputs como nome, etc... com .title, .capitalize, essas coisas para padronização.
54. [ ] Criar uma função para analisar o input em `contato` (Aluguéis e Pagamentos) a fim de verificar se é telefone ou email para incluir na padronização.
55. [x] Adicionar categoria de "Adiantamento" em Despesas para o caso de adiantamento de valores ao proprietário do apartamento.
56. [x] Permitir alterações pelo usuário diretamente nos DataFrames utilizados para gerar Relatórios.
57. [x] Criar os scripts em SQL para inserir os dados de uma vez e testar o banco e o app.
58. [x] Aplicar as mudanças do banco nas páginas do app
59. [x] criar tabela para relatórios, deixar os pagamentos apenas para os depósitos de reserva, parcelas, etc. relacionados aos alugueis.
60. [x] Em despesas criar a categoria para adiantamento de valores destinado aos proprietários.
61. [x] Utilizar o apto+checkin para encontrar uma aluguel.
62. [x] Dar um jeito de interagir com os dataframes (para pesquisas ou mais informações)
63. [x] Adicionar parâmetros de filtro opcionais aos endpoints, para facilitar as consultas.
64. [x] Criar a página inicial, que terá todo tipo de consulta.
65. [x] Configurar uma máquina para ser o servidor na rede local. IP estático e chave SSH.
66. [x] Fazer o Deploy e sincronizar utilizando `rsync`.
67. [x] Mudar o host da API de 0.0.0.0 para o nome do container, com intenção de aumentar um pouco a segurança no protótipo.
68. [ ] Usar índices nas tabelas do banco de dados.
69. [x] Instalar o faker para criar dados fake.
70. [x] Criar script para para inserir dados de teste no banco, com SQLAlchemy.
71. [x] Separar as dependências de cada conteiner e manejar com UV diretamente.
72. [x] Inserir um pequeno delay para iniciar a API, para que espere o DB ficar completamente pronto.
73. [ ] Adicionar registro de cash flow.
