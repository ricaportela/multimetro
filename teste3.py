
# coding: utf-8

# In[168]:

import pandas as pd
from datetime import datetime
from matplotlib.pyplot import *

get_ipython().magic('matplotlib inline')


# In[169]:

df = pd.read_csv('data/teste.csv', sep=';')


# In[170]:

df.head(11)


# In[171]:

df.dtypes


# In[172]:

df['hora'] = pd.to_datetime(df.hora)


# In[173]:

df.dtypes


# In[175]:

df.plot()


# In[165]:

df.hora.plot()


# In[ ]:



