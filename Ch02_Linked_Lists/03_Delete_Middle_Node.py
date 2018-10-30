from LinkedList import LinkedList


def delete_middle_node_one(sll):
    if len(sll) < 3:
        return

    index = 0
    mid = int(len(sll) / 2)

    curr = sll.head
    prev = None
    while curr.next:
        if index == (mid - 1):
            prev = curr
        elif index == mid:
            prev.next = curr.next
            curr = prev

        curr = curr.next
        index += 1

    return sll


if __name__ == '__main__':
    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4, 5, 6, 7, 8, 9])

    print(ll)
    print(delete_middle_node_one(ll))
