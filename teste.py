import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('esgotarpilhas.csv')
df['date'] = pd.to_datetime(df['no'], format='%H:%M:%S')
del df['hora']
del df['func']
del df['unidade']
del df['auto']
del df['no']

# Tirando dados gerais
# print(df.head())
# print(df.describe())
"""
            valor
count  65535.000000 (itens)
mean      14.821530 (media)
std        5.866914 (desvio padrão)
min        2.000000 (menor valor)
25%       15.000000 (Q1)
50%       15.000000 (Q2)
75%       19.000000 (Q3)
max       24.000000 (maior valor)
"""

df.plot(x='date') # todos os dados em seus horarios

# Tirando dados por minutoXvalor em cada hora
df = df.groupby([df['date'].dt.to_period('H'), 'valor']).count().unstack()


df.columns = df.columns.droplevel()
df.plot(kind='bar')

"""
Observações sobre o problema na geração dos dados.

Só o foram pegas %H:%M:%S, para ter uma tratamento mais limpo,
    seriam necessarios os timestamps completos.
"""


plt.show()
