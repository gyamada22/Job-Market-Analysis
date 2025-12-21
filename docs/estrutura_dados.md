# Estrutura de Dados para Extração de Vagas do LinkedIn

Este documento descreve a **estrutura de abas do Excel** e o **prompt usado para extrair dados de vagas** do LinkedIn, gerando arquivos prontos para análise no Excel, Python ou SQL.

---

## 1️⃣ Estrutura das abas do Excel

### Aba `vagas`
Colunas:  ID,Empresa,Cargo,Modelo_Trab,Area_Atuacao,Data,Nível,Salario,Link_Vaga,Destaque,Localizacao,Tipo_Contratacao,Num_Candidatos,Idiomas,Beneficios,Departamento,Ferramentas_Específicas,Remoto

### Aba `skills`
Colunas:  Vaga_ID, Skill, Tipo, Nivel_Conhecimento, Obrigatoria, Categoria

---

## 2️⃣ Prompt para extrair dados do LinkedIn

```
Você vai receber a descrição completa de uma vaga de emprego.

Seu objetivo é extrair os dados para DUAS abas de Excel:
- vagas
- skills

⚠️ REGRAS CRÍTICAS (NÃO IGNORAR)

1. A aba "vagas" DEVE TER EXATAMENTE 20 COLUNAS, NA ORDEM FIXA ABAIXO.
2. A aba "skills" DEVE TER EXATAMENTE 6 COLUNAS, NA ORDEM FIXA ABAIXO.
3. Se uma informação não existir, deixe o campo VAZIO, mas mantenha a vírgula.
4. ⚠️ REGRA CSV OBRIGATÓRIA:
   QUALQUER CAMPO QUE CONTENHA VÍRGULA (,) DEVE ESTAR ENTRE ASPAS DUPLAS (" ").
   Exemplos obrigatórios:
   - "São Paulo, SP"
   - "Vila Velha, Espírito Santo, Brasil"
   - "Plano de saúde; Vale Refeição, Vale Alimentação"
5. NÃO criar colunas extras.
6. NÃO mover informações entre colunas.
7. NÃO explicar nada no output final.

==================================================
ABA "vagas" (1 linha por vaga)
ORDEM FIXA DAS COLUNAS (20):

ID,
Empresa,
Cargo,
Modelo_Trab,
Area_Atuacao,
Data,
Nível,
Salario,
Link_Vaga,
Destaque,
Localizacao,
Tipo_Contratacao,
Num_Candidatos,
Idiomas,
Beneficios,
Departamento,
Ferramentas_Específicas,
Remoto,
Categoria,
Fonte_Vaga
==================================================

ABA "skills" (1 linha por skill)
ORDEM FIXA DAS COLUNAS (6):

Vaga_ID,
Skill,
Tipo,
Nivel_Conhecimento,
Obrigatoria,
Categoria
==================================================

REGRAS DE EXTRAÇÃO

- Data padrão se ausente: 18/01/2024
- Nível SOMENTE se explícito: Júnior | Pleno | Sênior
- Skills obrigatórias:
  termos como: requisito, necessário, obrigatório
- Skills diferenciais:
  termos como: desejável, diferencial, plus
- Nivel_Conhecimento só se explícito
- Obrigatoria:
  Sim = obrigatória
  Não = diferencial
- Categoria da vaga: resumo da área principal (ex: Dados)
- Fonte_Vaga: origem explícita (ex: LinkedIn)
- Usar o MESMO ID da vaga em todas as skills
- NÃO repetir cabeçalhos
- NÃO agrupar múltiplas vagas

==================================================
FORMATO FINAL DE SAÍDA (POWERSHELL)

BLOCO 1 — ABA VAGAS
• Enviar APENAS a linha CSV da vaga
• NÃO adicionar comentários
• NÃO adicionar títulos
• NÃO adicionar linhas em branco
• Deve conter exatamente 20 colunas
• Usar aspas sempre que houver vírgula no campo

BLOCO 2 — ABA SKILLS
• Enviar APENAS linhas CSV das skills
• Uma skill por linha
• NÃO adicionar comentários
• NÃO adicionar títulos
• Deve conter exatamente 6 colunas por linha
• Usar aspas sempre que houver vírgula no campo

==================================================

Descrição da vaga:
[COLE AQUI A DESCRIÇÃO COMPLETA]

```
