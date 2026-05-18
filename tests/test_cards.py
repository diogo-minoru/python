from models.users import User
from models.banks import Bank
from models.cards import Card
from models.stores import Store

# 1. Valid transaction - reduces card-balance
def test_successful_transaction_reduces_card_balance():
    # Arrange
    user = User("Diogo", "04-08-1997", "Marialva", "Parana", "Brazil", "diogo@example.com", "44999999999")
    bank = Bank("Nubank", "Sao Paulo", "Sao Paulo", "Brazil")
    store = Store("Store 1", "Groceries", "Sao Paulo", "Sao Paulo", "Brazil")
    card = Card(user, bank, 1000)

    # Act
    transaction = card.make_transaction(200, store)

    # Assert
    assert transaction.status == "success"
    assert card.balance == 800
    assert len(card.transactions) == 1


# 2. Amount is zero
def test_transaction_amount_equals_zero():
    # Arrange
    user = User("Diogo", "04-08-1997", "Marialva", "Parana", "Brazil", "diogo@example.com", "44999999999")
    bank = Bank("Nubank", "Sao Paulo", "Sao Paulo", "Brazil")
    store = Store("Store 1", "Groceries", "Sao Paulo", "Sao Paulo", "Brazil")
    card = Card(user, bank, 1000)

    # Act
    transaction = card.make_transaction(0, store)

    # Assert
    assert transaction.status == 'failure'
    assert card.balance == card.balance
    assert len(card.transactions) == 1
    assert transaction.failure_reason == 'Amount must be greater than $0'

# 3. Amount is negative
def test_transaction_amount_negative():
    # Arrange
    user = User("Diogo", "04-08-1997", "Marialva", "Parana", "Brazil", "diogo@example.com", "44999999999")
    bank = Bank("Nubank", "Sao Paulo", "Sao Paulo", "Brazil")
    store = Store("Store 1", "Groceries", "Sao Paulo", "Sao Paulo", "Brazil")
    card = Card(user, bank, 1000)

    # Act
    transaction = card.make_transaction(-100, store)

    # Assert
    assert transaction.status == 'failure'
    assert card.balance == card.balance
    assert len(card.transactions) == 1
    assert transaction.failure_reason == 'Amount must be greater than $0'
# 4. Amount is greater than balance
def test_amount_greater_than_balance():
    # Arrange
    user = User("Diogo", "04-08-1997", "Marialva", "Parana", "Brazil", "diogo@example.com", "44999999999")
    bank = Bank("Nubank", "Sao Paulo", "Sao Paulo", "Brazil")
    store = Store("Store 1", "Groceries", "Sao Paulo", "Sao Paulo", "Brazil")
    card = Card(user, bank, 1000)

    # Act
    transaction = card.make_transaction(10000, store)

    # Assert
    assert transaction.status == 'failure'
    assert card.balance == card.balance
    assert len(card.transactions) == 1
    assert transaction.failure_reason == 'Insufficient Balance'