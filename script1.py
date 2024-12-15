import yfinance as yf
import pandas as pd

# Pobieranie danych dla symbolu
data = yf.download("AAPL", start="2023-01-01", end="2023-12-31")
data = pd.DataFrame(data) # zmieniam na pandas
data = data[["Close", "Open", "High", "Low"]]
data = data.fillna(0)  # Uzupełnij NaN zerami

