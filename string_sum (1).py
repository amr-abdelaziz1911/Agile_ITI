import re

def extract_integers(text: str) -> list[int]:
    """Extract all integers *including negatives* from a string."""
    tokens = re.findall(r"-?\d+", text)
    digits = []
    for token in tokens:
        is_negative = token.startswith("-")
        for i, digit in enumerate(token.lstrip("-")):
            digits.append(-int(digit) if is_negative and i == 0 else int(digit))
    return digits


def sum_integers_in_string(text: str) -> int:
    """ A function to summ the integrs we extrat """
    if not isinstance(text, str):
        raise TypeError(f"Expected a string, got {type(text).__name__!r}")

    integers = extract_integers(text)

    return sum(integers)


if __name__ == "__main__":
    examples = [
        "I have 3 cats and 2 dogs",
        "Temperatures: -10 and 20",
        "no numbers here",
        "10 Saqr 22 Amr 9",
        "100",
        "Mix: 5 apples, -3 oranges, and 8 bananas"
    ]

    for example in examples:
        result = sum_integers_in_string(example)
        print(f"Input : {example!r}")
        print(f"Result: {result}\n")


