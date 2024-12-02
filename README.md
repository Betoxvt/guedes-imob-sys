# Sistema para imobiliária

## Problema

A imobiliária deseja um sistema que permita:
- Cadastrar imóvel, o número do apartamento e edifício, incluir se possível o codigo da celesc, do gás, da internet, Wifi - ID e Senha, senha da fechadura
- Cadastrar proprietário/responsável do imóvel, Nome, CPF, telefone (whatsapp) e e-mail
- Registrar os gastos variáveis e despesas fixas, detalhados, com data e com a nota (se aplicável)
- Registrar aluguel/reserva em um calendário, com valor da diária, valor da taxa de limpeza, valor da taxa de administração/comissão (calculado automáticamente)
- Gerar o relatório descritivo da contabilidade para cada apto, com as datas relacionadas
- Registrar o valor acumulado de cada apto
- Registrar saque dos valores de cada apto (com data, descrição e recibo)

Bônus:
- Integrar com AI para consultar datas disponíveis dos apartamentos, via chat com voz
- Integrar com AI para marcar reservas, via char com voz
- Registrar as vagas de garagens, vinculadas ao número do apartamento
- Registrar aluguel das vagas de garagem, com o preço por dia, e qual apto ocupará

Mais informações:
- Deve permitir a alteração dos dados, editar ou excluir
- Deve ser possível cancelar reservas
- Não devem haver custos adicionais
- Deve ser compatível com windows 10, fedora41 (linux), iOS 18.1.1 e android 14

## Objetivos

### Primeira versão

- A princípio, desenvolver um sistema em rede local para os computadores da imobiliária, utilizando a linguagem Python 3.13
- Configurar o banco de dados SQLite utilizando o SQLModel (SQLAlchemy + Pydantic)
- Backend com FastAPI
- Frontend com Streamlit
- Produção em conteineres com Kubernetes

## Banco de dados

### Tabela apartamentos

- Coluna apartamento [TEXT]: O apartamento é identificado com o bloco+número, por exemplo A251. (primary key)
- Coluna edificio [TEXT]: O nome do edifício em que o apartamento está inserido
- Coluna endereco [TEXT]: Endereço do edifício
- Coluna celesc [INTEGER]: Código da unidade consumidora
- Coluna supergasbras [INTEGER]: Código da unidade consumidora
- Coluna internet [TEXT]: Provedor de internet
- Coluna wifiid [TEXT]: Identificação da rede wireless
- Coluna wifipass [TEXT]: Senha da rede wifi
- Coluna lockpass [INTEGER]: Senha da fechadura
- Coluna proprietario [INTEGER]: cpf do proprietário (foreign-key - proprietarios)

### Tabela proprietarios

- Coluna cpf [INTEGER]: cpf do proprietário ou documento de estrangeiro
- Coluna nome [TEXT]: nome do proprietário
- Coluna telefone [INTEGER]: número do telefone, preferenciávelmente whatsapp, do proprietário
- Coluna email [TEXT]: endereço de email do proprietário
- Coluna apto1 [TEXT]: número do apto do proprietário (foreign-key - apartamentos)
- Coluna apto2 [TEXT]: número do apto do proprietário (foreign-key - apartamentos)
- Coluna apto3 [TEXT]: número do apto do proprietário (foreign-key - apartamentos)
- Coluna apto4 [TEXT]: número do apto do proprietário (foreign-key - apartamentos)

### Tabela despesas_fixas

- Coluna id [INTEGER]: identificação única (primary-key)
- Coluna data_pagamento [TEXT]: ISO8601 ("YYYY-MM-DD") do pagamento
- Coluna valor [REAL]: em reais da conta
- Coluna tipo_despesa [TEXT]: iptu, condominio, gas, luz, internet...
- Coluna apto [TEXT]: número do apto (foreign-key - apartamentos)

### Tabela gastos_variaveis

- Coluna id [INTEGER]: identificação única (primary-key)
- Coluna data_pagamento [TEXT]: ISO8601 ("YYYY-MM-DD") do pagamento
- Coluna valor_material [REAL]: custo com materiais, peças, etc.
- Coluna valor_mo [REAL]: custo com mão-de-obra
- Coluna valor_total [REAL]: custo total do gasto em reais
- Coluna descricao [TEXT]: breve descrição do gasto
- Coluna apto [TEXT]: número do apto (foreign-key - apartamentos)

### Tabela alugueis

- Coluna id [INTEGER]: identificação única (primary-key)
- Coluna checkin [TEXT]: ISO8601 ("YYYY-MM-DD")
- Coluna checkout [TEXT]: ISO8601 ("YYYY-MM-DD")
- Coluna diarias [INTEGER]: quantidade de dias checkout - checkin (JULIANDAYS)
- Coluna valor_diaria [REAL]: preço em reais da diária
- Coluna taxa_adm [REAL]: percentual retido pela imobiliaria
- Coluna valor_total [REAL]: diarias * valor_diária
- Coluna valor_imob [REAL]: valor_total * taxa_adm
- Coluna valor_prop [REAL]: valor_total - valor_imob
- Coluna apto [TEXT]: número do apto (foreign-key - apartamentos)

### Tabela garagens

- Coluna id [INTEGER]: identificação única (primary-key)
- Coluna checkin [TEXT]: ISO8601 ("YYYY-MM-DD")
- Coluna checkout [TEXT]: ISO8601 ("YYYY-MM-DD")
- Coluna diarias [INTEGER]: quantidade de dias checkout - checkin (JULIANDAYS)
- Coluna valor_diaria [REAL]: preço em reais da diária
- Coluna taxa_adm [REAL]: percentual retido pela imobiliaria
- Coluna valor_total [REAL]: diarias * valor_diária
- Coluna valor_imob [REAL]: valor_total * taxa_adm
- Coluna valor_prop [REAL]: valor_total - valor_imob
- Coluna apto_destino [TEXT]: apto para qual a vaga foi alugada (foreign-key - apartamentos)
- Coluna apto_origem [TEXT]: apto proprietário da vaga (foreign-key - apartamentos)


