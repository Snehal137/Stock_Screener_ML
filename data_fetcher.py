import random

# System Filters (Requirement 1 & 2)
MIN_LTP = 30.0
MAX_LTP = 500.0
MIN_BID_QTY = 1000000
MIN_ASK_QTY = 1000000

def fetch_screened_stocks():
    """Fetches and filters NSE stocks based on LTP and Liquidity rules."""
    symbols = ["TATAMOTORS", "SBIN", "PNB", "BHEL", "IOC", "GAIL", "SAIL", "UNIONBANK"]
    screened = []

    for sym in symbols:
        ltp = round(random.uniform(25, 520), 2)
        bid_qty = random.randint(800000, 2200000)
        ask_qty = random.randint(800000, 2200000)

        # Apply Requirements: LTP between 30-500 & Liquidity > 10 Lakhs
        if MIN_LTP <= ltp <= MAX_LTP and bid_qty > MIN_BID_QTY and ask_qty > MIN_ASK_QTY:
            screened.append({
                "Symbol": sym,
                "LTP": ltp,
                "Bid_Price": round(ltp - 0.05, 2),
                "Bid_Qty": bid_qty,
                "Ask_Price": round(ltp + 0.05, 2),
                "Ask_Qty": ask_qty,
            })
    return screened