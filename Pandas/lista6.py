import pandas as pd
import numpy as np
df = pd.read_excel (r'C:\Users\ALUNO.LAB01-PC-01\Desktop\Diego\pi.py\Pandas\Vendas - Dez.xls')

#1- 
#3- 
#4- 
new_df = df.assign(Desconto = 0.15,V_ComDesconto = 0, Vendedor = 'Diego', Estoque_Atual = 100)
#print(new_df['Desconto'])

#2- 
new_df['V_ComDesconto'] = new_df['Valor Final'] * (1 - new_df['Desconto'])

#5- 
df_index = list(df.index)
indexs = np.random.choice(df_index,20)
new_df2 = df.iloc[indexs]
#print(new_df2)

#6-
new_df.loc[df['Código Venda'] == 65017,'Quantidade'] = 3
new_df.loc[df['Código Venda'] == 65017,'Valor Final'] = (new_df['Quantidade'] * new_df['Valor Unitário']) 
new_df.loc[df['Código Venda'] == 65017,'V_ComDesconto'] = (new_df['Valor Final']) * (1 - new_df['Desconto'])
#print(new_df.loc[df['Código Venda'] == 65017])

#7-
new_df.loc[df['Código Venda'] == 65027,'Quantidade'] = 15
new_df.loc[df['Código Venda'] == 65027,'Valor Final'] = (new_df['Quantidade'] * new_df['Valor Unitário']) 
new_df.loc[df['Código Venda'] == 65027,'V_ComDesconto'] = (new_df['Valor Final']) * (1 - new_df['Desconto'])
#print(new_df.loc[df['Código Venda'] == 65027])

#8-
new_df.loc[df['Código Venda'] == 65027,'Quantidade'] = 5
new_df.loc[df['Código Venda'] == 65027,'Valor Final'] = (new_df['Quantidade'] * new_df['Valor Unitário']) 
new_df.loc[df['Código Venda'] == 65027,'V_ComDesconto'] = (new_df['Valor Final']) * (1 - new_df['Desconto'])
#print(new_df.loc[df['Código Venda'] == 65027])

#9-
new_df = new_df.assign(Nome = 'Diego')
#print(new_df)
new_df = new_df.drop(['Nome'], axis=1)
#print(new_df)

#10-
new_df = new_df.assign(Nome_Cliente = 'Diego')
#print(new_df)
new_df = new_df.drop(['Nome_Cliente'], axis=1)
#print(new_df)

#11-
#print(produto[produto['Produto'] == 'Mochila Estampa'].groupby('Produto').count())

#12-
#print(produto[produto['ID Loja'] == 'Bourbon Shopping SP'].groupby('ID Loja').count())

#13-
#print(produto[produto['Valor Final'] == 1000].groupby('Valor Final').count())

#14-
#print(produto[produto['Data'] == '2019-12-01'].groupby('Data').count())

#15-
#print(produto[produto['Produto'] == 'Mochila Xadrez'].groupby('Produto').count())

