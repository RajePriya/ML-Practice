#!/usr/bin/env python
# coding: utf-8

# # Data Encoding
#    
#   1. Nominal/OHE Encoding
#   2. Label and Ordinal Encoding
#   3. Target Guided Ordinal Encoding

# ### Nominal/OHE Encoding
# 
# One hot encoding, also known as nominal encoding, is a technique used to represent categorical data as numerical data, which is more suitable for machine learning algorithms. In this technique, each category is represented as a binary vector where each bit corresponds to a unique category. For example, if we have a categorical variable "color" with three possible values (red, green, blue), we can represent it using one hot encoding as follows:
# 
# 1. Red: [1,0,0]
# 2. Green: [0,1,0]
# 3. Blue: [0,0,1]

# In[5]:


import pandas as pd
from sklearn.preprocessing import OneHotEncoder


# In[6]:


df = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'green', 'red', 'blue']
})


# In[7]:


df.head()


# In[8]:


from sklearn.preprocessing import LabelEncoder
lbl_encoder=LabelEncoder()


# In[9]:


lbl_encoder.fit_transform(df[['color']])


# In[10]:


lbl_encoder.transform([['red']])


# In[11]:


lbl_encoder.transform([['blue']])


# In[12]:


lbl_encoder.transform([['green']])


# ## Ordinal Encoding
# It is used to encode categorical data that have an intrinsic order or ranking. In this technique, each category is assigned a numerical value based on its position in the order. For example, if we have a categorical variable "education level" with four possible values (high school, college, graduate, post-graduate), we can represent it using ordinal encoding as follows:
# 
# 1. High school: 1
# 2. College: 2
# 3. Graduate: 3
# 4. Post-graduate: 4

# In[13]:


## Ordinal Encoding
from sklearn.preprocessing import OrdinalEncoder


# In[14]:


# Create a sample dataframe with an ordinal variable
df = pd.DataFrame({
    'size' : ['small', 'medium', 'large', 'medium', 'small', 'large']
})


# In[16]:


df


# In[17]:


## create an instance of OrdinalEncoder and then fit_transform
encoder=OrdinalEncoder(categories=[['small','medium','large']])


# In[18]:


encoder.fit_transform(df[['size']])


# In[21]:


encoder.transform([['small']])


# In[ ]:




