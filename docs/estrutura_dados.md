# Estrutura de Dados para Extração de Vagas do LinkedIn

Este documento descreve a **estrutura de abas do Excel** e o **prompt usado para extrair dados de vagas** do LinkedIn, gerando arquivos prontos para análise no Excel, Python ou SQL.

---

##  Estrutura das abas do Excel

### Aba `vagas`
ID, Empresa, Cargo, Modelo_Trab, Area_Atuacao, Data, Nível, Salario, Link_Vaga, Destaque, Localizacao, Tipo_Contratacao, Num_Candidatos, Idiomas, Beneficios, Departamento, Ferramentas_Específicas, Remoto, Categoria, Fonte_Vaga

### Aba `skills`
Colunas:  Vaga_ID, Skill, Tipo, Nivel_Conhecimento, Obrigatoria, Categoria

---

##  Critério de pesquisa no LinkedIn

As vagas foram coletadas manualmente a partir do LinkedIn utilizando a seguinte **query de busca**:

("analista de dados" OR "cientista de dados" OR "analista bi") AND (sql OR python OR excel OR "power bi")


---

##  Prompt para extrair dados do LinkedIn

```
# PROMPT FINAL — EXTRAÇÃO DE VAGAS (TSV COM VALIDAÇÃO DE COLUNAS)

Você vai receber a descrição completa de uma vaga de emprego.

Seu objetivo é extrair os dados para **DUAS abas de Excel**, no formato **TSV (Tab-Separated Values)**:
- `vagas`
- `skills`

⚠️ **REGRAS CRÍTICAS — NÃO IGNORAR**

## 1️⃣ Validação estrutural obrigatória
- A aba **`vagas` DEVE TER EXATAMENTE 20 COLUNAS**
- A aba **`skills` DEVE TER EXATAMENTE 6 COLUNAS**
- **NUNCA** pode haver deslocamento de dados entre colunas
- **Toda coluna inexistente deve ser representada por um TAB vazio**
- **Antes de enviar o resultado final, valide mentalmente coluna por coluna**

## 2️⃣ Regras TSV (OBRIGATÓRIAS)
- Separador: **TAB**
- **Nunca usar vírgula como separador**
- Campos podem conter vírgulas, ponto e vírgula e textos longos **sem aspas**
- **Coluna vazia = TAB TAB**
- O output deve conter:
  - `vagas` → **19 TABs**
  - `skills` → **5 TABs por linha**

## 3️⃣ Regras absolutas de output
- ❌ NÃO explicar nada no output final
- ❌ NÃO adicionar títulos
- ❌ NÃO adicionar comentários
- ❌ NÃO adicionar linhas em branco
- ❌ NÃO repetir cabeçalhos
- ❌ NÃO agrupar múltiplas vagas

---

## 📊 ESTRUTURA DAS ABAS

### ABA `vagas` — ORDEM FIXA (20 colunas)

1. ID  
2. Empresa  
3. Cargo  
4. Modelo_Trab  
5. Area_Atuacao  
6. Data  
7. Nível  
8. Salario  
9. Link_Vaga  
10. Destaque  
11. Localizacao  
12. Tipo_Contratacao  
13. Num_Candidatos  
14. Idiomas  
15. Beneficios  
16. Departamento  
17. Ferramentas_Específicas  
18. Remoto  
19. Categoria  
20. Fonte_Vaga  

---

### ABA `skills` — ORDEM FIXA (6 colunas)

1. Vaga_ID  
2. Skill  
3. Tipo  
4. Nivel_Conhecimento  
5. Obrigatoria  
6. Categoria  

---

## 📌 REGRAS DE EXTRAÇÃO

- Data padrão se ausente: **18/01/2024**
- Nível SOMENTE se explícito: **Júnior | Pleno | Sênior**
- Skills obrigatórias:
  - termos como: *requisito, necessário, obrigatório*
- Skills diferenciais:
  - termos como: *desejável, diferencial, plus*
- Nivel_Conhecimento somente se explícito
- Obrigatoria:
  - **Sim** = obrigatória
  - **Não** = diferencial
- Categoria da vaga: resumo da área principal (ex: Dados)
- Fonte_Vaga: origem explícita (ex: LinkedIn)
- Usar o **MESMO ID da vaga** em todas as skills
- NÃO repetir skills
- NÃO inferir informações não explícitas

---

## 📤 FORMATO FINAL DE SAÍDA (POWERSHELL / TSV)

### BLOCO 1 — ABA `vagas`
- Enviar **APENAS uma linha TSV**
- Deve conter exatamente **20 colunas (19 TABs)**
- Nenhuma validação textual ou explicação

### BLOCO 2 — ABA `skills`
- Enviar **APENAS linhas TSV**
- Uma skill por linha
- Cada linha deve conter exatamente **6 colunas (5 TABs)**

---

Descrição da vaga:


```
