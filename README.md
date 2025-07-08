# Suicides Analysis

This project performs EDA on Suicides dataset in India. 
The dataset is provided by *National Crime Records Bureau (NCRB), Govt of India.*

[Link to the Dataset](https://www.kaggle.com/datasets/rajanand/suicides-in-india)

## EDA

The dataset consists of suicides information from 2001 - 2012. It consists of different parameters such as Suicide causes, Education status, By means adopted, Professional profile, Social status. They are also classifed with gender, state-wise also.

The analysis shows the rising trend of suicides in India. We see that it has risen from 3.3 Crore deathsto 4.1 Crores in  the span of 12 years. Men's suicide rate had increased from 2 Crore deaths per year to 2.5 Crore deaths. Although there is not much change seen in suicide's rate as it stayed around 1.2 Crore.

### By State

We also see the State wise Analysis, where states like **Andhra Pradesh, Karnataka, Kerala, Madhya Pradesh, Tamil Nadu, and West Bengal**, have the **highest** suicides reported as per the dataset throughout 2001 - 2012. Highest no. of suicides being 5.4 Lakh suicides reported in Maharashtra. Some states show a rising trend, whereas some states show fluctuating.

### By Cause

Analysis based on cause by checking each state show that the top reasons for suicides is **Family Problems** (~60,000+ suicides) followed by **Prolonged Illness** (~30,000+ suicides). There are other causes such as Love Affairs, Drug Abuse, Mental Illness, Poverty, Bankruptcy, Unemployment (5,000 - 10,000 suicides each category).

### By Professional Profile

Analysis based on professional profile of deceased, indicate that the majority of suicides are of **Farmers** and **Housewives** (~40,000 each). Followed by Private Sector  Employee, Student, Unemployed (each 10,000 - 20,000 suicides). Retired Persosn, Public Sector Undertaking, and Government Employees are shown having the least of the suicides rate.

### By Educational Status

Analysis based on educational status, shows that **majority** of suicides are people with less than graduation, it includes **No Education, Primary, Middle, Secondary, Pre-University/Intermediate**. Here apart from Pre-University/Intermediate the rest are of the mentioned have more than 20,000 suicides overall timespan (2001 - 2012). We  also see that compared to women, men seems to be more likely to commit suicides for the same educational status.

### By Age Group

Analysis based on age group, indicate that the **majority** of suicides are in an age group of **15-29** and **30-44**, having more that 1.1 Lakh suicides each year and a slow rise is seen based on trend. 

## Prediction Application

This project uses Machine Learning Algorithm to predict the future annual suicides numbers.
We use pandas framework to clean the data to remove the noisy data.
The pandas data is converted to numpy and splitted into training and testing sets of 7:3

The data which is then feeded into a method provided by `scikit-learn` package to perform the **Linear Regression**.
Since the data is sub-classified into different categories, such as, age, gender, type of suicide, etc.
We took an iterative approach to make the model learn the patterns found.

