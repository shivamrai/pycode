"""Banking System - Multi-Level Simulation.

LeetCode 2382: Manage bank accounts with deposit, transfer operations.
Note: timestamp parameter included for future time-based features.
"""


class BankAccount:
    """Represents a single bank account."""

    def __init__(self, account_id: str):
        """Initialize a bank account with account_id."""
        self.account_id = account_id
        self.balance = 0


class BankingSystem:
    """Banking system supporting account creation, deposits, and transfers."""

    def __init__(self):
        """Initialize the banking system."""
        self.accounts = {}
        self.last_timestamp = -1

    def create_account(self, _timestamp: int, account_id: str) -> bool:
        """Create a new account.

        Args:
            _timestamp: Time of operation (unused in Part 1).
            account_id: Unique identifier for the account.

        Returns:
            True if account was created, False if it already exists.
        """
        if account_id in self.accounts:
            return False
        self.accounts[account_id] = 0
        return True

    def deposit(self, _timestamp: int, account_id: str, amount: int) -> int | None:
        """Deposit money into an account.

        Args:
            _timestamp: Time of operation (unused in Part 1).
            account_id: Account to deposit into.
            amount: Amount to deposit.

        Returns:
            Updated account balance, or None if account doesn't exist.
        """
        if account_id not in self.accounts:
            return None
        self.accounts[account_id] += amount
        return self.accounts[account_id]

    def transfer(
        self,
        _timestamp: int,
        source_account_id: str,
        target_account_id: str,
        amount: int,
    ) -> int | None:
        """Transfer money between accounts.

        Args:
            _timestamp: Time of operation (unused in Part 1).
            source_account_id: Account to transfer from.
            target_account_id: Account to transfer to.
            amount: Amount to transfer.

        Returns:
            New balance of source account, or None if transfer is invalid.
        """
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
    print(bank.create_account(7, "A1"))  # False (account already exists)
