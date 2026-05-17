class BankingSystem:
    def __init__(self):
        self.users = []
        self.cards = []
        self.banks = []
        self.stores = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def add_user(self, user):
        self.users.append(user)
    
    def add_bank(self, bank):
        self.banks.append(bank)
    
    def add_store(self, store):
        self.stores.append(store)

    def get_all_transactions(self):
        all_transactions = []
        for card in self.cards:
            for transaction in card.transactions:
                all_transactions.append(transaction.to_dict())
        return all_transactions
    
    def get_failed_transactions(self):
        failed_transactions = []
        for transaction in self.get_all_transactions():
            if transaction.get('status') == 'failure':
                failed_transactions.append(transaction)
        return failed_transactions
    
    def get_transactions_from_store(self, store):
        store_transactions = []
        for transaction in self.get_all_transactions():
            if transaction.get('store_name') == store:
                store_transactions.append(transaction)
        return store_transactions
    
    def get_total_transaction_volume(self):
        transactions = 0
        volume = 0
        for transaction in self.get_all_transactions():
            if transaction.get('status') == 'success':
                transactions += 1
                volume += transaction.get('amount')
        
        return {
                    "successful_transactions": transactions,
                    "total_volume": volume
                }