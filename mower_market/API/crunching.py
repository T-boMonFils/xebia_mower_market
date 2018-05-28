import os
import pandas as pd
import numpy as np

def clean_df(df):
	'''
	Function that cleans the dataframe
	'''
	
	df.prod_cost = pd.to_numeric(df.prod_cost, errors='coerce')
	
	df = df[df['prod_cost'].isnull()==False]
	
	df.warranty = df.apply(lambda x : pd.to_numeric(x.warranty[0], errors='coerce'), axis=1)
	
	quality_dico = {'Low' : 1, 'Medium' : 2, 'Hight' : 3}
	df.quality.replace(quality_dico, inplace=True)
	
	df = pd.get_dummies(df, columns=["product_type"])
	
	df = df[0 < df.prod_cost]
	
	return df