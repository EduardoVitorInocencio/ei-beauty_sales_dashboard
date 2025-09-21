from pptx.chart.data import CategoryChartData
from pptx import Presentation
from app.graphs.base_graph import BaseGraph

class ProductSalesGraph(BaseGraph):
    """
    Gráfico de vendas por produto (Página 1).
    Atualiza o gráfico existente no template pelo nome padronizado.
    """

    CHART_NAME = "Chart_Produto"  # Nome do gráfico no template

    # Filtros fixos
    FILTERS = {
        "formats": "T. Embalagens",
        "region": "Total Brasil",
        "channels": "Hipermercados",
        "periods": "YTD Dec-20",
        "brands": "Coca-Cola Cia"
    }

    # Colunas que queremos no DataFrame final
    SELECT_COLS = [
        "units","value_(r$)","weighted_hholds","weighted_buyers","penetration_(%)",
        "units_per_buyer","spend_per_buyer_(r$)","units_per_trip","spend_per_trip",
        "frequency","avg_price_per_unit"
    ]

    COLS_RENAME = {
        "units": "Units",
        "value_(r$)": "Value_(R$)",
        "weighted_hholds": "Weighted_HHOLDS",
        "weighted_buyers": "Weighted_Buyers",
        "penetration_(%)": "Penetration_(%)",
        "units_per_buyer": "Units_per_Buyer",
        "spend_per_buyer_(r$)": "Spend_per_Buyer_(R$)",
        "units_per_trip": "Units_per_Trip",
        "spend_per_trip": "Spend_per_Trip",
        "frequency": "Frequency",
        "avg_price_per_unit": "Avg_Price_per_Unit"
    }

    def filter_data(self):
        """
        Aplicar os filtros e selecionar/renomear as colunas desejadas.
        """
        df = self.data.copy()

        for col, val in self.FILTERS.items():
            df = df[df[col] == val]

    def update_chart(self):
        """
        Atualiza o gráfico existente no template pelo nome.
        """
        for slide in self.ppt.slides:
            for shape in slide.shapes:
                if shape.has_chart and shape.name == self.CHART_NAME:
                    chart_data = CategoryChartData()
                    chart_data.categories = self.filtered_data["produto"]
                    chart_data.add_series(
                        "Vendas", self.filtered_data["vendas"]
                    )
                    shape.chart.replace_data(chart_data)
                    return  # Sai após atualizar o gráfico
        # Se chegar aqui, o gráfico não foi encontrado
        raise ValueError(f"Gráfico '{self.CHART_NAME}' não encontrado no template.")
