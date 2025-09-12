from app.graphs.product_sales import ProductSalesGraph
from app.graphs.region_sales import RegionSalesGraph
from app.graphs.monthly_sales import MonthlySalesGraph
from app.graphs.regional_share import RegionalShareGraph
from app.graphs.cumulative_sales import CumulativeSalesGraph
from pptx import Presentation
import pandas as pd


class GraphFactory:

    @staticmethod
    def create_graph(page_number: int, data: pd.DataFrame, ppt: Presentation):
        if page_number == 1:
            return ProductSalesGraph(data, ppt)
        elif page_number == 2:
            return RegionSalesGraph(data, ppt)
        elif page_number == 3:
            return MonthlySalesGraph(data, ppt)
        elif page_number == 4:
            return RegionalShareGraph(data, ppt)
        elif page_number == 5:
            return CumulativeSalesGraph(data, ppt)
        else:
            raise ValueError(f"Página {page_number} inválida. Somente 1 a 5 são permitidos.")

