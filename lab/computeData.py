import networkx as nx
import xml.etree.ElementTree as ET
import csv
from entity import PaireGraphs
import matplotlib.pyplot as plt

# Fonction qui va nous retourner les resultats attendus
# On effectue d'abord un travail sur le fichier pour le liberer pendant le traitement futur
def grecLowLevelInfo(filepath):

    # Nous ouvrons le fichier au format csv
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        # Nous creeons la structure qui va contenir les informations qui nous interessent
        '''
        Structure de data : (liste_information)
            liste_information = (nomGraphe1, nomGraphe2, distance, matching)
        '''
        data = []
        for row in reader:
            nouvelle_entree = []
            nouvelle_entree.append(row['Graph1 Name'])
            nouvelle_entree.append(row['Graph2 Name'])
            nouvelle_entree.append(row[' distance'])
            nouvelle_entree.append(row['matching'])
            data.append(nouvelle_entree)
        return data

# Ici, une fonction qui nous retournera les informations du graphe de nom "name"
def readGraph(name):
    tree = ET.parse('Data/GREC/' + name)
    root = tree.getroot()

    # Nous creeons la structure qui representera un graphe
    '''
        Structure du graphe : (nom, liste_noeuds, liste_aretes)
        nom : le nom du graphe, a savoir le nom du fichier d'origine
        liste_noeuds : liste qui contiendra tous les noeuds du graphe
        liste_aretes : liste qui contiendra toutes les aretes du graphe
    '''
    graphe = []
    graphe.append(name)

    # Nous recuperons les noeuds du graphe en cours de traitement
    '''
        Structure du noeud : (id, (x,y,type))
        id : L'id du noeud, pour le reconnaitre dans le traitement des aretes
        (x, y, type) : label du noeud
            x : abscisse du noeud
            y : ordonnee du noeud
            type : type du noeud
    '''
    liste_noeud = []
    for node in root.iter('node'):
        noeud = []
        id = node.get('id')
        noeud.append(id)
        label = []
        for attr in node.iter('attr'):
            for child in attr:
                value = child.text
                label.append(value)
        noeud.append(label)
        liste_noeud.append(noeud)

    # print(liste_noeud)

    # Nous recuperons les aretes du graphes en cours de traitement
    '''
        Structure d'une arete : (from, to, (frequence, type, angle))
        from : id du noeud de depart
        to : id du noeud d'arrivee
        (frequence, type, angle) : label de l'arete
            frequence : ?
            type : le type d'arete
            angle : valeur de l'angle entre le noeud de depart et d'arrivee        
    '''
    liste_arete = []
    for edge in root.iter('edge'):
        arete = []
        depart = edge.get('from')
        arrivee = edge.get('to')
        arete.append(depart)
        arete.append(arrivee)
        label = []
        for attr in edge.iter('attr'):
            for child in attr:
                value = child.text
                label.append(value)
        arete.append(label)
        liste_arete.append(arete)

    # print(liste_arete)

    graphe.append(liste_noeud)
    graphe.append(liste_arete)

    return graphe

# Fonction qui va generer un graphe de type Networkx
'''
    listeInfo : (nomDuGraphe, liste_noeuds, liste_aretes)
'''
def generateGraph(listeInfo):

    # Creation du graphe au format networkx
    graph = nx.Graph()

    #Recuperation des noeuds & aretes
    liste_Noeuds = listeInfo[1]
    liste_Aretes = listeInfo[2]

    # Ajout des noeuds
    for node in liste_Noeuds:
        id = node[0]
        label = node[1]
        graph.add_node(id, label = label)

    # Ajout des aretes
    for edge in liste_Aretes:
        fr = edge[0]
        to = edge[1]
        label = edge[2]
        graph.add_edge(fr, to, label = label)

    return graph

def generatePaireGraph(graphe1, graphe2, matching):
    gr1 = generateGraph(graphe1)
    gr2 = generateGraph(graphe2)

    matching = matching.split("/")
    liste_matching = []

    # On recupere les cellules correspondant aux node et non aux edge
    liste_node_cell = []
    for cell in matching:
        if "Node:" in cell:
            liste_node_cell.append(cell)

    # On va recuperer les matching
    for cell in liste_node_cell:
        new_matching = []
        new_matching.append(cell[5])
        new_matching.append(cell[8])
        liste_matching.append(new_matching)

    nouvelle_paire = PaireGraphs.PaireGraphs(gr1, gr2, liste_matching)

    return nouvelle_paire

'''
    Partie verification
'''
# data = grecLowLevelInfo('Data/LevelInfo/GREC10-lowlevelinfo.csv')
#
# g = data[1][3]
# g = g.split("/")
# print(g)
# trueG = []
# for cell in g:
#     if "Node:" in cell:
#         trueG.append(cell)
# for cell in trueG:
#     print(cell[5])
#     print(cell[8])

# print(g)
#
# gG = generateGraph(g)
#
# nx.draw(gG)
# plt.show()