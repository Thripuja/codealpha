import yfinance as yf

def get_stock_price(symbol):

    stock = yf.Ticker(symbol)
    price = stock.history(period="1d")['Close'].iloc[-1]
    return price
def track_portfolio(portfolio):

    total_value = 0.0
    for symbol, shares in portfolio.items():
        price = get_stock_price(symbol)
        value = price * shares
        print(f"{symbol}: ${price:.2f} x {shares} shares = ${value:.2f}")
        total_value += value
    return total_value


def main():

    portfolio = {
        "AAPL": 10,  # Example: 10 shares of Apple
        "GOOGL": 5,  # Example: 5 shares of Google
        "MSFT": 8  # Example: 8 shares of Microsoft
    }

    print("Stock Portfolio Tracker")
    total_value = track_portfolio(portfolio)
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")


if __name__ == "__main__":
    main()
