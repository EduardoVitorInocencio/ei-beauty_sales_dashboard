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
        expected_cols = {
                        "formats","region","channels","periods","brands","units","value_(r$)",
                        "weighted_hholds","weighted_buyers","penetration_(%)","units_per_buyer",
                        "spend_per_buyer_(r$)","units_per_trip","spend_per_trip","frequency",
                        "avg_price_per_unit"
                        }
        if not expected_cols.issubset(set(df.columns)):
            raise ValueError(
                f"Colunas esperadas {expected_cols}, mas encontrado {set(df.columns)}"
            )

        # Converter colunas

        return df

    except Exception as e:
        raise RuntimeError(f"Erro ao carregar dados do Excel: {str(e)}") from e
