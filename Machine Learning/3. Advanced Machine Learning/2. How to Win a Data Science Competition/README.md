<h1>Week 1</h1>



<h2>Feature Preprocessing and Generation with Respect to Models</h2>


<h3>Numeric features</h3>

Numeric feature preprocessing is different for tree and non-tree models:
- Tree-based models doesn’t depend on scaling
- Non-tree-based models hugely depend on scaling


__Preprocessing: scaling__

<img src="../2. How to Win a Data Science Competition/images/scaling.jpg">

__Preprocessing: outliers__


__Preprocessing: rank__


__Feature Generation__


<h3>Categorical and ordinal features</h3>

__Label encoding__

Label encoding maps categories to numbers

__Frequency encoding__

Frequency encoding maps categories to their frequencies

__One-hot encoding__

Label and Frequency encodings are often used for tree based models. One-hot encoding is often used for non-tree-based models.

<h3>Datetime and coordinates</h3>



<h3>Handling missing values</h3>

__Missing data, numeric__


__Missing values reconstruction__


__Feature generation with missing values__



<h2>Feature extraction from text and images</h2>


<h3>Bag of words</h3>

__Bag of words__


__Bag of words: TFiDF__


__N-grams__


__Texts preprocessing: lemmatization and stemming__


__Texts preprocessing: stopwords__


<h3>Word2vec, CNN</h3>



<h1>Week 2</h1>



<h2>Exploratory Data Analysis</h2>


<h3>Building intuition about the data</h3>



<h3>Exploring anonymized data</h3>



<h3>Visualizations</h3>



<h3>Dataset cleaning and other things to check</h3>

__EDA Checklnst__

- Get domain knowledge
- Check if the data is intuitive
- Understand how the data was generated
- Explore individual features
- Explore pairs and groups
- Clean features up
- Check for leaks! (later in this course)

<h3>Springleaf competition EDA I</h3>


<h3>Springleaf competition EDA II</h3>


<h3>Numerai competition EDA</h3>



<h2>Validation</h2>


<h3>Validation and overfitting</h3>



<h3>Validation strategies</h3>

a) Holdout scheme:

- Split train data into two parts: partA and partB.
- Fit the model on partA, predict for partB.
- Use predictions for partB for estimating model quality. Find such hyper-parameters, that quality on partB is maximized.

b) K-Fold scheme:

- Split train data into K folds.
- Iterate though each fold: retrain the model on all folds except current fold, predict for the current fold.
- Use the predictions to calculate quality on each fold. Find such hyper-parameters, that quality on each fold is maximized. You can also estimate mean and variance of the loss. This is very helpful in order to understand significance of improvement.

c) LOO (Leave-One-Out) scheme:

- Iterate over samples: retrain the model on all samples except current sample, predict for the current sample. You will need to retrain the model N times (if N is the number of samples in the dataset).
- In the end you will get LOO predictions for every sample in the trainset and can calculate loss.

<h3>Data splitting strategies</h3>



<h3>Problems occurring during validation</h3>



<h2>Data Leakages</h2>


<h3>Basic data leaks</h3>



<h3>Leaderboard probing and examples of rare data leaks</h3>



<h3>Expedia challenge</h3>




<h1>Week 3</h1>



<h2>Metrics Optimization</h2>


<h3>Regression metrics review I</h3>

__Mean Square Error__


__Root Mean Square Error__


__R-squared__


__Mean Absolute Error__

_MAE vs MSE_

- Do you have outliers in the data? Use MAE
- Are you sure they are outliers? Use MAE
- Or they are just unexpected values we should still care about? Use MSE

MSE, RMSE, R-squared are the same from optimization perspective.

MAE is robust to outliers.

__MSPE__

Weighted version of MSE.

__MAPE__

Weighted version of MAE.

__Root Mean Square Logarithmic Error__

MSE in log space.

<h3>Classification metrics review</h3>



<h3>General approaches for metrics optimization</h3>

_Target metric_ is a function which we want to use to evaluate the quality of our model.

_Optimization loss_ is what model optimizes.

<h3>Regression metrics optimization</h3>



<h3>Classification metrics optimization I</h3>




<h2>Advanced Feature Engineering I</h2>


<h3>Concept of mean encoding</h3>


<h3>Regularization</h3>


<h3>Extensions and generalizations</h3>





<h1>Week 4</h1>



<h2>Hyperparameter Optimization</h2>





<h2>Advanced feature engineering II</h2>





<h2>Ensembling</h2>






<h1>Week 5: Final Project</h1>
