import pandas as pd
import pyodbc

CONFIG = {
    'server': 'localhost\\SQLEXPRESS',
    'database': 'projeto_vagas',
    'table_vagas': 'Vagas',
    'table_skills': 'Skills',
    'excel_origem': r'C:\MeusProjetos\projeto_vagas\Dados\Vagas_Coletadas.xlsx',
    'excel_processado': r'C:\MeusProjetos\projeto_vagas\Dados\analise_vagas.xlsx'
}


def transformar_dados():
    vagas = pd.read_excel(CONFIG['excel_origem'], sheet_name='Vagas')
    skills = pd.read_excel(CONFIG['excel_origem'], sheet_name='Skills')
    
    def padronizar_cargo(cargo):
        if pd.isna(cargo): 
            return cargo
        cargo_str = str(cargo).lower()
        if 'alis' in cargo_str: 
            return 'Analista de Dados'
        elif 'enti' in cargo_str: 
            return 'Cientista de Dados'
        return cargo
    
def transformar_dados():
    vagas = pd.read_excel(CONFIG['excel_origem'], sheet_name='Vagas')
    skills = pd.read_excel(CONFIG['excel_origem'], sheet_name='Skills')
    
    def padronizar_cargo(cargo):
        if pd.isna(cargo): 
            return cargo
        cargo_str = str(cargo).lower()
        if 'alis' in cargo_str: 
            return 'Analista de Dados'
        elif 'enti' in cargo_str: 
            return 'Cientista de Dados'
        return cargo
    
    def extrair_estado(local):
        if pd.isna(local):
            return local
        
        local_str = str(local).lower()
        
        mapeamento = {
            'ão pau': 'São Paulo', 'barueri': 'São Paulo', 'campinas': 'São Paulo', 'sp': 'São Paulo',
            'rio de jan': 'Rio de Janeiro', 'rj': 'Rio de Janeiro',
            'minas': 'Minas Gerais', 'belo horizonte': 'Minas Gerais', 'mg': 'Minas Gerais',
            'espírito': 'Espírito Santo', 'vitória': 'Espírito Santo', 'es': 'Espírito Santo',
            'aran': 'Paraná', 'maringá': 'Paraná', 'pr': 'Paraná',
            'santa cat': 'Santa Catarina', 'sc': 'Santa Catarina',
            'rio grande': 'Rio Grande do Sul', 'porto alegre': 'Rio Grande do Sul', 'rs': 'Rio Grande do Sul',
            'bahia': 'Bahia', 'salvador': 'Bahia', 'ba': 'Bahia',
            'ceará': 'Ceará', 'fortaleza': 'Ceará', 'ce': 'Ceará',
            'pernambuco': 'Pernambuco', 'recife': 'Pernambuco', 'pe': 'Pernambuco',
            'paraíba': 'Paraíba', 'joão pessoa': 'Paraíba', 'pb': 'Paraíba',
            'alagoas': 'Alagoas', 'maceió': 'Alagoas', 'al': 'Alagoas',
            'sergipe': 'Sergipe', 'lagarto': 'Sergipe', 'se': 'Sergipe',
            'piauí': 'Piauí', 'teresina': 'Piauí', 'pi': 'Piauí',
            'maranhão': 'Maranhão', 'ma': 'Maranhão',
            'goiás': 'Goiás', 'goiânia': 'Goiás', 'go': 'Goiás',
            'distrito': 'Distrito Federal', 'brasília': 'Distrito Federal', 'df': 'Distrito Federal',
            'mato grosso': 'Mato Grosso', 'mt': 'Mato Grosso',
            'mato grosso do sul': 'Mato Grosso do Sul', 'dourados': 'Mato Grosso do Sul', 'ms': 'Mato Grosso do Sul',
            'pará': 'Pará', 'belém': 'Pará', 'pa': 'Pará',
            'amazonas': 'Amazonas', 'am': 'Amazonas',
            'rondônia': 'Rondônia', 'ro': 'Rondônia',
            'tocantins': 'Tocantins', 'to': 'Tocantins',
            'roraima': 'Roraima', 'rr': 'Roraima',
            'amapá': 'Amapá', 'ap': 'Amapá',
            'acre': 'Acre', 'ac': 'Acre',
            'remoto': 'Remoto', 'remote': 'Remoto'
        }
        
        for parte, estado in mapeamento.items():
            if parte in local_str:
                return estado
        
        return local
    
    def classificar_requisito(valor):
        if pd.isna(valor):
            return "Não informado"
        valor_str = str(valor).strip().lower()
        if valor_str in ['básico', 'basico', 'sim', 'obrigatório', 'obrigatorio']:
            return "Obrigatório"
        elif valor_str in ['diferencial', 'não', 'nao', 'não obrigatório']:
            return "Diferencial"
        return valor_str.capitalize()
    
    def limpar_skill_agrupada(skill):
        if pd.isna(skill):
            return "Não informado"
        skill_lower = str(skill).strip().lower()
        mapeamento = {
            'python': 'Python', 'sql': 'SQL', 'excel': 'Excel Avançado',
            'power bi': 'Power BI', 'tableau': 'Tableau'
        }
        for term, padrao in mapeamento.items():
            if term in skill_lower:
                return padrao
        return "Outra Skill"
    
    vagas['Cargo_Padronizado'] = vagas['Cargo'].apply(padronizar_cargo)
    vagas['Estado'] = vagas['Localização'].apply(extrair_estado)
    skills['Requisito'] = skills['Obrigatório/Diferencial'].apply(classificar_requisito)
    skills['Skill_Agrupada'] = skills['Skill'].apply(limpar_skill_agrupada)
    
    df_vagas = vagas[['ID', 'Empresa', 'Setor', 'Modelo_Trabalho', 'Senioridade', 'Cargo_Padronizado', 'Estado']]
    df_vagas = df_vagas.rename(columns={
        'Modelo_Trabalho': 'Modalidade',
        'Cargo_Padronizado': 'Cargo'
    })
    
    df_skills = skills[['Vaga_ID', 'Skill_Agrupada', 'Requisito']].copy()
    df_skills = df_skills.rename(columns={
        'Vaga_ID': 'ID_Vaga',
        'Skill_Agrupada': 'Skill'
    })
    
    with pd.ExcelWriter(CONFIG['excel_processado'], engine='openpyxl') as writer:
        df_vagas.to_excel(writer, sheet_name='Vagas', index=False)
        df_skills.to_excel(writer, sheet_name='Skills', index=False)
    
    return df_vagas, df_skills


    
    def classificar_requisito(valor):
        if pd.isna(valor):
            return "Não informado"
        valor_str = str(valor).strip().lower()
        if valor_str in ['básico', 'basico', 'sim', 'obrigatório', 'obrigatorio']:
            return "Obrigatório"
        elif valor_str in ['diferencial', 'não', 'nao', 'não obrigatório']:
            return "Diferencial"
        return valor_str.capitalize()
    
    def limpar_skill_agrupada(skill):
        if pd.isna(skill):
            return "Não informado"
        skill_lower = str(skill).strip().lower()
        mapeamento = {
            'python': 'Python', 'sql': 'SQL', 'excel': 'Excel Avançado',
            'power bi': 'Power BI', 'tableau': 'Tableau'
        }
        for term, padrao in mapeamento.items():
            if term in skill_lower:
                return padrao
        return "Outra Skill"
    
    vagas['Cargo_Padronizado'] = vagas['Cargo'].apply(padronizar_cargo)
    vagas['Estado'] = vagas['Localização'].apply(extrair_estado)
    skills['Requisito'] = skills['Obrigatório/Diferencial'].apply(classificar_requisito)
    skills['Skill_Agrupada'] = skills['Skill'].apply(limpar_skill_agrupada)
    
    df_vagas = vagas[['ID', 'Empresa', 'Setor', 'Modelo_Trabalho', 'Senioridade', 'Cargo_Padronizado', 'Estado']]
    df_vagas = df_vagas.rename(columns={
        'Modelo_Trabalho': 'Modalidade',
        'Cargo_Padronizado': 'Cargo'
    })
    
    df_skills = skills[['Vaga_ID', 'Skill_Agrupada', 'Requisito']].copy()
    df_skills = df_skills.rename(columns={
        'Vaga_ID': 'ID_Vaga',
        'Skill_Agrupada': 'Skill'
    })
    
    with pd.ExcelWriter(CONFIG['excel_processado'], engine='openpyxl') as writer:
        df_vagas.to_excel(writer, sheet_name='Vagas', index=False)
        df_skills.to_excel(writer, sheet_name='Skills', index=False)
    
    return df_vagas, df_skills


