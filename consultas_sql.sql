-- Total de vendas de cada produto (Quantidade * Preço) em ordem decrescente
-- Seleção das colunas a serem mostradas
SELECT 
    Produto,
    Categoria,
    --Soma da quantidade * preço para obter o total de vendas para cada produto
    SUM(Quantidade * Preco) AS Total_Vendas
-- Especificando em qual tabela deve ser feita a query
FROM vendas
-- Agrupando por produto e categoria (para poder usar no select
-- porque toda coluna que nao ta em função deve ser usada 
-- no agrupamento para ser selecionada)
GROUP BY Produto, Categoria
-- Ordenando em ordem decrescente pelo total de vendas
ORDER BY Total_Vendas DESC;


-- Produto com menor quantidade de vendas no mês de Junho de 2023
-- (no arquivo word ta 2024 mas os dados gerados na simulação com python 
-- estão em 2023 então mantive 2023)
SELECT 
    Produto,
    Categoria,
    SUM(Quantidade) AS Total_Unidades_Vendidas
FROM vendas
-- Especificando o range de datas
WHERE Data BETWEEN '2023-06-01' AND '2023-06-30'
GROUP BY Produto, Categoria
-- Ordena em ordem ascendente de modo que a primeira
-- linha contenha o produto com menor quantidade de vendas
ORDER BY Total_Unidades_Vendidas ASC;
-- Usamos limit 1 para retornar apenas a primeira linha
LIMIT 1
