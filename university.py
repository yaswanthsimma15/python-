attended = int(input("Classes attended: "))
conducted = int(input("Classes conducted: "))
target = float(input("Eligibility percentage (e.g. 75): "))
 
if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance details.")
elif not 0 < target <= 100:
    print("Target must be greater than 0 and at most 100.")
else:
    current = attended / conducted * 100
    print(f"Current attendance: {current:.2f}%")
    if current >= target:
        print("You already meet the eligibility threshold.")
    else:
        for scenario in [1.0, 0.9, 0.75]:
            future = 0
            while ((attended + future * scenario) /
                   (conducted + future)) * 100 < target:
                future += 1
            # For non-perfect attendance, simulate attended future classes
            # by counting only the assumed proportion as attended.
            print(f"Future attendance rate {scenario*100:.0f}%: "
                  f"about {future} classes to reach target.")
