import networkx as nx
import matplotlib.pyplot as plt
from factory import FactoryNode
import random

#Generer n graphes de x sommet

def GraphsGenerate(nbGraphes, nbNoeuds):

    #On cree une liste de graphe vide
    listGraph = []

    #On recupere la liste des noeuds generer
    listNode = FactoryNode.NodesGenerate(nbNoeuds)

    #On cree n graph et on les ajoute a la liste
    graphDansListe = 0
    while graphDansListe < nbGraphes :
        G = nx.Graph()
        for node in listNode:
            G.add_node(node)
        listGraph.append(G)
        graphDansListe += 1



    for graph in listGraph:
        #On commence par relier chaque noeud a un autre aleatoirement pour eviter les noeuds isoles
        for noeud in list(G.nodes):
            noeudCouple = random.randint(0,G.number_of_nodes()-1)

            #On ecrase le noeud couple si c est le noeud traite
            while noeudCouple == noeud :
                    noeudCouple = random.randint(0, G.number_of_nodes() - 1)
            graph.add_edge(noeud,noeudCouple)

        #On choisi aleatoirement le nombre d arete du graphe
        nbEdge= random.randint(1, (nbNoeuds - 1) * (nbNoeuds - 1)) - nbNoeuds
        cpt =0
        while cpt < nbEdge :
            graph.add_edge(random.randint(0,G.number_of_nodes()-1),random.randint(0,G.number_of_nodes()-1))
            cpt += 1




    #Permet d'afficher et sauvegarder les graphes pour test
    cptGraph = 1
    for graph in listGraph:
        nx.draw(graph)
        plt.show()
        nx.write_gexf(graph,"test"+str(cptGraph)+".gexf")
        cptGraph += 1


GraphsGenerate(50,10)