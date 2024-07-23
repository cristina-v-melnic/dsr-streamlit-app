import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create the scatter plot
def create_scatter_plot(data, year):
    fig = px.scatter(
        data[data['Year'] == year],
        x='GDP per capita',
        y='Life Expectancy (IHME)',
        hover_name='Entity',
        log_x=True,  # Use log scale for GDP
        size='Population',  # Adjust point size based on population
        color='Entity',  # Color points by continent
        title=f'Life Expectancy vs GDP per capita ({year})',
        labels={'GDP per capita': 'GDP per capita log scale',
                'Life expectancy': 'Life Expectancy (years)'}
    )
    return fig

def display_global_stats(life_exp_df, gdp_df, enable=False):
    if enable:

        # Merge the dataframes
        merged_df = pd.merge(life_exp_df, gdp_df, on=['Entity', 'Year'])

        # Streamlit app
        st.title(f'## Global Life Expectancy vs GDP per capita')

        # Slider for year selection
        year = st.slider('Select Year', min_value=int(merged_df['Year'].min()),
                    max_value=int(merged_df['Year'].max()),
                    value=int(merged_df['Year'].max()))

        # Create and display the plot
        fig = create_scatter_plot(merged_df, year)
        st.plotly_chart(fig, use_container_width=True)


        # Optional: Display the data table
        if st.checkbox('Show Data Table'):
            st.write(year_data)


        # Display some statistics
        st.write(f"### Statistics for {year}")
        year_data = merged_df[merged_df['Year'] == year]
        st.write(f"Number of countries: {len(year_data)}")
        st.write(f"Average Life Expectancy: {year_data['Life Expectancy (IHME)'].mean():.2f} years")
        st.write(f"Average GDP per capita: ${year_data['GDP per capita'].mean():.2f}")

            

def create_country_plot(life_exp_data, gdp_data, country):
    # Merge the dataframes for the selected country
    merged_data = pd.merge(
        life_exp_data[life_exp_data['Entity'] == country],
        gdp_data[gdp_data['Entity'] == country],
        on=['Entity', 'Year']
    )
    
    # Create the figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add life expectancy trace
    fig.add_trace(
        go.Scatter(x=merged_data['Year'], y=merged_data['Life Expectancy (IHME)'],
                   name="Life Expectancy", line=dict(color="blue")),
        secondary_y=False,
    )
    
    # Add GDP per capita trace
    fig.add_trace(
        go.Scatter(x=merged_data['Year'], y=merged_data['GDP per capita'],
                   name="GDP per capita", line=dict(color="red")),
        secondary_y=True,
    )
    
    # Set x-axis title
    fig.update_xaxes(title_text="Year")
    
    # Set y-axes titles
    fig.update_yaxes(title_text="Life Expectancy (years)", secondary_y=False)
    fig.update_yaxes(title_text="GDP per capita", secondary_y=True)
    
    # Set title
    fig.update_layout(
        title_text=f"Life Expectancy and GDP per capita in {country} over time",
        hovermode="x unified"
    )
    
    return fig


# Load data
@st.cache_data
def load_data():
    
    poverty_url = 'https://raw.githubusercontent.com/owid/poverty-data/main/datasets/pip_dataset.csv'
    life_exp_url = "https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Healthy%20Life%20Expectancy%20-%20IHME/Healthy%20Life%20Expectancy%20-%20IHME.csv"
    gdp_url = 'https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Maddison%20Project%20Database%202020%20(Bolt%20and%20van%20Zanden%20(2020))/Maddison%20Project%20Database%202020%20(Bolt%20and%20van%20Zanden%20(2020)).csv'
    poverty_df = pd.read_csv(poverty_url)
    life_exp_df = pd.read_csv(life_exp_url)
    gdp_df = pd.read_csv(gdp_url)

    return poverty_df, life_exp_df, gdp_df

def filter_time(x, min_year=1900):
    return x>min_year



