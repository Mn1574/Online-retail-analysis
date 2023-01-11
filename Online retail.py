#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import datetime as dt


# In[8]:


result=pd.read_excel('Online Retail.xlsx')


# In[9]:


result


# In[10]:


result.head()


# # Preprocessing and cleaning a data

# In[11]:


result.tail()


# In[12]:


result.sample(10)


# In[10]:


result.shape


# In[12]:


result.describe()


# In[13]:


result.info()


# In[13]:


result.isnull().sum()


# In[14]:


result.dropna()


# In[91]:


result.duplicated


# In[15]:


result.drop_duplicates()


# In[96]:


result.isnull().sum()


# # Check the quantity 

# In[16]:


result[result['Quantity']>0]


# # Check the price

# In[18]:


result[result['UnitPrice']>=0]


# In[19]:


data=result[(result['UnitPrice'])>=0 & (result['Quantity']>0)]


# In[20]:


data


# In[21]:


result.columns


# In[22]:


len(result.columns)


# # Exploration of a data analysis (EDA)

# # what is  the total sales?

# In[23]:


total_sales=result['Quantity']*result['UnitPrice']


# In[24]:


result['total_sales']=total_sales


# In[25]:


result


# In[26]:


result.dropna(inplace =True)


# In[27]:


data=result[result['total_sales']>=0]


# In[28]:


data.head()


# In[29]:


data.shape


# # Add a year column

# In[30]:


time=data['InvoiceDate'].dt.year
data['year']=time


# In[111]:


data.head()


# # Total sales of each year

# In[31]:


data.groupby('year')['total_sales'].sum()


# In[113]:


data.groupby('year')['total_sales'].sum().plot(kind='bar')


# # Total sales of each Month

# In[45]:


data['month']=data['InvoiceDate'].dt.month
data['months']=data['InvoiceDate'].dt.month_name()
data.groupby(['month','year'])['total_sales'].sum()


# In[46]:


data.groupby(['month','year'])['total_sales'].sum().plot(kind='bar',title='sales of year')


# 

# In[ ]:





# In[43]:


data_new=data[data.Country!='United Kingdom']


# In[47]:


data_new.head()


# # Top 10 countries which are generating the highest revenue
# 

# In[87]:


high_revenue=data_new.groupby('Country')['total_sales'].sum().sort_values(ascending=False)[:10]


# In[117]:


high_revenue.plot(kind='bar')


# In[124]:


data_new.groupby('Quantity')['total_sales'].sum().sort_values(ascending=False)


# # Top 10 customers by revenue

# In[157]:


top_10_customers=data.groupby('CustomerID')['total_sales'].sum().sort_values(ascending=False).head(10)


# In[158]:


top_10_customers


# In[154]:


top_10_customers.plot(kind='bar')


# In[ ]:


# Demand for the products by Country


# In[172]:


data['Country'].count()


# # Top countries by products

# In[199]:


df=data_new.groupby('Country')['Description'].count().sort_values(ascending=False)


# In[201]:


df


# In[202]:


df.plot(kind='bar')


# In[57]:


data.head()


# In[59]:


data.to_csv('online_retail_new.csv')


# In[ ]:




