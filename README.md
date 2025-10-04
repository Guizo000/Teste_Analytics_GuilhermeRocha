# Teste_Analytics_GuilhermeRocha

## OBJETIVO 
Este repositório contém a resolução das tarefas propostas no Teste para Estagiário de Analytics da Quod. O projeto cobre todas as etapas do pipeline de análise de dados: **simulação e limpeza de dados (Python)**, **análise e visualização (Python)**, **consultas em SQL** e a **interpretação de resultados** com foco na extração de *insights* estratégicos de negócio.

## ESTRUTURA 
```
├── src/  
│   ├── simulacao_vendas.py       # Script de simulação e geração do dataset  
│   ├── graficos_vendas.py        # Script de análises gráficas e exploração   
│   └── data_clean.csv            # Dataset limpo gerado por simulacao_vendas.py  
├── docs/  
│   ├── relatorio_insights.pdf    # Relatório final (até 300 palavras)  
│   └── respostas_textuais.docx   # Respostas textuais adicionais  
├── consultas_sql.sql             # Consultas SQL   
└── README.md                     # Este documento
```

## COMO EXECUTAR
Para executar os scripts faça:
1. Baixe a pasta src ou clone o repositório:

     ```
     git clone https://github.com/guizo000/Teste_Analytics_Guilherme.git
     cd Teste_Analytics_GuilhermeRocha/src
     ```
2. Instale as dependências:
   
    ```
    pip install pandas numpy matplotlib
    ```
3. Na pasta src execute o script de geração do dataset:

   ```
   python simulacao_vendas.py
   ```
4. Execute o script de visualização dos gráficos:
    ```
   python graficos_vendas.py
   ```
## FERRAMENTAS UTILIZADAS
- Python 3.12.3
- Pandas para manipulação de dados.
- NumPy para geração de dados aleatórios.
- Matplotlib para visualização gráfica.
- SQL para consultas.
  
## OBSERVAÇÕES
 - Embora a Parte 2 solicitasse a identificação do produto com menor venda em Junho de 2024, o dataset simulado (Parte 1) contém dados apenas de 2023. Para manter a conformidade dos dados, a query no arquivo consultas_sql.sql foi corrigida para utilizar o período de Junho de 2023, e a lógica foi detalhada nos comentários do script.
