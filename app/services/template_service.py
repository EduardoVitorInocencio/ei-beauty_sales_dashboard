import os
from pptx import Presentation
from app.data.data_loader import load_data
from app.graphs.factory import GraphFactory
import pandas as pd

def update_template(data_path: str, template_path: str, output_path: str):
    """
    Atualiza os gráficos do template PowerPoint com os dados de vendas.

    Args:
        data_path (str): Caminho para o Excel com os dados.
        template_path (str): Caminho para o template PowerPoint existente.
        output_path (str): Caminho para salvar o template atualizado.

    Returns:
        str: Caminho do arquivo atualizado.
    """
    # 1. Carregar dados
    data = load_data(data_path)

    # 2. Abrir template existente
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template não encontrado em {template_path}")
    ppt = Presentation(template_path)

    # 3. Atualizar gráficos página por página (1 a 3)
    for page_number in range(1, 6):  # páginas 1 a 5
        graph = GraphFactory.create_graph(page_number, data, ppt)
        graph.filter_data()
        graph.update_chart()


    # 4. Salvar template atualizado
    ppt.save(output_path)
    print(f"Template atualizado salvo em: {output_path}")

    return output_path
