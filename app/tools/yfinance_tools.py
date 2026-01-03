import yfinance as yf
#from pydantic import ...

def fetch_stock_summary(ticker):
    dat = yf.Ticker(ticker)
    return dat.info

def fetch_stock_history():
    pass

if __name__ == "__main__":
    data = fetch_stock_summary("NVDA")
    print(data)