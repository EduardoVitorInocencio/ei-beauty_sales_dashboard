import pytest
import pandas as pd
from app.graphs.product_sales import ProductSalesGraph
from app.graphs.region_sales import RegionSalesGraph
from app.graphs.monthly_sales import MonthlySalesGraph
from pptx import Presentation

def mock_ppt():
    # Apenas um PPT vazio para passar no construtor
    return Presentation()

def test_product_sales_filter():
    df = pd.DataFrame({
        "produto": ["A", "A", "B"],
        "regiao": ["N", "S", "N"],
        "data": pd.to_datetime(["2025-01-01", "2025-01-02", "2025-01-01"]),
        "vendas": [10, 20, 30]
    })
    ppt = mock_ppt()
    graph = ProductSalesGraph(df, ppt)
    graph.filter_data()
    assert graph.filtered_data["vendas"].sum() == 60
    assert "produto" in graph.filtered_data.columns

def test_region_sales_filter():
    df = pd.DataFrame({
        "produto": ["A", "B"],
        "regiao": ["N", "S"],
        "data": pd.to_datetime(["2025-01-01", "2025-01-02"]),
        "vendas": [10, 20]
    })
    ppt = mock_ppt()
    graph = RegionSalesGraph(df, ppt)
    graph.filter_data()
    assert graph.filtered_data["vendas"].sum() == 30
    assert "regiao" in graph.filtered_data.columns

def test_monthly_sales_filter():
    df = pd.DataFrame({
        "produto": ["A", "B"],
        "regiao": ["N", "S"],
        "data": pd.to_datetime(["2025-01-01", "2025-02-01"]),
        "vendas": [10, 20]
    })
    ppt = mock_ppt()
    graph = MonthlySalesGraph(df, ppt)
    graph.filter_data()
    assert graph.filtered_data["vendas"].sum() == 30
    assert "data" in graph.filtered_data.columns
