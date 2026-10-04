def calculate_statistics(numbers):
    """
    Calculate total, average, minimum and maximum
    from a list of numbers.
    """

    if not isinstance(numbers, list):
        raise ValueError("Input must be a list.")

    if not numbers:
        raise ValueError("The list cannot be empty.")

    if not all(isinstance(number, (int, float)) for number in numbers):
        raise ValueError("All values must be numbers.")

    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)

    return total, average, minimum, maximum


def display_statistics(numbers):
    """Display the calculated statistics."""

    try:
        total, average, minimum, maximum = calculate_statistics(numbers)

        print("=== NUMBER STATISTICS ANALYZER ===")
        print(f"Input numbers : {numbers}")
        print(f"Total         : {total}")
        print(f"Average       : {average:.2f}")
        print(f"Minimum       : {minimum}")
        print(f"Maximum       : {maximum}")

    except ValueError as error:
        print(f"Validation Error: {error}")


if __name__ == "__main__":

    # Example QC inspection data
    inspection_results = [95, 98, 92, 97, 96]

    display_statistics(inspection_results)