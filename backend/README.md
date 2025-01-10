# Protótipo - Backend

## Tasks:
1. Adicionar colunas para data de criação e data de modificação.
2. Ver no `models.py` e talvez no `schemas.py` também, a questão de valores default para agilizar no trabalho de criar elementos.
3. Rever aqui no `README.md` a descrição, a estrutura e a descrição dos módulos.
4. Criar e melhorar as docstrings, comentários e documentação. (De preferência em inglês, exceto o banco de dados que deve se manter em português).
5. Criar um módulo que permita preencher a 'ficha de controle de inquilino' requisitada pelo condomínio. E assim associar estes dados ao seu respectivo aluguel. Acredito que uma nova tabela seja necessária.
6. Verificar se realmente há necessidade do skip e limit nas funções de `read_<all>` em `crud.py` ou se fica melhor diretamente no **frontend**.


# Banco de Dados - Sistema de Reservas Imobiliárias

Este documento apresenta a especificação técnica do modelo de banco de dados utilizado no sistema de reservas imobiliárias. O objetivo do sistema é gerenciar informações relacionadas a aluguéis temporários, apartamentos, despesas recorrentes, edifícios, alugueis de vagas de garagem, gastos variáveis e proprietários.

---

## Estrutura do Banco de Dados (`imob.db`)

### 1. **Tabela Aluguéis (`alugueis`)**
Registra as informações pertinentes aos aluguéis realizados nos apartamentos.

- **id** *(INTEGER, PK)*: Identificação única do aluguel.
- **checkin** *(DATE)*: Data de entrada do hóspede.
- **checkout** *(DATE)*: Data de saída do hóspede.
- **diarias** *(INTEGER)*: Quantidade de diárias contratadas.
- **valor_diaria** *(NUMERIC(10, 2))*: Valor unitário da diária.
- **taxa_adm** *(NUMERIC(5, 2))*: Percentual retido pela imobiliária como taxa administrativa.
- **valor_total** *(NUMERIC(10, 2))*: Valor total do aluguel (*diarias × valor_diaria*).
- **valor_imob** *(NUMERIC(10, 2))*: Valor destinado à imobiliária (*valor_total × taxa_adm*).
- **valor_prop** *(NUMERIC(10, 2))*: Valor destinado ao proprietário (*valor_total - valor_imob*).
- **apartamento_id** *(INTEGER, FK)*: Referência ao apartamento alugado.

**Constraints**:
- `ck_taxa_adm_range`: `taxa_adm` deve estar no intervalo de 0 a 100.
- `ck_valor_diaria_nonnegative`: `valor_diaria ≥ 0`.
- `ck_valor_total_nonnegative`: `valor_total ≥ 0`.

**Relacionamentos**:
- **Apartamento**: N:1 (*muitos-para-um*).

---

### 2. **Tabela Apartamentos (`apartamentos`)**
Gerencia os dados cadastrais dos apartamentos.

- **id** *(INTEGER, PK)*: Identificação única do apartamento.
- **apartamento** *(VARCHAR(10))*: Código do apartamento (bloco e número).
- **celesc** *(INTEGER)*: Código da unidade consumidora de energia.
- **supergasbras** *(INTEGER)*: Código da unidade consumidora de gás.
- **internet_provedor** *(TEXT)*: Nome do provedor de internet.
- **wifiid** *(TEXT)*: Identificador da rede Wi-Fi.
- **wifipass** *(TEXT)*: Senha da rede Wi-Fi.
- **lockpass** *(INTEGER)*: Senha da fechadura eletrônica.
- **edificio_id** *(INTEGER, FK)*: Referência ao edifício onde o apartamento está localizado.
- **proprietario_id** *(INTEGER, FK)*: Referência ao proprietário do apartamento.

**Constraints**:
- `uq_apartamento_edificio`: Combinação única de `apartamento` e `edificio_id`.

**Relacionamentos**:
- **Alugueis**: 1:N (*um-para-muitos*).
- **Edificio**: N:1 (*muitos-para-um*).
- **Proprietário**: N:1 (*muitos-para-um*).
- **Despesas**: 1:N (*um-para-muitos*).
- **Gastos**: 1:N (*um-para-muitos*).
- **Garagens**: 1:N (*um-para-muitos*).

---

