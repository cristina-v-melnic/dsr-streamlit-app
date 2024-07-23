import streamlit as st
import pandas as pd
import numpy as np


def get_data_visuals(df):
    st.write("Data Preview:")
    st.write(df.head())

    st.write("Data Summary:")
    st.write(df.describe())

    columns = list(df.columns)
    # Plot
    if len(columns)==1:
            st.scatter_chart(df)
    else:
        st.write('Scatter plot of the goods funnel')
        #st.scatter_chart(df[columns[1:]])
        st.scatter_chart(df[[columns[1], columns[2]]])
        #for i in range(len(columns)):
        #    st.scatter_chart(df[columns[0]], df[columns[i]])

        st.write('Revenue over time')
        st.line_chart(df[columns[3]])

def main():

    

    with st.sidebar:
        st.header('Please choose:')
        button_upload = st.button("Upload Data")
        button_explore = st.button("Example Visuals")

    if button_upload:
        st.title("Visualise Your Data")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            get_data_visuals(df)
    elif button_explore:
         st.title("Data Visualisation Example") 
         df_default = pd.read_csv('../data/default_data/sales_data.csv')
         get_data_visuals(df_default)


if __name__ == "__main__":
    main()