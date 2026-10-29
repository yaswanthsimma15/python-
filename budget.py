
budget = float(input("Shopping budget (Rs): "))
n = int(input("Number of products: "))

items = []

if budget < 0 or n <= 0:
    print("Invalid budget or product count.")
else:
    for i in range(n):
        print(f"\nProduct {i + 1}")

        name = input("Name: ")
        price = float(input("Unit price (Rs): "))
        qty = int(input("Quantity: "))
        threshold = float(input("Discount threshold subtotal (Rs): "))
        discount_pct = float(input("Discount percentage: "))

        if (price < 0 or qty < 0 or threshold < 0
                or not 0 <= discount_pct <= 100):
            print("Invalid product data.")
            continue

        items.append({
            "name": name,
            "price": price,
            "qty": qty,
            "threshold": threshold,
            "discount": discount_pct
        })

    def line_total(item):
        subtotal = item["price"] * item["qty"]

        if subtotal >= item["threshold"]:
            rate = item["discount"]
        else:
            rate = 0

        return subtotal * (1 - rate / 100)

    original = sum(line_total(item) for item in items)
    print(f"\nOriginal basket total: Rs {original:.2f}")

    # Reduce quantities in reverse entry order until within budget.
    for item in reversed(items):
        while (
            sum(line_total(x) for x in items) > budget
            and item["qty"] > 0
        ):
            item["qty"] -= 1

    final_total = sum(line_total(item) for item in items)

    print("\n--- Final Basket ---")

    for item in items:
        print(
            f"{item['name']}: quantity {item['qty']}, "
            f"line total Rs {line_total(item):.2f}"
        )

    print(f"Final total: Rs {final_total:.2f}")
    print(f"Amount within budget: Rs {budget - final_total:.2f}")

    if final_total > budget:
        print("Budget cannot be met with the remaining basket.")
    else:
        print("Basket is within budget.")
