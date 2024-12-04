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
- Configurar o banco de dados PostgreSQL utilizando SQLAlchemy + Pydantic
- Backend com FastAPI
- Frontend com Streamlit

### Primeira versão

- Criar banco de dados MongoDB para armazenar imagens ou PDFs de recibos, notas, contratos e serviços
- Implantar em contêineres utilizando Kubernetes
- Documentar com o DBT-core

### Segunda versão

- Criar banco de dados vetorial para o funcionamento da IA
- Implementar IA

## Banco de Dados imob.db

### Tabela alugueis

- Coluna id [SERIAL]: identificação única (primary-key)
- Coluna checkin [DATE]: dia que entra o hóspede
- Coluna checkout [DATE]: dia que sai o hóspede
- Coluna diarias [INTEGER]: quantidade de dias checkout - checkin
- Coluna valor_diaria [NUMERIC(10, 2)]: preço em reais da diária
- Coluna taxa_adm [NUMERIC(10, 2)]: percentual retido pela imobiliária
- Coluna valor_total [NUMERIC(10, 2)]: diarias * valor_diária
- Coluna valor_imob [NUMERIC(10, 2)]: valor_total * taxa_adm
- Coluna valor_prop [NUMERIC(10, 2)]: valor_total - valor_imob
- Coluna apto [VARCHAR(10)]: número do apto (foreign-key - apartamentos)

### Tabela apartamentos

- Coluna apto [VARCHAR(10)]: O apartamento é identificado com o bloco+número, por exemplo A251. (primary-key)
- Coluna edificio [TEXT]: O nome do edifício em que o apartamento está inserido
- Coluna endereco [TEXT]: Endereço do edifício
- Coluna celesc [INTEGER]: Código da unidade consumidora
- Coluna supergasbras [INTEGER]: Código da unidade consumidora
- Coluna internet [TEXT]: Provedor de internet
- Coluna wifiid [TEXT]: Identificação da rede wireless
- Coluna wifipass [TEXT]: Senha da rede wifi
- Coluna lockpass [INTEGER]: Senha da fechadura
- Coluna proprietario [BIGINT]: cpf do proprietário (foreign-key - proprietarios)

### Tabela despesas_fixas

- Coluna id [INTEGER]: identificação única (primary-key)
- Coluna data_pagamento [DATE]: data do pagamento
- Coluna valor [NUMERIC(10, 2)]: em reais da conta
- Coluna descricao [TEXT]: iptu, condominio, gás, luz, internet...
- Coluna apto [VARCHAR(10)]: número do apto (foreign-key - apartamentos)

### Tabela garagens

- Coluna id [SERIAL]: identificação única (primary-key)
- Coluna checkin [DATE]: dia que entra o hóspede
- Coluna checkout [DATE]: dia que sai o hóspede
- Coluna diarias [INTEGER]: quantidade de dias checkout - checkin
- Coluna valor_diaria [NUMERIC(10, 2)]: preço em reais da diária
- Coluna taxa_adm [NUMERIC(10, 2)]: percentual retido pela imobiliária
- Coluna valor_total [NUMERIC(10, 2)]: diarias * valor_diária
- Coluna valor_imob [NUMERIC(10, 2)]: valor_total * taxa_adm
- Coluna valor_prop [NUMERIC(10, 2)]: valor_total - valor_imob
- Coluna apto_destino [VARCHAR(10)]: apto para qual a vaga foi alugada (foreign-key - apartamentos)
- Coluna apto_origem [VARCHAR(10)]: apto proprietário da vaga (foreign-key - apartamentos)

### Tabela gastos_variaveis

- Coluna id [INTEGER]: identificação única (primary-key)
- Coluna data_pagamento [DATE]: data do pagamento
- Coluna valor_material [NUMERIC(10, 2)]: custo com materiais, peças, etc.
- Coluna valor_mo [NUMERIC(10, 2)]: custo com mão-de-obra
- Coluna valor_total [NUMERIC(10, 2)]: custo total do gasto em reais
- Coluna descricao [TEXT]: breve descrição do gasto
- Coluna apto [VARCHAR(10)]: número do apto (foreign-key - apartamentos)

### Tabela proprietarios

- Coluna cpf [BIGINT]: cpf do proprietário ou documento de estrangeiro (primary-key)
- Coluna nome [TEXT]: nome do proprietário
- Coluna telefone [INTEGER]: número do telefone, preferenciávelmente whatsapp, do proprietário
- Coluna email [TEXT]: endereço de email do proprietário
- Coluna apto1 [VARCHAR(10)]: número do apto do proprietário (foreign-key - apartamentos)
- Coluna apto2 [VARCHAR(10)]: número do apto do proprietário (foreign-key - apartamentos)
- Coluna apto3 [VARCHAR(10)]: número do apto do proprietário (foreign-key - apartamentos)
- Coluna apto4 [VARCHAR(10)]: número do apto do proprietário (foreign-key - apartamentos)