from collections import Counter


def find_duplicates(values):
    """
    Find duplicate values in a list.

    Returns a dictionary containing only values
    that appear more than once.
    """

    if not isinstance(values, list):
        raise ValueError("Input must be a list.")

    if not values:
        return {}

    counts = Counter(values)

    duplicates = {
        value: count
        for value, count in counts.items()
        if count > 1
    }

    return duplicates


def display_duplicates(values):
    """Display duplicate values in a simple report."""

    try:
        duplicates = find_duplicates(values)

        print("=== DUPLICATE VALUE ANALYZER ===")
        print(f"Input values : {values}")

        if not duplicates:
            print("Duplicates   : None")
            return

        print("Duplicates:")

        for value, count in duplicates.items():
            print(f"  {value} -> {count} times")

    except ValueError as error:
        print(f"Validation Error: {error}")


if __name__ == "__main__":

    # Sample QC data
    sample_values = [
        "Camera",
        "Router",
        "NVR",
        "Camera",
        "Power",
        "Router",
        "Camera"
    ]

    display_duplicates(sample_values)