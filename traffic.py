fine_rules = {
    "CAR": {"SPEEDING": 1000, "NO_HELMET": 0,
            "NO_LICENCE": 5000, "DANGEROUS_DRIVING": 5000},
    "BIKE": {"SPEEDING": 1000, "NO_HELMET": 500,
             "NO_LICENCE": 5000, "DANGEROUS_DRIVING": 5000},
    "TRUCK": {"SPEEDING": 2000, "NO_HELMET": 0,
              "NO_LICENCE": 5000, "DANGEROUS_DRIVING": 10000}
}
disqualifying = {"NO_LICENCE", "DANGEROUS_DRIVING"}
n = int(input("Number of violations: "))
total = 0
warnings = []
 
for i in range(n):
    print(f"\nViolation {i+1}")
    vehicle = input("Vehicle (CAR/BIKE/TRUCK): ").upper()
    offence = input("Offence (SPEEDING/NO_HELMET/NO_LICENCE/"
                    "DANGEROUS_DRIVING): ").upper()
    repeat = input("Repeat offence? (Y/N): ").upper()
 
    if vehicle not in fine_rules or offence not in fine_rules[vehicle]:
        print("Invalid vehicle category or offence.")
        continue
    if repeat not in ("Y", "N"):
        print("Invalid repeat-offence value.")
        continue
 
    fine = fine_rules[vehicle][offence]
    if repeat == "Y":
        fine *= 2
    total += fine
    print("Penalty: Rs", fine)
    if offence in disqualifying:
        warning = f"{vehicle}: {offence} - disqualification review required"
        warnings.append(warning)
        print("WARNING:", warning)
 
print("\n--- Penalty Summary ---")
print("Total penalty: Rs", total)
if warnings:
    print("Disqualification conditions:")
    for warning in warnings:
        print("-", warning)
else:
    print("No disqualification warning under these sample rules.")
