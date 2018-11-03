from BinaryTree import BinaryTree


def depth_of_list(lists_dict, root, level=0):
    if root is None:
        return

    if level in lists_dict:
        lists_dict[level].append(root.data)
    else:
        lists_dict[level] = [root.data]

    level += 1
    depth_of_list(lists_dict, root.left, level)
    depth_of_list(lists_dict, root.right, level)

    return lists_dict


if __name__ == '__main__':
    bt = BinaryTree(samples=15)
    print(bt)

    out_dict = dict()
    print(depth_of_list(out_dict, bt.root))
