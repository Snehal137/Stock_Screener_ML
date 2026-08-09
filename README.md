# Stock_Screener_ML

# 📊 Stock Screener ML & Automated Financial Dashboard

An interactive, automated financial data dashboard and machine learning screener designed to fetch real-time stock data, calculate technical indicators, run ML predictions, and visualize insights seamlessly using **Python**, **Streamlit**, and **MySQL**.

---

## 🌟 Key Features

* **Real-time API Data Fetching:** Automatically retrieves live stock market metrics via custom API integrators (`data_fetcher.py`).
* **Technical Indicators:** Computes key technical analysis metrics (`indicators.py`) to evaluate market trends.
* **Machine Learning Analytics:** Integrates ML algorithms (`ml_model.py`) to process historical stock data and identify market patterns.
* **Modular Configuration:** Clean architecture separating API keys, database settings, and global parameters (`config.py`).
* **Interactive UI:** Dynamic web dashboard built with Streamlit (`app.py`) for easy screening and data exploration.

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Frontend / Dashboard:** Streamlit
* **Database:** MySQL
* **Machine Learning & Data Processing:** Pandas, Scikit-learn
* **APIs & Web Requests:** Requests (NSE / Financial APIs)

---

## 📂 Project Architecture

```text
Stock_Screener_ML/
├── app.py             # Main Streamlit UI application
├── app.spec           # PyInstaller build specification
├── config.py          # Configuration settings and API/DB parameters
├── data_fetcher.py    # API request handling and data ingestion
├── indicators.py      # Technical indicator calculation logic
├── ml_model.py        # Machine Learning model training & predictions
└── README.md          # Project documentation
