import numpy as np

def calculate_smma(prices, period):
    """Smoothed Moving Average (SMMA) calculation."""
    if len(prices) < period:
        return None
    smma = [sum(prices[:period]) / period]
    for price in prices[period:]:
        smma.append((smma[-1] * (period - 1) + price) / period)
    return smma[-1]

def calculate_avg_ltp(prices, period):
    """Average LTP over N periods."""
    if len(prices) < period:
        return np.mean(prices) if prices else 0.0
    return np.mean(prices[-period:])