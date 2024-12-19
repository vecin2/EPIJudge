from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x==0:
        return "0"

    sign = -1 if x< 0 else 1
    x *= sign
    chars = []
    while x > 0:
        chars.append(chr(x%10 + ord('0')))
        x //= 10

    result ="" if sign ==1 else "-"
    return result +  "".join(reversed(chars))

def string_to_int(s: str) -> int:
    result = 0
    start = 1 if s[0] in "+-" else 0
    for char in s[start:]:
        result = result * 10 + (ord(char) - ord('0'))

    return result* (1 if s[0] != "-" else -1)


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
