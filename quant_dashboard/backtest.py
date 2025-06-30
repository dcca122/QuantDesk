diff --git a//dev/null b/quant_dashboard/backtest.py
index 0000000000000000000000000000000000000000..98be6d7a3c1d18292d2b2562beafc765fac292b3 100644
--- a//dev/null
+++ b/quant_dashboard/backtest.py
@@ -0,0 +1,17 @@
+import pandas as pd
+import numpy as np
+
+
+def backtest(prices: pd.Series, signals: pd.Series) -> pd.DataFrame:
+    """Simple backtest applying signals to price returns."""
+    returns = prices.pct_change().fillna(0)
+    strategy_returns = returns * signals.shift(1).fillna(0)
+    cum = (1 + strategy_returns).cumprod()
+    dd = cum / cum.cummax() - 1
+    stats = {
+        "Cumulative Return": cum.iloc[-1] - 1,
+        "Sharpe": np.sqrt(252) * strategy_returns.mean() / strategy_returns.std(ddof=0),
+        "Max Drawdown": dd.min(),
+        "Win Rate": (strategy_returns > 0).mean(),
+    }
+    return pd.DataFrame(stats, index=[0]), cum, dd
