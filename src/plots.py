import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


# Create scatter plot
def create_scatter_plot(data, year):

    custom_data=['headcount_ratio_upper_mid_income_povline']
    fig = px.scatter(
        data[data['year'] == year],
        x='GDP per capita',
        y='Life Expectancy (IHME)',
        hover_name='country',
        log_x=True,
        size='headcount_ratio_upper_mid_income_povline',
        color='country',
        title=f'Life Expectancy vs GDP per capita ({year})',
        labels={'GDP per capita': 'GDP per capita (log scale)',
                'Life Expectancy (IHME)': 'Life Expectancy (years)',
                'headcount_ratio_upper_mid_income_povline': 'Poverty (%)'},
        custom_data=custom_data
    )
    fig.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>Life Expectancy: %{y:.1f} years<br>GDP per capita: $%{x:,.0f}<br>Poverty: %{customdata[0]:,.2f}% <extra></extra>"
    )

    return fig



def create_country_plot_past(country_data, country):
    # Sort the data by year to ensure proper line plotting
    country_data = country_data.sort_values('year')

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(x=country_data['year'], y=country_data['Life Expectancy (IHME)'],
                   name="Life Expectancy", line=dict(color="blue")),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Scatter(x=country_data['year'], y=country_data['GDP per capita'],
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

def create_country_plot(merged_data, country):
    # Filter data for the selected country
    country_data = merged_data[merged_data['country'] == country].copy()
    
    # Ensure we only use years where both GDP and life expectancy data are available
    country_data = country_data.dropna(subset=['Life Expectancy (IHME)', 'GDP per capita'])
    
    # Sort the data by year to ensure proper line plotting
    country_data = country_data.sort_values('year')

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add Life Expectancy trace
    fig.add_trace(
        go.Scatter(
            x=country_data['year'], 
            y=country_data['Life Expectancy (IHME)'],
            name="Life Expectancy",
            line=dict(color="#3366cc", width=3),
            mode='lines+markers'
        ),
        secondary_y=False,
    )
    
    # Add GDP per capita trace
    fig.add_trace(
        go.Scatter(
            x=country_data['year'], 
            y=country_data['GDP per capita'],
            name="GDP per capita",
            line=dict(color="#dc3912", width=3),
            mode='lines+markers'
        ),
        secondary_y=True,
    )
    
    # Update layout
    fig.update_layout(
        title={
            'text': f"Life Expectancy and GDP per capita in {country}",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24)
        },
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        plot_bgcolor='white',
        hovermode="x unified",
        margin=dict(l=80, r=80, t=100, b=80),
    )
    
    # Update axes
    fig.update_xaxes(
        title_text="Year",
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgrey',
        tickangle=45,
    )
    
    fig.update_yaxes(
        title_text="Life Expectancy (years)",
        secondary_y=False,
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgrey',
        tickformat=".1f"
    )
    
    fig.update_yaxes(
        title_text="GDP per capita ($)",
        secondary_y=True,
        showgrid=False,
        tickformat="$,.0f"
    )
    
    return fig


def create_comparison_plots_past(merged_data, country_data, country, year):
   # Filter data for the specific year
    year_data = merged_data[merged_data['year'] == year].copy()
    country_year_data = country_data[country_data['year'] == year].iloc[0]
    
    # Calculate world averages (excluding the selected country)
    world_data = year_data[year_data['country'] != country]
    world_gdp_avg = world_data['GDP per capita'].mean()
    world_life_exp_avg = world_data['Life Expectancy (IHME)'].mean()
    world_poverty_avg = world_data['headcount_ratio_upper_mid_income_povline'].mean()
    
    # Create subplots
    fig = make_subplots(rows=3, cols=1, 
                        subplot_titles=("GDP per capita", "Life Expectancy (Years)", "Poverty Headcount Ratio (%)"),
                        vertical_spacing=0.1)

    # GDP per capita comparison
    gdp_data = year_data['GDP per capita'].dropna()
    fig.add_trace(
        go.Histogram(x=gdp_data, nbinsx=40, name='World', marker_color='#3366cc'),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=[country_year_data['GDP per capita']], y=[0], mode='markers', 
                   marker=dict(color='red', size=30, symbol='triangle-up'),
                   name=country),
        row=1, col=1
    )

    # Life Expectancy comparison
    life_exp_data = year_data['Life Expectancy (IHME)'].dropna()
    fig.add_trace(
        go.Histogram(x=life_exp_data, nbinsx=40, name='World', marker_color='#3366cc'),
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=[country_year_data['Life Expectancy (IHME)']], y=[0], mode='markers', 
                   marker=dict(color='red', size=30, symbol='triangle-up'),
                   name=country),
        row=2, col=1
    )
    # Poverty Headcount Ratio comparison
    poverty_data = year_data['headcount_ratio_upper_mid_income_povline'].dropna()
    fig.add_trace(
        go.Histogram(x=poverty_data, nbinsx=40, name='World', marker_color='#3366cc'),
        row=3, col=1
    )
    fig.add_trace(
        go.Scatter(x=[country_year_data['headcount_ratio_upper_mid_income_povline']], y=[0], mode='markers', 
                   marker=dict(color='red', size=30, symbol='triangle-up'),
                   name=country),
        row=3, col=1
    )

    # Update layout
    fig.update_layout(
        height=1000,  # Adjust the height as needed
        showlegend=False,
        plot_bgcolor='white',
    )

    # Update x-axes
    #fig.update_xaxes(title_text="GDP per capita ($)", row=1, col=1, tickformat="$,.0f")
    #fig.update_xaxes(title_text="Years", row=2, col=1)
    #fig.update_xaxes(title_text="% of population", row=3, col=1, tickformat=".1f")

    # Update y-axes
    for i in range(1, 4):
        fig.update_yaxes(title_text="Count", row=i, col=1)
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', row=i, col=1)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', row=i, col=1)

    return fig



