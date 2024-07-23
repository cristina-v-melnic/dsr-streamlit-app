import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


# Create scatter plot
def create_scatter_plot(data, year):
    fig = px.scatter(
        data[data['year'] == year],
        x='GDP per capita',
        y='Life Expectancy (IHME)',
        hover_name='country',
        log_x=True,
        size='Population',
        color='country',
        title=f'Life Expectancy vs GDP per capita ({year})',
        labels={'GDP per capita': 'GDP per capita (log scale)',
                'Life Expectancy (IHME)': 'Life Expectancy (years)'}
    )
    fig.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>Life Expectancy: %{y:.1f} years<br>GDP per capita: $%{x:,.0f}<extra></extra>"
    )
    return fig



# Create country plot
def create_country_plot(merged_data, country):

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(x=merged_data['year'], y=merged_data['Life Expectancy (IHME)'],
                   name="Life Expectancy", line=dict(color="blue")),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Scatter(x=merged_data['year'], y=merged_data['GDP per capita'],
                   name="GDP per capita", line=dict(color="red")),
        secondary_y=True,
    )
    
    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text="Life Expectancy (years)", secondary_y=False)
    fig.update_yaxes(title_text="GDP per capita", secondary_y=True)
    
    fig.update_layout(
        title_text=f"Life Expectancy and GDP per capita in {country} over time",
        hovermode="x unified"
    )
    
    return fig