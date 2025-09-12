from app.data.data_loader import load_data

if __name__ == "__main__":
    path = "dados/vendas_produtos.xlsx"  # coloque um Excel de exemplo
    df = load_data(path)
    print(df.head())
