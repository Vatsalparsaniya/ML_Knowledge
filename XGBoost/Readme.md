# Introduction
XGBoost is an algorithm that has recently been dominating applied machine learning for structured or tabular data.
XGBoost is an implementation of gradient boosted decision trees designed for speed and performance .
XGBoost can be used in both regression as well as classification problems.

# Working
XGBoost is a popular and efficient open-source implementation of the gradient boosted trees algorithm. Gradient boosting is a supervised learning algorithm, which attempts to accurately predict a target variable by combining the estimates of a set of simpler, weaker models.
<br />
<br />
When using gradient boosting for regression, the weak learners are regression trees, and each regression treemaps an input data point to one of its leafs that contains a continuous score. XGBoost minimizes a regularized (L1 and L2) objective function that combines a convex loss function (based on the difference between the predicted and target outputs) and a penalty term for model complexity.
<br />
<br />
The training proceeds iteratively, adding new trees that predict the residuals or errors of prior trees that are then combined with previous trees to make the final prediction. It’s called gradient boosting because it uses a gradient descent algorithm to minimize the loss when adding new models.

# Advantages & Disadvantages 
## Advantages
1. <b>Regularization</b>: XGBoost has in-built L1 (Lasso Regression) and L2 (Ridge Regression) regularization which prevents the model from overfitting. That is why, XGBoost is also called regularized form of GBM (Gradient Boosting Machine).
2. <b>Handling Missing Values</b>: XGBoost has an in-built capability to handle missing values. When XGBoost encounters a missing value at a node, it tries both the left and right hand split and learns the way leading to higher loss for each node. It then does the same when working on the testing data.
3. <b>Parallel Processing</b>: XGBoost utilizes the power of parallel processing and that is why it is much faster than GBM. It uses multiple CPU cores to execute the model.

## Disadvantages
1. <b>Overfitting</b>: Overfiting is likely to occur in xgboost if xgboost parameters are not tuned properly.
2. <b>Training time</b>: Training time is pretty high for larger dataset, if you compare against catboost/lightgbm.

# Where to use XGBoost? 
One can use xgboost approaches in both regression as well as classification tasks. 

# References
1. https://machinelearningmastery.com/gentle-introduction-xgboost-applied-machine-learning/
2. https://towardsdatascience.com/what-is-xgboost-and-how-to-optimize-it-d3c24e0e41b4
