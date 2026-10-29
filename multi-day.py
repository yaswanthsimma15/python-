capacity = float(input("Tank capacity (litres): "))
level = float(input("Initial water level (litres): "))
target = float(input("Target level (litres): "))
days = int(input("Number of intervals/days: "))
 
if capacity <= 0 or not 0 <= level <= capacity or not 0 <= target <= capacity or days < 0:
    print("Invalid tank details.")
else:
    first_reached = None
    for day in range(1, days + 1):
        inflow = float(input(f"Day {day} inflow (litres): "))
        outflow = float(input(f"Day {day} outflow (litres): "))
        if inflow < 0 or outflow < 0:
            print("Inflow and outflow must be non-negative.")
            continue
        tentative = level + inflow - outflow
        if tentative > capacity:
            print(f"Day {day}: OVERFLOW of {tentative-capacity:.2f} litres.")
        if tentative < 0:
            print(f"Day {day}: SHORTAGE of {-tentative:.2f} litres.")
        level = min(capacity, max(0, tentative))
        print(f"Day {day} ending level: {level:.2f} litres")
        if first_reached is None and level >= target:
            first_reached = day
    print("\nFinal water level:", round(level, 2), "litres")
    if first_reached is None:
        print("Target level was not reached.")
    else:
        print("First interval reaching target:", first_reached)
