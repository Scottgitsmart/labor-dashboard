OVERTIME_THRESHOLD = 40  # hours per week


def calculate_overtime(hours_worked):
    """Return overtime hours beyond the standard threshold."""
    if hours_worked <= OVERTIME_THRESHOLD:
        return 0
    return hours_worked - OVERTIME_THRESHOLD


def calculate_pay(hours_worked, hourly_rate, overtime_multiplier=1.5):
    """Calculate total pay including overtime."""
    regular_hours = min(hours_worked, OVERTIME_THRESHOLD)
    overtime_hours = calculate_overtime(hours_worked)
    return (regular_hours * hourly_rate) + (overtime_hours * hourly_rate * overtime_multiplier)


if __name__ == "__main__":
    print("Labor Dashboard")
    print("---------------")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter hourly rate: $"))
    total = calculate_pay(hours, rate)
    print(f"Total pay: ${total:.2f}")
