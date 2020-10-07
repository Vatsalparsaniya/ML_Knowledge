# Data Normalization

---
* **Concept**
  - It is technique often applied as part of data preparation in Machine learning.
  - It basically changes the the values of numeric columns to a common scale in the dataset, without distorting differences
    in the ranges of values.
  - It is basically a scaling(i.e transforming your data so that it fits within a specific scale) technique in which
    values are shifted and rescaled so that they end up ranging between 0 and 1.

* **How Algorithm Works**
  For example, assume your input dataset that contains one column with values ranging from 0 to 1, and another column with
  values ranging from 10,000 to 100,000. The great difference in the scale of the numbers could cause problems when you
  attempt to combine the values as features during modeling.

  Normalization avoids these problems by creating new values that maintain the general distribution and ratios in the
  source data, while keeping values within a scale applied across all numeric columns used in the model.

  The Normalization offers several options for transforming numeric data:

   - You can change all values to a 0-1 scale, or transform the values by representing them as percentile ranks rather
     than absolute values.
   - You can apply normalization to a single column, or to multiple columns in the same dataset.
   - If you need to repeat the experiment, or apply the same normalization steps to other data, you can save the steps
     as a normalization transform, and apply it to other datasets that have the same schema.

* **Advantages of Normalization**
  - Makes training less sensitive to the scale of features.
  - Consistency for comparing results across models.
  - Makes optimization well-conditioned.


  
* **Normalization : A preprocessing stage in ML**
[Link 1](https://arxiv.org/ftp/arxiv/papers/1503/1503.06462.pdf)
