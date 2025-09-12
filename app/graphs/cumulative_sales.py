from pptx.chart.data import CategoryChartData
from pptx import Presentation
from app.graphs.base_graph import BaseGraph
import pandas as pd

class CumulativeSalesGraph(BaseGraph):
    """
    Gráfico de vendas acumuladas ao longo do tempo.
    """

    CHART_NAME = "Chart_Cumulative_Sales"  # Nome do gráfico no template

    def filter_data(self):
        """
        Calcula o valor acumulado de vendas por data.
        """
        # Garante que a coluna data seja datetime
        self.data["data"] = pd.to_datetime(self.data["data"])
        df = self.data.groupby("data")["vendas"].sum().sort_index().cumsum().reset_index()
        self.filtered_data = df

    def update_chart(self):
        """
        Atualiza o gráfico existente no template pelo nome.
        """
        for slide in self.ppt.slides:
            for shape in slide.shapes:
                if shape.has_chart and shape.name == self.CHART_NAME:
                    chart_data = CategoryChartData()
                    chart_data.categories = self.filtered_data["data"].dt.strftime("%Y-%m-%d")
                    chart_data.add_series(
                        "Vendas Acumuladas", self.filtered_data["vendas"]
                    )
                    shape.chart.replace_data(chart_data)
                    return
        raise ValueError(f"Gráfico '{self.CHART_NAME}' não encontrado no template.")
