from systems.banking_system import BankingSystem
from systems.reporting import Reporting
from models.cards import Card
from models.banks import Bank
from models.stores import Store
from models.users import User

def test_get_all_transactions_dict_returns_dictionaries():
    system = BankingSystem()
    reporting = Reporting(system)

    user1 = User("Cabelo", "04/08/1997", "Ribeirão Preto", "São Paulo", "Brazil", "cabelo@example.com", "44999999999")
    bank1 = Bank("Itaú", "São Paulo", "São Paulo", "Brazil")
    card1 = Card(user1, bank1, 50000)
    store1 = Store("Store 1", "Eletronic", "Ribeirão Preto", "São Paulo", "Brazil")

    system.add_user(user1)
    system.add_card(card1)
    system.add_bank(bank1)
    system.add_store(store1)
    card1.make_transaction(1000, store1)

    transactions = reporting.get_all_transactions_dict()

    assert type(transactions[0]) == type(dict())

def test_get_failed_transactions_returns_only_failures():
    system = BankingSystem()
    reporting = Reporting(system)

    user1 = User("Cabelo", "04/08/1997", "Ribeirão Preto", "São Paulo", "Brazil", "cabelo@example.com", "44999999999")
    bank1 = Bank("Itaú", "São Paulo", "São Paulo", "Brazil")
    card1 = Card(user1, bank1, 500)
    store1 = Store("Store 1", "Eletronic", "Ribeirão Preto", "São Paulo", "Brazil")

    system.add_user(user1)
    system.add_card(card1)
    system.add_bank(bank1)
    system.add_store(store1)
    card1.make_transaction(1000, store1)
    card1.make_transaction(400, store1)
    card1.make_transaction(200, store1)
    card1.make_transaction(100, store1)

    transactions = reporting.get_failed_transactions()
    status = [transaction.get('status') for transaction in transactions]

    assert 'success' not in status