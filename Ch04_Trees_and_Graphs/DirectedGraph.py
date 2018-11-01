from Queue import Queue


class DirectedGraph:

    class Node:
        def __init__(self, data):
            self.data = data
            self.links = list()
            self.visited = False

        def __str__(self):
            return '{}'.format(self.data)

        def points_to(self, target_node):
            self.links.append(target_node)

    def __init__(self):
        self.nodes = []

    def __repr__(self):
        connections = ''
        for node in self.nodes:
            for link in node.links:
                connections += '{} -> {}\n'.format(node.data, link.data)
        return connections

    def unvisited(self):
        for node in self.nodes:
            node.visited = False

    def add_node(self, data):
        new_node = self.Node(data)
        self.nodes.append(new_node)
        return new_node

    def dfs_search(self, root):
        if not root:
            return
        print(root.data)
        root.visited = True
        for node in root.links:
            if node.visited is False:
                self.dfs_search(node)

    def bfs_search(self, root):
        queue = Queue()
        root.visited = True
        queue.enqueue(root)

        while not queue.is_empty():
            r = queue.dequeue()
            print(r)
            for node in r.links:
                if node.visited is False:
                    node.visited = True
                    queue.enqueue(node)


if __name__ == '__main__':
    g = DirectedGraph()

    a = g.add_node('A')
    b = g.add_node('B')
    c = g.add_node('C')
    d = g.add_node('D')
    e = g.add_node('E')
    f = g.add_node('F')

    a.points_to(b)
    a.points_to(e)
    a.points_to(d)

    b.points_to(e)
    b.points_to(f)

    c.points_to(b)

    e.points_to(f)

    f.points_to(c)

    print(g)

    print('Breadth-First Search:')
    print('{}\n'.format(g.bfs_search(a)))

    g.unvisited()

    print('Depth-First Search:')
    print('{}\n'.format(g.dfs_search(a)))
