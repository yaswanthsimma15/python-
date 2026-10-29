distance = float(input("Journey distance (km): "))
price = float(input("Fuel price per litre (Rs): "))
reserve_pct = float(input("Reserve percentage (e.g. 10): "))
n = int(input("Number of vehicles to compare: "))
 
if distance <= 0 or price <= 0 or reserve_pct < 0 or n <= 0:
    print("Invalid journey details.")
else:
    best = None
    for i in range(n):
        print(f"\nVehicle {i+1}")
        name = input("Vehicle name: ")
        mileage = float(input("Mileage (km/litre): "))
        tank = float(input("Available fuel capacity (litres): "))
        if mileage <= 0 or tank < 0:
            print("Invalid mileage or capacity; skipped.")
            continue
        trip_fuel = distance / mileage
        required = trip_fuel * (1 + reserve_pct / 100)
        cost = trip_fuel * price
        feasible = required <= tank
        print(f"Trip fuel: {trip_fuel:.2f} L")
        print(f"Fuel including reserve: {required:.2f} L")
        print(f"Estimated cost: Rs {cost:.2f}")
        print("Feasible:", "Yes" if feasible else "No")
        if feasible and (best is None or cost < best[1]):
            best = (name, cost, required)
    if best:
        print(f"\nLowest-cost feasible option: {best[0]}")
        print(f"Estimated journey fuel cost: Rs {best[1]:.2f}")
        print(f"Fuel including reserve: {best[2]:.2f} L")
    else:
        print("\nNo vehicle meets the fuel-capacity requirement.")
