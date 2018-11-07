import random

# Time complexity  : O(n^2)
# Space complexity : O(1)


def selection_sort(arr):
    arr_len = len(arr)

    for i in range(arr_len):
        min_val, min_key = min(arr[i:]), arr.index(min(arr[i:]))
        if min_key != i:
            arr[i], arr[min_key] = arr[min_key], arr[i]
    return arr


if __name__ == '__main__':
    test_arr = random.sample(range(10), 10)
    print('before: ', test_arr)
    print('after:  ', selection_sort(test_arr))
