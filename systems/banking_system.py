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

    def get_transaction_by_id(self, transactionid):
        for card in self.cards:
            for transaction in card.transactions:
                if transaction.transactionid == transactionid:
                    return transaction 
    
    def get_all_transaction_objects(self):
        transaction_objects = []
        for card in self.cards:
            for transaction in card.transactions:
                transaction_objects.append(transaction)
        return transaction_objects