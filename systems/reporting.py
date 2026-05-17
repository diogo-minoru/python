class Reporting:
    def __init__(self, banking_system):
        self.banking_system = banking_system
    
    def get_all_transactions_dict(self):
        all_transactions = []
        for transaction in self.banking_system.get_all_transaction_objects():
            all_transactions.append(transaction.to_dict())
        return all_transactions
    
    def get_failed_transactions(self):
        failed_transactions = []
        for transaction in self.get_all_transactions_dict():
            if transaction.get('status') == 'failure':
                failed_transactions.append(transaction)
        return failed_transactions
    
    def get_transactions_from_store(self, store):
        store_transactions = []
        for transaction in self.get_all_transactions_dict():
            if transaction.get('store_name') == store:
                store_transactions.append(transaction)
        return store_transactions
    
    def get_total_transaction_volume(self):
        transactions = 0
        volume = 0
        for transaction in self.get_all_transactions_dict():
            if transaction.get('status') == 'success':
                transactions += 1
                volume += transaction.get('amount')
        
        return {
                    "successful_transactions": transactions,
                    "total_volume": volume
                }