def main():
    st.set_page_config(layout="wide")
    st.title("Global Poverty and Life Quality Analysis")

    # Load data
    poverty_df, life_exp_df, gdp_df = load_data()

    # Sidebar for country selection
    countries = sorted(list(set(poverty_df['country']) & set(life_exp_df['Entity']) & set(gdp_df['Entity'])))
    country = st.selectbox("#### Please select a country", countries)

    # Filter data for selected country
    poverty_data = poverty_df[poverty_df['country'] == country]
    life_exp_data = life_exp_df[life_exp_df['Entity'] == country]
    gdp_data = gdp_df[gdp_df['Entity'] == country]

    # Display basic information
    #st.write(f"## {country}")
    st.write("\n")
    st.write("\n")

    st.write(f"## General indicators")
    # Poverty rate
    latest_poverty_year = poverty_data['year'].max()
    earliest_poverty_year = poverty_data['year'].min()
    latest_poverty_rate = poverty_data[poverty_data['year'] == latest_poverty_year]['headcount_ratio_international_povline'].values[0]
    st.write(f"#### Poverty rate in {latest_poverty_year}:")
    st.write("{:.2f}%".format(latest_poverty_rate))
    st.write("living on less than $1.90 a day.")

    # Life expectancy
    latest_life_exp_year = life_exp_data['Year'].max()
    earliest_life_exp_year = life_exp_data['Year'].min()
    latest_life_exp = life_exp_data[life_exp_data['Year'] == latest_life_exp_year]['Life Expectancy (IHME)'].values[0]
    st.write(f"#### Life expectancy in {latest_life_exp_year}:")
    st.write("{:.1f} years".format(latest_life_exp))

    # GDP per capita
    latest_gdp_year = gdp_data['Year'].max()
    earliest_gdp_year = gdp_data['Year'].min()
    latest_gdp = gdp_data[gdp_data['Year'] == latest_gdp_year]['GDP per capita'].values[0]
    st.write(f"#### GDP per capita in {latest_gdp_year}: ")
    st.write("${:.2f}".format(latest_gdp))
    st.write("\n")
    st.write("\n")

    # Plot life expectancy and GDP per capita over time

    st.write("## Life Expectancy and GDP per capita Over Time")

    # Create and display the plot
    fig = create_country_plot(life_exp_df, gdp_df, country=country)
    st.plotly_chart(fig, use_container_width=True)
    #st.pyplot(fig)

    st.write("\n")
    st.write("\n")
    # Simple ML model to predict life expectancy based on GDP per capita
    st.write("## Model Life Expectancy based on personal GDP in {}".format(country))
    #st.write("This model uses specific GDP per capita to predict life expectancy in {}.".format(country))

    # Prepare data for ML model
    life_exp_mask = life_exp_data['Year'].apply(filter_time, min_year=max(earliest_gdp_year, earliest_life_exp_year))
    gdp_mask = gdp_data['Year'].apply(filter_time, min_year=max(earliest_gdp_year, earliest_life_exp_year))

    merged_data = pd.merge(life_exp_data[life_exp_mask], gdp_data[gdp_mask], on='Year')
    X = merged_data['GDP per capita'].values.reshape(-1, 1)
    y = merged_data['Life Expectancy (IHME)'].values

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Model performance
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.write("\n")
    st.write(f"**Model accuracy scores**")
    st.write(f"     Mean Squared Error = {mse:.2f}")
    st.write(f"     R-squared Score = {r2:.2f}")
    st.write("\n")

    # User input for prediction
    user_input = st.number_input(f"### Enter GDP per capita:", min_value=0.0, value=latest_gdp, max_value=100000.0)
    
    if st.button("Predict"):
        prediction = model.predict([[user_input]])
        st.write(f"Predicted life expectancy: {prediction[0]:.1f} years")

    st.write("\n")
    st.write("\n")

    display_global_stats(life_exp_df, gdp_df, enable=False)

if __name__ == "__main__":
    main()