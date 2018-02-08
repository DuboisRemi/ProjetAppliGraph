from factory.FactoryGraph import GraphsGenerate

def GenerateGraphsContol(inputNbPairesGraph, inputNbNoeuds):
    try :
        listePairesGraphs = GraphsGenerate(inputNbPairesGraph, inputNbNoeuds)

    except ValueError :
        print("Erreur")




