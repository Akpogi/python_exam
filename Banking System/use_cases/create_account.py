import entities.account as accountEntity

class CreateAccount:
    def create_account(customer_id, name, email, phone_number):
        account = accountEntity.Account(customer_id)
        account.name = name
        account.email = email
        account.phone_number = phone_number

        return account
