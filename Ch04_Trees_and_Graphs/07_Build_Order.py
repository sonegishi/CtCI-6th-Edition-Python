from BTNode import BTNode

# TODO


def minimal_tree(arr):
    if len(arr) == 0:
        return

    mid = len(arr) // 2
    node = BTNode(arr[mid])
    small_arr = arr[0:mid]
    big_arr = arr[mid+1:]

    node.left = minimal_tree(small_arr)
    node.right = minimal_tree(big_arr)

    return node


def build_order(nodes, links):
    dep_dict = {node: list() for node in nodes}
    for (source, target) in links:
        dep_dict[target].append(source)
    print(dep_dict)

    order_list = list()
    for key, val in dep_dict.items():
        print('current key: ', key)
        if key not in order_list:
            order_list = build_order_helper(key, order_list, dep_dict)
            if key not in order_list:
                order_list.append(key)
        print('current order: ', order_list)

    return order_list


def build_order_helper(key, order_list, dep_dict):
    val_list = dep_dict[key]
    print(val_list)
    if len(val_list) == 0:
        if key not in order_list:
            order_list.append(key)
    else:
        first_element = val_list[0]
        order_list = build_order_helper(first_element, order_list, dep_dict)

    return order_list


if __name__ == '__main__':
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

    print(build_order(projects, dependencies))