def conectar_banco():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={CONFIG['server']};"
        f"DATABASE={CONFIG['database']};"
        f"Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)


def importar_dados(conn, df_vagas, df_skills):
    cursor = conn.cursor()
    
    cursor.execute(f"DELETE FROM {CONFIG['table_skills']}")
    cursor.execute(f"DELETE FROM {CONFIG['table_vagas']}")
    
    vagas_data = [
        (row['ID'], row['Empresa'], row['Setor'], row['Modalidade'], 
         row['Senioridade'], row['Cargo'], row['Estado'])
        for _, row in df_vagas.iterrows()
    ]
    
    skills_data = [
        (row['ID_Vaga'], row['Skill'], row['Requisito'])
        for _, row in df_skills.iterrows()
    ]
    
    cursor.executemany(f"""
        INSERT INTO {CONFIG['table_vagas']} 
        (ID, Empresa, Setor, Modalidade, Senioridade, Cargo, Estado)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, vagas_data)
    
    cursor.executemany(f"""
        INSERT INTO {CONFIG['table_skills']} 
        (ID_Vaga, Skill, Requisito)
        VALUES (?, ?, ?)
    """, skills_data)
    
    conn.commit()
    cursor.close()


def main():
    df_vagas, df_skills = transformar_dados()
    conn = conectar_banco()
    importar_dados(conn, df_vagas, df_skills)
    conn.close()


if __name__ == "__main__":
    main()