import networkx as nx
import matplotlib.pyplot as plt
from factory import FactoryNode
from entity import PaireGraphs
import random

#Fonction qui creer des aretes aleatoire entre les points des graphes
def creerAretes(graphe):
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




def GraphsGenerate(nbPairesGraphes, nbNoeuds, nbPairesIsomorphes):

    #On cree une liste de paires de graphes vide
    listPaireGraphs = []

    #On recupere la liste des noeuds generer
    listNode = FactoryNode.NodesGenerate(nbNoeuds)



    #On creer tout d'abord des paires identiques
    while len(listPaireGraphs) < nbPairesIsomorphes :
        G = nx.Graph()
        for node in listNode:
            G.add_node(node)
        G = creerAretes(G)
        paireGraphe = PaireGraphs.PaireGraphs(G, G, True)
        listPaireGraphs.append(paireGraphe)





    #On considere que les graphes generes aleatoirement ne sont pas isomorphes ( c est probable quand meme )
    while len(listPaireGraphs)< nbPairesGraphes :
        G1 = nx.Graph()
        for node in listNode:
            G1.add_node(node)
        G1 = creerAretes(G1)
        G2 = nx.Graph()
        for node in listNode:
            G2.add_node(node)
        G2 = creerAretes(G2)
        paireGraphe = PaireGraphs.PaireGraphs(G1, G2, False)
        listPaireGraphs.append(paireGraphe)






    #Permet d'afficher et sauvegarder les graphes pour test
    for paire in listPaireGraphs:
        graph1 = paire.premierGraphe
        nx.draw(graph1)
        plt.show()
        #nx.write_gexf(graph1,"test"+str(cptGraph)+".gexf")
        graph2 = paire.secondGraphe
        nx.draw(graph2)
        plt.show()



GraphsGenerate(10,10,3)