from typing import Iterable

from aoc import cache


class Node:
    def __init__(self, name: str):
        self.name = name
        self.links = set()


def link_nodes(node_a: Node, node_b: Node) -> None:
    node_a.links.add(node_b)
    node_b.links.add(node_a)


def build_graph():
    nodes_by_name = {}
    for line in cache.input_for_day(12).lines():
        node_names = line.split('-')
        nodes = []
        for node_name in node_names:
            node = nodes_by_name.get(node_name)
            if node is None:
                node = Node(node_name)
                nodes_by_name[node_name] = node
            nodes.append(node)
        link_nodes(*nodes)
    return nodes_by_name


def solve():
    nodes_by_name = build_graph()
    results = []
    queue = [["start"]]
    while len(queue):
        chain = queue.pop(0)
        latest_node_name = chain[-1]
        if latest_node_name == "end":
            results.append(",".join(chain))
            continue
        latest_node = nodes_by_name[latest_node_name]
        for link in latest_node.links:
            if link.name.islower() and link.name in chain:
                continue
            queue.append(list(chain) + [link.name])
    return results


if __name__ == "__main__":
    print(len(solve()))
