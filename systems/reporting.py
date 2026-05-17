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
    
    def get_summary_by_bank(self):
        summary_by_bank = {}
        for transaction in self.get_all_transactions_dict():
            bank_name = transaction.get('bank_name')
            amount = transaction.get('amount')
            if transaction.get('status') == 'success':
                if bank_name not in summary_by_bank:
                    summary_by_bank[bank_name] = {
                        'transaction_count': 0,
                        'transaction_amount': 0
                        }
                summary_by_bank[bank_name]['transaction_count'] += 1
                summary_by_bank[bank_name]['transaction_amount'] += amount

        return summary_by_bank
    
    def get_summary_by_store(self):
        summary_by_store = {}
        for transaction in self.get_all_transactions_dict():
            store = transaction.get('store_name')
            amount = transaction.get('amount')
            if transaction.get('status') == 'success':
                if store not in summary_by_store:
                    summary_by_store[store] = {
                        'transaction_count': 0,
                        'transaction_amount': 0
                    }
                summary_by_store[store]['transaction_count'] += 1
                summary_by_store[store]['transaction_amount'] += amount
        return summary_by_store
    
    def get_summary_by_category(self):
        summary_by_category = {}
        for transaction in self.get_all_transactions_dict():
            category = transaction.get('store_category')
            amount = transaction.get('amount')
            if transaction.get('status') == 'success':
                if category not in summary_by_category:
                    summary_by_category[category] = {
                        'transaction_count': 0,
                        'transaction_amount': 0
                    }
                summary_by_category[category]['transaction_count'] += 1
                summary_by_category[category]['transaction_amount'] += amount
        return summary_by_category

    def get_summary_by_user(self):
        summary_by_user = {}
        for transaction in self.get_all_transactions_dict():
            user = transaction.get('card_holder')
            amount = transaction.get('amount')
            if transaction.get('status') == 'success':
                if user not in summary_by_user:
                    summary_by_user[user] = {
                        'transaction_count': 0,
                        'transaction_amount': 0
                    }
                summary_by_user[user]['transaction_count'] += 1
                summary_by_user[user]['transaction_amount'] += amount
        return summary_by_user