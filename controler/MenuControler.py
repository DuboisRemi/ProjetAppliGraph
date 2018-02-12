import networkx as nx
from numpy import linalg


def umeyama(listPairesGraphs):

    for paires in listPairesGraphs :
        # Retourne les matrice d adjacences ( on transforme en array de array )
        adjacency_matrix_un = nx.adjacency_matrix(paires.premierGraphe).toarray()
        adjacency_matrix_deux = nx.adjacency_matrix(paires.secondGraphe).toarray()

        # Recupere les vecteurs propres des matrices d adjacences
        vecteurs_propres_un = linalg.eig(adjacency_matrix_un)[1]
        vecteurs_propres_deux = linalg.eig(adjacency_matrix_deux)[1]


