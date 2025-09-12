from pptx.chart.data import CategoryChartData
from pptx import Presentation
from app.graphs.base_graph import BaseGraph

class RegionalShareGraph(BaseGraph):
    """
    Gráfico de participação percentual de vendas por região.
    """

    CHART_NAME = "Chart_Share_Regiao"  # Nome do gráfico no template

    def filter_data(self):
        """
        Calcula a participação percentual das vendas por região.
        """
        grouped = self.data.groupby("regiao")["vendas"].sum().reset_index()
        total = grouped["vendas"].sum()
        grouped["participacao"] = grouped["vendas"] / total * 100
        self.filtered_data = grouped

    def update_chart(self):
        """
        Atualiza o gráfico existente no template pelo nome.
        """
        for slide in self.ppt.slides:
            for shape in slide.shapes:
                if shape.has_chart and shape.name == self.CHART_NAME:
                    chart_data = CategoryChartData()
                    chart_data.categories = self.filtered_data["regiao"]
                    chart_data.add_series(
                        "Participação (%)", self.filtered_data["participacao"]
                    )
                    shape.chart.replace_data(chart_data)
                    return
        raise ValueError(f"Gráfico '{self.CHART_NAME}' não encontrado no template.")
