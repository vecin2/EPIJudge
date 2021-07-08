import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    start_index, end_index = 0, len(s) - 1

    while start_index < end_index:
        s[start_index], s[end_index] = s[end_index], s[start_index]
        start_index += 1
        end_index -= 1

    start_index = 0

    while start_index < len(s):
        word_index = start_index

        while word_index < len(s) and s[word_index] != " ":
            word_index += 1

        endword_index = word_index - 1

        while start_index < endword_index:
            s[start_index], s[endword_index] = s[endword_index], s[start_index]
            start_index += 1
            endword_index -= 1

        start_index = word_index + 1

    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return "".join(s_copy)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_words.py", "reverse_words.tsv", reverse_words_wrapper
        )
    )
