import pandas as pd

#1- Leitura e importação da tabela
df = pd.read_excel (r'C:\Users\ALUNO.LAB01-PC-01\Desktop\Diego\pi.py\Pandas\Vendas - Dez.xls')
#Imprimir as 3 linhas da tabela 
#print(df.head())
#2- Quantidade de linhas e colunas da tabela
#print(df.shape)
#3- Imprimir coluna data, produto e quantidade
#dpq = df [['Data','Produto','Quantidade']]
#print(dpq)
#4- Imprimir todas as vendas do produto casaco listrado
#print(df.loc[df['Produto']=='Casaco Listrado'])
#5- Imprimir todas as vendas do produto “Camisa Listrado" que ocorreram entre o dia 1 e 10 de dezembro
#s_data = '12-1-2019'
#f_data = '12-10-2019'
#print(df.loc[(df['Produto']== 'Camisa Listrado') & (df['Data'] > s_data) & (df['Data'] < f_data)])
#6- Imprimir todas as vendas do produto “Tênis Linho” ocorridas na loja “Shopping Morumbi”
#print(df.loc[(df['Produto']== 'Tênis Linho') & (df['ID Loja'] == 'Shopping Morumbi')])
#7- Imprimir todas as vendas que tenham ultrapassado o valor de 100 reais;
#print(df.loc[df['Valor Final'] > 100])
#8 - Imprimir todas as vendas da loja “Iguatemi Campinas” inferiores a 120 reais;
#print(df.loc[(df['ID Loja'] == 'Iguatemi Campinas') & (df['Valor Final'] < 120)])
#9 - Imprimir apenas as colunas “data”, “produto” e “Valor Final” de todas as vendas ocorridas entre o dia 1 e 15 da loja “Norte Shopping”;
#print(df.loc[(df['Data'] > '12-1-2019') & (df['Data'] < '12-15-2019') & (df['ID Loja'] == 'Norte Shopping'),['Data','Produto','Valor Final']])
#10 - Imprimir a coluna “Produto” de todos os produtos que possuam o valor unitário superior a 50 reais;
#print(df.loc[df['Valor Unitário'] > 50,['Produto']])
#11 - Imprimir todas as vendas que tenham valor inferior a 60 reais;
#print(df.loc[df['Valor Final'] < 60])
#12 - Imprimir todas as vendas do produto “Calça” ocorridos na loja “Palladium Shopping Curitiba";
#print(df.loc[(df['Produto'] == 'Calça') & (df['ID Loja'] == 'Palladium Shopping Curitiba')])
#13 - Imprimir todas todas as vendas ocorridas no dia 7 de dezembro que ultrapassem o valor de 500 reais;
#print(df.loc[(df['Valor Final'] > 500) & (df['Data'] == '12-7-2019')])
#14 - Imprimir todos os produtos que foram vendidos na loja “Rio Mar Recife”;
#print(df.loc[df['ID Loja']=='Rio Mar Recife'])
#15 - 15 - Imprimir a coluna “Produto” de todas as vendas com quantidade superior a 4 unidades; 
#print(df.loc[df['Quantidade'] > 4])



