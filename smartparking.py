rates = {"CAR": 30, "BIKE": 15, "VAN": 50}
daily_caps = {"CAR": 250, "BIKE": 120, "VAN": 400}
allowed_hours = 24
penalty = 200
 
def to_minutes(value):
    parts = value.split(":")
    if len(parts) != 2:
        raise ValueError
    hour, minute = int(parts[0]), int(parts[1])
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        raise ValueError
    return hour * 60 + minute
 
try:
    entry = to_minutes(input("Entry time (HH:MM): "))
    exit_time = to_minutes(input("Exit time (HH:MM): "))
    vehicle = input("Vehicle type (CAR/BIKE/VAN): ").upper()
 
    if vehicle not in rates:
        print("Invalid vehicle category.")
    else:
        duration = exit_time - entry
        if duration < 0:
            duration += 24 * 60  # overnight parking
        hours = ceil(duration / 60)
        base_fee = min(hours * rates[vehicle], daily_caps[vehicle])
        extra_penalty = penalty if duration > allowed_hours * 60 else 0
        total = base_fee + extra_penalty
        print(f"Parking duration: {duration // 60} hours "
              f"{duration % 60} minutes")
        print("Hourly charge before cap: Rs", hours * rates[vehicle])
        print("Daily cap: Rs", daily_caps[vehicle])
        print("Penalty: Rs", extra_penalty)
        print(f"Total parking fee: Rs {total:.2f}")
except (ValueError, IndexError):
    print("Invalid time. Use 24-hour HH:MM format.")
