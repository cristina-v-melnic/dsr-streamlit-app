import streamlit as st
import pandas as pd
import numpy as np

from plots import create_scatter_plot, create_country_plot
from data import get_data

def main():
    st.set_page_config(layout="wide")

    st.markdown("# 🌍 Global Life Quality and Economic Analysis 📊")

    st.markdown("""
    This app allows you to explore the relationships between Human Development Index (HDI), 
    life expectancy, and GDP across different countries and years. 
    Use the sidebar to select options and interact with the data.
    """)

    # Get the merged dataframes
    merged_df = get_data()
    
    # Sidebar
    st.sidebar.header("Customize Your View")
    year_range = st.sidebar.slider("Select Year Range", 
                                   min_value=int(merged_df['year'].min()), 
                                   max_value=int(merged_df['year'].max()), 
                                   value=(int(merged_df['year'].min()), int(merged_df['year'].max())))
    
    #continents = st.sidebar.multiselect("Select Continents", 
    #                                    merged_df['Continent'].unique().tolist(),
    #                                    default=merged_df['Continent'].unique().tolist())

    # Filter data based on sidebar selections
    filtered_df = merged_df[(merged_df['year'].between(year_range[0], year_range[1]))]
    #                         & (merged_df['Continent'].isin(continents))]

    # Tabs
    tab1, tab2, tab3 = st.tabs(["Global Overview", "Country Deep Dive", "Data Explorer"])

    with tab1:
        st.header("Global Overview")

        # Key statistics
        latest_year = filtered_df['year'].max()
        latest_data = filtered_df[filtered_df['year'] == latest_year]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Global Average Life Expectancy", f"{latest_data['Life Expectancy (IHME)'].mean():.1f} years")
        with col2:
            st.metric("Global Median GDP per capita", f"${latest_data['GDP per capita'].median():,.0f}")
        with col3:
            st.metric("Number of Countries", f"{latest_data['country'].nunique()}")

        # Scatter plot
        year = st.slider("Select Year for Visualization", min_value=year_range[0], max_value=year_range[1], value=year_range[1])
        fig = create_scatter_plot(filtered_df, year)
        st.plotly_chart(fig, use_container_width=True)

        # Correlation analysis
        correlation = filtered_df['Life Expectancy (IHME)'].corr(filtered_df['GDP per capita'])
        st.write(f"Correlation between Life Expectancy and GDP per capita: {correlation:.2f}")

        st.markdown("""
        ### Key Insights:
        - There's a strong positive correlation between GDP per capita and life expectancy.
        - However, some countries achieve high life expectancy with relatively lower GDP.
        - The gap between the highest and lowest life expectancies has narrowed over time.
        """)

    with tab2:
        st.header("Country Deep Dive")

        # Country selection
        countries = sorted(filtered_df['country'].unique())
        country = st.selectbox('Select a Country', countries)

        # Country plot
        fig = create_country_plot(filtered_df, country)
        st.plotly_chart(fig, use_container_width=True)

        # Latest statistics for selected country
        latest_country_data = filtered_df[(filtered_df['country'] == country) & (filtered_df['year'] == latest_year)].iloc[0]
        st.write(f"### Latest Statistics for {country} ({latest_year})")
        st.write(f"Life Expectancy: {latest_country_data['Life Expectancy (IHME)']:.2f} years")
        st.write(f"GDP per capita: ${latest_country_data['GDP per capita']:,.2f}")
        #st.write(f"Human Development Index: {latest_country_data['Human Development Index']:.3f}")

    with tab3:
        st.header("Data Explorer")

        # Data table
        st.write(filtered_df)

        # Download option
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='global_development_data.csv',
            mime='text/csv',
        )



if __name__ == "__main__":
    main()