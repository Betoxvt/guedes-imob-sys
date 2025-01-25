# Sistema para imobiliária, um estudo sobre sistemas

## Tasks

1. [x] Adicionar colunas para data de criação e data de modificação.
2. [ ] Criar checks e validations em `models.py`.
3. [ ] Criar um `README.md` top.
4. [ ] Criar e melhorar as docstrings, comentários e documentação. (De preferência em inglês, exceto o banco de dados que deve se manter em português).
5. [x] Criar um módulo que permita preencher e exportar em PDF a 'ficha de controle de inquilino' requisitada pelo condomínio. E assim associar estes dados ao seu respectivo aluguel. Acredito que uma nova tabela seja necessária, seriam os dados do inquilino, acompanhantes, veículo, etc.
6. [x] Verificar se realmente há necessidade do offset e limit nas funções de `read_<all>` em `crud.py` ou se fica melhor diretamente no **frontend**.
7. [x] Renomear routes para router e checar os schemas de response.
8. [x] Adicionar tratamento de erros.
9. [x] Adicionar logs.
10. [ ] Verificação de CEP, CPF, RG, Telefone...
11. [x] Formato de apresentação e input para Apto, CEP, CPF, RG, Telefone...
12. [x] Importar csv para ficha de inquilino.
13. [x] Refazer os models/schemas/crud: Fix nos tipos de dados que estão int para str (cep, cpf, telefone, rg...)
14. [x] Criar todas as páginas.
15. [ ] Valores default e autocomplete para create, pode se extender às **task 25** e **task 40**.
16. [ ] Ver como é a configuração para aplicar offset e limit das querys no frontend.
17. [ ] Fazer o login direito.
18. [x] Revisar os dfs, dicts, responses, keys e importações no frontend, paginas 1 a 6.
19. [x] Marcar campos Obrigatórios com um '*'.
20. [x] Tentar recriar as páginas que fazem cálculos para exibição instantânea do resultado, aprendi que não pode ser dentro de um `st.form()`.
21. [ ] Ver quais funções deveriam ser `async`com `asyncio` estudar e aplicar.
22. [ ] Reduzir as repetições de código com funções e decoradores.
23. [x] Melhor aquele esquema do if update_id... etc
24. [x] A tabela fichas tera um campo para RG ou CPF em vez de dois campos para cada acompanhante (no front pelo menos ta certo).
25. [ ] Colocar valores que se repetem diretamente no pdf e remover do banco de dados (na verdade deixa assim, quando estiver em produção talvez).
26. [x] Na visualização de DataFrames, colocar a coluna id na primeira posição.
27. [x] Reescrever o modo como os 'acompanhantes' são armazenados, array ou json (dict).
28. [ ] Descobrir um jeito de verificar a nível do banco de dados os JSON dos acompanhantes.
29. [x] Descobrir um jeito de reduzir o número de linhas que ocupa o formulário de acompanhantes.
30. [x] Na Page Fichas colocar botão para obter o PDF.
31. [x] Pedir confirmação antes de deletar um registro.
32. [x] Incluir categorias nos modelos para o banco de dados.
33. [x] Alterar a forma que o modificar funciona. Atualmente está utilizando os schemas de update, onde todos os campos são opcionais, mas como são enviados com put e não com patch, todos os campos devem ser enviados (incluindo nulos), o que pode atrapalhar a verificação do schema, ficando por conta do banco de dados e não é o ideal.
34. [ ] Adicionar com cuidado um st.rerun(), somente se um registro for efetuado com sucesso no banco de dados, a intenção é limpar os campos de entrada.
35. [x] Incluir ao sistema o valor já depositado (de uma reserva/aluguel), assim também mostrando o quanto falta (para o valor total). Adicionar para garagens também.
36. [x] Adicionar a página para visualização das tabelas de reservas.
37. [x] Marcar campos obrigatórios. E resaltalos no caso de ausência ao enviar um registro.
38. [x] Incluir ao sistema tabela de registros de pagamentos recebidos referentes aos alugueis.
39. [ ] Criar as views (com dbt?) que serão utilizadas nos relatórios.
40. [ ] Utilizar variáveis de ambiente (.env) para valores que desejo aplicar automáticamente ao sistema, sem subir para o GitHub.
41. [x] Criar função que sera utilizadas para gerar a planilha com as reservas.
42. [x] Criar trigger para bloquear alugueis de um mesmo apto com datas conflitantes.
43. [x] Usar como primary-key o próprio nome do apartamento, na table apartamentos. E fazer as devidas alterações no restante do projeto.
44. [x] Alterar pagamentos, alugueis e garagens para atender melhor a necessidade de registros precisos.
45. [ ] Placeholders e help.
46. [x] Mostrar uma identificação mais amigável ao inserir IDs.
47. [x] Incluir DIC, RIP, Inscrição Imobiliária e Matrícula como colunas dos apartamentos.
48. [ ] Utilizar o apto+checkin para encontrar uma ficha.
49. [x] Por conveniência, colunas com nome e contato devem estar na table de alugueis.
50. [x] Consulta de disponibilidade
51. [x] Bloquear overbooking
52. [x] Separar em duas planilhas, para os dois tipos de aptos, conforme as regras de negócio.
53. [x] Adicionar a data na tabela de pagamentos e no restante do sistema.
54. [ ] Criar a página para gerar os relatórios.
55. [ ] Definir relations em `models.py`
56. [ ] Mostrar se há depositos para uma reserva, qual é o total, quanto foi depositado, quanto falta, se está paga.
57. [x] Configurar Docker para instalar locale e setar com pt-br

**Pensar em como utilizar o patch para alterações individuais de campos, ainda não vejo muito sentido nisso, mas como estudo pode ser bom.**
**Agora até vejo que pode ser útil para atualizar os valores depositados para cada aluguel, e o valores entregues para os proprietarios**

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

- A princípio, desenvolver um sistema em rede local para os computadores da imobiliária, utilizando a linguagem Python 3.13
- Configurar o banco de dados PostgreSQL utilizando SQLAlchemy
- Verificar/Validar dados com Pydantic
- Backend com FastAPI (inserir, editar, apagar)
- Frontend com Streamlit. Integração com as funções do fastAPI
- Gerador de PDF com os dados preenchidos para impressão de fichas dos inquilinos, no mesmo modelo que o exigido pelo condomínio
- Importar dados do Google Forms e/ou .csv
- Exibir tabelas (de reservas) mensais com dias como colunas, aptos como linhas, campos preenchidos terão diferença visual para checkin, checkout e dias ocupados. Mais informações, como Contato, valor total e valor já depositado são muito importantes.

### Primeira versão

- Criar banco de dados MongoDB para testar
- Configurar backup automático dos bancos de dados
- Implantar em contêineres utilizando Docker
- Documentar e orquestrar SQL com o DBT-core
- Aproveitar para utilizar o briefer

### Segunda versão

- Criar banco de dados vetorial para o funcionamento da IA (ChromeDB?)
- Implementar IA (Groq?)
- Integrar com whatsapp (EvolutionAPI?)
