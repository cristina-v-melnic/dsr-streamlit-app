# Global Life Quality Dashboard

Interactive dashboard exploring relationships between life expectancy, GDP, and poverty rates worldwide using data from Our World in Data.

[Live Demo]([https://your-demo-link.com](https://cristina-v-melnic-dsr-streamlit-app-srcmain-sadmp3.streamlit.app/)

![Dashboard Preview](/api/placeholder/800/400)

## Features
- Global overview with interactive scatter plots
- Country-specific deep dive analysis
- Time series visualizations
- Predictive modeling for life expectancy
- Data explorer with download options

## Installation

```bash
git clone https://github.com/your-username/dsr-streamlit-app.git
cd dsr-streamlit-app
pip install -r requirements.txt
```

## Usage

Run the dashboard:
```bash
streamlit run src/main.py
```

## Data Sources
- Life Expectancy: IHME via Our World in Data
- GDP per capita: Maddison Project Database
- Poverty rates: World Bank via Our World in Data

## Project Structure
```
src/
├── main.py         # Main Streamlit application
├── data.py        # Data loading and processing
├── models.py      # Predictive models
└── plots.py       # Visualization functions
```

## Contributing
Pull requests welcome. For major changes, please open an issue first.

## License
[MIT](https://choosealicense.com/licenses/mit/)
