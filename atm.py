n = int(input("Number of transactions: "))
withdrawal_limit = 10000
successful = rejected = 0
deposited = withdrawn = 0.0
 
if balance < 0 or n < 0:
    print("Invalid opening balance or transaction count.")
else:
    for i in range(n):
        kind = input(f"Transaction {i+1} (D=deposit/W=withdrawal): ").upper()
        amount = float(input("Amount (Rs): "))
        if amount <= 0:
            print("Rejected: amount must be positive.")
            rejected += 1
        elif kind == "D":
            balance += amount
            deposited += amount
            successful += 1
            print("Deposit successful.")
        elif kind == "W":
            if amount > withdrawal_limit:
                print("Rejected: withdrawal limit is Rs 10000.")
                rejected += 1
            elif amount > balance:
                print("Rejected: insufficient balance.")
                rejected += 1
            else:
                balance -= amount
                withdrawn += amount
                successful += 1
                print("Withdrawal successful.")
        else:
            print("Rejected: unknown transaction type.")
            rejected += 1
    print("\n--- Transaction Summary ---")
    print(f"Closing balance: Rs {balance:.2f}")
    print(f"Deposited: Rs {deposited:.2f}")
    print(f"Withdrawn: Rs {withdrawn:.2f}")
    print("Successful transactions:", successful)
    print("Rejected transactions:", rejected)
