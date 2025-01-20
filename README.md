# Sistema para imobiliária

## Tasks

1. [x] Adicionar colunas para data de criação e data de modificação.
2. [ ] Criar checks e validations em `models.py`.
3. [ ] Criar um `README.md` top.
4. [ ] Criar e melhorar as docstrings, comentários e documentação. (De preferência em inglês, exceto o banco de dados que deve se manter em português).
5. [x] Criar um módulo que permita preencher e exportar em PDF a 'ficha de controle de inquilino' requisitada pelo condomínio. E assim associar estes dados ao seu respectivo aluguel. Acredito que uma nova tabela seja necessária, seriam os dados do inquilino, acompanhantes, veículo, etc.
6. [x] Verificar se realmente há necessidade do offset e limit nas funções de `read_<all>` em `crud.py` ou se fica melhor diretamente no **frontend**.
7. [x] Renomear routes para router e checar os schemas de response.
8. [ ] Adicionar tratamento de erros.
9. [ ] Adicionar logs.
10. [ ] Validação de CEP, CPF, RG, Telefone...
11. [ ] Formato de apresentação de CEP, CPF, RG, Telefone...
12. [ ] Importar forms ou tipos de arquivo (csv/json) para ficha de inquilino.
13. [x] Refazer os models/schemas/crud: Fix nos tipos de dados que estão int para str (cep, cpf, telefone, rg...)
14. [ ] Criar todas as páginas.
15. [ ] Valores default e autocomplete para create.
16. [ ] Ver como é a configuração para aplicar offset e limit das querys no frontend.
17. [ ] Fazer o login direito.
18. [x] Revisar os dfs, dicts, responses, keys e importações no frontend, paginas 1 a 6.
19. [ ] Definir Placeholders nos formulários do frontend páginas 1 a 6. E marcar campos Obrigatórios com um '*'.
20. [x] Tentar recriar as páginas que fazem cálculos para exibição instantânea do resultado, aprendi que não pode ser dentro de um `st.form()`, OU, inserir botão de 'refresh' para recalcular diárias e valor_total, mas também não sei como.
21. [ ] Ver quais funções deveriam ser `async`com `asyncio` estudar e aplicar.
22. [ ] Pegar o subtitulo dos dados ao ter erro como unprocessable content e mostrar os dados que não foram inseridos com o titulo correto
23. [x] Melhor aquele esquema do if update_id... etc
24. [x] A tabela fichas tera um campo para RG ou CPF em vez de dois campos para cada acompanhante (no front pelo menos ta certo).
25. [ ] Colocar valores que se repetem diretamente no pdf e remover do banco de dados (na verdade deixa assim, quando estiver em produção talvez).
26. [x] Na visualização de DataFrames, colocar a coluna id na primeira posição.
27. [x] Reescrever o modo como os 'acompanhantes' são armazenados, array ou json (dict).
28. [ ] Descobrir um jeito de validar a nível do banco de dados os JSON dos acompanhantes.
29. [ ] Descobrir um jeito de reduzir o número de linhas que ocupa o formulário de acompanhantes.
30. [x] Na Page Fichas colocar botão para obter o PDF.
31. [ ] Pedir confirmação antes de deletar um registro.
32. [x] Incluir categorias nos modelos para o banco de dados.
33. [ ] Alterar a forma que o modificar funciona, atualmente está utilizando schemas de update, onde todos os campos são opcionais, mas na verdade como são enviados com put e não com patch, a verificação fica por conta do banco de dados e não é o ideal.

**Pensar em como utilizar o patch para alterações individuais de campos, ainda não vejo muito sentido nisso, mas como estudo pode ser bom.**

**Provavelmente todos os valores monetários eu devesse usar str e depois passar para float no front, aceitando como separador decimal tanto ',' quanto '.'.**

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
- Validar dados com Pydantic
- Backend com FastAPI (inserir, editar, apagar)
- Frontend com Streamlit. Integração com as funções do fastAPI e dataviz
- Gerador de PDF com os dados preenchidos para impressão de fichas dos inquilinos, no mesmo modelo que o exigido pelo condomínio
- Importar dados de forms (ainda não decidi qual, mas creio que do google)

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
