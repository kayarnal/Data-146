import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

ss = StandardScaler()
lin_reg = LinearRegression()

#homes = pd.read_csv('charleston_ask.csv')
 homes = pd.read_csv('charleston_act.csv')

homes.shape
homes

#X = np.array(homes.iloc[:,1:4])
X = np.array(homes.iloc[:,1:28])
y = np.array(homes.iloc[:,0])

# With more splits, the testing set is smaller and there will be more
# variability in the results

kf = KFold(n_splits = 50, shuffle=True)

train_scores=[]
test_scores=[]

# The for loop splits up the training and testing data and creates
# four objects for fitting in linear regression

for idxTrain, idxTest in kf.split(X):
    Xtrain = X[idxTrain, :]
    Xtest = X[idxTest, :]
    ytrain = y[idxTrain]
    ytest = y[idxTest]

    lin_reg.fit(Xtrain, ytrain)

    train_scores.append(lin_reg.score(Xtrain, ytrain))
    test_scores.append(lin_reg.score(Xtest, ytest))

test_scores
train_scores

# Ideal value would be 1, highly correlated
# External validity is less than zero, with the negative testing R2

print('Training: ' + format(np.mean(train_scores), '.3f'))
print('Testing: ' + format(np.mean(test_scores), '.3f'))

# Standardize to improve validity

homes_tform = ss.fit_transform(homes)
homes_tform.shape

#Xt = homes_tform[:,1:3]
Xt = homes_tform[:, 1:28]
yt = homes_tform[:,0]

kf = KFold(n_splits = 50, shuffle=True)

train_scores=[]
test_scores=[]

for idxTrain, idxTest in kf.split(Xt):
    Xtrain = Xt[idxTrain, :]
    Xtest = Xt[idxTest, :]
    ytrain = y[idxTrain]
    ytest = y[idxTest]

    lin_reg.fit(Xtrain, ytrain)

    train_scores.append(lin_reg.score(Xtrain, ytrain))
    test_scores.append(lin_reg.score(Xtest, ytest))

test_scores
train_scores

print('Training: ' + format(np.mean(train_scores), '.3f'))
print('Testing: ' + format(np.mean(test_scores), '.3f'))

# Ridge Regression - penalizes a model with more parameters and/or larger parameters
# Minimizes sum of squared errors while added sum of squared Betas multiplied by alpha

def DoKFold(model, X, y, k, standardize=False, random_state=146):
    if standardize:
        from sklearn.preprocessing import StandardScaler as SS
        ss = SS()

    kf = KFold(n_splits=k, shuffle=True, random_state=random_state)

    train_scores = []
    test_scores = []

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

    return train_scores, test_scores

train_scores, test_scores = DoKFold(lin_reg,X,y,10)

print('Training: ' + format(np.mean(train_scores), '.3f'))
print('Testing: ' + format(np.mean(test_scores), '.3f'))

a_range = np.linspace(0, 100, 100)

k = 50

avg_tr_score = []
avg_te_score = []

for a in a_range:
    rid_reg = Ridge(alpha=a)
    train_scores, test_scores = DoKFold(rid_reg, X, y, k, standardize=True)
    avg_tr_score.append(np.mean(train_scores))
    avg_te_score.append(np.mean(test_scores))

idx = np.argmax(avg_te_score)
print('Optimal alpha value: ' + format(a_range[idx], '.3f'))
print('Training score for this value: ' + format(avg_tr_score[idx],'.3f'))
print('Testing score for this value: ' + format(avg_te_score[idx], '.3f'))

# Lasso Regression

from sklearn.linear_model import Lasso

a_range = np.linspace(0.01, 0.03, 100)

k = 10

avg_tr_score=[]
avg_te_score=[]

for a in a_range:
    las_reg = Lasso(alpha=a)
    train_scores,test_scores = DoKFold(las_reg,X,y,k,standardize=True)
    avg_tr_score.append(np.mean(train_scores))
    avg_te_score.append(np.mean(test_scores))

idx = np.argmax(avg_te_score)
print('Optimal alpha value: ' + format(a_range[idx], '.3f'))
print('Training score for this value: ' + format(avg_tr_score[idx],'.3f'))
print('Testing score for this value: ' + format(avg_te_score[idx], '.3f'))