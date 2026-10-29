subjects = ("Maths", "Physics", "Chemistry", "English", "Python")
PASS_MARK = 40
TREND_MARGIN = 5
 
students = [
    ("Asha", [[55, 60, 48, 70, 65], [62, 66, 52, 72, 70],
              [70, 71, 58, 75, 78]]),
    ("Ravi", [[80, 75, 70, 68, 90], [72, 70, 65, 60, 84],
              [65, 62, 60, 58, 80]]),
    ("Meena", [[35, 38, 50, 60, 45], [30, 36, 55, 62, 48],
               [38, 39, 52, 61, 50]])
]
 
for name, exams in students:
    first, last = exams[0], exams[-1]
    weak = [subjects[i] for i in range(len(subjects))
            if all(exam[i] < PASS_MARK for exam in exams)]
    print("\nStudent:", name)
    print(f"{'Subject':<12}{'First':>7}{'Last':>7}{'Change':>9}")
    for i, subject in enumerate(subjects):
        change = last[i] - first[i]
        print(f"{subject:<12}{first[i]:>7}{last[i]:>7}{change:>+9}")
    first_avg = sum(first) / len(first)
    last_avg = sum(last) / len(last)
    diff = last_avg - first_avg
    if len(weak) >= 2:
        category = "At Risk"
    elif diff > TREND_MARGIN:
        category = "Improving"
    elif diff < -TREND_MARGIN:
        category = "Declining"
    else:
        category = "Consistent"
    print(f"Average: {first_avg:.2f} -> {last_avg:.2f} ({diff:+.2f})")
    print("Consistently weak:", ", ".join(weak) if weak else "None")
    print("Classification:", category)
