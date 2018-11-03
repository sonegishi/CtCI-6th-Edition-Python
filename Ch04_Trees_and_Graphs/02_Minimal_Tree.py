from BinaryTree import BinaryTree


def minimal_tree(arr):
    if len(arr) == 0:
        return

    mid = len(arr) // 2

    node = BinaryTree.Node(arr[mid])
    small_arr = arr[0:mid]
    big_arr = arr[mid+1:]

    node.left = minimal_tree(small_arr)
    node.right = minimal_tree(big_arr)

    return node


if __name__ == '__main__':
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    bst = minimal_tree(test_arr)
    print(bst)
