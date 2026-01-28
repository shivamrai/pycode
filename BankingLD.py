class BankAccount:
    def __init__(self, account_id: str):
        self.account_id = account_id
        self.balance = 0


class BankingSystem:
    def __init__(self):
        self.accounts = {}
        self.last_timestamp = -1

    def create_account(self, timestamp: int, account_id: str) -> bool:
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = 0
        return True

    def deposit(
            self,
            timestamp: int,
            account_id: str,
            amount: int) -> int | None:
        if account_id not in self.accounts:
            return None
        self.accounts[account_id] += amount
        return self.accounts[account_id]

    def transfer(
        self,
        timestamp: int,
        source_account_id: str,
        target_account_id: str,
        amount: int,
    ) -> int | None:
        if (
            source_account_id not in self.accounts
            or target_account_id not in self.accounts
            or source_account_id == target_account_id
            or self.accounts[source_account_id] < amount
        ):
            return None
        self.accounts[source_account_id] -= amount
        self.accounts[target_account_id] += amount
        return self.accounts[source_account_id]


if __name__ == "__main__":
    # Example usage
    bank = BankingSystem()
    print(bank.create_account(1, "A1"))  # True
    print(bank.deposit(2, "A1", 100))  # 100
    print(bank.create_account(3, "A2"))  # True
    print(bank.transfer(4, "A1", "A2", 50))  # 50
    print(bank.transfer(5, "A1", "A2", 100))  # None (insufficient funds)
    print(bank.deposit(6, "A3", 200))  # None (account does not exist)
    print(bank.create_account(7, "A1"))  # False (account already exists
