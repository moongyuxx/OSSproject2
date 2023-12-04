# -*- coding: utf-8 -*-
"""Project#2-2_12223544_문규원.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qpKWghyhOyx1dETPLiKE1ENATzUWeq9X
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def sort_dataset(dataset_df):
	#TODO: Implement this function
    sorted_df = dataset_df.sort_values(by='year', ascending=True).reset_index(drop=True)
    return sorted_df

def split_dataset(dataset_df):
	#TODO: Implement this function
    X = dataset_df.drop(columns='salary', axis=1)
    Y = dataset_df['salary'].mul(0.001)

    X_train = X[:1718]
    X_test = X[1718:]
    Y_train = Y[:1718]
    Y_test = Y[1718:]

    return X_train, X_test, Y_train, Y_test

def extract_numerical_cols(dataset_df):
	#TODO: Implement this function
	numerical_cols = ['age','G','PA','AB','R','H','2B','3B','HR','RBI','SB','CS','BB','HBP','SO','GDP','fly','war']
	numerical_df = dataset_df[numerical_cols]

	return numerical_df


def train_predict_decision_tree(X_train, Y_train, X_test):

	#TODO: Implement this function
	dt_reg = DecisionTreeRegressor()
	dt_reg.fit(X_train, Y_train)

	predicted = dt_reg.predict(X_test)

	return predicted

def train_predict_random_forest(X_train, Y_train, X_test):
	#TODO: Implement this function
	rf_reg = RandomForestRegressor()
	rf_reg.fit(X_train, Y_train)

	predicted = rf_reg.predict(X_test)

	return predicted

def train_predict_svm(X_train, Y_train, X_test):
	#TODO: Implement this function
	svm_pipe = make_pipeline(
		  StandardScaler(),
		  SVR()
	)
	svm_pipe.fit(X_train, Y_train)

	predicted = svm_pipe.predict(X_test)

	return predicted


def calculate_RMSE(labels, predictions):
	#TODO: Implement this function
	RMSE = np.sqrt(np.mean((predictions-labels)**2))
	return RMSE

if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

	sorted_df = sort_dataset(data_df)
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)

	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)

	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))