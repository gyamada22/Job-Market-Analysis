# Scripts

## `etl.py`

Script Python responsável por:

1. Padronizar cargos, estados, skills e requisitos
2. Remover duplicatas
3. Gerar o arquivo `Vagas_Coletadas_Cleaned.xlsx`
4. Atualizar o banco SQL Server (`projeto_vagas`) com tabelas `Vagas` e `Skills`

### Como usar

```bash
python scripts/etl.py
