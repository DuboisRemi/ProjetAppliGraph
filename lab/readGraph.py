import xml.etree.ElementTree as ET
import os

#
# On initialise la future collection qui va contenir les graphes
liste_graphes = []

# On parcours tous les fichiers du dossiers contenant les graphes
for file in os.listdir('GREC'):
    # print(file)
    tree = ET.parse('GREC/'+file)
    root = tree.getroot()

    # Nous creeons la structure qui representera un graphe
    '''
        Structure du graphe : (nom, liste_noeuds, liste_aretes)
        nom : le nom du graphe, a savoir le nom du fichier d'origine
        liste_noeuds : liste qui contiendra tous les noeuds du graphe
        liste_aretes : liste qui contiendra toutes les aretes du graphe
    '''
    graphe = []
    graphe.append(file)

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

    liste_graphes.append(graphe)

print(liste_graphes[0])
