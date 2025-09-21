from app.data.load_data_from_sql import load_data_from_db

if __name__ == "__main__":
    # path = "dados/vendas_produtos.xlsx"  # coloque um Excel de exemplo
    df = load_data_from_db()
    print(df.head())