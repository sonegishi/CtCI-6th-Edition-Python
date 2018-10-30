import time


def is_unique(string):
    char_dict = {}

    for char in string:
        if char in char_dict:
            return False
        char_dict[char] = True
    return True


def is_unique_two(string):
    str_list = sorted(list(string))

    for key in range(len(str_list)-1):
        if str_list[key] == str_list[key+1]:
            return False
    return True


# From CtCI GitHub
def is_unique_three(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True

    return True


# TODO
# From the book
def is_unique_four(string):
    checker = 0
    for i in range(len(string)):
        val = ord(string[i]) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True


if __name__ == '__main__':
    start = time.time()

    sample_one = 'gfedc=ba'
    sample_two = '=gfed=dcba='

    # print(is_unique(sample_one))
    # print(is_unique(sample_two))
    #
    # print(is_unique_two(sample_one))
    # print(is_unique_two(sample_two))
    #
    # print(is_unique_three(sample_one))
    # print(is_unique_three(sample_two))

    print(is_unique_four(sample_one))
    print(is_unique_four(sample_two))

    end = time.time()
    print('Elapsed time: {} sec'.format(end - start))
