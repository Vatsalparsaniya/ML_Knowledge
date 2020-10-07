#!/usr/bin/env python
# coding: utf-8

# # Importing all the necessary libraries
# The libraries used are scikit-learn,numpy and xgboost

# In[1]:


import numpy as np
import xgboost
from xgboost import XGBClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# # Loading & Preprocessing Data
# The datasets used is that of breast cancer classifications which can already be found at scikit-learn. Here the dataset is loaded and splits into training and testing data. The spliting is done by the built in function of scikit-learn.

# In[2]:


data = load_breast_cancer()
X = data.data
y = data.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=21,shuffle=True)


# # Making the model

# In[3]:


model = XGBClassifier(n_estimators=100)
model.fit(X_train,y_train)


# # Evaluation 
# Printing the values of accuracy on training as well as testing data using a built-in function of scikit-learn.

# In[9]:


print('Training Accuracy :{}'.format(accuracy_score(y_true=y_train,y_pred=model.predict(X_train))))
print('Testing Accuracy  :{}'.format(accuracy_score(y_true=y_test,y_pred=model.predict(X_test))))

