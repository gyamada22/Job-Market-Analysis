# Análise do Mercado de Dados — Evolução por Senioridade

> 📌 **Projeto de Análise do Mercado de Dados Brasileiro**  
> Baseado em vagas reais, utilizando IA para classificar competências técnicas por senioridade e nível de exigência (**Obrigatório** vs **Diferencial**).

---

## 1. Metodologia

O projeto mapeou o mercado de dados brasileiro por meio da extração de informações de vagas reais.  
As descrições textuais foram processadas com apoio de IA para converter requisitos técnicos em métricas estruturadas, classificadas como:

- **Obrigatório**
- **Diferencial**

Essa abordagem permite identificar padrões de exigência técnica ao longo da progressão de carreira.

---

## 2. Evolução por Senioridade

###  Júnior (101 Vagas)

**Visão Geral:**  
O nível Júnior é dominado por ferramentas de BI e análise básica. Diferenciais técnicos ainda não são amplamente exigidos, mas já criam vantagem competitiva.

**Principais Insights**
- **Obrigatório:** Power BI (27,36%), Excel Avançado (20,27%) e SQL (18,58%)
- **Diferencial:** Bibliotecas Python (8,85%) e Tableau (5,31%)
- **Leitura estratégica:** Python começa a separar candidatos já no início da carreira

<p align="center">
  <img src="./docs/images/junior_project.png" width="650">
</p>



---

###  Pleno (137 Vagas)

**Visão Geral:**  
No nível Pleno ocorre a transição crítica de BI para engenharia analítica. Python deixa de ser diferencial e passa a ser um pilar técnico.

**Principais Insights**
- **Obrigatório:** Power BI (37,50%), SQL (35,81%) e Python (28,38%)
- **Diferencial estratégico:** Tableau (7,21%)
- **Mudança estrutural:** ETL e Machine Learning surgem como exigências recorrentes (9,91%)

<p align="center">
  <img src="./docs/images/pleno_project.png" width="650">
</p>


---

###  Sênior (64 Vagas)

**Visão Geral:**  
O foco no nível Sênior migra da análise para arquitetura, escala e governança de dados.

**Principais Insights**
- **Obrigatório:** SQL (18,24%), Python (15,54%) e ETL (12,50%)
- **Diferencial dominante:** AWS (10,34%) e Big Data (9,48%)
- **Leitura técnica:** Senioridade está associada à capacidade de orquestrar pipelines e ambientes complexos

<p align="center">
  <img src="./docs/images/senior_project.png" width="650">
</p>


---

## 3. O Peso Estratégico do Tableau

Embora o **Power BI** concentre o maior volume de exigências ao longo da carreira, o **Tableau** surge como o principal diferencial competitivo.

Seu pico ocorre no nível Pleno, onde:
- é o **3º maior diferencial técnico (7,21%)**
- atinge **10,73% de obrigatoriedade técnica** quando ferramentas básicas são desconsideradas

Isso indica que o Tableau funciona como um **marcador de especialização**, especialmente fora do ecossistema Microsoft.

---

## 4. Recomendações de Carreira (Pathing)

1. **Início (Júnior):**  
   Priorize Power BI e SQL. Estude Bibliotecas Python e Tableau para criar diferenciais competitivos.

2. **Meio (Pleno):**  
   Domine Python (Pandas, NumPy), ETL e consolide SQL. Use Tableau para visualizações mais complexas.

3. **Fim (Sênior):**  
   Direcione o aprendizado para arquitetura em nuvem (AWS/Azure), Big Data e orquestração de pipelines (ex.: Apache Airflow).

---

## 5. Conclusão

A análise demonstra uma progressão clara do mercado:  
o profissional evolui de um perfil focado em **consumo de dados** (Júnior/BI) para um perfil de **construção e governança de arquitetura** (Sênior/ETL/Cloud).

O Tableau atua como uma ponte estratégica nesse caminho, oferecendo um diferencial competitivo sólido para quem busca posições de maior senioridade e especialização técnica.























-------------------------------------
# Job Market Analysis 

## 🖥️ Descrição do Projeto
- Este projeto tem como objetivo analisar **vagas reais de emprego na área de dados**, coletadas a partir de plataformas de recrutamento (ex: LinkedIn), para extrair insights sobre **skills demandadas, tendências do mercado e gaps de competências**.

- A análise é inicialmente focada no **mercado brasileiro**, com posterior **comparação com dados internacionais**, visando identificar padrões globais e possíveis tendências que podem chegar ao Brasil no futuro.

- O projeto transforma dados não estruturados em **insights analíticos e dashboards interativos**, documentando todo o pipeline de dados de forma clara e profissional.

---

## 🔹 Coleta de Dados
> **Desafio:** LinkedIn possui API fechada, impossibilitando a coleta automatizada de vagas diretamente via Python.

> **Solução:** Para contornar, coletei os dados manualmente, visitando cada vaga e usando prompts de IA para extrair informações estruturadas (empresa, cargo, localização, data e skills).

Essa abordagem garantiu **eficiência e confiabilidade** para o pipeline subsequente.

---

## 🛠️ Tecnologias e Ferramentas

O fluxo do projeto segue:

**Coleta** ![IA](https://img.shields.io/badge/IA-AI-blue) ⟶ **Visualização** ![Excel](https://img.shields.io/badge/Excel-217346?style=flat&logo=microsoft-excel&logoColor=white) ⟶ **Limpeza** ![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=white) ⟶ **Análise** ![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white) ⟶ **Apresentação** ![Power BI](https://img.shields.io/badge/Dashboard-F2C811?style=flat&logo=power-bi&logoColor=black) ⟶ **Documentação** ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)

| Etapa | Ferramenta | Função |
|-------|------------|------|
| Coleta & extração | IA via prompts | Extrai dados estruturados da vaga |
| Visualização inicial | Excel | Conferência e revisão rápida. Arquivo: **[Raw Data](https://raw.githubusercontent.com/gyamada22/Job-Market-Analysis/main/data/Vagas_Coletadas_Raw.xlsx)** |
| Limpeza e padronização | Python | Padroniza dados, corrige inconsistências e gera Excel/SQL. Arquivo: **[Cleaned Data](https://raw.githubusercontent.com/gyamada22/Job-Market-Analysis/main/data/Vagas_Coletadas_Cleaned.xlsx)**, Script: **[ETL.py](https://github.com/gyamada22/Job-Market-Analysis/blob/main/data/ETL.py)** |
| Modelagem e análise | SQL | Criação de tabelas, views e queries analíticas *(em desenvolvimento)* |
| Dashboards | Power BI | Visualização interativa, insights e storytelling |
| Documentação | GitHub | Registro completo do projeto, metodologia e exemplos de dashboards |

> 💡 Observação: Python permite **automatizar toda a cadeia de transformação**, tornando o fluxo de dados mais eficiente e escalável do que usar Excel para limpeza manual.

---

## 🎯 Objetivos
- Coletar dados de vagas reais: empresa, cargo, localização, data, nível de senioridade e requisitos técnicos.  
- Padronizar e estruturar dados textuais não estruturados (descrições de vagas).  
- Identificar **skills mais demandadas** por área e nível (estágio, júnior, pleno, sênior).  
- Analisar **diferenças e gaps de competências** entre níveis de senioridade.  
- Comparar o mercado brasileiro com dados internacionais para identificar **tendências emergentes**.  
- Criar dashboards interativos que apoiem **decisões de carreira e estudo**.  
- Documentar todo o pipeline: **coleta → limpeza → análise → visualização**.

---

## ✅ Status Atual
- [x] Estrutura de pastas criada  
- [x] Coleta de dados inicial 
- [ ] Modelagem do banco de dados  
- [ ] Primeiras análises  
- [ ] Dashboard inicial  

---

## 🔹 Observações Finais
- Pipeline eficiente, contornando limitações do LinkedIn  
- Uso integrado de IA, Python, SQL, Power BI e Excel
- Documentação clara, garantindo transparência e profissionalismo para portfólio
