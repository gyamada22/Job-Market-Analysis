# 📂 Dados Raw – Vagas_Coletadas_Raw.xlsx

Este arquivo contém os dados coletados diretamente das plataformas de recrutamento (ex: LinkedIn), sem nenhum processamento ou padronização. Ele serve como **ponto de partida para toda a análise**, garantindo a preservação dos dados originais.

## 🗂 Estrutura do Arquivo

O Excel possui **duas abas principais**: `vagas` e `skills`.

---

### 1️⃣ Aba `vagas`

| Coluna | Descrição | Tipo de dado | Observações |
|--------|-----------|-------------|------------|
| ID | Identificador único da vaga | Numérico | Serve como chave primária para relacionar com a aba `skills` |
| Empresa | Nome da empresa que publicou a vaga | Texto | Pode conter variações de grafia se coletadas diretamente do LinkedIn |
| Setor | Setor de atuação da empresa | Texto | Pode estar vazio ou inconsistente |
| Cargo | Nome do cargo anunciado | Texto | Ex: Cientista de Dados, Analista de BI |
| Modelo_Trabalho | Regime de trabalho | Texto | Ex: Presencial, Remoto, Híbrido |
| Area_Atuacao | Área da vaga | Texto | Ex: Dados, Engenharia de Software |
| Data | Data de publicação da vaga | Data | Pode precisar padronização de formato |
| Nível | Nível de senioridade | Texto | Ex: Estágio, Júnior, Pleno, Sênior |
| Localizacao | Cidade/Estado da vaga | Texto | Pode conter variações no formato |
| Tipo_Contratacao | Regime de contratação | Texto | Ex: CLT, PJ, Temporário |
| Ferramentas_Específicas | Ferramentas ou tecnologias mencionadas | Texto | Ex: Python, SQL, Tableau |
| Remoto | Indica se a vaga é remota | Booleano/Texto | Sim/Não, pode precisar padronização |
| Categoria | Categoria do cargo ou função | Texto | Ex: Analytics, Engenharia, BI |
| Fonte_Vaga | Plataforma de origem da vaga | Texto | Ex: LinkedIn, Indeed |

---

### 2️⃣ Aba `skills`

| Coluna | Descrição | Tipo de dado | Observações |
|--------|-----------|-------------|------------|
| Vaga_ID | ID da vaga correspondente (chave estrangeira) | Numérico | Relaciona a skill à vaga na aba `vagas` |
| Skill | Nome da skill mencionada | Texto | Ex: Python, SQL, Tableau |
| Tipo | Tipo de skill | Texto | Ex: Técnica, Comportamental |
| Nivel_Conhecimento | Nível exigido da skill | Texto | Ex: Básico, Intermediário, Avançado |
| Obrigatoria | Indica se a skill é obrigatória | Booleano/Texto | Sim/Não |
| Categoria | Categoria da skill | Texto | Ex: Programação, BI, Soft Skill |

---

## 💡 Observações Gerais

- Os dados são **não processados**, portanto podem conter inconsistências, duplicatas ou variações de grafia.  
- A coluna `ID` na aba `vagas` é **crucial** para relacionar com as skills na aba `skills`.  
- O próximo passo no pipeline é **limpeza e padronização** utilizando Python, preparando os dados para análise e modelagem em SQL ou Power BI.