### 3. **Tabela Despesas Fixas (`despesas`)**
Registra despesas fixas associadas aos apartamentos.

- **id** *(INTEGER, PK)*: Identificação única da despesa.
- **data_pagamento** *(DATETIME)*: Data de pagamento.
- **valor** *(NUMERIC(10, 2))*: Valor da despesa.
- **descricao** *(TEXT)*: Descrição da despesa.
- **apartamento_id** *(INTEGER, FK)*: Referência ao apartamento correspondente.

**Relacionamentos**:
- **Apartamento**: N:1 (*muitos-para-um*).

---

### 4. **Tabela Edifícios (`edificios`)**
Registra as informações dos edifícios.

- **id** *(INTEGER, PK)*: Identificação única do edifício.
- **nome** *(TEXT)*: Nome do edifício.
- **endereco** *(TEXT)*: Endereço do edifício.
- **numero** *(INTEGER)*: Número do edifício.
- **bairro** *(TEXT)*: Bairro onde o edifício está localizado.
- **cidade** *(TEXT)*: Cidade onde o edifício está localizado.
- **estado** *(VARCHAR(2))*: Sigla do estado.
- **cep** *(INTEGER)*: Código postal do edifício.

**Constraints**:
- `ck_estado_length`: O campo `estado` deve conter exatamente dois caracteres.

**Relacionamentos**:
- **Apartamentos**: 1:N (*um-para-muitos*).

---

### 5. **Tabela Garagens (`garagens`)**
Registra aluguéis de vagas de garagem entre apartamentos.

- **id** *(INTEGER, PK)*: Identificação única do aluguel de garagem.
- **checkin** *(DATE)*: Data de início do aluguel.
- **checkout** *(DATE)*: Data de término do aluguel.
- **diarias** *(INTEGER)*: Quantidade de diárias contratadas.
- **valor_diaria** *(NUMERIC(10, 2))*: Valor unitário da diária.
- **taxa_adm** *(NUMERIC(5, 2))*: Percentual retido pela imobiliária.
- **valor_total** *(NUMERIC(10, 2))*: Valor total do aluguel.
- **valor_imob** *(NUMERIC(10, 2))*: Valor destinado à imobiliária.
- **valor_prop** *(NUMERIC(10, 2))*: Valor destinado ao proprietário.
- **apto_destino_id** *(INTEGER, FK)*: Referência ao apartamento destinatário da vaga.
- **apto_origem_id** *(INTEGER, FK)*: Referência ao apartamento proprietário da vaga.

**Relacionamentos**:
- **Apartamento (Destino)**: N:1 (*muitos-para-um*).
- **Apartamento (Origem)**: N:1 (*muitos-para-um*).

---

### 6. **Tabela Gastos Variáveis (`gastos`)**
Registra despesas eventuais associadas aos apartamentos.

- **id** *(INTEGER, PK)*: Identificação única do gasto.
- **data_pagamento** *(DATETIME)*: Data de pagamento.
- **valor_material** *(NUMERIC(10, 2))*: Valor gasto com materiais.
- **valor_mo** *(NUMERIC(10, 2))*: Valor gasto com mão de obra.
- **valor_total** *(NUMERIC(10, 2))*: Valor total da despesa.
- **descricao** *(TEXT)*: Descrição do gasto.
- **apartamento_id** *(INTEGER, FK)*: Referência ao apartamento correspondente.

**Relacionamentos**:
- **Apartamento**: N:1 (*muitos-para-um*).

---

### 7. **Tabela Proprietários (`proprietarios`)**
Armazena informações dos proprietários dos apartamentos.

- **id** *(INTEGER, PK)*: Identificação única do proprietário.
- **cpf** *(BIGINT)*: CPF do proprietário (único).
- **nome** *(TEXT)*: Nome completo do proprietário.
- **telefone** *(BIGINT)*: Número de telefone de contato.
- **email** *(TEXT)*: Endereço de e-mail do proprietário (único).

**Relacionamentos**:
- **Apartamentos**: 1:N (*um-para-muitos*).

---

**Nota:** Para consultas SQL e especificações de integração, consulte a documentação de desenvolvimento.

---

# Módulo database

# Módulo models

# Módulo schemas

# Módulo crud

# Módulo routes

# Módulo main