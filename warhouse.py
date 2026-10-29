n = int(input("Number of products: "))
 
if n <= 0:
    print("Enter at least one product.")
else:
    for i in range(n):
        print(f"\nProduct {i+1}")
        name = input("Product name: ")
        opening = int(input("Opening stock: "))
        incoming = int(input("Incoming quantity: "))
        dispatched = int(input("Dispatched quantity: "))
        closing = int(input("Recorded closing stock: "))
        minimum = int(input("Minimum desired stock: "))
 
        values = [opening, incoming, dispatched, closing, minimum]
        if min(values) < 0 or dispatched > opening + incoming:
            print("Invalid quantities; check this product's data.")
            continue
 
        expected = opening + incoming - dispatched
        discrepancy = closing - expected
        replenish = max(0, minimum - closing)
        print("Expected closing stock:", expected)
        print("Recorded closing stock:", closing)
        print("Discrepancy (recorded - expected):", discrepancy)
        print("Replenishment required:", replenish)
        print("Status:", "MATCH" if discrepancy == 0 else "DISCREPANCY FOUND")
