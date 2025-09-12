# 💄 Beauty Sales Dashboard

**Atualização automatizada de gráficos em PowerPoint a partir de dados de vendas de produtos de beleza.**

Este projeto fornece uma solução **flexível, escalável e extensível** para atualizar dashboards existentes de PowerPoint com dados do Excel. Ele utiliza o **Factory Pattern** para facilitar a adição de novos gráficos e está preparado para integração via **API FastAPI**.

---

## 📂 Estrutura do Projeto

```
beauty_sales_dashboard/
│
├── app/
│   ├── main.py                 # Ponto de entrada da API
│   ├── config.py               # Configurações globais
│   │
│   ├── data/
│   │   └── data_loader.py      # Carregamento e validação do Excel
│   │
│   ├── graphs/
│   │   ├── base_graph.py       # Classe base para todos os gráficos
│   │   ├── product_sales.py    # Gráfico de vendas por produto
│   │   ├── region_sales.py     # Gráfico de vendas por região
│   │   ├── monthly_sales.py    # Gráfico de vendas mensais
│   │   ├── regional_share.py   # Gráfico de participação percentual por região
│   │   ├── cumulative_sales.py # Gráfico de vendas acumuladas
│   │   └── factory.py           # Factory para criação de gráficos
│   │
│   ├── services/
│   │   └── template_service.py # Lógica de atualização do PowerPoint
│   │
│   └── utils/
│       └── pptx_helpers.py     # Funções auxiliares para PowerPoint
│
├── templates/
│   └── template_vendas.pptx    # Template PowerPoint base
│
├── scripts/
│   └── update_template.py      # Script executável para atualização local
│
├── tests/
│   ├── test_data_loader.py
│   ├── test_graphs.py
│   └── test_update_template.py
│
├── requirements.txt
└── README.md
```

---

## ⚡ Fluxo da Aplicação

1. **Carregamento de Dados (Excel)**

   * O `data_loader.py` lê o Excel e normaliza colunas (`produto`, `regiao`, `data`, `vendas`).
   * Valida se todas as colunas necessárias estão presentes.

2. **Criação de Gráficos (Factory Pattern)**

   * Cada gráfico herda de `BaseGraph` e implementa `filter_data()` e `update_chart()`.
   * Exemplo de gráficos disponíveis:

     * Vendas por produto (Página 1)
     * Vendas por região (Página 2)
     * Vendas mensais (Página 3)
     * Participação percentual por região (Página 4)
     * Vendas acumuladas ao longo do tempo (Página 5)
   * O `GraphFactory` cria a classe correta com base no número da página.

3. **Atualização do Template PowerPoint**

   * `template_service.py` abre o template existente (`template_vendas.pptx`).
   * Itera por todas as páginas (1 a 5), criando cada gráfico via Factory.
   * Aplica `filter_data()` e `update_chart()` para atualizar os dados.
   * Salva o arquivo atualizado em `templates/template_vendas_atualizado.pptx`.

4. **Execução Local**

   * `scripts/update_template.py` permite rodar todo o fluxo via terminal:

     ```bash
     python -m scripts.update_template
     ```
   * Verifica a existência dos arquivos e imprime mensagens de sucesso ou erro.

5. **Integração API (FastAPI)**

   * O projeto já está preparado para rodar como **API**, aceitando uploads de Excel e retornando o PPTX atualizado.
   * Facilita integração em sistemas web ou dashboards automáticos.

6. **Testes Automatizados**

   * Testes unitários com `pytest` para cada módulo:

     * Data Loader (`test_data_loader.py`)
     * Gráficos (`test_graphs.py`)
     * Template Service (`test_update_template.py`)
   * Os testes usam arquivos temporários para **não depender de dados reais**, garantindo segurança e reprodutibilidade.

---

## 🛠 Tecnologias Utilizadas

* **Python 3.12**
* **pandas** – manipulação de dados
* **python-pptx** – atualização de gráficos PowerPoint
* **pytest** – testes automatizados
* **FastAPI** – API para integração futura

---

## 🚀 Como Executar

1. Ative o ambiente virtual:

```bash
venv\Scripts\activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Execute o script de atualização:

```bash
python -m scripts.update_template
```

4. Para rodar os testes:

```bash
pytest -v
```

5. Para rodar a API (quando implementada):

```bash
uvicorn app.main:app --reload
```

---

## 💡 Extensibilidade

* **Adicionar novos gráficos:**

  * Criar uma classe que herda de `BaseGraph`.
  * Implementar `filter_data()` e `update_chart()`.
  * Adicionar a classe no `GraphFactory`.

* **Alterar template:**

  * Adicionar gráficos no PPTX com nomes padronizados.
  * Atualizar o `CHART_NAME` na classe correspondente.

* **API e automação:**

  * Pode receber arquivos Excel via upload.
  * Retornar PPTX atualizado automaticamente.

---

## 📈 Benefícios

* Totalmente **modular e escalável**
* **Não depende de template fixo** – apenas nomes padronizados
* **Testes automatizados** garantem confiabilidade
* Fácil integração com dashboards e ferramentas externas

---
