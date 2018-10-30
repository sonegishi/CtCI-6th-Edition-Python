import time
import unittest


# O(N)
def palindrome_permutation_one(str):
    odds = False
    dict = {}

    for char in str.lower():
        if char == ' ':
            pass
        elif char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    for _, val in dict.items():
        if val % 2 == 1:
            if odds:
                return False
            else:
                odds = True

    return True


# From CtCI GitHub
def palindrome_permutation_two(phrase):
    '''function checks if a string is a permutation of a palindrome or not'''
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    countodd = 0
    for c in phrase:
        x = char_number(c)
        if x != -1:
            table[x] += 1
            if table[x] % 2:
                countodd += 1
            else:
                countodd -= 1

    return countodd <= 1


# From CtCI GitHub
def char_number(c):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    Z = ord('Z')
    val = ord(c)

    if a <= val <= z:
        return val - a
    elif A <= val <= Z:
        return val - A
    return -1


class Test(unittest.TestCase):
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)
    ]

    def test_palindrome_permutation_one(self):
        for [test_string, expected] in self.data:
            actual = palindrome_permutation_one(test_string)
            self.assertEqual(actual, expected)

    def test_palindrome_permutation_two(self):
        for [test_string, expected] in self.data:
            actual = palindrome_permutation_two(test_string)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    start = time.time()

    unittest.main()

    end = time.time()
    print('Elapsed time: {} sec'.format(end - start))
