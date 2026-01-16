import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account('testuser')

    def test_initialization(self):
        self.assertEqual(self.account.username, 'testuser')
        self.assertEqual(self.account.balance, 0.0)
        self.assertEqual(self.account.initial_deposit, 0.0)
        self.assertEqual(self.account.holdings, {})
        self.assertEqual(self.account.transactions, [])

    def test_deposit(self):
        self.account.deposit(1000)
        self.assertEqual(self.account.balance, 1000)
        self.assertEqual(self.account.initial_deposit, 1000)
        self.assertEqual(len(self.account.transactions), 1)
        self.assertEqual(self.account.transactions[0]['type'], 'deposit')
        
        # Test negative deposit
        self.account.deposit(-500)
        self.assertEqual(self.account.balance, 1000)

    def test_withdraw(self):
        self.account.deposit(1000)
        result = self.account.withdraw(500)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 500)
        self.assertEqual(len(self.account.transactions), 2)
        self.assertEqual(self.account.transactions[1]['type'], 'withdraw')

        # Test overwithdraw
        result = self.account.withdraw(600)
        self.assertFalse(result)
        self.assertEqual(self.account.balance, 500)

    def test_buy_shares(self):
        self.account.deposit(10000)
        result = self.account.buy_shares('AAPL', 10)
        self.assertTrue(result)
        self.assertEqual(self.account.holdings['AAPL'], 10)
        self.assertEqual(len(self.account.transactions), 2)
        self.assertEqual(self.account.transactions[1]['type'], 'buy')

        # Test insufficient funds for buying shares
        result = self.account.buy_shares('AAPL', 100)
        self.assertFalse(result)

    def test_sell_shares(self):
        self.account.deposit(10000)
        self.account.buy_shares('AAPL', 10)
        result = self.account.sell_shares('AAPL', 5)
        self.assertTrue(result)
        self.assertEqual(self.account.holdings['AAPL'], 5)
        self.assertEqual(len(self.account.transactions), 3)
        self.assertEqual(self.account.transactions[2]['type'], 'sell')

        # Test selling more than holdings
        result = self.account.sell_shares('AAPL', 10)
        self.assertFalse(result)

    def test_calculate_portfolio_value(self):
        self.account.deposit(10000)
        self.account.buy_shares('AAPL', 10)
        portfolio_value = self.account.calculate_portfolio_value()
        self.assertEqual(portfolio_value, self.account.balance + 1500)

    def test_calculate_profit_or_loss(self):
        self.account.deposit(2000)
        self.account.buy_shares('AAPL', 10)
        profit_or_loss = self.account.calculate_profit_or_loss()
        self.assertEqual(profit_or_loss, self.account.calculate_portfolio_value() - 2000)

    def test_get_holdings(self):
        self.account.deposit(10000)
        self.account.buy_shares('AAPL', 10)
        holdings = self.account.get_holdings()
        self.assertEqual(holdings, {'AAPL': 10})

    def test_get_transactions(self):
        self.account.deposit(10000)
        self.account.buy_shares('AAPL', 10)
        transactions = self.account.get_transactions()
        self.assertEqual(len(transactions), 2)

    def test_get_share_price(self):
        self.assertEqual(get_share_price('AAPL'), 150)
        self.assertEqual(get_share_price('TSLA'), 800)
        self.assertEqual(get_share_price('GOOGL'), 2800)
        self.assertEqual(get_share_price('UNKNOWN'), 0)

if __name__ == '__main__':
    unittest.main()