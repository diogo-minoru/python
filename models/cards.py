from models.transactions import Transaction

class Card:
    def __init__(self, card_holder, bank, balance):
        self.card_holder = card_holder
        self.bank = bank
        self.balance = balance
        self.transactions = []
    
    def __str__(self):
        return f"Card Holder: {self.card_holder.name} | Bank: {self.bank.name} | Balance: {self.balance:.2f}"
    
    def make_transaction(self, amount, store):
        if amount <= 0:
            status = 'failure'
            failure_reason = 'Amount must be greater than $0'
        elif self.balance >= amount:
            self.balance -= amount
            status = 'success'
            failure_reason = None
        else:
            status = 'failure'
            failure_reason = 'Insufficient Balance'
        transaction = Transaction(amount, status, store, self, failure_reason)
        self.transactions.append(transaction)
        return transaction