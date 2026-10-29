rules = {
    "CSE": {"aggregate": 75, "subject": 70},
    "ECE": {"aggregate": 65, "subject": 60},
    "MECH": {"aggregate": 55, "subject": 50}
}
n = int(input("Number of applicants: "))
eligible = []
 
for i in range(n):
    print(f"\nApplicant {i+1}")
    name = input("Name: ")
    course = input("Course (CSE/ECE/MECH): ").upper()
    aggregate = float(input("Aggregate percentage: "))
    subject = float(input("Required subject percentage: "))
    entrance = float(input("Entrance score (0-100): "))
 
    if course not in rules:
        print("Rejected: unknown course.")
        continue
    if not (0 <= aggregate <= 100 and 0 <= subject <= 100
            and 0 <= entrance <= 100):
        print("Rejected: marks must be between 0 and 100.")
        continue
 
    cutoff = rules[course]
    reasons = []
    if aggregate < cutoff["aggregate"]:
        reasons.append(f"aggregate below {cutoff['aggregate']}%")
    if subject < cutoff["subject"]:
        reasons.append(f"subject marks below {cutoff['subject']}%")
    if reasons:
        print("Not eligible:", ", ".join(reasons))
    else:
        eligible.append((aggregate, entrance, name, course))
        print("Eligible for ranking.")
 
eligible.sort(key=lambda x: (-x[0], -x[1], x[2].lower()))
print("\n--- Ranked Eligible Applicants ---")
if not eligible:
    print("No eligible applicants.")
else:
    for rank, (aggregate, entrance, name, course) in enumerate(eligible, 1):
        print(f"{rank}. {name} | {course} | Aggregate: {aggregate:.2f}% "
              f"| Entrance: {entrance:.2f}")
