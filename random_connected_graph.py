# Copyright (C) 2013 Brian Wesley Baugh
# CSCE 6933: Social Network Analysis
# Created: January 22, 2013
"""Generate a randomly connected graph with N nodes and E edges."""
import random
import argparse
from pprint import pprint


def check_num_edges(num_nodes, num_edges, loops, multigraph, digraph):
    """Checks that the number of requested edges is acceptable."""
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


def naive(num_nodes, num_edges, loops=False, multigraph=False, digraph=False):
    check_num_edges(num_nodes, num_edges, loops, multigraph, digraph)

    nodes = [x for x in xrange(num_nodes)]
    edges, edge_set = [], set()
    graph = (nodes, edges)

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
            # Add the edge if the graph type allows it
            if multigraph or edge not in edge_set:
                edges.append(edge)
                edge_set.add(edge)
                if not digraph:
                    edge_set.add(edge[::-1])  # add other direction to set
        if len(components) == 1:
            break
        else:
            edges[:], edge_set = [], set()

    return graph


def better(num_nodes, num_edges, loops=False, multigraph=False, digraph=False):
    # Algorithm reference:
    # http://stackoverflow.com/questions/2041517/random-simple-connected-graph-generation-with-given-sparseness
    raise NotImplementedError


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('nodes', type=int,
                        help='number of nodes OR filename containing node '
                             'labels')
    parser.add_argument('edges', type=int,
                        help='number of edges')
    parser.add_argument('-l', '--loops', action='store_true',
                        help="allow self-loop edges")
    parser.add_argument('-m', '--multigraph', action='store_true',
                        help="allow parallel edges between nodes")
    parser.add_argument('-d', '--digraph', action='store_true',
                        help="make edges unidirectional")
    parser.add_argument('-n', '--naive', action='store_false',
                        help="DON'T use a naive generation algorithm (slower)")
    args = parser.parse_args()

    if args.naive:
        approach = naive
    else:
        approach = better
    nodes, edges = approach(args.nodes, args.edges, args.loops, args.multigraph,
                            args.digraph)
    pprint(sorted(edges))
