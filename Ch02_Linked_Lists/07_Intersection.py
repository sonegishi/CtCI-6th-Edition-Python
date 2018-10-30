from LinkedList import LinkedList


def intersection_one(sll_a, sll_b):
    ref_list = list()
    curr_a = sll_a.head
    curr_b = sll_b.head

    while curr_a:
        ref_list.append(curr_a.next)
        curr_a = curr_a.next

    while curr_b:
        if curr_b.next in ref_list:
            return curr_b.next

        curr_b = curr_b.next

    return -1


# From CtCI GitHub
def intersection_two(list1, list2):
    if list1.tail is not list2.tail:
        return False

    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) < len(list2) else list1

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for i in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


if __name__ == '__main__':
    pass
