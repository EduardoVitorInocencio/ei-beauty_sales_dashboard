import pytest
import pandas as pd
from app.data.data_loader import load_data
import os

def test_load_data_success(tmp_path):
    # Cria um Excel temporário com dados de teste
    df_test = pd.DataFrame({
        "produto": ["Produto A", "Produto B"],
        "regiao": ["Norte", "Sul"],
        "data": ["2025-01-01", "2025-01-02"],
        "vendas": [100, 200]
    })
    file_path = tmp_path / "test.xlsx"
    df_test.to_excel(file_path, index=False)

    df_loaded = load_data(str(file_path))

    assert isinstance(df_loaded, pd.DataFrame)
    assert set(["produto", "regiao", "data", "vendas"]).issubset(df_loaded.columns)
    assert df_loaded["vendas"].sum() == 300

def test_load_data_missing_column(tmp_path):
    df_test = pd.DataFrame({
        "produto": ["Produto A"],
        "data": ["2025-01-01"],
        "vendas": [100]
    })
    file_path = tmp_path / "test_missing.xlsx"
    df_test.to_excel(file_path, index=False)

    with pytest.raises(RuntimeError) as e_info:
        load_data(str(file_path))
    assert "Colunas esperadas" in str(e_info.value)

