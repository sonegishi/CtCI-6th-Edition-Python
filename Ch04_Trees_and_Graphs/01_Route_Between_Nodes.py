from DirectedGraph import DirectedGraph
from Queue import Queue


def route_between_nodes(graph, source, target):
    graph.unvisited()
    queue = Queue()
    source.visited = True
    queue.enqueue(source)

    while not queue.is_empty():
        r = queue.dequeue()
        for node in r.links:
            if node.visited is False:
                print(node, target)
                if node == target:
                    return True
                node.visited = True
                queue.enqueue(node)
    return False


if __name__ == '__main__':
    g = DirectedGraph()

    a = g.add_node('A')
    b = g.add_node('B')
    c = g.add_node('C')
    d = g.add_node('D')
    e = g.add_node('E')
    f = g.add_node('F')

    a.points_to(b)
    a.points_to(f)

    b.points_to(d)
    b.points_to(e)

    c.points_to(b)

    d.points_to(c)
    d.points_to(e)

    print(route_between_nodes(g, d, b))