def create_comparison_plots(merged_data, country_data, country, year):
    # Filter data for the specific year
    year_data = merged_data[merged_data['year'] == year].copy()
    country_year_data = country_data[country_data['year'] == year].iloc[0]

    # Create a custom color palette
    colors = px.colors.qualitative.Set2
    #'Poverty headcount ratio below $5.50 a day (% of population)'
    # Create subplots
    fig = make_subplots(rows=3, cols=1, 
                        subplot_titles=("<b>GDP per capita</b>", "<b>Life Expectancy</b>", "<b>Poverty Headcount Ratio</b>"),
                        vertical_spacing=0.1)

    # GDP per capita histogram
    gdp_data = year_data['GDP per capita'].dropna()
    fig.add_trace(
        go.Histogram(x=gdp_data, nbinsx=30, name='World', marker_color=colors[0], opacity=0.7),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=[country_year_data['GDP per capita']], y=[0], mode='markers', 
                   marker=dict(color=colors[1], size=30, symbol='triangle-up', line=dict(width=2, color='white')),
                   name=country),
        row=1, col=1
    )

    # Life Expectancy histogram
    life_exp_data = year_data['Life Expectancy (IHME)'].dropna()
    fig.add_trace(
        go.Histogram(x=life_exp_data, nbinsx=30, name='World', marker_color=colors[0], opacity=0.7),
        row=2, col=1
    )
    fig.add_trace(
        go.Scatter(x=[country_year_data['Life Expectancy (IHME)']], y=[0], mode='markers', 
                   marker=dict(color=colors[1], size=30, symbol='triangle-up', line=dict(width=2, color='white')),
                   name=country),
        row=2, col=1
    )

    # Poverty Headcount Ratio histogram
    poverty_data = year_data['headcount_ratio_upper_mid_income_povline'].dropna()
    fig.add_trace(
        go.Histogram(x=poverty_data, nbinsx=30, name='World', marker_color=colors[0], opacity=0.7),
        row=3, col=1
    )
    fig.add_trace(
        go.Scatter(x=[country_year_data['headcount_ratio_upper_mid_income_povline']], y=[0], mode='markers', 
                   marker=dict(color=colors[1], size=30, symbol='triangle-up', line=dict(width=2, color='white')),
                   name=country),
        row=3, col=1
    )

    # Update layout
    fig.update_layout(
        height=1000,
        title=dict(
            text=f"<b>{country} and World Distribution in {year}</b>",
            font=dict(size=24)
        ),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        plot_bgcolor='rgba(240,240,240,0.5)',
        paper_bgcolor='white',
        font=dict(family="Arial, sans-serif", size=14),
    )

    # Update x-axes
    #fig.update_xaxes(title_text="<b>GDP per capita ($)</b>", row=1, col=1, tickformat="$,.0f", tickfont=dict(size=12))
    #fig.update_xaxes(title_text="<b>Years</b>", row=2, col=1, tickfont=dict(size=12))
    #fig.update_xaxes(title_text="<b>% of population</b>", row=3, col=1, tickformat=".1f", tickfont=dict(size=12))

    # Update y-axes
    for i in range(1, 4):
        fig.update_yaxes(title_text="<b>Count</b>", row=i, col=1, tickfont=dict(size=12))
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', row=i, col=1)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey', row=i, col=1)

    # Add annotations for country values
    annotations = [
        dict(x=country_year_data['GDP per capita'], y=0, text=f"{country}: ${country_year_data['GDP per capita']:,.0f}", showarrow=True, arrowhead=2, row=1, col=1, yshift=10, font=dict(size=12, color=colors[1])),
        dict(x=country_year_data['Life Expectancy (IHME)'], y=0, text=f"{country}: {country_year_data['Life Expectancy (IHME)']:.1f} years", showarrow=True, arrowhead=2, row=2, col=1, yshift=10, font=dict(size=12, color=colors[1])),
        dict(x=country_year_data['headcount_ratio_upper_mid_income_povline'], y=0, text=f"{country}: {country_year_data['headcount_ratio_upper_mid_income_povline']:.1f}%", showarrow=True, arrowhead=2, row=3, col=1, yshift=10, font=dict(size=12, color=colors[1]))
    ]
    #fig.update_layout(annotations=annotations)

    return fig