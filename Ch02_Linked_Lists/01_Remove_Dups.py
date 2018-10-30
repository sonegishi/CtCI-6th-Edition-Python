import unittest
from LinkedList import LinkedList


def remove_dups_one(ull):
    if ull.head is None:
        return

    curr = ull.head
    char_dict = dict()
    char_dict[curr.value] = True

    while curr.next:
        if curr.next.value in char_dict:
            curr.next = curr.next.next
        else:
            char_dict[curr.next.value] = True
            curr = curr.next

    return ull


# From CtCI GitHub
def remove_dups_two(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return ll

# From CtCI GitHub
def remove_dups_followup(ll):
    if ll.head is None:
        return

    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return ll.head


# class Test(unittest.TestCase):
#     # Test Cases
#     data = [
#         ('erbottlewat', True),
#         ('bar', False),
#         ('foofoo', False)
#     ]
#
#     def test_string_rotation_one(self):
#         for [ll, expected] in self.data:
#             actual = remove_dups_one(ll)
#             self.assertEqual(actual, expected)


if __name__ == '__main__':
    # unittest.main()

    ll = LinkedList()
    ll.generate(100, 0, 9)
    print(ll)
    remove_dups_one(ll)
    print(ll)
    remove_dups_two(ll)
    print(ll)

    ll.generate(100, 0, 9)
    print(ll)
    remove_dups_followup(ll)
    print(ll)
