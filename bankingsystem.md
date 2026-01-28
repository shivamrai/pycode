---

```markdown
# Banking System — Multi-Level Simulation (CodeSignal / Karat Style)

This project implements a progressively more complex banking system across **four levels**, as used in multi-stage coding assessments (CodeSignal, Karat, Coinbase, etc.).

Each level builds on the previous one and introduces new system behaviors, data structures, and time-based execution logic.

---

# 📘 Part 1 — Basic Banking System

### Implement the following APIs:

#### `create_account(timestamp, account_id) → bool`
Creates a new account with balance **0**.

- Return `False` if the account already exists.
- Otherwise create the account and return `True`.

#### `deposit(timestamp, account_id, amount) → int | None`
Deposits money into an existing account.

- Return `None` if the account does not exist.
- Otherwise increase balance and return the updated balance.

#### `transfer(timestamp, source, target, amount) → int | None`
Transfers money between accounts.

Return `None` if:
- either account does not exist  
- source == target  
- insufficient funds  

Otherwise:
- subtract from source  
- add to target  
- return **source’s new balance**

### Notes
- All timestamps are strictly increasing.
- Part 1 does not use timestamps for logic.
- Balances cannot become negative.

---

# 📗 Part 2 — Top Spenders / Analytics

Extends Part 1 by tracking **outgoing transfer amounts** and ranking accounts based on spending.

### New API

#### `top_spenders(timestamp, n) → List[str]`

Returns the **top n** accounts sorted by:

1. **Descending outgoing transfer amount**
2. **Alphabetical account_id** for ties

Format each result as:

```

"<account_id>(<outgoing_total>)"

```

### Additional Details
- Only **successful transfers** contribute to outgoing totals.
- Deposits do NOT count.
- If fewer than `n` accounts exist, return all of them.

---

# 📙 Part 3 — Scheduled Payments (Delayed Execution)

Adds support for **one-time scheduled debits** that run automatically at future timestamps.

### New APIs

#### `schedule_payment(timestamp, account_id, amount, delay) → str | None`

Schedules a payment that will attempt to deduct `amount` from the account at:

```

execute_time = timestamp + delay

```

Return a unique ID such as `"payment1"`, or `None` if the account does not exist.

#### `cancel_payment(timestamp, account_id, payment_id) → bool`

Cancels a pending payment.

Return `True` only if:

- the payment exists  
- belongs to the given account  
- has not executed  
- has not already been canceled  

Otherwise return `False`.

---

### Scheduled Payment Execution Rules

Before processing any API call at timestamp `T`:

> Execute all scheduled payments with `execute_time <= T`  
> **in the order they were created (FIFO).**

For each payment:
- If the account has enough balance → deduct it  
- If not → skip (no deduction)  
- Either way → remove the payment from pending schedule

---

# 📕 Part 4 — Merging Accounts & Historical Balances

Adds account merging and full time-travel balance queries based on historical snapshots.

### New APIs

#### `merge_accounts(timestamp, account_id_1, account_id_2) → bool`

Merges **account_id_2 into account_id_1**.

Return `False` if:
- either account does not exist  
- account IDs are equal  

Otherwise:

- Add account2’s balance into account1  
- Combine outgoing totals (for top_spenders)  
- Reassign scheduled payments from account2 to account1  
- Remove account2 from the system  
- Return `True`

---

#### `get_balance(timestamp, account_id, time_at) → int | None`

Returns the **balance of the account at timestamp `time_at`**.

Rules:
- If the account did not exist at `time_at` → return `None`
- Must reflect:
  - deposits
  - transfers
  - scheduled payments executed by `time_at`
  - merges that occurred before or at `time_at`
- Requires maintaining a `balance_history` list:
```

[(timestamp, balance_after_change), ...]

```
- Use binary search to find the latest entry with `timestamp <= time_at`.

---

# 🧱 System Requirements Summary

| Feature | Part |
|--------|------|
| Create / Deposit / Transfer | 1 |
| Track outgoing totals | 2 |
| Rank top spenders | 2 |
| Scheduled future payments | 3 |
| Cancel scheduled payments | 3 |
| Execute scheduled payments at correct time | 3 |
| Merge accounts | 4 |
| Move scheduled payments to merged account | 4 |
| Combine outgoing totals | 4 |
| Historical balance lookup | 4 |

---

# 🛠 Suggested Class Structure

```

BankingSystem                (Part 1)
↑
BankingSystemWithAnalytics   (Part 2)
↑
BankingSystemWithScheduled   (Part 3)
↑
BankingSystemWithHistory     (Part 4)

```

Each class extends the previous one, adding new functionality.

---

# 📦 Recommended Repository Structure

```

.
├── part1_basic/
│   └── banking_system_part1.py
├── part2_analytics/
│   └── banking_system_part2.py
├── part3_scheduled/
│   └── banking_system_part3.py
├── part4_history/
│   └── banking_system_part4.py
└── README.md

```

---

# ✔ Ready for Implementation

This README describes all four stages clearly in a real interview-style format.

If you want, I can also generate:

- starter code for each part  
- full working implementations  
- test scripts  
- a combined final class

Just tell me!
```

---
