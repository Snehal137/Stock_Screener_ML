import numpy as np
from sklearn.ensemble import RandomForestClassifier

class SignalClassifier:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=50, random_state=42)
        self._fit_initial_model()

    def _fit_initial_model(self):
        # Initial training on sample quantitative features
        # Features: [LTQ_Spike_Ratio, Bid_Ask_Imbalance, SMMA_Diff_Pct]
        X = [
            [2.5, 0.6, 1.2],   # Volume spike + strong bid -> Profitable
            [0.4, -0.5, -0.8],  # Weak volume -> Losing trade
            [1.8, 0.4, 0.5],   # Moderate spike -> Profitable
            [0.2, -0.2, -0.1]   # Low volume -> Avoid
        ]
        y = [1, 0, 1, 0] # 1: Accept, 0: Reject
        self.model.fit(X, y)

    def predict_crossover(self, ltq_2m, ltq_5m, bid_qty, ask_qty, smma_20, smma_120):
        ltq_ratio = ltq_2m / (ltq_5m + 1e-5)
        bid_ask_imbalance = (bid_qty - ask_qty) / (bid_qty + ask_qty + 1e-5)
        smma_diff = ((smma_20 - smma_120) / smma_120) * 100

        features = [[ltq_ratio, bid_ask_imbalance, smma_diff]]
        prob = self.model.predict_proba(features)[0][1]
        
        accept = prob >= 0.50
        reason = "LTQ volume spike detected in trade direction." if accept else "Avoid: Weak LTQ momentum during crossover."
        
        return ("ACCEPT" if accept else "REJECT"), round(prob * 100, 1), reason