stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3300,
    "MSFT": 350
}


portfolio = {}

print("📈 Enter your stock portfolio (type 'done' to finish):")

while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print(f"❌ '{stock}' not in stock price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 1:
            print("❌ Quantity must be at least 1.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Invalid quantity. Please enter a number.")

#total investment value
total_value = 0
print("\n📊 Your Portfolio Summary:")
print("-" * 40)
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")
print("-" * 40)
print(f"💰 Total Investment Value: ${total_value}")
print("-" * 40)

#save the report
save = input("Would you like to save this report? (yes/no): ").lower()
if save == 'yes':
    file_format = input("Enter file format (txt/csv): ").lower()
    filename = f"portfolio_report.{file_format}"
    
    try:
        with open(filename, 'w') as file:
            if file_format == 'csv':
                file.write("Stock,Quantity,Price,Value\n")
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    value = qty * price
                    file.write(f"{stock},{qty},{price},{value}\n")
                file.write(f"Total Investment Value,,,{total_value}\n")
            else:  
                file.write("Stock Portfolio Report\n\n")
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    value = qty * price
                    file.write(f"{stock}: {qty} × ${price} = ${value}\n")
                file.write(f"\nTotal Investment Value: ${total_value}\n")
        print(f"✅ Report saved as '{filename}'")
    except Exception as e:
        print(f"❌ Error saving file: {e}")
