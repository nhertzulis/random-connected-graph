# Copyright (C) 2013 Brian Wesley Baugh
# CSCE 6933: Social Network Analysis
# Created: January 22, 2013
# Updated: January, 28, 2013
"""Generate a randomly connected graph with N nodes and E edges."""
import random
import argparse
from pprint import pprint


class Graph(object):
    def __init__(self, nodes, edges=[], digraph=False):
        self.nodes = nodes
        self.edges = edges
        self.digraph = digraph

    def sort_edges(self):
        """If undirected, sort order that the nodes are listed in the edge."""
        if not self.digraph:
            self.edges = [((t, s) if t < s else (s, t)) for s, t in self.edges]
        self.edges.sort()

    def generate_gml(self):
        # Inspiration:
        # http://networkx.lanl.gov/_modules/networkx/readwrite/gml.html#generate_gml
        indent = ' ' * 4

        yield 'graph ['
        if self.digraph:
            yield indent + 'directed 1'

        # Write nodes
        for index, node in enumerate(self.nodes):
            yield indent + 'node ['
            yield indent * 2 + 'id {}'.format(index)
            yield indent * 2 + 'label "{}"'.format(str(node))
            yield indent + ']'

        # Write edges
        for source, target in self.edges:
            yield indent + 'edge ['
            yield indent * 2 + 'source {}'.format(self.nodes.index(source))
            yield indent * 2 + 'target {}'.format(self.nodes.index(target))
            yield indent + ']'

        yield ']'

    def write_gml(self, fname):
        with open(fname, mode='w') as f:
            for line in self.generate_gml():
                line += '\n'
                f.write(line.encode('latin-1'))


def check_num_edges(nodes, num_edges, loops, multigraph, digraph):
    """Checks that the number of requested edges is acceptable."""
    num_nodes = len(nodes)
    # Check min edges
    min_edges = num_nodes - 1
    if num_edges < min_edges:
        raise ValueError('num_edges less than minimum (%i)' % min_edges)
    # Check max edges
    max_edges = num_nodes * (num_nodes - 1)
    if not digraph:
        max_edges /= 2
    if loops:
        max_edges += num_nodes
    if not multigraph and num_edges > max_edges:
            raise ValueError('num_edges greater than maximum (%i)' % max_edges)


def naive(nodes, num_edges, loops=False, multigraph=False, digraph=False):
    # Idea:
    # Each node starts off in its own component.
    # Keep track of the components, combining them when an edge merges two.
    # While there are less edges than requested:
    #     Randomly select two nodes, and create an edge between them.
    # If there is more than one component remaining, repeat the process.

    check_num_edges(nodes, num_edges, loops, multigraph, digraph)

    edges, edge_set = [], set()

    if loops:
        # With replacement.
        random_edge = lambda: (random.choice(nodes), random.choice(nodes))
    else:
        # Without replacement.
        random_edge = lambda: tuple(random.sample(nodes, 2))

    while True:
        # Start with each node in its own component.
        components = [set([x]) for x in nodes]
        while len(edges) < num_edges:
            # Generate a random edge.
            edge = random_edge()
            # Update the component list.
            comp_index = [None] * 2
            for index, comp in enumerate(components):
                for i in (0, 1):
                    if edge[i] in comp:
                        comp_index[i] = index
                # Break early once we have found both sets.
                if all(x is not None for x in comp_index):
                    break
            assert all(x is not None for x in comp_index)
            # Combine components if the nodes aren't already in the same one.
            if comp_index[0] != comp_index[1]:
                components[comp_index[0]] |= components[comp_index[1]]
                del components[comp_index[1]]
            # Add the edge if the graph type allows it.
            if multigraph or edge not in edge_set:
                edges.append(edge)
                edge_set.add(edge)
                if not digraph:
                    edge_set.add(edge[::-1])  # add other direction to set.
        if len(components) == 1:
            break
        else:
            edges[:], edge_set = [], set()

    return Graph(nodes, edges, digraph)


def better(nodes, num_edges, loops=False, multigraph=False, digraph=False):
    # Algorithm inspiration:
    # http://stackoverflow.com/questions/2041517/random-simple-connected-graph-generation-with-given-sparseness

    # Idea:
    # Create a random connected graph.
    # Add random edges until the number of desired edges is reached.

    check_num_edges(nodes, num_edges, loops, multigraph, digraph)

    edges, edge_set = [], set()

    # Create two partitions, S and T. Initially store all nodes in S.
    S, T = set(nodes), set()

    # Randomly select a first node, and place it in T.
    node_s = random.sample(S, 1).pop()
    S.remove(node_s)
    T.add(node_s)

    # Create a random connected graph.
    while S:
        # Select random node from S, and another in T.
        node_s, node_t = random.sample(S, 1).pop(), random.sample(T, 1).pop()
        # Create an edge between the nodes, and move the node from S to T.
        edge = (node_s, node_t)
        S.remove(node_s)
        T.add(node_s)
        # Add the edge if the graph type allows it.
        if multigraph or edge not in edge_set:
            edges.append(edge)
            edge_set.add(edge)
            if not digraph:
                edge_set.add(edge[::-1])  # add other direction to set.

    # Add random edges until the number of desired edges is reached.
    while len(edges) < num_edges:
        # Randomly select two nodes (in T, which is all), and create an edge.
        if loops:
            # With replacement.
            edge = random.choice(nodes), random.choice(nodes)
        else:
            # Without replacement.
            edge = tuple(random.sample(nodes, 2))
        # Add the edge if the graph type allows it.
        if multigraph or edge not in edge_set:
            edges.append(edge)
            edge_set.add(edge)
            if not digraph:
                edge_set.add(edge[::-1])  # add other direction to set.

    return Graph(nodes, edges, digraph)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('nodes',
                        help='filename containing node labels (one per line) '
                             'OR integer number of nodes to generate')
    parser.add_argument('-e', '--edges', type=int,
                        help='number of edges (default is minimum possible)')
    parser.add_argument('-l', '--loops', action='store_true',
                        help="allow self-loop edges")
    parser.add_argument('-m', '--multigraph', action='store_true',
                        help="allow parallel edges between nodes")
    parser.add_argument('-d', '--digraph', action='store_true',
                        help="make edges unidirectional")
    parser.add_argument('-n', '--naive', action='store_true',
                        help="use a naive generation algorithm (slower)")
    parser.add_argument('-p', '--pretty', action='store_true',
                        help="print large graphs with each edge on a new line")
    parser.add_argument('-g', '--gml',
                        help="filename to save the graph to in GML format")
    args = parser.parse_args()

    # Nodes
    try:
        nodes = []
        with open(args.nodes) as f:
            for line in f:
                nodes.append(line.strip())
    except IOError:
        try:
            nodes = [x for x in xrange(int(args.nodes))]
        except ValueError:
            raise TypeError('nodes argument must be a filename or an integer')

    # Edges
    if args.edges is None:
        num_edges = len(nodes) - 1
    else:
        num_edges = args.edges

    # Approach
    if args.naive:
        approach = naive
    else:
        approach = better

    # Run
    graph = approach(nodes, num_edges, args.loops, args.multigraph,
                     args.digraph)

    # Display
    graph.sort_edges()
    if args.pretty:
        pprint(graph.edges)
    else:
        print(graph.edges)

    # Save to GML
    if args.gml:
        graph.write_gml(args.gml)
