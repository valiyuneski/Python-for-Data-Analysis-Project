# Python for Data Analysis Project

A beginner-friendly data analysis project using Python, Pandas, NumPy, Matplotlib, and Seaborn.

## Project Overview

This project demonstrates fundamental data analysis techniques on a car dataset (`data.csv`), including:

- Data cleaning and handling missing values
- Data type conversions
- Filtering and string operations
- Feature engineering (creating new columns)
- Exploratory Data Analysis (EDA)
- Data grouping and aggregation
- Data visualization (histograms, bar charts, scatter plots, boxplots)
- Correlation analysis with heatmaps

## Setup Instructions

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate   # On Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the notebook

Open `project.ipynb` in Jupyter Notebook, VS Code, or any IDE that supports `.ipynb` files, and run the cells sequentially.

## File Structure

```
.
├── data.csv              # Car dataset
├── project.ipynb         # Main analysis notebook
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Dependencies

- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `matplotlib` - Plotting and visualization
- `seaborn` - Statistical data visualization

## Dataset Columns

- `Make`, `Model`, `Year` - Vehicle identification
- `Engine Fuel Type`, `Engine HP`, `Engine Cylinders` - Engine specs
- `Transmission Type`, `Driven_Wheels` - Drivetrain
- `Number of Doors`, `Vehicle Size`, `Vehicle Style` - Body specs
- `highway MPG`, `city mpg` - Fuel efficiency
- `Popularity`, `MSRP` - Market data

## Notes

- The notebook includes inline package installation (`!{sys.executable} -m pip install`) for environments where dependencies may not be pre-installed.
- All visualizations are generated using Matplotlib and Seaborn.
