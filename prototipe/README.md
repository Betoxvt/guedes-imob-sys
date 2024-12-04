# Protótipo

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

## Módulo controller

## Módulo db

## Módulo models

## Módulo schemas

## Módulo routes
