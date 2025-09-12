from pptx.chart.data import CategoryChartData
from pptx import Presentation
from app.graphs.base_graph import BaseGraph

class MonthlySalesGraph(BaseGraph):
    """
    Gráfico de vendas mensais (Página 3).
    Atualiza o gráfico existente no template pelo nome padronizado.
    """

    CHART_NAME = "Chart_Mensal"

    def filter_data(self):
        """
        Agrupa os dados por mês e soma as vendas.
        """
        self.filtered_data = (
            self.data.groupby(self.data["data"].dt.to_period("M"))["vendas"]
            .sum()
            .reset_index()
        )
        # Converte Period para string para usar como categorias
        self.filtered_data["data"] = self.filtered_data["data"].astype(str)

    def update_chart(self):
        for slide in self.ppt.slides:
            for shape in slide.shapes:
                if shape.has_chart and shape.name == self.CHART_NAME:
                    chart_data = CategoryChartData()
                    chart_data.categories = self.filtered_data["data"]
                    chart_data.add_series(
                        "Vendas", self.filtered_data["vendas"]
                    )
                    shape.chart.replace_data(chart_data)
                    return
        raise ValueError(f"Gráfico '{self.CHART_NAME}' não encontrado no template.")
