import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score



def get_life_from_gdp(filtered_df):
    # ALE Prediction model
    st.header("Predict Life Expectancy")
    st.write("This model uses GDP per capita to predict Life Expectancy .")

    X = filtered_df[['GDP per capita']].values
    y = filtered_df['Life Expectancy (IHME)'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.write(f"Model Performance:")
    st.write(f"Mean Squared Error: {mse:.4f}")
    st.write(f"R-squared Score: {r2:.4f}")

    gdp_input = st.number_input(f"### Enter your yearly income:", min_value=0.0, value=10000.0, value=filtered_df[])
    #life_exp_input = st.number_input("Enter Life Expectancy:", min_value=0.0, max_value=100.0, value=70.0)
    
    if st.button("Predict"):
        prediction = model.predict([[gdp_input]])
        st.write(f"Predicted Life Expectancy:: {prediction[0]:.3f}")