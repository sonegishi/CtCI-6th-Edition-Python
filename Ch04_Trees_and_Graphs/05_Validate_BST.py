from BinaryTree import BinaryTree


def validate_bst(curr):
    if not curr:
        return True
    elif not curr.left and not curr.right:
        return True

    if curr.left:
        if curr.data < curr.left.data:
            return False

    if curr.right:
        if curr.right.data < curr.data:
            return False

    if curr.left.right:
        if curr.left.right.data > curr.data:
            return False

    return validate_bst(curr.left) and validate_bst(curr.right)


if __name__ == '__main__':
    bt = BinaryTree(samples=15)
    print(bt)
    print(validate_bst(bt.root))

    bst = BinaryTree(type='bst', samples=15)
    print(bst)
    print(validate_bst(bst.root))
