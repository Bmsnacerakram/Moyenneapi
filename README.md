# MoyenneAPI 🌤️

## 📌 About the Project

MoyenneAPI is a Python project that collects weather data from three different weather APIs using geographical coordinates (latitude and longitude).

The project retrieves the maximum daily temperature from each API, calculates the average temperature, and saves the results in a CSV file using Pandas.

## 🚀 Features

- Get weather data using latitude and longitude.
- Connect to three different weather APIs.
- Retrieve maximum daily temperatures.
- Calculate the average temperature from three API sources.
- Display the results in a Pandas DataFrame.
- Export the final results to a CSV file.

## 🔗 APIs Used

1. **Open-Meteo API** – Provides daily maximum temperature data.
2. **7Timer API** – Provides weather forecast information.
3. **WeatherAPI** – Provides historical weather data.

## 🛠️ Technologies

- Python
- Requests
- Pandas
- Datetime
- OS

## 📦 Installation

Install the required libraries:

```bash
pip install requests pandas
```

## ▶️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/Bmsnacerakram/Moyenneapi.git
```

2. Open the project folder:

```bash
cd Moyenneapi
```

3. Run the Python script:

```bash
python main.py
```

4. Enter your latitude and longitude when requested.

5. Enter your WeatherAPI key when requested.

## 📊 Output

The program calculates the average maximum temperature from the three API sources.

The results are displayed in a Pandas DataFrame and saved as a CSV file:

```text
temporateur_moy/
    └── table.csv
```

## 🎯 Project Goal

The main goal of this project is to practice working with multiple APIs, collecting and processing data, using Pandas, and exporting results to CSV files.

## 👨‍💻 Author

**Bmsnacerakram**

GitHub: https://github.com/Bmsnacerakram
