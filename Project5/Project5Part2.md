## 1

After importing the necessary libraries, functions, and commands, I imported the 'city_persons.csv' data and set the features and target values, with the target equal to the variable 'wealthC'.

`X = df.drop(["wealthC"], axis = 1)`

`y = df.wealthC`

## 2

Before adding the distance weight to the KNN model, the best results were produced with the model with n_neighbors equal to 102, from a range of 20 to 200, yielding a testing score of 0.594503. Adding a distance weight with n_neighbors set to 102 produced smaller testing scores of 0.566685.

## 3

When the logistic regression was run on the data - with max iterations set to 1000, the testing scores changed to 0.597348, demonstrating the logistic model is slightly more accurate to the data than the K-nearest neighbors model. 

## 4

With the number of estimators set to 100, 500, 1000, and 5000, the specification most likely to return the best model is that with 500 trees - returning scores on the training and testing values of 0.8274739 and 0.5690580. The training and testing scores for the rest of the estimator models were as follows:

| Estimators  | Training | Testing |
| ------------- | ------------- | ---------- |
| 100  | 0.827473958  | 0.56320156 |
| 500  | 0.827473958 | 0.56905807 |
| 1000 | 0.827473958 | 0.56124938 |
| 5000 | 0.827473958 | 0.56710590 |

After running random forests models on a range of data, it was found that the minimum number of samples required to split an internal node was 25, yielding a training and testing set of 0.7041695 and 0.6090504, better results than both the logistic regression and the K-nearest neighbors model.

The standardized data produced models of greater accuracy with the accuracy results for standardized, unstandardized estimators of 100, 500, 1000, and 5000 listed below:


| Estimators  | Standardized Accuracy | Unstandardized Accuracy |
| ------------- | ------------- | ------------- |
| 100  | 0.56417764  |  0.55880917 |
| 500  | 0.56808199 | 0.56027330 |
| 1000 | 0.57393850 | 0.56173743 |
| 5000 | 0.56954612 | 0.56515373 |


## 5

Repeat the previous steps after recoding the wealth classes 2 and 3 into a single outcome. Do any of your models improve? Are you able to explain why your results have changed?

The accuracy of the model decreases when wealth classes 2 and 3 are collapsed into a single outcome. In the KNN model, the best specification of neighbors equal to 61 produced a testing score of 0.5441343, which decreased to 0.4993198 upon adding the distance weight. 

In the logistic regression, the accuracy increases slightly to 0.5496975. 

When running a model of random forests, the standardized, unstandardized accuracy scores of 100, 500, 1000, and 5000 estimators are as follows:

| Estimators  | Standardized Accuracy | Unstandardized Accuracy |
| ------------- | ------------- | ------------- |
| 100  | 0.50317227  |  0.50073206 |
| 500  | 0.49829184 | 0.50219619 |
| 1000 | 0.50414836 | 0.5056124 |
| 5000 | 0.50366032 | 0.5021961 |

When two values of the dependent variable are recoded into a single variable, the predictive ability of each of the three models decreases by about 0.5, claiming the chosen models accurately predict the result of the model only about 50% of the time. This could be because there is now less variability in the data. Before the collapsing of the two values, wealth class C had a large majority in the feature variable, which increased when wealth class 2 was collapsed into it. As most of the feature data has the same value, the lower variability could explain the worsened predictive quality of the second data set.

## 6

The original dataset, with wealth classes 2 and 3 split, produced better results than that of the condensed feature variable. Of the models produced by the orginal data, the best results in predicting wealth of all people throughout the West African capital city were provided in the logistic regression. In this model, predictive accuracy was shown to be 0.597348, suggesting it accurately predicts the wealth of people in this West African city nearly 60% of the time, compared to about 56% for the other models. 


