import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import plotly.graph_objects as go


def get_life_prediction(data_df):
    # ALE Prediction model
    st.header("Predict Life Expectancy")
    st.write("This model uses timestamp, GDP per capita, and poverty rates to predict Life Expectancy.")
    feature_names = ['GDP per capita', 'headcount_ratio_upper_mid_income_povline', 'year']
    X = data_df[feature_names].values
    y = data_df['Life Expectancy (IHME)'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #model = LinearRegression()
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)


    st.write(f"#### Model Performance:")
    st.write(f"Mean Squared Error: {mse:.4f}")
    #st.write(f"R-squared Score: {r2:.4f}")

    mdi_importances = pd.Series(
    model.feature_importances_, index=['GDP', 'Poverty rate','Year']
    ).sort_values(ascending=True)


    #ax = mdi_importances.plot.barh()
    #ax.set_title("Random Forest Feature Importances (MDI)")
    #ax.figure.tight_layout()
    mcol1, mcol2 = st.columns(2)


    fig = go.Figure()
    fig.add_trace(go.Bar(
    y= mdi_importances.index,
    x= mdi_importances.values,
    name='SF Zoo',
    orientation='h',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))
    with mcol1:
        st.write("Model feature importance")
        st.plotly_chart(fig, use_container_width=True)

    default_gdp = data_df['GDP per capita'].median()
    default_poverty = data_df['headcount_ratio_upper_mid_income_povline'].median()
    default_year = 2016

    with mcol2:
        gdp_input = st.number_input(f"### Enter the GDP (dollars):", min_value=0.0, max_value=100000.0, value=default_gdp)
        poverty_input = st.number_input("Enter the Poverty Rate (%):", min_value=0.0, max_value=100.0, value=default_poverty)
        year_input = st.number_input("Year of prediction:", min_value=1920, max_value=2016, value=default_year)
    
        if st.button("Predict"):
            prediction = model.predict([[gdp_input, poverty_input, year_input]])
            st.write(f"Predicted Life Expectancy:: {prediction[0]:.3f} Years")