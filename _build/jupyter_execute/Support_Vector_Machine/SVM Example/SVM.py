#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

a = np.array([[1]])
plt.imshow(a,cmap = 'gray')


# In[2]:


a = np.array([[1,2,3,5,10]])
plt.imshow(a,cmap = 'gray')
plt.show()


# In[3]:


from sklearn import datasets


# In[4]:


digits = datasets.load_digits()
digits


# In[5]:


#Dataframe
digits.data


# In[6]:


digits.target


# In[7]:


digits.target_names
#Unique values


# In[8]:


digits.images[0]


# In[9]:


digits.data[0]


# In[10]:


plt.imshow(digits.images[0],cmap='gray')


# In[11]:


digits.images[0].shape


# In[12]:


import pandas as pd

df = pd.DataFrame(digits.data)
df.head()


# In[13]:


df.shape


# In[14]:


df['Target'] = digits.target


# In[15]:


df.head()


# In[16]:


plt.imshow(digits.images[1796],cmap = 'gray')


# In[17]:


# Classification : SVC used here

#Support Vector Machine

x = digits.data
y = digits.target

from sklearn.svm import SVC


# In[18]:


model = SVC()


# In[19]:


model.fit(x,y)
model.predict(x[[23]])


# In[20]:


plt.imshow(digits.images[23],cmap = 'gray')


# In[21]:


# split at 70-30
m1 = SVC(kernel = 'poly')
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size = 0.7,random_state = 100)


# In[22]:


m1.fit(x_train,y_train)


# In[23]:


m1.predict(x[[1000]])


# In[24]:


digits.target[1000]


# In[25]:


y_pred = m1.predict(x_test)


# In[26]:


from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Mean Squared Error 
metrics.mean_squared_error(y_test,y_pred)


# In[ ]:


#Accuracy score

metrics.r2_score(y_test,y_pred)


# In[ ]:


y_pred1 = model.predict(x_test)


# In[ ]:


metrics.r2_score(y_test,y_pred1)*100


# In[ ]:


accuracy_score(y_pred,y_test)*100


# In[ ]:


confusion_matrix(y_pred,y_test)


# In[ ]:




