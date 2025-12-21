# Job Market Analysis — Análise de Requisitos de Vagas

## 🖥️ Descrição do Projeto
- Este projeto tem como objetivo analisar **vagas de emprego na área de dados** e extrair insights sobre os **requisitos de skills** mais demandados pelo mercado.
- O objetivo é transformar dados não estruturados em **insights visuais e dashboards interativos**, documentando todo o pipeline de forma profissional.

---

## 🎯 Objetivos
- Coletar informações de vagas: empresa, cargo, localização, data, skills obrigatórias e diferenciais.  
- Padronizar e organizar os dados para análise.  
- Identificar skills mais demandadas, combinações e tendências.  
- Criar dashboards interativos para exploração visual.  
- Documentar todo o processo, mostrando pipeline completo de dados.
---

## 🔹 Coleta de Dados
> **Desafio:** LinkedIn possui API fechada, impossibilitando a coleta automatizada de vagas diretamente via Python.

> **Solução:** Para contornar, usei IA via prompts, extraindo dados estruturados de cada vaga: empresa, cargo, localização, data e skills (obrigatórias/diferenciais).

Essa abordagem garantiu **eficiência e confiabilidade** para o pipeline subsequente.

---

## 🛠️ Tecnologias e Ferramentas

| Etapa | Ferramenta | Função |
|-------|------------|------|
| Coleta & extração | IA via prompts | Extrai dados estruturados da vaga |
| Visualização inicial | Excel | Conferência e revisão rápida |
| Limpeza e padronização | Python | Padroniza dados, corrige inconsistências, remove duplicatas e gera CSV pronto para SQL |
| Modelagem e análise | SQL | Criação de tabelas, views e queries analíticas |
| Dashboards | Power BI | Visualização interativa, insights e storytelling |
| Documentação | GitHub | Registro completo do projeto, metodologia e exemplos de dashboards |

> 💡 Observação: Python permite **automatizar toda a cadeia de transformação**, tornando o fluxo de dados mais eficiente e escalável do que usar Excel para limpeza manual.

---
## 📊 Pipeline do Projeto

**Resumo das etapas:**
1. **Coleta com IA** – Extrai dados estruturados de cada vaga.  
2. **Processamento (Python)** – Limpeza, padronização e geração de CSV pronto para SQL.  
3. **Análise (SQL)** – Criação de tabelas, views e queries para identificar padrões e tendências.  
4. **Visualização (Power BI)** – Dashboards interativos filtráveis por skill, empresa e localização.  
5. **Documentação (GitHub)** – Registro completo do pipeline, metodologia e insights.


---

## 📊 Pipeline do Projeto 

1. **🤖 COLETA COM IA**
   - Extrai dados estruturados de vagas
   - Captura: empresa, cargo, local, data, skills

2. **🐍 PROCESSAMENTO (Python)**
   - Limpeza e padronização de dados
   - Remoção de duplicatas e inconsistências
   - Geração de CSV pronto para SQL

3. **🗄️ ANÁLISE (SQL)**
   - Criação de tabelas e views analíticas
   - Queries para identificar padrões e tendências

4. **📊 VISUALIZAÇÃO (Power BI)**
   - Dashboards interativos
   - Filtros por skill, empresa, localização

5. **📚 DOCUMENTAÇÃO (GitHub)**
   - README completo
   - Explicação da metodologia
   - Resultados e insights

---

## ✅ Status Atual
- [x] Estrutura de pastas criada  
- [x] Coleta de dados inicial (10 vagas)  
- [] Modelagem do banco de dados  
- [] Primeiras análises  
- [] Dashboard inicial  

---

## 🔹 Observações Finais
- Pipeline eficiente, contornando limitações do LinkedIn  
- Uso integrado de IA, Python, SQL, Power BI e Excel
- Documentação clara, garantindo transparência e profissionalismo para portfólio
