# 📊 Análise de Mercado de Trabalho — DBT

## 🛠 Sobre o Projeto
Este projeto utiliza **DBT (Data Build Tool)** para transformar dados brutos da camada **Bronze** em tabelas e views consolidadas na camada **Gold**. O objetivo é gerar insights sobre vagas de emprego, senioridade, skills e setores.  

## 💡 Estrutura de Dados
- **Bronze**: tabelas originais `VAGAS` e `SKILLS`.
- **Gold**: tabelas transformadas, incluindo:
  - `VAGAS_SENIORIDADE` — volume de vagas por senioridade
  - `TOP3SKILL_OBRI_SENIORI` — top 3 skills obrigatórias por senioridade
  - `TOP3SKILL_DIF_SENIORI` — top 3 skills diferenciais por senioridade
  - `VAGAS_ESTADO` — distribuição de vagas por estado
  - `PERCENTUAL_VAGAS_ESTADO` — percentual de vagas por estado
  - `VAGAS_MODALIDADE` — distribuição de vagas por modalidade
  - `VAGAS_SETOR` — top 5 setores por quantidade de vagas
  - `TOP5SKILL_OBG_SETOR` — top 5 skills obrigatórias por setor
  - `TOP5SKILL_DIF_SETOR` — top 5 skills diferenciais por setor

## ⚡ Funcionalidades do DBT
- Criação automática de tabelas e views a partir de queries SQL.
- Definição de **sources** para padronizar referência às tabelas brutas.
- Testes de qualidade de dados (`not_null`, `unique`) aplicados automaticamente.
- Catálogo de documentação gerado (`dbt docs generate`).

## 🚀 Como Rodar
1. Configurar conexão com **Snowflake** no `profiles.yml`.
2. Executar transformações:
   ```bash
   dbt run
