
# coding: utf-8

import pandas as pd
from datetime import datetime


df = pd.read_csv('data/teste.csv', sep=';')

df['hora'] = pd.to_datetime(df.hora)

df['horario'] = df.hora.dt.time

df['valores'] = df.valor.values

df.horario.value_counts().sort_index().plot()

df2 = ['horario','valores']

X = df.loc[1:, df2]

X.plot()


