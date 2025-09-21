import os
from app.services.template_service import update_template

if __name__ == "__main__":
    # Caminhos fixos (ajuste conforme seu projeto)
    data_path = "dados/vendas_produtos.xlsx"  # Excel de exemplo
    template_path = "templates/template_vendas.pptx"
    output_path = "templates/template_vendas_atualizado.pptx"

    # Verifica se os arquivos existem
    if not os.path.exists(data_path):
        print(f"Arquivo de dados não encontrado: {data_path}")
        exit(1)
    if not os.path.exists(template_path):
        print(f"Template não encontrado: {template_path}")
        exit(1)

    # Atualiza o template
    updated_file = update_template(data_path, template_path, output_path)
    # try:
    #     print(f"Template atualizado com sucesso! Arquivo salvo em: {updated_file}")
    # except Exception as e:
    #     print(f"Erro ao atualizar template: {e}")
