# Automated Data Cleaning and Preprocessing Tool

## Overview

This project is an Automated Data Cleaning and Preprocessing Tool designed to handle any datasets, in this case it's focused on patient data related to cancer. The tool reads a dataset, cleans it by handling missing values, removing duplicates, and standardising formats, and then outputs the cleaned data for further analysis.

## Features

- **Missing Value Handling**: Automatically fills missing values based on specific strategies (e.g., mean/mode filling).
- **Duplicate Removal**: Detects and removes duplicate records from the dataset.
- **Data Standardisation**: Ensures that categorical variables are standardised and consistent across the dataset.
- **Output**: Saves the cleaned dataset into a specified directory for easy access and further analysis.

## Project Structure

```plaintext
.
├── data/
│   └── data.csv                     # Raw dataset
├── reports/
│   └── cleaned_data.csv             # Cleaned dataset output
├── scripts/
│   └── main.py                      # Main Python script for data cleaning
├── .venv/                           # Python virtual environment (optional)
├── README.md                        # Project documentation
└── requirements.txt                 # Python dependencies
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/automated-data-cleaning.git
   cd automated-data-cleaning
   ```

2. **Set Up a Virtual Environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install Dependencies:**
Install the required Python libraries using pip:

    ```bash
    pip install -r requirements.txt
   ```


4. **Add Dataset:**
Ensure the dataset (data.csv) is located in the data/ directory.
