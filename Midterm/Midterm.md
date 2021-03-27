# Midterm Questions 15-24

## 15

`Xy = X_df.copy()`

`Xy['y'] = y`

`Xy.corr()`

Of the four given features, MedInc has the greatest correlation with the target value, with a correlation coefficient of .688. 

## 16

`Xs = ss.fit_transform(X)`

`Xs_df = pd.DataFrame(Xs, columns = X_names)`

`Xsy_df = Xs_df.copy()`

`Xsy_df['y'] = y`

`Xsy_df.corr()`

Upon standardizing the dataset, the correlation coefficients of the given features do not change. 

## 17

The score of the linear regression model run on the target and MedInc in .47. 

## 18

Running a linear regression on the standardized data with 20 folds returns a $R^2$ value of .60198.

## 19

Running a ridge regression on the standardized data with 20 folds returns a $R^2$ value of .60201.

## 20

Running a linear regression on the standardized data with 20 folds returns a $R^2$ value of .60213.

## 21

Of all of the feature values, the least corrleated is AveOccup. After running the three models on standardized data, the Lasso regression returns the smallest coefficient for AveOccup, .037618 in comparison to .039326 and .039412. 

## 22

Of all of the feature values, the most corrleated is MedInc. After running the three models on standardized data, the Lasso regression returns the smallest coefficient for MedInc, 0.82001 in comparison to 0.82961 and 0.82888. 

## 23

If looking at the MSE instead of $R^2$ in a Ridge Regression, the optimal alpha value will change from 25.8 to 26.1.

## 24

If looking at the MSE instead of $R^2$ in a Lasso Regression, the optimal alpha value will remain the same at .00186.


[Midterm Code](MidtermAnswers.py)
