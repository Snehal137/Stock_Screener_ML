import time
import random
import pandas as pd
import streamlit as st

# Streamlit config - हा कमांड सर्वात आधी असावा
st.set_page_config(page_title="AI/ML Stock Screener", layout="wide")

# Custom Modules Import
from indicators import calculate_smma, calculate_avg_ltp
from ml_model import SignalClassifier
from data_fetcher import fetch_screened_stocks

st.title("📈 Real-Time Stock Screener & AI Signal Analyzer")
st.caption("Live Filter: LTP ₹30-₹500 | Bid Qty & Ask Qty > 10,00,000")

# Initialize Classifier and Placeholders
classifier = SignalClassifier()
placeholder = st.empty()

# Historical Price Data Store
symbols_list = ["TATAMOTORS", "SBIN", "PNB", "BHEL", "IOC", "GAIL", "SAIL", "UNIONBANK"]
price_history = {sym: [random.uniform(40, 50) for _ in range(130)] for sym in symbols_list}

# Live Dashboard Loop
while True:
    stocks = fetch_screened_stocks()
    rows = []

    for s in stocks:
        sym = s["Symbol"]
        ltp = s["LTP"]

        price_history[sym].append(ltp)
        prices = price_history[sym][-130:]

        # Indicator Calculations
        smma_20 = round(calculate_smma(prices, 20), 2)
        smma_120 = round(calculate_smma(prices, 120), 2)

        # ETQ Data
        etq_5m = random.randint(60000, 180000)
        etq_20m = etq_5m * 3 + random.randint(10000, 40000)
        etq_60m = etq_20m * 2 + random.randint(20000, 50000)

        # Average LTP Calculations
        avg_ltp_20m = round(calculate_avg_ltp(prices, 20), 2)
        avg_ltp_60m = round(calculate_avg_ltp(prices, 60), 2)

        # Crossover Logic
        signal = "BUY" if smma_20 > smma_120 else "SELL"

        # AI Prediction
        ltq_2m = random.randint(20000, 70000)
        ltq_5m = random.randint(50000, 110000)
        decision, prob, reason = classifier.predict_crossover(
            ltq_2m, ltq_5m, s["Bid_Qty"], s["Ask_Qty"], smma_20, smma_120
        )

        rows.append({
            "Symbol": sym,
            "LTP": f"₹{ltp}",
            "Bid Price / Qty": f"₹{s['Bid_Price']} ({s['Bid_Qty']:,})",
            "Ask Price / Qty": f"₹{s['Ask_Price']} ({s['Ask_Qty']:,})",
            "SMMA(20)": smma_20,
            "SMMA(120)": smma_120,
            "ETQ (5m / 20m / 60m)": f"{etq_5m:,} / {etq_20m:,} / {etq_60m:,}",
            "Avg LTP (20m / 60m)": f"₹{avg_ltp_20m} / ₹{avg_ltp_60m}",
            "Crossover": signal,
            "AI Prediction": f"{decision} ({prob}%)",
            "Reason": reason
        })

    df = pd.DataFrame(rows)

    with placeholder.container():
        st.dataframe(df, use_container_width=True)
        st.caption("⚡ Live Updating Dashboard (Refreshes every 3 seconds)")

    time.sleep(3)