# A. Import the libraries you will need

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from matplotlib.pyplot import pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error

lin_reg = LinearRegression()
ss = StandardScaler()

# B. Create your DoKFold

def DoKFold(model, X, y, k, standardize = False, random_state = 146):

            if standardize:
                from sklearn.preprocessing import StandardScaler as SS
                ss = SS()

            kf = KFold(n_splits=k, shuffle=True, random_state=random_state)

            train_scores = []
            test_scores = []

            train_MSE = []
            test_MSE = []

            for idxTrain, idxTest in kf.split(X):
                Xtrain = X[idxTrain, :]
                Xtest = X[idxTest, :]
                ytrain = y[idxTrain]
                ytest = y[idxTest]

                if standardize:
                    Xtrain = ss.fit_transform(Xtrain)
                    Xtest = ss.transform(Xtest)

                model.fit(Xtrain, ytrain)

                train_scores.append(model.score(Xtrain, ytrain))
                test_scores.append(model.score(Xtest, ytest))

                pred_train = model.predict(Xtrain)
                pred_test = model.predict(Xtest)

                train_MSE.append(np.sqrt(mean_squared_error(ytrain, pred_train)))
                test_MSE.append(np.sqrt(mean_squared_error(ytest, pred_test)))


            return train_scores,test_scores,train_MSE,test_MSE

# C. Import the the California Housing data

from sklearn.datasets import fetch_california_housing

# D.    # 1. set up X as your features from data.data
        # 2. create a names object from data.feature_names
        # 3. set up y as your target from data.target
        # 4. use pandas to create a data frame from your features and names object

data = fetch_california_housing()
X = data.data
X_names = data.feature_names
y = data.target
y_names = data.target_names

X_df = pd.DataFrame(X, columns = X_names)

### 15. ###

# 1. create a data frame that has all of your features as well as your target
# 2. calculate the correlations of all variables

Xy = X_df.copy()
Xy['y'] = y
Xy.corr()

### 16. ###

# 1. fit transform your features
# 2. create a data frame with the transformed data
# 3. add your target to the data frame
# 4. calculate correlations amongst all variables

Xs = ss.fit_transform(X)

Xs_df = pd.DataFrame(Xs, columns = X_names)
Xsy_df = Xs_df.copy()
Xsy_df['y'] = y
Xsy_df.corr()

### 17 ###

# If we were to perform a linear regression using only the feature identified in question 15,
# what would be the coefficient of determination?
# Enter your answer to two decimal places, for example: 0.12

X_medincome = X[:,0]
X_0 = []
for i in X_medincome:
    i = [i]
    X_0.append(i)

lin_reg.fit(X_0, y)
lin_reg.score(X_0,y)

### 18 ###

Xs = ss.fit_transform(X)

kf = KFold(n_splits = 20, random_state=146, shuffle=True)

train_scores=[]
test_scores=[]

for idxTrain, idxTest in kf.split(Xs):
  Xtrain = Xs[idxTrain, :]
  Xtest = Xs[idxTest, :]
  ytrain = y[idxTrain]
  ytest = y[idxTest]

  lin_reg.fit(Xtrain, ytrain)

  train_scores.append(lin_reg.score(Xtrain, ytrain))
  test_scores.append(lin_reg.score(Xtest, ytest))

print('Testing: ' + format(np.mean(test_scores), '.5f'))

### 19 ###

# Next, try Ridge regression.

rid_a_range = np.linspace(20, 30, 101)

k = 20

avg_tr_score = []
avg_te_score = []

rid_mse_tr = []
rid_mse_te = []

for a in rid_a_range:
    rid_reg = Ridge(alpha=a)
    train_scores, test_scores, train_MSE, test_MSE = DoKFold(rid_reg, X, y, k, standardize=True)
    avg_tr_score.append(np.mean(train_scores))
    avg_te_score.append(np.mean(test_scores))
    rid_mse_tr.append(train_MSE)
    rid_mse_te.append(test_MSE)

idx = np.argmax(avg_te_score)
print('Optimal alpha value: ' + format(rid_a_range[idx], '.5f'))
# alpha = 25.8
print('Testing score for this value: ' + format(avg_te_score[idx], '.5f'))

### 20 ###

las_a_range = np.linspace(.001, .003, 101)

k = 20

avg_tr_score = []
avg_te_score = []

las_mse_tr = []
las_mse_te = []

for a in las_a_range:
    las_reg = Lasso(alpha=a)
    train_scores, test_scores, train_MSE, test_MSE = DoKFold(las_reg, X, y, k, standardize=True)
    avg_tr_score.append(np.mean(train_scores))
    avg_te_score.append(np.mean(test_scores))
    las_mse_tr.append(np.mean(train_MSE))
    las_mse_te.append(np.mean(test_MSE))

idx = np.argmax(avg_te_score)
print('Optimal alpha value: ' + format(las_a_range[idx], '.5f'))
# alpha = .00186
print('Testing score for this value: ' + format(avg_te_score[idx], '.5f'))

### 21 ###

Xs = ss.fit_transform(X)

np.corrcoef(Xs[:,5], y)
X_names

# Least correlated is average occupancy

lin_reg.fit(Xs,y)
lin_coefs = lin_reg.coef_
lin_coefs

# -.03932627

a_range = np.linspace(20, 30, 101)
rid_coefs = []
for a in a_range:
    rid_reg = Ridge(alpha=25.8)
    rid_reg.fit(Xs,y)
    rid_coefs.append(rid_reg.coef_)

rid_coefs

# -.03941257

a_range = np.linspace(0.001, 0.003, 101)

las_coefs = []
for a in a_range:
    las_reg = Lasso(alpha=.00186)
    las_reg.fit(Xs,y)
    las_coefs.append(las_reg.coef_)

las_coefs
# -.03761823

### 22 ###

Xs = ss.fit_transform(X)

np.corrcoef(Xs[:,0], y)
X_names

# Most correlated is median income

lin_reg.fit(Xs,y)
lin_coefs = lin_reg.coef_
lin_coefs

# .8296193

a_range = np.linspace(20, 30, 101)
rid_coefs = []
for a in a_range:
    rid_reg = Ridge(alpha=25.8)
    rid_reg.fit(Xs,y)
    rid_coefs.append(rid_reg.coef_)

rid_coefs

# .82888925

a_range = np.linspace(0.001, 0.003, 101)

las_coefs = []
for a in a_range:
    las_reg = Lasso(alpha=.00186)
    las_reg.fit(Xs,y)
    las_coefs.append(las_reg.coef_)

las_coefs

# .82001408

### 23 ###

# If we had looked at MSE instead of R2 when doing our Ridge regression (question 19),
# would we have determined the same optimal value for alpha, or something different?

idx = np.argmin(rid_mse_te)
print(rid_a_range[idx], rid_mse_tr[idx], rid_mse_te[idx])

### 24 ###

# If we had looked at MSE instead of R2 when doing our Lasso regression (question 20),
# what would we have determined the optimal value for alpha to be?
# Enter your answer to 5 decimal places, for example: 0.12345

idx = np.argmin(las_mse_te)
print(las_a_range[idx], las_mse_te[idx], las_mse_tr[idx])