#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r'C:\Users\shrey\Downloads\mtcars.csv')


# In[3]:


df.head()


# In[4]:


df.iloc[df['mpg'].idxmax()]


# In[5]:


df.iloc[df['mpg'].idxmin()]


# In[6]:


df.iloc[df['qsec'].idxmax()]


# In[7]:


quartiles = np.percentile(df['disp'], [25, 50, 75])
print('Minimum: %.3f' % df['disp'].min())
print('Q1: %.3f' % quartiles[0])
print('Median: %.3f' % quartiles[1])
print('Q3: %.3f' % quartiles[2])
print('Maximum: %.3f' % df['disp'].max())


# In[8]:


df['hp'].median()


# In[9]:


print(f"Mileage - manual cars: {df['mpg'][df['am'] == 0].mean()}")
print(f"Mileage - automatic cars: {df['mpg'][df['am'] == 1].mean()}")


# In[10]:


hist= df['mpg'].hist()


# In[11]:


df['mpg'][df['am'] == 0].plot.box()


# In[12]:


df['mpg'][df['am'] == 1].plot.box()


# In[13]:


pd.crosstab(df['am']==1,df['am']==0)


# In[14]:


pd.crosstab(df['am'],df['cyl'])


# In[15]:


c_1= df['wt']
c_2= df['mpg']
co= c_1.corr(c_2)
co


# In[ ]:




