# Banking Transaction System

A small Python project built to practice object-oriented programming and basic data engineering concepts. The project models a simple banking transaction flow with users, banks, cards, stores, transactions, reporting, tests, and CSV export.

## Project Goal

The goal of this project is to understand how Python objects can represent a business system, and how those objects can later be transformed into analytical data.

## Architecture

```text
models/
  users.py
  banks.py
  stores.py
  cards.py
  transactions.py

systems/
  banking_system.py
  reporting.py
  exporter.py

tests/
  test_cards.py
  test_banking_system.py
  test_reporting.py

main.py
```

## Responsibilities

### Models

The `models` package contains the main business objects:

- `User`: represents a card holder.
- `Bank`: represents the bank that issued a card.
- `Store`: represents the store where a transaction happens.
- `Card`: owns a user, a bank, a balance, and transaction history.
- `Transaction`: represents one transaction attempt, successful or failed.

### BankingSystem

`BankingSystem` is the system layer. It stores collections of users, banks, stores, and cards.

It is responsible for:

- Adding users, banks, stores, and cards
- Searching transactions by ID
- Returning all transaction objects from all cards

### Reporting

`Reporting` is the analytics layer. It receives a `BankingSystem` object and transforms transaction objects into dictionaries.

It is responsible for:

- Returning all transactions as dictionaries
- Returning failed transactions
- Calculating total transaction volume
- Grouping transaction summaries by bank, store, category, and user

### Exporter

`Exporter` is responsible for saving analytical data to CSV.

Current export flow:

```text
Reporting.get_all_transactions_dict()
-> Exporter.export_to_csv()
-> exports/transactions.csv
```
