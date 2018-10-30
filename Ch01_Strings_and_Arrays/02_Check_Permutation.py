import time
from collections import Counter


def check_permutation_one(str_a, str_b):
    dict = {}

    if len(str_a) != len(str_b):
        return False

    for char in str_a:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    for char in str_b:
        if char not in dict:
            return False
        else:
            dict[char] -= 1

        if dict[char] == 0:
            return False

    return True


# From CtCI GitHub
def check_permutation_two(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True


# From the book
def check_permutation_three(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


if __name__ == '__main__':
    start = time.time()

    sample_one_a = "asdfghjkl"
    sample_one_b = "lkjhgfdsa"

    sample_two_a = "qwertyujip"
    sample_two_b = "poiuytrewq"

    sample_three_a = "zxcvbn"
    sample_three_b = "zxcvbnm"

    print(check_permutation_one(sample_one_a, sample_one_b))
    print(check_permutation_one(sample_two_a, sample_two_b))
    print(check_permutation_one(sample_three_a, sample_three_b))

    print(check_permutation_two(sample_one_a, sample_one_b))
    print(check_permutation_two(sample_two_a, sample_two_b))
    print(check_permutation_two(sample_three_a, sample_three_b))

    print(check_permutation_three(sample_one_a, sample_one_b))
    print(check_permutation_three(sample_two_a, sample_two_b))
    print(check_permutation_three(sample_three_a, sample_three_b))

    end = time.time()
    print('Elapsed time: {} sec'.format(end - start))
