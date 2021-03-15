# Project 3

## 1

With originally 10 folds in the model, the training and testing scores produced R-Squared values of .019 and -.003, respectively. With 30 folds, the testing score decreases to -.186, and to -.581 with 50 folds. Such a low R-Squared value suggests the current linear regression model is a poor fit for the data, showing little to no correlation between the feature and target values. Increasing the number of folds in the model results in the external validity continually getting much smaller in comparison to the internal validity. The model poorly predicts both the data it was trained on, and the data it wasn't trained on, indicating it is poor fit for this data. 

## 2

With 10 folds in the model, the training and testing scores produced respective values of .019 and -.014. With 30 folds, the testing score decreases to -.088, and then to -.512 with 50 folds. The standardized features perform nearly exactly the same as with the original regression model. The model still performs poorly and returns testing scores that are much smaller than the training scores. 

## 3

Using standardized data in a ridge regression model with 10 folds, a training score of .019 is produced, along with a testing score of -.034. 30 folds provides respective training and testing scores of .019 and -.209, while 50 folds produce values of .019 and -.446. While the model still performs poorly, with an increase in to 50 folds, this model does perform better than the previous two models, with there being a smaller gap between the testing and training scores. 

## 4

Sticking with 50 folds, the dataset charleston_act.csv provides training and testing scores of .004 and -.151 in the original linear regression model. Upon standardizing the data, the scores change to .004 and -.13, while the standardized ridge regression reveals training and testing scores of .004 and -.155. In comparison to the dataset of asking prices, actual prices produce a model with much closer internal and external validity; however, the values are even lower than that of the original data - suggesting each model is very under-fit. With R-squared values of .004, less than 1% of the trained data is explained by the model. 

## 5

Including the zip code dummy variables in the model of actual prices increases the training and testing scores across all three models. In OLS linear regression using 50 folds, there was a training score of .337 and a testing score of .127. Upon standardizing, the testing score increased to .314, suggesting the standardized model is a better fit for the full data set of actual home prices. In the final, ridge regression model, the testing score produced a value of .065. Each model claims about 33% of the trained data is explained by the model, while the predictive power of the un-trained, new data changes more dramatically, shifting from 6% to 12% and 31%.  Including the zip code data improves the standardized model, suggesting the location of the homes has a greater impact on prices than the size of the homes. 

## 6

Of the models ran, the best results were produced using standardized linear regression with the data set including the zip code dummy variables. With a closer connection between the external and internal validity of this model, and the low values of both validities, this model is estimated to be underfit, however it is a much better fit than that of the datasets excluding the zip code variables. There was likely an issue of omitted variables in those model, as the three included features had such a low impact on the model. Including zip code boosted the predictive power of the model, and likely, the inclusion of other possible independent variables would further improve the model's predictive power. If I was working at Zillow, in the linear regression model of the final data set, I would include additional variables that could influence home prices, such as when the home was built and other aspects of location, such as proximity to cities or schools, or if any included neighborhoods were considered low-income housing. 
