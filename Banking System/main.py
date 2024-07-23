import infrastracture.account_repository as account_repository
import use_cases.transaction as transaction
import use_cases.account_statement as account_statement
import use_cases.create_account as create_account

# Create New Accounts
create_acc = create_account.CreateAccount
new_account1 = create_acc.create_account('01', 'Juan Dela Cruz', 'jdc@gmail.com', '09124567854')
new_account2 = create_acc.create_account('02', 'John Doe', 'j2@gmail.com', '0954124638')

# Save the accounts
account_repo = account_repository.AccountRepository()
account_repo.save_account(new_account1)
account_repo.save_account(new_account2)

# Transaction

# Account statement instance
account_statement = account_statement.AccountStatement()
# Transaction instance
transaction = transaction.Transaction(account_repo, account_statement)

# Make a deposit transaction
print("Deposit")
transaction.make_transaction('02', 520, 'deposit')

# Make a withdrawal transaction
print("Withdraw")
transaction.make_transaction('02', 521, 'withdraw')

# Generate and print account statement
account_statement.generate_account_statement('02')

# Find account using account_id
print("Find account with Account ID of '02'")
account_repo.find_account_by_id('02')

# Find account using customer_id
print("Find account with Customer ID of '02'")
account_repo.find_accounts_by_customer_id('02')







