'''
Done By KrishnaKumar
'''
class BankAdmin:
    def __init__(self, admin_id, username, password, email):
        self.admin_id = admin_id
        self.username = username
        self.password = password
        self.email = email

    def create_account(self, customer_name, account_type, initial_balance):
        pass

    def manage_accounts(self):
        pass

    def generate_report(self):
        pass

    def __str__(self):
        return f"Bank Admin {self.username} ({self.email})"