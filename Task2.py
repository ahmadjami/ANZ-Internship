#!/usr/bin/env python
# coding: utf-8

# # Imports and loading dataset

# In[1]:


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor


# In[2]:


df = pd.read_excel("ANZ synthesised transaction dataset.xlsx")


# ## Modifying data to obtain salaries for each customer

# In[3]:


df_salaries = df[df["txn_description"]=="PAY/SALARY"].groupby("customer_id").mean()
df_salaries.head()


# In[4]:


salaries = []

for customer_id in df["customer_id"]:
    salaries.append(int(df_salaries.loc[customer_id]["amount"]))
    
df["annual_salary"] = salaries


# In[5]:


df_cus = df.groupby("customer_id").mean()
df_cus.head()


# # Predictive Analytics

# ## Linear Regression

# In[6]:


N_train = int(len(df_cus)*0.8)
X_train = df_cus.drop("annual_salary", axis=1).iloc[:N_train]
Y_train = df_cus["annual_salary"].iloc[:N_train]
X_test = df_cus.drop("annual_salary", axis=1).iloc[N_train:]
Y_test = df_cus["annual_salary"].iloc[N_train:]


# In[7]:


linear_reg = LinearRegression()


# In[8]:


linear_reg.fit(X_train, Y_train)
linear_reg.score(X_train, Y_train)


# In[9]:


linear_reg.predict(X_test)


# In[10]:


linear_reg.score(X_test, Y_test)


# ## Decision Tree - Classification and Regression

# In[11]:


df_cat = df[["txn_description", "gender", "age", "merchant_state", "movement"]]


# In[12]:


pd.get_dummies(df_cat).head()


# In[13]:


N_train = int(len(df)*0.8)
X_train = pd.get_dummies(df_cat).iloc[:N_train]
Y_train = df["annual_salary"].iloc[:N_train]
X_test = pd.get_dummies(df_cat).iloc[N_train:]
Y_test = df["annual_salary"].iloc[N_train:]


# ### Classification

# In[14]:


decision_tree_class = DecisionTreeClassifier()


# In[15]:


decision_tree_class.fit(X_train, Y_train)
decision_tree_class.score(X_train, Y_train)


# In[16]:


decision_tree_class.predict(X_test)


# In[17]:


decision_tree_class.score(X_test, Y_test)


# ### Regression

# In[18]:


decision_tree_reg = DecisionTreeRegressor()


# In[19]:


decision_tree_reg.fit(X_train, Y_train)
decision_tree_reg.score(X_train, Y_train)


# In[20]:


decision_tree_reg.predict(X_test)


# In[21]:


decision_tree_reg.score(X_test, Y_test)

