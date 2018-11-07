import random

# Time complexity  : O(n^2)
# Space complexity : O(1)


def bubble_sort(arr):
    arr_len = len(arr)

    for i in range(arr_len):
        for j in range(arr_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == '__main__':
    test_arr = random.sample(range(10), 10)
    print('before: ', test_arr)
    print('after:  ', bubble_sort(test_arr))
