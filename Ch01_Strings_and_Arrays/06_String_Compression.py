import unittest


def string_compression_one(string):
    counter = 0
    out_str = ''

    for key in range(len(string) - 1):
        if string[key] == string[key+1]:
            counter += 1
        else:
            counter += 1
            out_str += string[key]
            out_str += str(counter)
            counter = 0

    counter += 1
    out_str += string[-1]
    out_str += str(counter)

    return min(string, out_str, key=len)


# From CtCI GitHub
def string_compression_two(string):
    compressed = []
    counter = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, ''.join(compressed), key=len)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression_one(self):
        for [test_string, expected] in self.data:
            actual = string_compression_one(test_string)
            self.assertEqual(actual, expected)

    def test_string_compression_two(self):
        for [test_string, expected] in self.data:
            actual = string_compression_two(test_string)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
