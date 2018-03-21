import os
import xml.etree.ElementTree as ET
import csv


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

data = grecLowLevelInfo('Data/LevelInfo/GREC10-lowlevelinfo.csv')

print(readGraph(data[0][0]))