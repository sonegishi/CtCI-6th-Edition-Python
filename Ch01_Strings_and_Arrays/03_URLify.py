import time
import unittest


# TODO
def urlify_one(str, size):
    out_str = []

    for key in range(size):
        if str[key] == '':
            out_str += list('%20')
        else:
            out_str += [str[key]]

    return out_str


# From CtCI GitHub
def urlify_two(str, size):
    # function replaces single spaces with %20 and removes trailing spaces
    new_index = len(str)

    for i in reversed(range(size)):
        if str[i] == ' ':
            # Replace spaces
            str[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            str[new_index - 1] = str[i]
            new_index -= 1

    return str


class Test(unittest.TestCase):
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22, list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))
    ]

    # def test_urlify_one(self):
    #     for [test_string, length, expected] in self.data:
    #         actual = urlify_one(test_string, length)
    #         self.assertEqual(actual, expected)

    def test_urlify_two(self):
        for [test_string, length, expected] in self.data:
            actual = urlify_two(test_string, length)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    start = time.time()

    unittest.main()

    end = time.time()
    print('Elapsed time: {} sec'.format(end - start))
