# This python file contains code to be used for predicting numerical output variables using my 
# created 'Linear_Regression' class.

import numpy as np

class Linear_Regression:
    ''' Linear_Regression class is used to predict the values based on calculated coefficients & 
    intercept of regression model using training data set '''
    
    def __init__(self):
        self.intercept_ = None # y_intercept
        self.coef_ = None # beta coefficients
 
    def fit(self,X_train: np, y_train: np):

        # insert one column at the beginning with 1's
        X_train = np.insert(X_train,0,1,axis=1)

        # beta_M is matrix of beta- b0 + b1 + b2 + ... + bn 
        # n - no. of features
        # formula beta = inv([X.trans].X).[X.trans].Y

        beta_M = np.linalg.inv(np.dot(X_train.transpose(),X_train)).dot(X_train.transpose()).dot(y_train)

        self.intercept_ = beta_M[0]
        self.coef_ = beta_M[1:]

    def predict(self,X_test: np):
        y_pred = np.dot(X_test,self.coef_) +self.intercept_ 
        return y_pred
