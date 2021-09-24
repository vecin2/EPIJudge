def is_permutation(word1, word2):
    freqs = []

    if len(word1) != len(word2):
        return False

    for char in word1:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1

    print(freqs)

    return True


word1 = "aaa"
word2 = "bbb"

if is_permutation(word1, word2):
    print(f"'{word1}' and '{word2}' are permutations")
else:
    print(f"'{word1}' and '{word2}' are NOT permutations")
