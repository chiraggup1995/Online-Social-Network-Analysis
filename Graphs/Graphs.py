# Creating Random Graph
%matplotlib inline
from itertools import combinations
import matplotlib.pyplot as plt
import networkx as nx
import random

'''Creating a random graph which and Calulcating the Degree Distribution and Clustering Coefficient to check, whether
Random Graph is similar to Realistic Model of Actual Network'''


def random_graphs(n, p, seed=123):
    G = nx.Graph()
    random.seed(seed)
    G.add_nodes_from(range(n))
    for edge in combinations(range(n), 2):
        if(random.random() < p):
            G.add_edge(edge[0], edge[1])
    print('Create Random Graph from p=%g N=%d E=%d' % (p, len(G.nodes()), len(G.edges())))
    return G

# Now, lets find the Graph Density


def total_edge(N):
    return N * (N - 1) / 2


G = random_graphs(20, 0.5)
nx.draw(G)
print("Graph Density: %.3f" % (1. * len(G.edges()) / (total_edge(len(G.nodes())))))
