"""
This module is used for pytest
"""

import pandas as pd
import numpy as np

data_df = pd.read_csv("rows-Copy1.csv?accessType=DOWNLOAD_copy")
list_cols = ['Date', 'Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk']

###### All functions that check conditions #######

def check_columns(df, lst_col):
    """
    @param df: dataframe 
    @param lst_col: column name of dataframe
    @return: return 1 if checking condition is true
    """
    return list(df.columns) == lst_col

def check_type_column(df):
    """
    @param df: dataframe 
    @return: return 1 if checking condition is true
    """
    return np.sum([df[x].map(type).nunique() -1 for x in df.columns]) == 0

def check_unique_type(df):
    """
    @param df: dataframe 
    @return: return 1 if checking condition is true
    """
    unique_check = []
    for col in list(df.columns):
        is_unique = np.sum([0 if type(df[col][0]) == type(df[col][i])\
                             else 1 for i in range(0,df.shape[0])])
        unique_check.append(is_unique)
    return np.sum(unique_check) == 0

def check_na(df):
    """
    @param df: dataframe 
    @return: return 1 if checking condition is true
    """
    return np.sum([df[x].isnull().sum() for x in df.columns]) == 0

def check_empty_dataframe(df):
    """
    @param df: dataframe 
    @return: return 1 if checking condition is true
    """
    return df.shape[0] >= 1

def check_num_row(df):
    """
    @param df: dataframe 
    @return: return 1 if checking condition is true
    """
    return df.shape[0] > 10


##### Test functions for pytest ######################

def test_columns_name():
	assert check_columns(data_df, list_cols) == 1

def test_type_column():
    assert check_type_column(data_df) == 1

def test_unique_type():
    assert check_unique_type(data_df) == 1

def test_empty_dataframe():
    assert check_empty_dataframe(data_df) == 1

def test_num_now():
    assert check_num_row(data_df) == 1

def test_na():
    assert check_na(data_df) == 1


