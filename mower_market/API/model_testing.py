import os
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn import linear_model as lm
from sklearn.externals import joblib

def split_dataframe(df, train_col, target_col):
	'''
	Function that split a dataframe between variables X, and target Y
	'''
	
	X = df[train_col]
	Y = df[target_col]
	
	return X, Y


def sample_dataframe(df, frac=0.8):
	'''
	Function that creates a train and a test set
	'''
	
	train = df.sample(frac=frac)
	test = df.drop(train.index)
	
	return train, test
	

def eval_model(df, model, train_col=None, target_col=None):
	'''
	Function that regiter model performance
	'''

	if not train_col: train_col =  list(filter(lambda x : x not in ['index', 'id', 'market_share', 'attractiveness'], df.columns))
	if not target_col : target_col = 'attractiveness'
	
	X , Y = split_dataframe(df, train_col, target_col)
	
	train_X, test_X = sample_dataframe(X)
	
	train_Y = Y[train_X.index.values.tolist()]
	test_Y = Y[test_X.index.values.tolist()]
	
	model.fit(train_X, np.log(train_Y+1))
	
	pred_test_X = model.predict(test_X)
	
	return sk.metrics.mean_squared_error(np.log(test_Y+1), pred_test_X)
	
def save_model(df, train_col, target_col, model, path='data/'):
	'''
	Function that saves the model and metadata scripts
	'''
	
	X, Y = split_dataframe(df, train_col, target_col)
	model.fit(X, np.log(Y+1))
	
	joblib.dump(model, path+'model/'+'mower_Ridge.save')
	