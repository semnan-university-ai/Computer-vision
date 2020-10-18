import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra, floyd_warshall


def answer_1(save, size, mu=0, sigma=0.1):
    random = np.random.normal(mu, sigma, size)
    print("Normal distribution random: {}".format(random))
    count, bins, ignored = plt.hist(random, 30, density=True)
    plt.plot(
        bins,
        1 / (sigma * np.sqrt(2 * np.pi)) *
        np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
        linewidth=2,
        color='r'
    )
    if save:
        plt.savefig('./output/answer_1_size_{}.png'.format(size))


def get_graph():
    graph = np.array([
        # A  B  C  D  E
        [0, 5, 1, 4, 10],  # A
        [0, 0, 0, 0, 6],  # B
        [0, 0, 0, 2, 0],  # C
        [0, 0, 0, 0, 5],  # D
        [0, 0, 0, 0, 0],  # E
    ])
    return graph


def answer_3_dijkstra(graph):
    distances, predecessors = dijkstra(csgraph=csr_matrix(graph), directed=True, return_predecessors=True)
    print("Dijkstra Result Path=", get_path(predecessors, 0, 4))


def answer_3_floyd(graph):
    distances, predecessors = floyd_warshall(csgraph=csr_matrix(graph), directed=True, return_predecessors=True)
    print("Floyd Result Path=", get_path(predecessors, 0, 4))


def get_path(Pr, i, j):
    nodes = ['A', 'B', 'C', 'D', 'E']
    path = [nodes[j]]
    k = j
    while Pr[i, k] != -9999:
        path.append(nodes[Pr[i, k]])
        k = Pr[i, k]

    return path[::-1]
