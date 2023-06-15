#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = {'Roll No.':[201,202,203,204,205,206,207,208,209,210], 'Name':['Shreya','Supriti','Ankita','Zed','Clea','Mia','Zendaya','Tim','Charlie','Lola'],'Gender':['F','F','F','M','M','F','F','M','M','M'], 'Marks1' : [91,60,88,10,41,54,83,46,92,12],
'Marks2' : [95,98,92,69,44,67,55,98,36,72],
'Marks3': [98,80,97,57,64,72,98,69,39,46]};
data


# In[3]:


s=pd.DataFrame(data)
s
s.index+=1
s


# In[5]:


col_list = list(s)
col_list.remove('Roll No.')
col_list



s['Total'] = s[col_list].sum(axis=1)
s


# In[6]:


min=s['Marks1'].min()
min


# In[8]:


max=s['Marks2'].max()
max


# In[10]:


av=s['Marks3'].mean()
av


# In[13]:


s['Average']=s[col_list].mean(axis=1)
s


# In[20]:



s[s.Average==s['Average'].max()]


# In[23]:


s[s['Marks2'] < 40]['Name'].count()


# In[ ]:




