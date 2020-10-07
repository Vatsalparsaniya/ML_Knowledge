#!/usr/bin/env python
# coding: utf-8

# Simple Linear Regression

# Importing The Libraries

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing The Dataset

# In[2]:


dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# Splitting The Dataset into the Training Set and Test Set

# In[3]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)


# In[4]:


print(X_train)


# In[5]:


print(X_test)


# In[6]:


print(y_train)


# In[7]:


print(y_test)


# Training the Simple Linear Regression model on the Training Set

# In[8]:


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)


# Predicting the Test Set result

# In[9]:


y_pred = regressor.predict(X_test)


# Visualising the Training Set results

# In[10]:


plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary v|s Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# Visualising the Test Set results

# In[11]:


plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('Salary v|s Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

