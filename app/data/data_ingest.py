import sqlite3
import os
import pandas as pd

def save_to_db(dataframe: pd.DataFrame):
    # Determina a pasta raiz do projeto (subindo dois níveis a partir deste script)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Cria a pasta database se não existir
    db_dir = os.path.join(base_dir, "database")
    os.makedirs(db_dir, exist_ok=True)

    # Caminho completo para o arquivo SQLite
    db_path = os.path.join(db_dir, "beauty_sales.db")

    # Conecta e salva o DataFrame
    conn = sqlite3.connect(db_path)
    dataframe.to_sql("fact_table", conn, if_exists="replace", index=False)
    conn.close()
