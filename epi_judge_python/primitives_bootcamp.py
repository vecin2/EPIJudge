def count_bits(x):
    counter = 0

    while x:
        current = x & 1
        print(f"bit is {current}")
        counter += current
        x >>= 1

    print(f"Return {counter}")

    return counter


count_bits(8)
