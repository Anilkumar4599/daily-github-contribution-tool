from collections import Counter


def count_word_frequency(filename):
    """
    Read a text file and count the frequency of each word.
    """

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")

    if not text.strip():
        return {}

    # Convert text to lowercase
    text = text.lower()

    # Remove common punctuation
    punctuation = ".,!?;:()[]{}\"'"

    for character in punctuation:
        text = text.replace(character, "")

    # Split text into words
    words = text.split()

    # Count each word
    frequency = Counter(words)

    return frequency


def display_word_frequency(filename):
    """Display word frequency results."""

    try:
        frequency = count_word_frequency(filename)

        print("=== WORD FREQUENCY ANALYZER ===")
        print(f"File: {filename}")

        if not frequency:
            print("No words found.")
            return

        print("\nWord Frequency:")

        for word, count in frequency.most_common():
            print(f"{word} -> {count}")

    except FileNotFoundError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    display_word_frequency("sample_report.txt")