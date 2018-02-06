import networkx as nx
import matplotlib.pyplot as plt
from factory import FactoryNode
import random

#Generer n graphes de x sommet

def GraphsGenerate(n,x):

    #On cree une liste de graphe vide
    listGraph = []

    #On recupere la liste des noeuds generer
    listNode = FactoryNode.NodesGenerate(x)

    #On cree n graph et on les ajoute a la liste
    nbGraph = 0
    while nbGraph < n :
        G = nx.Graph()
        for node in listNode:
            G.add_node(node)
        listGraph.append(G)
        nbGraph += 1

    for graph in listGraph:
        nbDeNoeud=random.randint(1,(x-1)*(x-1))
        cpt =0
        while cpt < nbDeNoeud :
            graph.add_edge(random.randint(0,G.number_of_nodes()-1),random.randint(0,G.number_of_nodes()-1))
            cpt += 1




    #Permet d'afficher et sauvegarder les graphes pour test
    cptGraph = 1
    for graph in listGraph:
        nx.draw(graph)
        plt.show()
        nx.write_gexf(graph,"test"+str(cptGraph)+".gexf")
        cptGraph += 1


GraphsGenerate(5,10)