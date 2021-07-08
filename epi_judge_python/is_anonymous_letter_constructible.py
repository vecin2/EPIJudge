import collections

from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str, magazine_text: str) -> bool:
    letter_occurrences = collections.defaultdict(int)

    for letter in letter_text:
        if letter != " ":
            letter_occurrences[letter] -= 1

    for letter in magazine_text:
        if letter != " ":
            letter_occurrences[letter] += 1

    for letter in letter_occurrences:
        if letter_occurrences[letter] < 0:
            return False

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_anonymous_letter_constructible.py",
            "is_anonymous_letter_constructible.tsv",
            is_letter_constructible_from_magazine,
        )
    )
