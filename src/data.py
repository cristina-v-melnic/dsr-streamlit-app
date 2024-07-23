import pandas as pd
import streamlit as st

poverty_url = 'https://raw.githubusercontent.com/owid/poverty-data/main/datasets/pip_dataset.csv'
life_exp_url = "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Healthy%20Life%20Expectancy%20-%20IHME/Healthy%20Life%20Expectancy%20-%20IHME.csv"
gdp_url = 'https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Maddison%20Project%20Database%202020%20(Bolt%20and%20van%20Zanden%20(2020))/Maddison%20Project%20Database%202020%20(Bolt%20and%20van%20Zanden%20(2020)).csv'
    

@st.cache_data
def load_data(poverty_url, life_exp_url, gdp_url):
    
    poverty_df = pd.read_csv(poverty_url)
    life_exp_df = pd.read_csv(life_exp_url)
    gdp_df = pd.read_csv(gdp_url)

    return poverty_df, life_exp_df, gdp_df



def standardize_column_names(df):
    '''
    For the life expectancy and gdp dataframes.
    '''
    cols = {'Year':'year', 'Entity': 'country'}
    return df.rename(cols, axis='columns')



def preprocess_data(poverty_df, life_exp_df, gdp_df):
    return poverty_df, standardize_column_names(life_exp_df), standardize_column_names(gdp_df)


def get_data():

    try:
        poverty_df, life_exp_df, gdp_df = load_data(poverty_url, life_exp_url, gdp_url)
    except Exception as e:
        st.error(f"An error occurred while loading the data: {e}")
        return
    poverty_df, life_exp_df, gdp_df = preprocess_data(poverty_df, life_exp_df, gdp_df)

    merged_df = pd.merge(poverty_df, life_exp_df, on=['country', 'year'])
    merged_df = pd.merge(merged_df, gdp_df, on=['country', 'year'])

    return merged_df
