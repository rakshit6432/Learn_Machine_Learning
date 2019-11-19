<h1>Week 1: Importing Datasets</h1>



<h2>Importing Datasets</h2>


Data acquisition is a process of loading and reading data into notebook from various sources. To read any data using Python's pandas package, there are two important factors to consider, format and file path. Format is the way data is encoded. The path tells us where the data is stored.

```python
import pandas as pd
# read the online file by the URL provided above, and assign it to variable "df"
path="https://archive.ics.uci.edu/ml/machine-learning-database/autos/imports-85.data"

df = pd.read_csv(path)
```



<h1>Week 2: Data Wrangling</h1>



<h2>Data Wrangling</h2>


<h3>Pre-processing Data in Python</h3>

Data preprocessing is the process of converting or mapping data from one raw form into another format to make it ready for further analysis.

<h3>Dealing with Missing Values in Python</h3>



<h3>Data Formatting in Python</h3>



<h3>Data Normalization in Python</h3>

<img src="../6. Data Analysis with Python/images/normalization.png">

<h3>Binning in Python</h3>



<h3>Turning categorical variables into quantitative variables in Python</h3>



<h1>Week 3: Exploratory Data Analysis</h1>



<h2>Exploratory Data Analysis</h2>


<h3>Descriptive Statistics</h3>

<img src="../6. Data Analysis with Python/images/box_plot.png">

<h3>GroupBy in Python</h3>



<h3>Correlation</h3>



<h3>Correlation - Statistics</h3>

One way to measure the strength of the correlation between continuous numerical variable is by using a method called Pearson correlation. Pearson correlation method will give you two values: the correlation coefficient and the P-value.

<img src="../6. Data Analysis with Python/images/correlation.png">

<h3>Analysis of Variance ANOVA</h3>

ANOVA is statistical test that stands for Analysis of Variance. ANOVA can be used to find the correlation between different groups of a categorical variable.

The ANOVA test returns two values, the F-test score and the p-value. The F-test calculates the ratio of variation between the groups mean, over the variation within each of the sample groups. The p-value shows whether the obtained result is statistically significant.

<img src="../6. Data Analysis with Python/images/anova_example.png">

<img src="../6. Data Analysis with Python/images/anova_example2.png">



<h1>Week 4: Model Development</h1>



<h2>Model Development</h2>


<h3>Linear Regression and Multiple Linear Regression</h3>

Linear regression will refer to one independent variable to make a prediction. Multiple linear regression will refer to multiple independent variables to make a prediction.

<img src="../6. Data Analysis with Python/images/linear_regression.png">

__Simple Linear Regression:__

<img src="../6. Data Analysis with Python/images/slr.png">


<h3>Model Evaluation using Visualization</h3>

__Regression Plot:__

Why use a regression plot?
It gives us a good estimate of:
1. The relationship between two variables
2. The strength of the correlation
3. The direction of the relationship (positive or negative)

<img src="../6. Data Analysis with Python/images/regression_plot.png">

The horizontal axis is the independent variable. The vertical axis is the dependent variable. Each point represents a different target point. The fitted line represents the predicted value.

__Residual Plot:__

The residual plot represents the error between the actual value.

<img src="../6. Data Analysis with Python/images/residual_plot.png">

We expect to see the results to have zero mean, distributed evenly around the x axis with similar variance. There is no curvature. This type of residual plot suggests a linear model is appropriate.

In the residual plot below, there is a curvature:

<img src="../6. Data Analysis with Python/images/residual_plot2.png">

The values of the error change with x. The residuals are not randomly separated. This suggests the linear assumption is incorrect. This plot suggests a nonlinear function.

In the plot below, we see the variance of the residuals increases with x. Therefore, our model is incorrect.

<img src="../6. Data Analysis with Python/images/residual_plot3.png">

__Distribution Plot:__

A distribution plot counts the predicted value versus the actual value. These plots are extremely useful for visualizing models with more than one independent variable or feature.

<img src="../6. Data Analysis with Python/images/distribution_plot.png">

In the plot above the dependent variable or feature is price. The fitted values that result from the model are in blue. The actual values are red. We see the predicted values for prices in the range from 40,000 to 50,000 are inaccurate. The prices in the region from 10,000 to 20,000 are much closer to the target value.

<h3>Polynomial Regression and Pipelines</h3>

Polynomial regression is a special case of the general linear regression. This method is beneficial for describing curvilinear relationships. Curvilinear relationship is what you get by squaring or setting higher order terms of the predictor variables in the model transforming the data.

<img src="../6. Data Analysis with Python/images/polynomial_regression.png">

The degree of the regression makes a big difference and can result in a better fit If you pick the right value. In all cases, the relationship between the variable and the parameter is always linear.

<h3>Measures for In-Sample Evaluation</h3>

__Mean Square Error:__

To measure the MSE, we find the difference between the actual value y and the predicted value yhat then square it.

__R-squared:__

R-squared is also called the coefficient of determination. It’s a measure to determine how close the data is to the fitted regression line. Think about it as comparing a regression model to a simple model, i.e., the mean of the data points.

<img src="../6. Data Analysis with Python/images/r_squared.png">

From the value that we get from the R-squared, we can say that approximately x% of the variation of the target label is explained by the linear model. Your R^2 value is usually between 0 and 1, if your R^2 is negative it can be due to overfitting.

<h3>Prediction and Decision Making</h3>



<h1>Week 5: Model Evaluation</h1>



<h2>Model Evaluation and Refinement</h2>


<h3>Model Evaluation and Refinement</h3>

Generalization error is a measure of how well our data does at predicting previously unseen data. The error we obtain using our testing data is an approximation of this error.

<h3>Overfitting, Underfitting and Model Selection</h3>



<h3>Ridge Regression</h3>



<h3>Grid Search</h3>
