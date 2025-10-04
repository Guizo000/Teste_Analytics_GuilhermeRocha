import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style


###Cores e estilo usado nas plotagens
style.use("fivethirtyeight")
cores_categorias = ['#00BCD4', '#FF9800', '#CDDC39'] 
cores_avancado = ['#00BCD4', '#0097A7', '#007985']
cores_intermediario = ['#CDDC39', '#AFB42B', '#827717']
cores_entrada = ['#FF9800', '#FB8C00', '#F57C00']


#Lendo o dataset, usando o argumento parse_dates 
#para converter tipo da coluna data para datetime
#(por padrão vem como string)
df = pd.read_csv("data_clean.csv", parse_dates=["Data"])


###FIGURE 1
plt.figure(1, figsize=(8, 7))
plt.suptitle("Tendência de Vendas Mensal")

##GRÁFICO TENDÊNCIA DE VENDAS POR MÊS 
#Converte a coluna data em período para agrupamento por mês
tendencia_vendas_mes = df.groupby(df["Data"].dt.to_period("M"))["Quantidade"].sum()
#Converte o index do total de vendas(as datas) para datetime denovo
#para poder plotar
tendencia_vendas_mes.index = tendencia_vendas_mes.index.to_timestamp()
#Plota a linha
plt.plot(tendencia_vendas_mes.index, tendencia_vendas_mes.values, c = 'red')
#Espalha os pontos para melhor visualização
plt.scatter(tendencia_vendas_mes.index, tendencia_vendas_mes.values, c = 'blue', zorder=3)
plt.title("Tendência de Vendas Mensal (2023)", fontsize=13)
plt.xlabel("Mês", fontsize=13)
plt.ylabel("Quantidade Vendida", fontsize=13)


###FIGURE 2
plt.figure(2, figsize=(13, 7))
plt.suptitle("Comparação de Categorias")

##GRÁFICO QUANTIDADE DE VENDAS POR CATEGORIA - GRÁFICO 1
#Retorna a quantidade de vendas por categoria
quantidade_vendas_categoria = df.groupby("Categoria")["Quantidade"].sum()
#Reordena o index para ficar na ordem desejada
quantidade_vendas_categoria = quantidade_vendas_categoria.reindex(["Avançado", "Intermediário", "Entrada"])

plt.subplot(1, 2, 1)
plt.bar(quantidade_vendas_categoria.index, quantidade_vendas_categoria.values, width=.5, color=cores_categorias)
plt.title("Quantidade Total de Vendas por Categoria (2023)", fontsize=13)
plt.xlabel("Categorias", fontsize=13)
plt.ylabel("Quantidade Vendida", fontsize=13)

##GRÁFICO TOTAL DE VENDAS POR CATEGORIA - GRÁFICO 2
#Retorna o total de vendas (faturamento) por categoria
total_vendas_categoria = df.groupby(["Categoria", "Produto"])["Quantidade"].sum() * df.groupby(["Categoria", "Produto"])["Preco"].mean()
total_vendas_categoria = total_vendas_categoria.groupby("Categoria").sum()
#Reordena o index para ficar na ordem desejada
total_vendas_categoria = total_vendas_categoria.reindex(["Avançado", "Intermediário", "Entrada"])

plt.subplot(1, 2, 2)
plt.bar(total_vendas_categoria.index, total_vendas_categoria.values/1000000, width=.5, color=cores_categorias)
plt.title("Total de Vendas por Categoria (2023) (em R$ Milhões)", fontsize=13)
plt.xlabel("Categorias", fontsize=13)
plt.ylabel("Faturamento (em R$ Milhões)", fontsize=13)

ticks_faturamento = np.arange(0, 1.3, 0.1)
plt.yticks(ticks_faturamento, [f"R${x:.1f}M" for x in ticks_faturamento])


###FIGURE 3
plt.figure(3, figsize=(13, 6.5))
plt.suptitle("Vendas por Produto em Cada Categoria")
#Retorna a quantidade de vendas de agrupada por categoria e produto
quantidade_vendas_categoria_produto = df.groupby(["Categoria", "Produto"])["Quantidade"].sum()

##GRÁFICO QUANTIDADE DE VENDAS POR PRODUTO EM CADA CATEGORIA - AVANÇADO
#Retorna a quantidade de vendas dos produtos da categoria Avançado
quantidade_vendas_avancado = quantidade_vendas_categoria_produto["Avançado"]
plt.subplot(2, 2, 1)
plt.bar(quantidade_vendas_avancado.index, quantidade_vendas_avancado.values, width=.5, color=cores_avancado)
plt.title("Quantidade Vendida por Produto – Categoria Avançado (2023)", fontsize=13)
plt.xlabel("Produtos", fontsize=13)
plt.ylabel("Quantidade Vendida", fontsize=13)

##GRÁFICO QUANTIDADE DE VENDAS POR PRODUTO EM CADA CATEGORIA - INTERMEDIÁRIO
#Retorna a quantidade de vendas dos produtos da categoria Intermediário
quantidade_vendas_intermediario = quantidade_vendas_categoria_produto["Intermediário"]
plt.subplot(2, 2, 2)
plt.bar(quantidade_vendas_intermediario.index, quantidade_vendas_intermediario.values, width=.5, color=cores_intermediario)
plt.title("Quantidade Vendida por Produto – Categoria Intermediário (2023)", fontsize=13)
plt.xlabel("Produtos", fontsize=13)
plt.ylabel("Quantidade Vendida", fontsize=13)

##GRÁFICO QUANTIDADE DE VENDAS POR PRODUTO EM CADA CATEGORIA - ENTRADA
#Retorna a quantidade de vendas dos produtos da categoria Entrada
quantidade_vendas_entrada = quantidade_vendas_categoria_produto["Entrada"]
plt.subplot(2, 2, 3)
plt.bar(quantidade_vendas_entrada.index, quantidade_vendas_entrada.values, width=.5, color=cores_entrada)
plt.title("Quantidade Vendida por Produto – Categoria Entrada (2023)", fontsize=13)
plt.xlabel("Produtos", fontsize=13)
plt.ylabel("Quantidade Vendida", fontsize=13)


#Mostra o gráfico e ajusta o layout para evitar sobreposição
plt.tight_layout()
plt.show()