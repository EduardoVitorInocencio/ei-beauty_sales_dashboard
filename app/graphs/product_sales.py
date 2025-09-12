from pptx.chart.data import CategoryChartData
from pptx import Presentation
from app.graphs.base_graph import BaseGraph

class ProductSalesGraph(BaseGraph):
    """
    Gráfico de vendas por produto (Página 1).
    Atualiza o gráfico existente no template pelo nome padronizado.
    """

    CHART_NAME = "Chart_Produto"  # Nome do gráfico no template

    def filter_data(self):
        """
        Agrupa os dados por produto e soma as vendas.
        """
        self.filtered_data = (
            self.data.groupby("produto")["vendas"]
            .sum()
            .reset_index()
        )

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
