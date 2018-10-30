from LinkedList import LinkedList


def loop_detection_one(cll):
    ref_list = list()
    curr = cll.head

    while curr:
        if curr.next in ref_list:
            return curr.next
        else:
            ref_list.append(curr.next)
        curr = curr.next

    return None


# From CtCI GitHub
def loop_detection_two(ll):
    fast = slow = ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast


if __name__ == '__main__':
    pass
