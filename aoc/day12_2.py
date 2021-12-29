from typing import MutableMapping, List, Set

from aoc.day12_1 import Node, build_graph


def traverse_next(next_node: Node, chain: List[Node], results: Set[str], small_limit=False) -> None:
    if next_node.name == "start" and next_node.visited == 1:
        return
    if next_node.small and next_node.visited == 2:
        return
    if next_node.small and next_node.visited == 1 and small_limit:
        return
    next_node.visited += 1
    if next_node.small and next_node.visited == 2:
        small_limit = True
    chain.append(next_node)
    if next_node.name != "end":
        for linked_node in next_node.links:
            traverse_next(linked_node, chain, results, small_limit)
    if next_node.name == "end":
        results.add(",".join([node.name for node in chain]))
    next_node.visited -= 1
    chain.pop()


def solve():
    graph = build_graph()
    chain = []
    results = set()
    traverse_next(graph["start"], chain, results)
    return results


if __name__ == "__main__":
    print(len(solve()))
