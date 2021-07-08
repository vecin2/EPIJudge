from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    # TODO - you fill in here.

    start_index, end_index = 0, len(s) - 1

    while start_index < end_index:
        if not s[start_index].isalnum:
            start_index = +1

            break
        elif not s[end_index].isalnum:
            end_index = -1

            break

        elif s[start_index].upper() != s[end_index].upper():
            return False
        else:
            start_index += 1
            end_index -= 1

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_palindromic.py", "is_string_palindromic.tsv", is_palindromic
        )
    )
