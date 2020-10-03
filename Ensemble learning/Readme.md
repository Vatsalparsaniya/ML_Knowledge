# Ensemble 

* Ensemble is a technique in machine learning in which we combine different machine learning models to achieve most optimal model.

* we use different base model(they are also called weak learners) such as one is **decision tree** and  **svm** to make one model(strong learner), with less bias and less variance. 
* Ensemble methods used extensively in machine learning.

## How this works

* First the same data points from training data set is passed through different model and result is  calculated by simply the choosing algorithm such as averages or max voting. 

![stacking](./Stacking.png)

 **Base Learners or weak learners** are individual model such as knn, decision tree classifers etc.
 **Meta Learner or strong learner** is combined model and is used for final prediction.
## There are different ensemble techniques.

* Basic ensemble techniques
1. [Max voting.](https://machinelearningmastery.com/voting-ensembles-with-python/)
2.  Averaging.
 3. [Weighted Average.](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean)
 *  Advanced ensemble techniques.   
  1. [Stacking.](https://machinelearningmastery.com/stacking-ensemble-machine-learning-with-python/)
  2. [Blending.](https://medium.com/@stevenyu530_73989/stacking-and-blending-intuitive-explanation-of-advanced-ensemble-methods-46b295da413c)  
  3. [Bagging.](https://en.wikipedia.org/wiki/Bootstrap_aggregating) 
  3. [Boosting.](https://en.wikipedia.org/wiki/Boosting_(machine_learning))
## Advantages of ensemble 

* This type of model is used to reduce bias from the individual base model having high bias.
* Better prediction than individual model.
* Ensembles can also be parallelized more easily, leading to more efficient performance.


##  Disadvantage of ensemble

* High  computation power is required as compared to individual models.
* Ensemble model is complex and can be more difficult to interpret.
* More time is consumed in training the ensemble models as compared to individual model.

## Applications
* Ensemble models are used to achieve low bias and low variance overall.
* Used in data science competition for optimizing the models and better performance.