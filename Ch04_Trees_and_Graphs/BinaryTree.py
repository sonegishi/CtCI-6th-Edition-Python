import random


class BinaryTree:

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

        def __str__(self):
            return 'Node(data={}, left={}, right={})'.format(self.data, self.left, self.right)

    def __init__(self, type='normal', samples=10):
        self.root = None

        random_nums = random.sample(range(1000), samples)
        if type == 'normal':
            self.root = self.create_tree(random_nums)
        elif type == 'bst':
            self.root = self.create_tree(sorted(random_nums))

    def __str__(self):
        return str(self.root)

    def create_tree(self, arr):
        if len(arr) == 0:
            return
        mid = len(arr) // 2
        node = BinaryTree.Node(arr[mid])

        node.left = self.create_tree(arr[0:mid])
        node.right = self.create_tree(arr[mid + 1:])
        return node

    def in_order_traversal(self, root='root'):
        nodes = list()
        if root == 'root':
            root = self.root
        if root:
            nodes = self.in_order_traversal(root.left)
            nodes.append(root.data)
            nodes += self.in_order_traversal(root.right)
        return nodes

    def pre_order_traversal(self, root='root'):
        nodes = list()

        if root == 'root':
            root = self.root
        if root:
            nodes.append(root.data)
            nodes += self.pre_order_traversal(root.left)
            nodes += self.pre_order_traversal(root.right)
        return nodes

    def post_order_traversal(self, root='root'):
        nodes = list()

        if root == 'root':
            root = self.root
        if root:
            nodes = self.post_order_traversal(root.left)
            nodes += self.post_order_traversal(root.right)
            nodes.append(root.data)
        return nodes

    def get_depth(self, root='root'):
        if root == 'root':
            root = self.root
        if root is None:
            return -1
        else:
            return 1 + max(self.get_depth(root.left), self.get_depth(root.right))


if __name__ == '__main__':
    tree = BinaryTree(type='bst', samples=10)

    print('In-Order Traversal:')
    print('{}\n'.format(tree.in_order_traversal()))

    print('Pre-Order Traversal:')
    print('{}\n'.format(tree.pre_order_traversal()))

    print('Post-Order Traversal:')
    print('{}\n'.format(tree.post_order_traversal()))

    print('Depth of the tree:')
    print('{}\n'.format(tree.get_depth()))
