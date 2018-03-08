import networkx as nx
from numpy import linalg, matmul,transpose
from munkres import Munkres, make_cost_matrix
from math import ceil,floor
import sys
import time
from entity import PaireGraphs


from factory import FactoryNode


def umeyama(liste_paires_graphes):

    # On lance le chrono
    chrono = time.clock()

    # Compteur d'erreur global
    cpt_erreur = 0

    # On stock la taille des graphes
    taille_graphe = liste_paires_graphes[0].premierGraphe.number_of_nodes()

    for paires in liste_paires_graphes :
        # Retourne les matrice d adjacences ( on transforme en array de array )
        adjacency_matrix_un = nx.adjacency_matrix(paires.premierGraphe).toarray()
        adjacency_matrix_deux = nx.adjacency_matrix(paires.secondGraphe).toarray()



        # Recupere les matrices modales issues des matrices d adjacences
        matrice_modale_un = linalg.eig(adjacency_matrix_un)[1]
        matrice_modale_deux = linalg.eig(adjacency_matrix_deux)[1]


        # Pour obtenir les matrices modales il faut utiliser les valeurs absolues dans les matrices
        for array in matrice_modale_un:
            for valeur in range(len(array)):
                array[valeur] = abs(array[valeur])

        for array2 in matrice_modale_deux:
            for valeur2 in range(len(array2)):
                array2[valeur2] = abs(array2[valeur2])

        # On calcule ensuite la matrice de similitude

        matrice_similarite = matmul(matrice_modale_un,transpose(matrice_modale_deux))
        cost_matrix = make_cost_matrix(matrice_similarite)

        # On fait l'algo hongrois ( munkres ) qui retourne des paires de noeuds apparies
        m = Munkres()
        paires_noeuds = m.compute(cost_matrix)

        # On regarde lez correspondances noeuds a noeuds et on compte les erreurs
        for noeuds_associes in paires_noeuds :
            node_1 = paires.premierGraphe.nodes.items()[noeuds_associes[0]][0]
            node_2 = paires.secondGraphe.nodes.items()[noeuds_associes[1]][0]

            # On prend en compte le decalage des 2 graphes dans la comparaison
            if node_1 < (taille_graphe/2):
                if node_1 + (int)(taille_graphe/2) != node_2:
                    cpt_erreur += 1

            else:
                if node_1 - (int)(taille_graphe/2) != node_2:
                    cpt_erreur += 1

    taux_erreur = float((cpt_erreur*100) / (taille_graphe*len(liste_paires_graphes)))

    print "Taux d erreur = %f\n"%taux_erreur
    print "Temps execution = %f\n"%(time.clock()-chrono)


