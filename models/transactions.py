from datetime import datetime
import itertools

class Transaction:
    counter = itertools.count(start=1, step=1)
    def __init__(self, amount, status, store, card, failure_reason=None):
        self.transactionid = next(Transaction.counter)
        self.amount = amount
        self.status = status
        self.store = store
        self.card = card
        self.failure_reason = failure_reason
        self.transactiondate = datetime.now()
    
    def __str__(self):
        if self.status == "failure":
            return (f"Store: {self.store.name} | "
                    f"Amount: {self.amount} | "
                    f"Status: {self.status} | "
                    f"Failure Reason: {self.failure_reason} | "
                    f"Transaction Date: {self.transactiondate}")
        else:
            return (f"Store: {self.store.name} | "
                    f"Amount: {self.amount} | "
                    f"Status: {self.status} | "
                    f"Transaction Date: {self.transactiondate}")
    
    def to_dict(self):
        return {
            "transaction_id": self.transactionid,
            "transaction_date": self.transactiondate,
            "amount": self.amount,
            "status": self.status,
            "failure_reason": self.failure_reason,
            "store_name": self.store.name,
            "store_category": self.store.category,
            "store_city": self.store.city,
            "card_holder": self.card.card_holder.name,
            "bank_name": self.card.bank.name
        }