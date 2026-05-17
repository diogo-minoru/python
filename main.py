from systems.banking_system import BankingSystem
from systems.reporting import Reporting
from models.users import User
from models.banks import Bank
from models.cards import Card
from models.stores import Store
    
system = BankingSystem()
reporting = Reporting(system)

user1 = User("Diogo", "04-08-1997", "Marialva", "Paraná", "Brazil", "diogominoru@example.com", "44999999999")
user2 = User("Jorisval", "04-08-1992", "Maringá", "Paraná", "Brazil", "jorisval@example.com", "44888888888")
user3 = User("Geralt", "04-08-1994", "Londres", "Paris", "França", "geraltrivia@example.com", "44777777777")

system.add_user(user1)
system.add_user(user2)
system.add_user(user3)

bank1 = Bank("Itaú", "São Paulo", "São Paulo", "Brazil")
bank2 = Bank("Nubank", "São Paulo", "São Paulo", "Brazil")
bank3 = Bank("BTG", "São Paulo", "São Paulo", "Brazil")

system.add_bank(bank1)
system.add_bank(bank2)
system.add_bank(bank3)

store1 = Store("Store 1", "Eletronic", "Ribeirão Preto", "São Paulo", "Brazil")
store2 = Store("Store 2", "Groceries", "São Paulo", "São Paulo", "Brazil")
store3 = Store("Store 3", "Auto", "Maringá", "Paraná", "Brazil")

system.add_store(store1)
system.add_store(store2)
system.add_store(store3)

card1 = Card(user1, bank1, 50000)
card2 = Card(user2, bank2, 10000)
card3 = Card(user3, bank2, 160000)

system.add_card(card1)
system.add_card(card2)
system.add_card(card3)

transaction11 = card1.make_transaction(10000, store1)
transaction12 = card1.make_transaction(5000, store2)
transaction13 = card1.make_transaction(9000, store2)

transaction21 = card2.make_transaction(8000, store3)
transaction22 = card2.make_transaction(2000, store3)
transaction23 = card2.make_transaction(1000, store2)

transaction31 = card3.make_transaction(10000, store1)
transaction32 = card3.make_transaction(-50000, store1)
transaction33 = card3.make_transaction(9000, store1)


# df = pd.DataFrame(system.get_all_transactions())
print(reporting.get_failed_transactions())