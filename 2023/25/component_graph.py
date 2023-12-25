# %%
from pathlib import Path
from collections import namedtuple
import sys

sys.setrecursionlimit(100000)

Coord = namedtuple("Coord", ["x", "y"])
from copy import copy

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class ComponentGraph():
    
    def __init__(self, puzzle_input: "list[str]"):
        
        self.component_graph = {}
        for component in puzzle_input:
            node, connections = component.split(": ")
            self.component_graph[node] = [connection for connection in connections.split()]
        
        self.component_graph = nx.from_dict_of_lists(self.component_graph)

        
    def draw_graph(self, graph):
        nx.draw(graph)
        plt.show()
        
    def split_product(self):
        product = 1
        cut_value, partitions = nx.connectivity.stoer_wagner(self.component_graph)
        if cut_value == 3:
            for partition in partitions:
                    product *= len(partition)
            return product
    
    def nodes(self, graph):
        nodes = set()
        for node, edges in graph.items():
            nodes.add(node)
            for edge in edges:
                nodes.add(edge)
        return nodes
        
# %%
if __name__ == "__main__":
    puzzle_input_path = Path("puzzle_input.txt")
    with open(puzzle_input_path) as puzzle_input_file:

        puzzle_input = puzzle_input_file.read().splitlines()
        component_graph = ComponentGraph(puzzle_input)
        print(f"Solutions to first problem: {component_graph.split_product()}")
        # hail_storm = ComponentGraph(puzzle_input)
        # print(f"Solution to second problem: {self.component_graph}")