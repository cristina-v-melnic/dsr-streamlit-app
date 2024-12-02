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

Run the dashboard from the `dsr-streamlit-app` directory:
```bash
streamlit run src/main.py
```

## Data Sources
- Life Expectancy:  [Institute for Health Metrics and Evaluation (IHME) via Our World in Data](https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Healthy%20Life%20Expectancy%20-%20IHME/Healthy%20Life%20Expectancy%20-%20IHME.csv)
- GDP per capita: [Maddison Project Database 2020](https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Maddison%20Project%20Database%202020%20(Bolt%20and%20van%20Zanden%20(2020))/Maddison%20Project%20Database%202020%20(Bolt%20and%20van%20Zanden%20(2020)).csv)
- Poverty rates: [World Bank's Poverty and Inequality Platform (PIP) via Our World in Data](https://raw.githubusercontent.com/owid/poverty-data/main/datasets/pip_dataset.csv)

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
