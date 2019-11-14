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









<h1>Week 5: Model Evaluation</h1>
