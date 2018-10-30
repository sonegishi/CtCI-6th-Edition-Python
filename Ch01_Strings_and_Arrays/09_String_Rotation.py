import unittest
import numpy as np


def string_rotation_one(s1, s2):
    if len(s1) != len(s2):
        return False

    index_s2 = [key for key, char in enumerate(s2) if char == s1[0]]

    if len(index_s2) == 0:
        return False

    for key in index_s2:
        if is_rotate(s1, s2, key):
            return True

    return False


def is_rotate(s1, s2, s2_key):
    for char in s1:
        if s2_key >= len(s2):
            s2_key = 0

        if char != s2[s2_key]:
            return False

        s2_key += 1

    return True


# From CtCI GitHub
def is_substring(string, sub):
    return string.find(sub) != -1


def string_rotation_two(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1 + s1, s2)
    return False


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation_one(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation_one(s1, s2)
            self.assertEqual(actual, expected)

    def test_string_rotation_two(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation_two(s1, s2)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
