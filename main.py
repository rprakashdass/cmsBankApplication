import admin, bankclass, customers, loan

class Admin:
    def __init__(self) -> None:
        pass
    def admin(self):
        print(admin.Bank().main())

class CustomerScreen:
    def __init__(self) -> None:
        pass

    def bank_statement(self) -> None:
        print(bankclass.Bank().bank_statement())

    def loan(self) -> None:
        print(loan.Bank().loan())

    def customers(self) -> None:
        print(customers.Bank().customers())

customer_obj = CustomerScreen()
admin_obj = Admin()

print("######################")
customer_obj.bank_statement()
print("######################")
customer_obj.loan()
print("######################")
customer_obj.customers()
print("######################")
admin_obj.admin()
print("######################")
