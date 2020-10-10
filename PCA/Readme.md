## Unsupervised ##

Unsupervised learning is a type of machine learning that looks for previously undetected patterns in a data set with no pre-existing labels and with a minimum of human supervision. In contrast to supervised learning that usually makes use of human-labeled data, unsupervised learning, also known as self-organization allows for modeling of probability densities over inputs.

## Principal Component Analysis ##

Principal component analysis (PCA) is a technique to bring out strong patterns in a dataset by supressing variations. It is used to clean data sets to make it easy to explore and analyse. The algorithm of Principal Component Analysis is based on a few mathematical ideas namely:

* **Variance and Convariance**
* **Eigen Vectors and Eigen values**

**Purpose of PCA** : Principal component analysis (PCA) is a technique for reducing the dimensionality of such datasets, increasing interpretability but at the same time minimizing information loss. It does so by creating new uncorrelated variables that successively maximize variance

## Algorithm ##

* **1 : Get your data**
Separate your data set into X and Y. X will be the training set and Y will be the validation set. In simple terms, we will use X for our study and use Y to check whether our study is correct.

* **2 : Structure your data**

Take the 2 dimensional matrix of independent variables X. Rows represent data items and columns represent features. The number of columns is the number of dimensions.

For each column, subtract the **mean** of that column from each entry. (This ensures that each column has a mean of zero.)

* **3 : Standardize your data**

Given the columns of X, are features with higher variance more important than features with lower variance, or is the importance of features independent of the variance? (In this case, importance means how well that feature predicts Y.)

If the importance of features is independent of the variance of the features, then divide each observation in a column by that column’s standard deviation. Call the centered and standardized matrix **Z**.

* **4 : Get Covariance of Z**

Take the matrix Z, transpose it and multiply the transposed matrix by Z.

  **Convariance of Z = ZᵀZ**

The resulting matrix is the covariance matrix of Z, up to a constant.

* **5 : Calculate Eigen Vectors and Eigen Values**

Calculate the eigenvectors and their corresponding eigenvalues of ZᵀZ.

The eigen decomposition of ZᵀZ is where we decompose ZᵀZ into PDP⁻¹,

where P is the matrix of eigenvectors
D is the diagonal matrix with eigenvalues on the diagonal and values of zero everywhere else.

The eigenvalues on the diagonal of D will be associated with the corresponding column in P — that is, the first element of D is λ₁ and the corresponding eigenvector is the first column of P. This holds for all elements in D and their corresponding eigenvectors in P. We will always be able to calculate PDP⁻¹ in this fashion.

* **6 : Sort the Eigen Vectors**

Take the eigenvalues λ₁, λ₂, …, λp and sort them from largest to smallest. In doing so, sort the eigenvectors in P accordingly. (For example, if λ4 is the largest eigenvalue, then take the forth column of P and place it in the first column position.)

Call this sorted matrix of eigenvectors P'. The columns of P' are the same as the columns of P in a different order. Note that these eigenvectors are independent of one another.

* **7 : Calculate the New Features**

Calculate Z' = ZP'.

This new matrix, Z', is a centered/standardized version of X but now each observation is a combination of the original variables, where the weights are determined by the eigenvector. As a bonus, because our eigenvectors in P' are independent of one another, each column of Z' is also independent of one another.

* **8 : Drop unimportant features from the new set**

There are three common methods to do this:

**Method 1**: Arbitrarily select how many dimensions we want to keep

**Method 2**: Calculate the proportion of variance for each feature, pick a threshold, and add features until you hit that threshold

**Method 3**: Calculate the proportion of variance for each feature, sort features by proportion of variance and plot the cumulative proportion of variance explained as you keep more features. One can pick how many features to include by identifying the point where adding a new feature has a significant drop in variance explained relative to the previous feature, and choosing features up until that point.

## Advantages of PCA ##
  * Removes Correlated Features
  * Improves Algorithm Performance
  * Reduces Overfitting
  * Improves Visualization

## Disadvantages of PCA ##
  * Independent variables become less interpretable
  * Data standardization is must before PCA
  * Information Loss

## Assumptions ##
  * You have multiple variables that should be measured at the continuous level (although ordinal variables are very frequently used).
  * There needs to be a linear relationship between all variables.
  * You should have sampling adequacy, which simply means that for PCA to produce a reliable result, large enough sample sizes are required.
  * Your data should be suitable for data reduction.
  * There should be no significant outliers.

References :
[Algorithm](https://iq.opengenus.org/algorithm-principal-component-analysis-pca/)
[more about advantages and disadvantages](http://theprofessionalspoint.blogspot.com/2019/03/advantages-and-disadvantages-of_4.html)
[more about PCA Assumptions](https://statistics.laerd.com/spss-tutorials/principal-components-analysis-pca-using-spss-statistics.php)
