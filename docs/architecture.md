# 📊 Projeto de Análise de Mercado de Trabalho — Snowflake + DBT

## 🔹 Objetivo
Migrar a ingestão e limpeza de dados para a nuvem usando **Snowflake** como banco central, seguindo a arquitetura **Medallion (Bronze / Silver / Gold)**, e aplicar o **DBT** para padronizar transformações, testes e documentação.

---

## 1. Configuração Inicial

- Conta **Snowflake** criada e acessível via `python-snowflake-connector`.
- Conexão segura configurada usando **.env** e variáveis de ambiente (nenhuma credencial exposta no código).
- Função Python `conectar_snowflake()` criada para reutilização em qualquer script.

---

## 2. Estrutura de Camadas (Medallion)

| Camada  | Conteúdo |
|---------|----------|
| **Bronze** | Dados brutos carregados diretamente do ETL Python (`VAGAS`, `SKILLS`). |
| **Silver** | Limpeza e padronização intermediária (opcional, pois o ETL já padronizou dados). |
| **Gold** | Tabelas finais prontas para análise, dashboards e consumo por ferramentas BI. |

### Tabelas Gold Criadas
1. `VAGAS_SENIORIDADE` — volume de vagas por senioridade  
2. `TOP3SKILL_OBRI_SENIORI` — top 3 skills obrigatórias por senioridade  
3. `TOP3SKILL_DIF_SENIORI` — top 3 skills diferenciais por senioridade  
4. `VAGAS_ESTADO` — distribuição de vagas por estado  
5. `PERCENTUAL_VAGAS_ESTADO` — percentual de vagas por estado  
6. `VAGAS_MODALIDADE` — distribuição de vagas por modalidade  
7. `VAGAS_SETOR` — top 5 setores por quantidade de vagas  
8. `TOP5SKILL_OBG_SETOR` — top 5 skills obrigatórias por setor  
9. `TOP5SKILL_DIF_SETOR` — top 5 skills diferenciais por setor  

---

## 3. Uso do DBT

Após criar as tabelas Gold, o **DBT** foi implementado para:

- Automatizar transformações SQL e criação de views/tabelas derivadas.  
- Definir **sources** para padronizar referência às tabelas brutas.  
- Aplicar **testes de qualidade de dados** (`not_null`, `unique`) em todas as tabelas Gold.  
- Gerar documentação navegável via `dbt docs`.

### Comandos principais

```bash
# Executar transformações
dbt run

# Rodar testes de qualidade de dados
dbt test

# Gerar documentação
dbt docs generate
dbt docs serve
