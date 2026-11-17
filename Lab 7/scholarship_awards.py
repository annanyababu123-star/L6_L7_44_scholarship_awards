import math


def parse_applicant(text):
    """Parse 'category:marks'. Returns (Category, marks) or None if invalid."""
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    category = parts[0].strip()
    if not category:
        return None
    try:
        marks = float(parts[1])
    except ValueError:
        return None
    if not math.isfinite(marks):
        return None
    return category.title(), marks


def marks_average(marks_csv):
    """Average of comma-separated integer marks. Returns None if invalid."""
    if not isinstance(marks_csv, str):
        return None
    try:
        values = [int(r) for r in marks_csv.split(',')]
    except ValueError:
        return None
    if not values:
        return None
    return sum(values) // len(values)


def payable_award(text):
    """Parse 'award|deduction' and return payable amount (>= 0), or None if invalid."""
    if not isinstance(text, str):
        return None
    parts = text.split('|')
    if len(parts) != 2:
        return None
    try:
        award = float(parts[0])
        deduction = float(parts[1])
    except ValueError:
        return None
    if not (math.isfinite(award) and math.isfinite(deduction)):
        return None
    total = award * 1.18 - deduction
    if not math.isfinite(total):
        return None
    return max(total, 0)


def main():
    print("==== Running parse_applicant ====")
    user_input = input("Enter category:marks (e.g. merit:82): ")
    result = parse_applicant(user_input)
    print("Category and Marks:", result if result is not None else "Invalid input")

    print("\n==== Running marks_average ====")
    user_input = input("Enter marks as CSV (e.g. 72,85,90): ")
    result = marks_average(user_input)
    print("Average Marks:", result if result is not None else "Invalid input")

    print("\n==== Running payable_award ====")
    user_input = input("Enter award|deduction (e.g. 5000|500): ")
    result = payable_award(user_input)
    print("Payable Award:", result if result is not None else "Invalid input")


if __name__ == "__main__":
    main()
