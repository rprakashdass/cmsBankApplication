class Bank:
    def __init__(self, name):
        self.name = name
    def loan(self, credit_score, income, debt):
        min_credit_score = 650
        min_income = 30000
        max_debt_to_income_ratio = 0.4
        debt_to_income_ratio = debt / income

        if credit_score >= min_credit_score and income >= min_income and debt_to_income_ratio <= max_debt_to_income_ratio:
            return "Loan Approved"
        else:
            return "Loan Denied"
bank = Bank("AML Bank")
credit_score = int(input("Enter Credit score:"))
income = int(input("Enter Your income:"))
debt = int(input("Enter your debt:"))
decision = bank.loan(credit_score, income, debt)
print(decision)
