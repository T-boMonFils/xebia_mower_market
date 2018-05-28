if __main__:
	import os
	os.chdir("..")
	
	import joblib
	import pandas as pd
	import numpy as np
	import sklearn as sk
	import API.crunching as cr
	
	scaler = joblib.load("data/scaler/mower_Ridge.pkl")
	model = joblib.load("data/model/mower_Ridge.pkl")
	df = pd.read_csv("Data/mower_market_datasets/submission_set.csv", sep=";")
	
	df = cr.clean_df(df)
	
	train_col =  list(filter(lambda x : x not in ['index', 'id', 'market_share', 'margin'], df.columns))
	df = df[train_col]
	
	scaled_df = scaler.transform(df)
	
	df['attractiveness_pred'] = np.exp(model.predict(scaled_df))-1
	df.to_csv('data/DF/submission.csv')