from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

from ds_min_priority_queue_tuple import MinPriorityQueue


def dijkstra(w_graph_d, start_vertex):
    """Dijkstra algorithm for singel-source shortest path problem 
    in a "weighted" graph.
    
    Time complexity for graph G(V, W): (|V|+|E|)log(|V|).
    """
    min_pq = MinPriorityQueue()

    distance_d = {v: np.inf for v in w_graph_d.keys()}
    visited_d = {v: False for v in w_graph_d.keys()}
    previous_d = {v: None for v in w_graph_d.keys()}
    
    min_pq.insert([0, start_vertex])
    distance_d[start_vertex] = 0
    visited_d[start_vertex] = True

    while min_pq.heap_size > 0:
        k, v = min_pq.extract_min()
        visited_d[v] = True

        for v_neighbor in w_graph_d[v].keys():
            if (not visited_d[v_neighbor] and 
                distance_d[v_neighbor] > 
                    distance_d[v] + w_graph_d[v][v_neighbor]):
                distance_d[v_neighbor] = distance_d[v] + w_graph_d[v][v_neighbor]
                previous_d[v_neighbor] = v
                min_pq.insert([distance_d[v_neighbor], v_neighbor])

    return distance_d, previous_d, visited_d


def main():
    w_graph_d = {
        's': {'a': 2, 'b': 6},
        'a': {'b': 3, 'c': 1},
        'b': {'a': 5, 'd': 2},
        'c': {'b': 1, 'e': 4, 'f': 2},
        'd': {'c': 3, 'f': 2},
        'e': {},
        'f': {'e': 1}
    }
    start_vertex = 's'
    print('w_graph_d:\n{}'.format(w_graph_d))
    print('Dijkstra shortest path from {}:'.format(start_vertex))
    
    distance_d, previous_d, visited_d = (
        dijkstra(w_graph_d, start_vertex))

    print('distance_d: {}'.format(distance_d))
    print('previous_d: {}'.format(previous_d))
    print('visited_d: {}'.format(visited_d))
   

if __name__ == '__main__':
    main()
