import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Carrega dados de vendas de um arquivo Excel.

    Args:
        file_path (str): Caminho do arquivo Excel.

    Returns:
        pd.DataFrame: DataFrame com os dados carregados.
    """
    try:
        df = pd.read_excel(file_path)

        # Normalização básica (ajustável conforme seu Excel real)
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        # Exemplo: garantir que colunas essenciais existam
        expected_cols = {"produto", "regiao", "data", "vendas"}
        if not expected_cols.issubset(set(df.columns)):
            raise ValueError(
                f"Colunas esperadas {expected_cols}, mas encontrado {set(df.columns)}"
            )

        # Converter colunas
        df["data"] = pd.to_datetime(df["data"], errors="coerce")
        df["vendas"] = pd.to_numeric(df["vendas"], errors="coerce").fillna(0)

        return df

    except Exception as e:
        raise RuntimeError(f"Erro ao carregar dados do Excel: {str(e)}") from e
