
# coding: utf-8

# In[34]:




import pandas as pd
from datetime import datetime
import matplotlib

get_ipython().magic('matplotlib inline')


df = pd.read_csv('data/teste.csv', sep=';')

df['hora'] = pd.to_datetime(df.hora)

df['horario'] = df.hora.dt.time

df['valores'] = df.valor.values

df.horario.value_counts().sort_index().plot()

df2 = ['horario','valores']

X = df.loc[1:, df2]


# In[35]:

X.dtypes


# In[36]:

X.plot()

