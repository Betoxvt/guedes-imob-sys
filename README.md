# Sistema para imobiliária

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

### Primeira versão

- Criar banco de dados MongoDB para armazenar imagens ou PDFs de recibos, notas, contratos e serviços
- Configurar backup automático dos bancos de dados
- Implantar em contêineres utilizando Docker
- Documentar e orquestrar SQL com o DBT-core
- Aproveitar para utilizar o briefer

### Segunda versão

- Criar banco de dados vetorial para o funcionamento da IA (ChromeDB?)
- Implementar IA (Groq?)
- Integrar com whatsapp (EvolutionAPI?)

