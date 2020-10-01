# Naive Bayes Classifier
---
* **Concept of Naive Bayes Classifier**
  - Naive Bayes is a simple, yet effective and commonly-used, machine learning classifier. 
  - It is a probabilistic classifier that makes classifications using the Maximum A Posteriori decision rule in a Bayesian setting. 
  - It can also be represented using a very simple Bayesian network. 
 
* **How Algorithm Works** 
  
* **Advantages of Naive Bayes Classifier**
  - The only work that must be done before prediction is finding the parameters for the features’ individual probability distributions, which can typically be done quickly and deterministically.
  - Naive Bayes classifiers can perform well even with high-dimensional data points and/or a large number of data points.
  - When assumption of independence holds, a Naive Bayes classifier performs better compare to other models like logistic regression and you need less training data.
  
* **Disadvantages of Naive Bayes Classifier**
  - If categorical variable has a category (in test data set), which was not observed in training data set, then model will assign a 0 (zero) probability and will be unable to make a prediction. This is often known as Zero Frequency. To solve this, we can use the smoothing technique. One of the simplest smoothing techniques is called Laplace estimation.
  - Another limitation of Naive Bayes is the assumption of independent predictors. In real life, it is almost impossible that we get a set of predictors which are completely independent.
  
* **Different Problem statement where you can Naive Bayes Classifier**
  - Naive Bayes classifiers have been especially popular for text classification, and are a traditional solution for problems such as spam detection.  
  - Sentiment Analysis
  - Spam classification
  - twitter sentiment analysis
  - document categorization


* Reference
  - [Naive Bayes Classifier](https://towardsdatascience.com/naive-bayes-classifier-81d512f50a7c)
  - [All about Naive Bayes](https://towardsdatascience.com/all-about-naive-bayes-8e13cef044cf)
