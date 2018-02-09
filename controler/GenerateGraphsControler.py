from factory.FactoryGraph import GraphsGenerate
from view.MenuView import init

def GenerateGraphsContol(inputNbPairesGraph, inputNbNoeuds):

    try :
        listePairesGraphs = GraphsGenerate(inputNbPairesGraph, inputNbNoeuds)
        init(listePairesGraphs)

    except ValueError :
        print("Erreur")





