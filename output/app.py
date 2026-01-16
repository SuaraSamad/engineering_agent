import gradio as gr
from accounts import Account, get_share_price


user_account = Account('test_user')


def create_account(username):
    global user_account
    if username:
        user_account = Account(username)
        return f"Account created for {username}"
    return "Please enter a username"


def deposit(amount):
    try:
        amount = float(amount)
        user_account.deposit(amount)
        return f"Deposited: ${amount:.2f}\nUpdated Balance: ${user_account.balance:.2f}"
    except (ValueError, TypeError):
        return "Please enter a valid amount"


def withdraw(amount):
    try:
        amount = float(amount)
        if user_account.withdraw(amount):
            return f"Withdrew: ${amount:.2f}\nUpdated Balance: ${user_account.balance:.2f}"
        else:
            return "Transaction Failed: Insufficient funds"
    except (ValueError, TypeError):
        return "Please enter a valid amount"


def buy_shares(symbol, quantity):
    try:
        quantity = int(quantity)
        if user_account.buy_shares(symbol, quantity):
            return f"Bought {quantity} shares of {symbol}\nUpdated Holdings: {user_account.get_holdings()}\nBalance: ${user_account.balance:.2f}"
        else:
            return "Transaction Failed: Insufficient funds or invalid quantity"
    except (ValueError, TypeError):
        return "Please enter valid symbol and quantity"


def sell_shares(symbol, quantity):
    try:
        quantity = int(quantity)
        if user_account.sell_shares(symbol, quantity):
            return f"Sold {quantity} shares of {symbol}\nUpdated Holdings: {user_account.get_holdings()}\nBalance: ${user_account.balance:.2f}"
        else:
            return "Transaction Failed: Insufficient holdings or invalid quantity"
    except (ValueError, TypeError):
        return "Please enter valid symbol and quantity"


def get_portfolio_value():
    value = user_account.calculate_portfolio_value()
    return f"Portfolio Value: ${value:.2f}"


def get_profit_or_loss():
    profit_or_loss = user_account.calculate_profit_or_loss()
    return f"Profit/Loss: ${profit_or_loss:.2f}"


def get_holdings():
    holdings = user_account.get_holdings()
    if holdings:
        return str(holdings)
    return "No holdings"


def get_transactions():
    transactions = user_account.get_transactions()
    if transactions:
        return "\n".join([str(t) for t in transactions])
    return "No transactions"


with gr.Blocks(title="Simple Trading Simulation") as demo:
    gr.Markdown("# Simple Trading Simulation")
    gr.Markdown("A simple account management system for a trading simulation platform.")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("## Account Management")
            username_input = gr.Textbox(label="Username", placeholder="Enter username")
            create_btn = gr.Button("Create Account")
            account_output = gr.Textbox(label="Account Status")
            create_btn.click(create_account, inputs=username_input, outputs=account_output)
        
        with gr.Column():
            gr.Markdown("## Transactions")
            deposit_amount = gr.Number(label="Deposit Amount")
            deposit_btn = gr.Button("Deposit")
            deposit_output = gr.Textbox(label="Deposit Status")
            deposit_btn.click(deposit, inputs=deposit_amount, outputs=deposit_output)
            
            withdraw_amount = gr.Number(label="Withdraw Amount")
            withdraw_btn = gr.Button("Withdraw")
            withdraw_output = gr.Textbox(label="Withdraw Status")
            withdraw_btn.click(withdraw, inputs=withdraw_amount, outputs=withdraw_output)
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("## Buy Shares")
            buy_symbol = gr.Textbox(label="Symbol", placeholder="e.g., AAPL")
            buy_quantity = gr.Number(label="Quantity", value=1)
            buy_btn = gr.Button("Buy Shares")
            buy_output = gr.Textbox(label="Buy Status")
            buy_btn.click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs=buy_output)
        
        with gr.Column():
            gr.Markdown("## Sell Shares")
            sell_symbol = gr.Textbox(label="Symbol", placeholder="e.g., AAPL")
            sell_quantity = gr.Number(label="Quantity", value=1)
            sell_btn = gr.Button("Sell Shares")
            sell_output = gr.Textbox(label="Sell Status")
            sell_btn.click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs=sell_output)
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("## Portfolio Information")
            portfolio_btn = gr.Button("Get Portfolio Value")
            portfolio_output = gr.Textbox(label="Portfolio Value")
            portfolio_btn.click(get_portfolio_value, outputs=portfolio_output)
            
            profit_loss_btn = gr.Button("Get Profit/Loss")
            profit_loss_output = gr.Textbox(label="Profit/Loss")
            profit_loss_btn.click(get_profit_or_loss, outputs=profit_loss_output)
        
        with gr.Column():
            holdings_btn = gr.Button("Get Holdings")
            holdings_output = gr.Textbox(label="Holdings")
            holdings_btn.click(get_holdings, outputs=holdings_output)
            
            transactions_btn = gr.Button("Get Transactions")
            transactions_output = gr.Textbox(label="Transactions", lines=10)
            transactions_btn.click(get_transactions, outputs=transactions_output)


if __name__ == '__main__':
    demo.launch()