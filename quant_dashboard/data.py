diff --git a//dev/null b/quant_dashboard/data.py
index 0000000000000000000000000000000000000000..a9ff7004c4b05f26cae48899c095ab94c2ef833b 100644
--- a//dev/null
+++ b/quant_dashboard/data.py
@@ -0,0 +1,9 @@
+import pandas as pd
+import yfinance as yf
+
+
+def load_data(ticker: str, start: str, end: str) -> pd.DataFrame:
+    """Download OHLCV data from Yahoo Finance."""
+    data = yf.download(ticker, start=start, end=end, progress=False)
+    data.index.name = "Date"
+    return data
