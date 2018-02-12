import networkx as nx
import matplotlib.pyplot as plt
from factory import FactoryNode
from entity import PaireGraphs
import random

#Fonction qui creer des aretes aleatoire entre les points des graphes
def CreerAretes(graphe):
    # On commence par relier chaque noeud a un autre aleatoirement pour eviter les noeuds isoles
    for noeud in list(graphe.nodes):
        noeudCouple = random.randint(0, graphe.number_of_nodes() - 1)

        # On ecrase le noeud couple si c est le noeud traite
        while noeudCouple == noeud:
            noeudCouple = random.randint(0, graphe.number_of_nodes() - 1)
        graphe.add_edge(noeud, noeudCouple)

    # On choisi aleatoirement le nombre d arete du graphe
    nbEdge = random.randint(1, (graphe.number_of_nodes() - 1)*(graphe.number_of_nodes() - 1))
    cpt = 0
    while cpt < nbEdge:
        graphe.add_edge(random.randint(0, graphe.number_of_nodes() - 1), random.randint(0, graphe.number_of_nodes() - 1))
        cpt += 1

    return graphe




def GraphsGenerate(nbPairesGraphes, nbNoeuds):

    #On cree une liste de paires de graphes vide
    listPaireGraphs = []

    #On recupere la liste des noeuds generer
    listNode = FactoryNode.NodesGenerate(nbNoeuds)



    #On creer des paires identiques
    while len(listPaireGraphs) < nbPairesGraphes :
        G = nx.Graph()
        for node in listNode:
            G.add_node(node)
        G = CreerAretes(G)
        paireGraphe = PaireGraphs.PaireGraphs(G, G, True)
        listPaireGraphs.append(paireGraphe)






    """Permet d'afficher et sauvegarder les graphes pour test
    for paire in listPaireGraphs:
        graph1 = paire.premierGraphe
        nx.draw(graph1)
        plt.show()
        #nx.write_gexf(graph1,"test"+str(cptGraph)+".gexf")
        graph2 = paire.secondGraphe
        nx.draw(graph2)
        plt.show()"""

    print(len(listPaireGraphs), " Paires de graphes generees")
    return listPaireGraphs



