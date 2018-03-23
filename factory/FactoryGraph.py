import networkx as nx
import matplotlib.pyplot as plt
from factory import FactoryNode
from entity import PaireGraphs
import random

#Fonction qui creer des aretes aleatoire entre les points des graphes
def CreerAretes(graphe_1, graphe_2):
    # On stock la taille des graphes
    taille_graphe = graphe_1.number_of_nodes()


    # On commence par relier chaque noeud a un autre aleatoirement pour eviter les noeuds isoles
    for noeud in list(graphe_1.nodes):
        noeudCouple = random.randint(0, taille_graphe - 1 )

        poids = random.randint(1,10)

        # On ecrase le noeud couple si c est le noeud traite
        while noeudCouple == noeud:
            noeudCouple = random.randint(0, taille_graphe - 1)

        graphe_1.add_edge(noeud, noeudCouple, weight=poids)

        # On decale sur le deuxieme graphe
        noeud_2 = noeud + (int)(taille_graphe/2)
        if noeud_2 > (taille_graphe - 1):
            noeud_2 -= taille_graphe
        noeudCouple_2 = noeudCouple + (int)(taille_graphe/2)
        if noeudCouple_2 > (taille_graphe - 1):
            noeudCouple_2 -= taille_graphe
        graphe_2.add_edge(noeud_2, noeudCouple_2, weight=poids)

    # On choisi aleatoirement le nombre d arete du graphe
    nbEdge = random.randint(1, (taille_graphe - 1)*(taille_graphe - 1))
    cpt = 0
    while cpt < nbEdge:
        noeud_1 = random.randint(0, taille_graphe - 1)
        noeud_2 = random.randint(0, taille_graphe - 1)
        poids = random.randint(1,10)
        graphe_1.add_edge(noeud_1, noeud_2, weight=poids)

        noeud_1 += (int)(taille_graphe/2)
        if noeud_1 > (int)(taille_graphe - 1):
            noeud_1 -= taille_graphe

        noeud_2 += (int)(taille_graphe/2)
        if noeud_2 > (taille_graphe - 1):
            noeud_2 -= taille_graphe
        graphe_2.add_edge(noeud_1, noeud_2, weight=poids)
        cpt += 1
    paire_graphes = [graphe_1, graphe_2]
    return paire_graphes




def GraphsGenerate(nbPairesGraphes, nbNoeuds):

    #On cree une liste de paires de graphes vide
    listPaireGraphs = []

    #On recupere la liste des noeuds generer
    listNode = FactoryNode.NodesGenerate(nbNoeuds)



    #On creer des paires de graphes
    while len(listPaireGraphs) < nbPairesGraphes :
        G1 = nx.Graph()
        G2 = nx.Graph()
        for node in listNode:
            G1.add_node(node, weight=random.randint(1, 10))
            G2.add_node(node, weight=random.randint(1, 10))
        liste_graphes = CreerAretes(G1,G2)
        paireGraphe = PaireGraphs.PaireGraphs(liste_graphes[0], liste_graphes[1], True)
        listPaireGraphs.append(paireGraphe)






    """Permet d afficher et sauvegarder les graphes pour test
    for paire in listPaireGraphs:
        graph1 = paire.premierGraphe
        nx.draw(graph1)
        plt.show()
        # nx.write_gexf(graph1,"test"+str(cptGraph)+".gexf")
        graph2 = paire.secondGraphe
        nx.draw(graph2)
        plt.show()"""

    print(len(listPaireGraphs), " Paires de graphes generees")
    return listPaireGraphs




