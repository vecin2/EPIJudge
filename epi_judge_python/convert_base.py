from test_framework import generic_test


def convert_to_int(num_as_string, base):
    result = 0

    for i in range(len(num_as_string)):
        exp = len(num_as_string) - 1 - i
        result += pow(base, exp) * int(num_as_string[i])

    return result


def convert_to_base(int_value, base):
    result = []

    while True:
        result.append(str(int_value % base))
        int_value //= 2
        print(result)

        if int_value == 0:
            break
    result.reverse()

    return "".join(result)


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    int_value = convert_to_int(num_as_string, b1)
    print(int_value)

    return convert_to_base(int_value, b2)


if __name__ == "__main__":
    # print(convert_base("12", 10, 2))
    exit(
        generic_test.generic_test_main(
            "convert_base.py", "convert_base.tsv", convert_base
        )
    )
