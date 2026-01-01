# 📘 Documentação Técnica — Análise do Mercado de Trabalho em Dados

## 🧠 Visão Geral

Este projeto foi desenvolvido com foco em **engenharia analítica**, utilizando uma arquitetura moderna baseada em **Snowflake + DBT**, com o objetivo de transformar dados brutos sobre vagas de emprego em **insights analíticos confiáveis** para visualização e tomada de decisão.

A solução adota conceitos de **Data Warehouse na nuvem**, **arquitetura Medallion (Bronze / Silver / Gold)** e **transformações versionadas via DBT**, garantindo rastreabilidade, qualidade e escalabilidade do pipeline analítico.

---

## 🏗 Arquitetura da Solução

**Fluxo Analítico**

Coleta (IA)  
⟶ ETL & Padronização (Python)  
⟶ Data Warehouse (Snowflake)  
⟶ Modelagem Analítica (SQL / DBT)  
⟶ Visualização (Power BI)  
⟶ Documentação (GitHub)

**Infraestrutura**
- **Snowflake** — Data Warehouse central
- **DBT** — Transformações, testes e documentação
- **Docker** — Padronização do ambiente de execução
- **Power BI** — Camada de visualização e storytelling

---

## 🥉🥈🥇 Arquitetura Medallion

### Bronze
- Dados brutos carregados diretamente pelo ETL em Python
- Tabelas principais:
  - `VAGAS`
  - `SKILLS`

### Silver
- Camada intermediária opcional
- A maior parte da padronização é realizada no ETL em Python, reduzindo complexidade nesta camada

### Gold
- Tabelas analíticas finais
- Otimizadas para consumo por BI, análises exploratórias e relatórios executivos

---

## 📊 Modelos Analíticos (Gold)

Principais tabelas e views criadas via DBT:

- `VAGAS_SENIORIDADE` — Volume de vagas por senioridade  
- `TOP3SKILL_OBRI_SENIORI` — Top 3 skills obrigatórias por senioridade  
- `TOP3SKILL_DIF_SENIORI` — Top 3 skills diferenciais por senioridade  
- `VAGAS_ESTADO` — Distribuição de vagas por estado  
- `PERCENTUAL_VAGAS_ESTADO` — Percentual de vagas por estado  
- `VAGAS_MODALIDADE` — Distribuição de vagas por modalidade (remoto, híbrido, presencial)  
- `VAGAS_SETOR` — Top 5 setores com maior número de vagas  
- `TOP5SKILL_OBG_SETOR` — Top 5 skills obrigatórias por setor  
- `TOP5SKILL_DIF_SETOR` — Top 5 skills diferenciais por setor  

---

## ⚙️ Uso do DBT

O DBT foi utilizado para padronizar e automatizar a camada de transformação analítica:

- Definição de **sources** para as tabelas da camada Bronze
- Criação de **models SQL** versionados para a camada Gold
- Aplicação de **testes de qualidade de dados**:
  - `not_null`
  - `unique`
- Geração de documentação navegável com `dbt docs`

### Comandos Principais

```bash
dbt run
dbt test
dbt docs generate
dbt docs serve
