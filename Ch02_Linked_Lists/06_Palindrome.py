from LinkedList import LinkedList


def is_palindrome(ll):
    val_dict = dict()
    curr = ll.head

    while curr:
        if curr.value not in val_dict:
            val_dict[curr.value] = 1
        else:
            val_dict[curr.value] += 1
        curr = curr.next

    odds = False
    for key, val in val_dict.items():
        if val % 2 == 1:
            if odds:
                return False
            else:
                odds = True

    return True


# From CtCI GitHub
def is_palindrome_two(ll):
    fast = slow = ll.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()

        if top != slow.value:
            return False

        slow = slow.next

    return True


if __name__ == '__main__':
    ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
    print(is_palindrome(ll_true))
    ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(is_palindrome(ll_false))