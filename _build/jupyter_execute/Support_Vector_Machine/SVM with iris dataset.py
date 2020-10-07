#!/usr/bin/env python
# coding: utf-8

# # Get Dataset

# In[1]:


import seaborn as sns


# In[2]:


iris = sns.load_dataset('iris')


# In[3]:


iris.head()


# # Exploratory Data Analysis

# In[4]:


import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


sns.pairplot(iris,hue='species',palette='Dark2')


# In[6]:


setosa = iris[iris['species']=='setosa']
sns.kdeplot(setosa['sepal_width'],setosa['sepal_length'],cmap='plasma',shade=True,shade_lowest=False)


# # Train Test Split

# In[7]:


from sklearn.model_selection import train_test_split


# In[8]:


X = iris.drop('species',axis=1)
y = iris['species']
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3)


# # Train a Model

# In[9]:


from sklearn.svm import SVC


# In[10]:


svc_model = SVC()


# In[11]:


svc_model.fit(X_train,y_train)


# # Model Evaluation

# In[12]:


predictions = svc_model.predict(X_test)


# In[13]:


from sklearn.metrics import classification_report,confusion_matrix


# In[14]:


print(confusion_matrix(y_test,predictions))


# In[15]:


print(classification_report(y_test,predictions))


# # GridSearch Practice

# In[16]:


from sklearn.model_selection import GridSearchCV


# In[17]:


param_grid = {'C':[0.1,1,10,100],'gamma':[1,0.1,0.01,0.001]}


# In[18]:


grid = GridSearchCV(SVC(),param_grid,verbose=2)
grid.fit(X_train,y_train)


# In[19]:


grid_predictions = grid.predict(X_test)


# In[20]:


print(confusion_matrix(y_test,grid_predictions))


# In[21]:


print(classification_report(y_test,grid_predictions))


# Both models did fairly out!!

# In[ ]:




