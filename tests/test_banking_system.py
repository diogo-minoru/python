from models.users import User
from models.banks import Bank
from models.cards import Card
from models.stores import Store
from systems.banking_system import BankingSystem

def test_add_user_stores_user():
    system = BankingSystem()

    user1 = User("Diogo", "04/08/1997", "Marialva", "Paraná", "Brazil", "diogominoru@example.com", "44999999999")
    user2 = User("Diogo", "04/08/1997", "Marialva", "Paraná", "Brazil", "diogominoru@example.com", "44999999999")
    user3 = User("Diogo", "04/08/1997", "Marialva", "Paraná", "Brazil", "diogominoru@example.com", "44999999999")
    
    system.add_user(user1)
    system.add_user(user2)
    system.add_user(user3)

    assert len(system.users) == 3

def test_add_bank_stores_bank():
    system = BankingSystem()

    bank1 = Bank("Itaú", "São Paulo", "São Paulo", "Brazil")
    bank2 = Bank("Nubank", "São Paulo", "São Paulo", "Brazil")

    system.add_bank(bank1)
    system.add_bank(bank2)

    assert len(system.banks) == 2

def test_get_transaction_by_id_returns_matching_transaction():
    system = BankingSystem()

    user1 = User("Diogo", "04/08/1997", "Marialva", "Paraná", "Brazil", "diogominoru@example.com", "44999999999")
    bank1 = Bank("Itaú", "São Paulo", "São Paulo", "Brazil")
    card1 = Card(user1, bank1, 10000)
    store1 = Store("Store 1", "Eletronic", "Ribeirão Preto", "São Paulo", "Brazil")
    
    system.add_card(card1)
    transaction = card1.make_transaction(1000, store1)

    assert system.get_transaction_by_id(transaction.transactionid) is transaction

def test_get_transaction_by_id_returns_none_when_not_found():
    system = BankingSystem()

    user2 = User("Diogo", "04/08/1997", "Marialva", "Paraná", "Brazil", "diogominoru@example.com", "44999999999")
    bank2 = Bank("Itaú", "São Paulo", "São Paulo", "Brazil")
    card2 = Card(user2, bank2, 10000)
    store1 = Store("Store 1", "Eletronic", "Ribeirão Preto", "São Paulo", "Brazil")
    
    system.add_card(card2)
    transaction = card2.make_transaction(1000, store1)

    assert system.get_transaction_by_id(transaction.transactionid + 1) is None

def test_get_all_transaction_objects_returns_transactions_from_all_cards():
    system = BankingSystem()

    user1 = User("Cabelo", "04/08/1997", "Ribeirão Preto", "São Paulo", "Brazil", "cabelo@example.com", "44999999999")
    user2 = User("Diogo", "04/08/1997", "Marialva", "Paraná", "Brazil", "diogominoru@example.com", "44999999999")
    bank2 = Bank("Itaú", "São Paulo", "São Paulo", "Brazil")
    card1 = Card(user1, bank2, 50000)
    card2 = Card(user2, bank2, 10000)
    store1 = Store("Store 1", "Eletronic", "Ribeirão Preto", "São Paulo", "Brazil")
    
    system.add_card(card1)
    system.add_card(card2)
    transaction11 = card1.make_transaction(12000, store1)
    transaction21 = card2.make_transaction(2000, store1)
    transaction22 = card2.make_transaction(3000, store1)

    transactions = system.get_all_transaction_objects()

    assert len(transactions) == 3
    assert transaction11 in transactions
    assert transaction21 in transactions
    assert transaction22 in transactions