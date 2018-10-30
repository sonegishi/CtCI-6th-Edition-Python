from LinkedList import LinkedList


def kth_to_last_one(sll, k):
    index = 0
    curr = sll.head

    while index < k:
        curr = curr.next
        index += 1

    sll.head = curr

    return sll


# From CtCI GitHub
def kth_to_last_two(ll, k):
    runner = current = ll.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current


if __name__ == '__main__':
    ll = LinkedList()
    ll.generate(10, 0, 99)
    print(ll)
    print(kth_to_last_one(ll, 3))
    print(kth_to_last_two(ll, 3))
