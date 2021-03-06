from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


def _update_distance(v, v_neighbor, 
                     w_graph_d, distance_d, previous_d):
    """Update distance with previous node."""
    if (distance_d[v_neighbor] > 
            distance_d[v] + w_graph_d[v][v_neighbor]):
        distance_d[v_neighbor] = (
            distance_d[v] + w_graph_d[v][v_neighbor])
        previous_d[v_neighbor] = v
    return distance_d, previous_d 


def _check_negative_cycle(distance_d, previous_d, w_graph_d):
    """Check negative cycle.

    Update distance once more and check if any diff.
    """
    _distance_d = distance_d.copy()
    _previous_d = previous_d.copy()

    for v in w_graph_d.keys():
        for v_neighbor in w_graph_d[v].keys():
            _distance_d, _previous_d = _update_distance(
                v, v_neighbor, w_graph_d, _distance_d, _previous_d)
            if _distance_d != distance_d:
                raise ValueError('Negative cycle exists.')


def bellman_ford(w_graph_d, start_vertex):
    """Bellman-Ford algorithm for single-source shortest path problem
    in "weighted negative" graph, G(V, E).

    Time complexity: O(|V|*|E|).
    Space complexity: O(|V|).
    """
    distance_d = {v: np.inf for v in w_graph_d.keys()}
    previous_d = {v: None for v in w_graph_d.keys()}

    distance_d[start_vertex] = 0

    # Run through |V| - 1 times, in each iteration update all edges's distances.
    n = len(w_graph_d.keys())
    for i in xrange(1, n):
        for v in w_graph_d.keys():
            for v_neighbor in w_graph_d[v].keys():
                distance_d, previous_d = _update_distance(
                    v, v_neighbor, w_graph_d, distance_d, previous_d)
    
    # Check negative cycle.
    _check_negative_cycle(distance_d, previous_d, w_graph_d)

    return distance_d, previous_d


def main():
    w_graph_d = {
        's': {'a': 2, 'b': 6},
        'a': {'b': 3, 'c': 1},
        # 'b': {'a': -5, 'd': 2}, # With negative cycle.
        'b': {'a': -2, 'd': 2},
        'c': {'b': 1, 'e': 4, 'f': 2},
        'd': {'c': 3, 'f': 2},
        'e': {},
        'f': {'e': 1}
    }
    start_vertex = 's'

    distance_d, previous_d = bellman_ford(w_graph_d, start_vertex)
    print('distance_d: {}'.format(distance_d))
    print('previous_d: {}'.format(previous_d))


if __name__ == '__main__':
    main()
