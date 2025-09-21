import os
import sqlite3
import pandas as pd

def load_data_from_db(table_name: str = "fact_table") -> pd.DataFrame:
    """
    Busca todos os dados da tabela SQLite e retorna como DataFrame.
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    db_path = os.path.join(base_dir, "database", "beauty_sales.db")
    
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    
    return df
