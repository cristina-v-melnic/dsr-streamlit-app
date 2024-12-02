# Global Life Quality Dashboard

Interactive dashboard exploring relationships between life expectancy, GDP, and poverty rates worldwide using data from Our World in Data.

[Live Demo](https://cristina-v-melnic-dsr-streamlit-app-srcmain-sadmp3.streamlit.app/)

## Features

- Global overview with interactive scatter plots
- Country-specific deep dive analysis
- Time series visualizations
- Predictive modeling for life expectancy
- Data explorer with download options

![Screenshot from 2024-12-02 18-16-39](https://github.com/user-attachments/assets/43012e3c-5a38-4d67-a7fb-cb4462183e15)
![Screenshot from 2024-12-02 17-58-31](https://github.com/user-attachments/assets/d4cccf9b-f81a-4fb1-ae53-eb50b0eeca02)


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
