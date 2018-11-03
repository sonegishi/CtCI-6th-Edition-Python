from BinaryTree import BinaryTree


def is_balanced(tree, root):
    if root is None:
        return True

    height_diff = tree.get_depth(root.left) - tree.get_depth(root.right)
    if abs(height_diff) > 1:
        return False
    else:
        return is_balanced(tree, root.left) and is_balanced(tree, root.right)


if __name__ == '__main__':
    bt = BinaryTree(samples=15)
    print(bt)

    print(is_balanced(bt, bt.root))
