#!/usr/bin/env python
# coding: utf-8

# Disclaimer: All this was extracted from the following URL: https://www.hackerearth.com/practice/machine-learning/machine-learning-algorithms/ml-decision-tree/tutorial/

# Coding a Decision Tree

# We will use the scikit-learn library to build the decision tree model. We will be using the iris dataset to build a decision tree classifier. The data set contains information of 3 classes of the iris plant with the following attributes: - sepal length - sepal width - petal length - petal width - class: Iris Setosa, Iris Versicolour, Iris Virginica

# In[1]:


#Importing required libraries
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


# The scikit-learn dataset library already has the iris dataset. You can either use the dataset from the source or import it from the scikit-learn dataset library.

# In[2]:


#Loading the iris data
data = load_iris()
print('Classes to predict: ', data.target_names)


# There are three classes of iris plants: 'setosa', 'versicolor' and 'virginica'. Now, we have imported the iris data in the variable 'data'. We will now extract the attribute data and the corresponding labels. We can extract the attributes and labels by calling .data and .target as shown below:

# In[3]:


#Extracting data attributes
X = data.data
### Extracting target/ class labels
y = data.target

print('Number of examples in the data:', X.shape[0])


# There are 150 examples/ samples in the data. The variable 'X' contains the attributes to the iris plant. The cell below shows the 4 attributes of the first four iris plants.

# In[4]:


#First four rows in the variable 'X'
X[:4]

#Output
#Out: array([[5.1, 3.5, 1.4, 0.2],
#        [4.9, 3. , 1.4, 0.2],
#        [4.7, 3.2, 1.3, 0.2],
#        [4.6, 3.1, 1.5, 0.2]])


# Now that we have extracted the data attributes and corresponding labels, we will split them to form train and test datasets. For this purpose, we will use the scikit-learn's 'train_test_split' function, which takes in the attributes and labels as inputs and produces the train and test sets.

# In[5]:


#Using the train_test_split to create train and test sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 47, test_size = 0.25)


# Since, this is a classification problem, we will import the DecisionTreeClassifier function from the sklearn library. Next, we will set the 'criterion' to 'entropy', which sets the measure for splitting the attribute to information gain.

# In[6]:


#Importing the Decision tree classifier from the sklearn library.
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion = 'entropy')


# Next, we will fit the classifier on the train attributes and labels.

# In[7]:


#Training the decision tree classifier. 
clf.fit(X_train, y_train)

#Output:
Out:DecisionTreeClassifier(class_weight=None, criterion='entropy', max_depth=None,
            max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False, random_state=None,
            splitter='best')


# Now, we will use the trained classifier/ model to predict the labels of the test attributes.

# In[8]:


#Predicting labels on the test set.
y_pred =  clf.predict(X_test)


# We will now evaluate the predicted classes using some metrics. For this case, we will use 'accuracy_score' to calculate the accuracy of the predicted labels.

# In[9]:


#Importing the accuracy metric from sklearn.metrics library

from sklearn.metrics import accuracy_score
print('Accuracy Score on train data: ', accuracy_score(y_true=y_train, y_pred=clf.predict(X_train)))
print('Accuracy Score on test data: ', accuracy_score(y_true=y_test, y_pred=y_pred))

#Output:
# Out: Accuracy Score on train data:  1.0
#     Accuracy Score on test data:  0.9473684210526315


# Next, we will tune the parameters of the decision tree to increase its accuracy. One of those parameters is 'min_samples_split', which is the minimum number of samples required to split an internal node. Its default value is equal to 2 because we cannot split on a node containing only one example/ sample.

# In[10]:


clf = DecisionTreeClassifier(criterion='entropy', min_samples_split=50)
clf.fit(X_train, y_train)
print('Accuracy Score on train data: ', accuracy_score(y_true=y_train, y_pred=clf.predict(X_train)))
print('Accuracy Score on the test data: ', accuracy_score(y_true=y_test, y_pred=clf.predict(X_test)))

#Output:
# Out: Accuracy Score on train data:  0.9553571428571429
#     Accuracy Score on test data:  0.9736842105263158


# We can see that the accuracy on the test set increased, while it decreased on the training set. This is because increasing the value of the min_sample_split smoothens the decision boundary and thus prevents it from overfitting.

# In[ ]:




