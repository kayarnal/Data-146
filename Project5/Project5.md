## 1 

First, I imported all the necessary libraries and created my DoKFold() function. I then imported the persons.csv data, and removed the rows that had empty values in them. This would have a bigger impact on a smaller data set, but with this data set of over 47,900 observations, removing 83 rows won't have a significant import on the results. From there, I changed the data types of the 'age' and 'edu' columns, so all the data in the data frame would be integers.

After cleaning the data, I set 'wealthC' as the target, and the rest of the columns as the features.

`X = df.drop(["wealthC", "wealthI"], axis = 1)`

`y = df.wealthC`

## 2

Computing the MSE after running a Linear Regression on the unstandardized data gives a result of 0.442810, less than 20% of the average target value. Upon standardizing the data, the MSE very slightly changed to 0.442813, 18.2% of the average target value of 2.43275.

The linear coefficients of the unstandardized and standardized models differ significantly. In the unstandardized model, coefficients of the first three parameters are 3.01812923e-02,  1.07882853e-02, and -5.57603897e-04, while in the standardized model they are 1.12548658e-01,  5.24358116e-03, and -1.08884589e-02. Some coefficients increase while others decrease, suggesting that standardizing the data has a significant impact on the individual coefficients, while not greatly impacting the overall results - as the R<sup>2</sup> and MSE values were so similar.  

## 3

Run a ridge regression and report your best results.

## 4

Run a lasso regression and report your best results.

## 5

Repeat the previous steps using the variable wealthI as your target.

## 6 

Which of the models produced the best results in predicting wealth of all persons throughout the smaller West African country being described? Support your results with plots, graphs and descriptions of your code and its implementation. You are welcome to incorporate snippets to illustrate an important step, but please do not paste verbose amounts of code within your project report. Alternatively, you are welcome to provide a link in your references at the end of your (part 1) Project 5 report.



