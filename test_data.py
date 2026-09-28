import yfinance as yf

t = yf.Ticker("TCS.NS")
print(t.info.get("longName"), t.info.get("debtToEquity"), t.info.get("operatingMargins"))
print(t.history(period="1mo").tail())