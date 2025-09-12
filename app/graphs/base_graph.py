from abc import ABC, abstractmethod
import pandas as pd
from pptx import Presentation

class BaseGraph(ABC):
    """
    Classe base para todos os gráficos.
    Fornece a interface padrão para filtrar dados e atualizar gráficos existentes no template.
    """

    def __init__(self, data: pd.DataFrame, ppt: Presentation):
        """
        Args:
            data (pd.DataFrame): Dados de vendas carregados.
            ppt (Presentation): Objeto Presentation do template PowerPoint.
        """
        self.data = data
        self.ppt = ppt
        self.filtered_data = None

    @abstractmethod
    def filter_data(self):
        """
        Método para aplicar filtros específicos do gráfico.
        Cada gráfico deve sobrescrever este método.
        """
        pass

    @abstractmethod
    def update_chart(self):
        """
        Método para atualizar os dados do gráfico no slide.
        Cada gráfico deve sobrescrever este método.
        """
        pass
