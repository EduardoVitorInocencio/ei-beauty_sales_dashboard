import os
import sqlite3
import pandas as pd

def load_data_from_db(table_name: str = "fact_table") -> pd.DataFrame:
    """
    Busca todos os dados da tabela SQLite e retorna como DataFrame.
    Funciona mesmo se o script estiver em app/data.
    """
    # base_dir = pasta app/data
    base_dir = os.path.abspath(os.path.dirname(__file__))
    # sobe um nível para app, depois entra em database
    db_path = os.path.join(base_dir, "..", "database", "beauty_sales.db")
    
    # normaliza o caminho
    db_path = os.path.normpath(db_path)
    
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    
    return df
