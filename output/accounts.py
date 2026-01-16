class Account:
    def __init__(self, username: str) -> None:
        self.username = username
        self.balance = 0.0
        self.initial_deposit = 0.0
        self.holdings = {}
        self.transactions = []

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            self.initial_deposit += amount
            self.transactions.append({'type': 'deposit', 'amount': amount})

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append({'type': 'withdraw', 'amount': amount})
            return True
        return False

    def buy_shares(self, symbol: str, quantity: int) -> bool:
        share_price = get_share_price(symbol)
        total_price = share_price * quantity
        if quantity > 0 and total_price <= self.balance:
            self.balance -= total_price
            if symbol in self.holdings:
                self.holdings[symbol] += quantity
            else:
                self.holdings[symbol] = quantity
            self.transactions.append({'type': 'buy', 'symbol': symbol, 'quantity': quantity})
            return True
        return False

    def sell_shares(self, symbol: str, quantity: int) -> bool:
        if symbol in self.holdings and 0 < quantity <= self.holdings[symbol]:
            share_price = get_share_price(symbol)
            total_price = share_price * quantity
            self.balance += total_price
            self.holdings[symbol] -= quantity
            if self.holdings[symbol] == 0:
                del self.holdings[symbol]
            self.transactions.append({'type': 'sell', 'symbol': symbol, 'quantity': quantity})
            return True
        return False

    def calculate_portfolio_value(self) -> float:
        portfolio_value = self.balance
        for symbol, quantity in self.holdings.items():
            portfolio_value += get_share_price(symbol) * quantity
        return portfolio_value

    def calculate_profit_or_loss(self) -> float:
        return self.calculate_portfolio_value() - self.initial_deposit

    def get_holdings(self) -> dict:
        return self.holdings

    def get_transactions(self) -> list:
        return self.transactions

def get_share_price(symbol: str) -> float:
    prices = {
        'AAPL': 150.0,
        'TSLA': 800.0,
        'GOOGL': 2800.0
    }
    return prices.get(symbol, 0.0)

# Sample usage
account = Account('user123')
account.deposit(10000)
account.buy_shares('AAPL', 20)
account.withdraw(500)
print(account.calculate_portfolio_value())
print(account.calculate_profit_or_loss())
print(account.get_holdings())
print(account.get_transactions())