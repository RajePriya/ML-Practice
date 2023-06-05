#!/usr/bin/env python
# coding: utf-8

# # Target Guided Ordinal Encoding
# 
# It is a technique used to encode categorical variables based on their relationship with the target variable. This encoding 
# technique is useful when we have a categorical variable with a large number of unique categories, and we want to use this 
# variable as a feature in our machine learning model.
# 
# In Target Guided Ordinal Encoding, we replace each category in the categorical variable with a numerical value based on the
# mean or median of the target variable for that category. This creates a monotonic relationship between the categorical 
# variable and the target variable, which can improve the predictive power of our model.

# In[1]:


import pandas as pd

# create a sample dataframe with a categorical variable and a target variable
df = pd.DataFrame({
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'New York', 'Paris'],
    'price': [200, 150, 300, 250, 180, 320]
})


# In[2]:


df


# In[3]:


df.groupby('city')['price'].mean()


# In[4]:


mean_price=df.groupby('city')['price'].mean().to_dict()


# In[5]:


mean_price


# In[6]:


df['city_encoded']=df['city'].map(mean_price)


# In[7]:


df


# In[8]:


df[['price','city_encoded']]


# In[9]:


import seaborn as sns
sns.load_dataset('tips')


# In[ ]:




