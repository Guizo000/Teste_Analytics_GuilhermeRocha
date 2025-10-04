import numpy as np
import pandas as pd

#Quantidade de linhas do dataset
qtd_linhas = 500
#Definição de seed para resultados previsíveis
np.random.seed(0)

#Categorias de produtos
categorias = ["Avançado", "Intermediário", "Entrada"]
#Produtos disponíveis em cada categoria
categorias_produtos = {
    "Avançado": ["Samsung S20 Ultra", "Redmi Note 16 Pro", "Moto G80 Plus"],
    "Intermediário": ["Samsung A15", "Redmi Note 14 Pro", "Moto G35"],
    "Entrada": ["Samsung M10 Plus", "Redmi Note 10", "Moto G10 Plus"]
}
#Gerando lista com todos os produtos
produtos = []
for i in categorias_produtos.values():
    produtos += i

#Gerando os precos individuais de cada produto em um dicionário de acordo com a categoria a qual pertence
produtos_precos = {
    p: np.random.randint(800, 2000) if categorias_produtos["Entrada"].__contains__(p)
    else (np.random.randint(2001, 3500) if categorias_produtos["Intermediário"].__contains__(p)
    else np.random.randint(3501, 5000))
    for p in produtos
}

#Gerando as listas que servirão como colunas no dataset
dados_categorias = np.random.choice(categorias, qtd_linhas)
dados_produtos = [(np.random.choice(categorias_produtos[i])) for i in dados_categorias]
dados_precos = [produtos_precos[i] for i in dados_produtos]
dados_id = np.arange(1, qtd_linhas+1)
dados_datas = pd.to_datetime(np.random.choice(pd.date_range("2023-01-01", "2023-12-31"), qtd_linhas))
dados_qtd = np.random.randint(1, 3, qtd_linhas)

#Dicionário para geração do dataset
dados = {
    "Id": dados_id,
    "Data": dados_datas,
    "Produto": dados_produtos,
    "Categoria": dados_categorias,
    "Quantidade": dados_qtd,
    "Preco": dados_precos
}

df = pd.DataFrame(dados)

###LIMPEZA DE DADOS
#Conversão de dados 
df["Data"] = pd.to_datetime(df["Data"])
df["Quantidade"] = pd.to_numeric(df["Quantidade"])
df["Preco"] = pd.to_numeric(df["Preco"])
#Remoção de duplicatas
df = df.drop_duplicates()
#Tratamento de valores faltantes
df = df.dropna()
#Cria arquivo .csv com dataset limpo
df.to_csv("data_clean.csv")

###Análises
##Calcula o total de vendas por produto
#Agrupa por produto somando a quantidade,
#Agrupa por produto fazendo a média dos preços (o que retorna o próprio preço de cada produto)
#E depois multiplica os dois
total_vendas_produto = df.groupby("Produto")["Quantidade"].sum() * df.groupby("Produto")["Preco"].mean()

##Retorna o produto com o maior número de vendas
#Agrupa por produto somando a quantidade,
#e retorna o valor máximo desse agrupamento
tendencia_vendas_max = df.groupby("Produto")["Quantidade"].sum().idxmax()

print(f"\nTOTAL DE VENDAS POR PRODUTO: \n {total_vendas_produto} \n")
print(f"PRODUTO COM MAIOR NÚMERO DE VENDAS: {tendencia_vendas_max}\n")

