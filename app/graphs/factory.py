from app.graphs.product_sales import ProductSalesGraph

from pptx import Presentation
import pandas as pd


class GraphFactory:

    @staticmethod
    def create_graph(page_number: int, ppt: Presentation):
        if page_number == 1:
            return ProductSalesGraph(ppt)
        

