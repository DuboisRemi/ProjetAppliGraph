import networkx as nx
from numpy import linalg, matmul, transpose, math, mean , zeros
from munkres import Munkres, make_cost_matrix
from math import ceil,floor
import sys
import time
from entity import PaireGraphs,signatureNoeud
import matplotlib.pyplot as plt



from factory import FactoryNode
from lab import computeData


def umeyama(liste_paires_graphes):

    # On lance le chrono
    chrono = time.clock()

    # Compteur d'erreur global
    cpt_erreur = 0

    cpt_noeud_traites = 0

    # On stock la taille des graphes
    taille_graphe = liste_paires_graphes[0].premierGraphe.number_of_nodes()

    for paires in liste_paires_graphes :
        # Retourne les matrice d adjacences ( on transforme en array de array )
        adjacency_matrix_un = nx.adjacency_matrix(paires.premierGraphe).toarray()
        adjacency_matrix_deux = nx.adjacency_matrix(paires.secondGraphe).toarray()



        # Recupere les matrices modales issues des matrices d adjacences
        matrice_modale_un = linalg.eig(adjacency_matrix_un)[1]
        matrice_modale_deux = linalg.eig(adjacency_matrix_deux)[1]


        # Pour obtenir les matrices modales il faut utiliser les valeurs absolues dans les matrices
        for array in matrice_modale_un:
            for valeur in range(len(array)):
                array[valeur] = abs(array[valeur])

        for array2 in matrice_modale_deux:
            for valeur2 in range(len(array2)):
                array2[valeur2] = abs(array2[valeur2])

        # On calcule ensuite la matrice de similitude


        matrice_similarite = matmul(matrice_modale_un,transpose(matrice_modale_deux))
        cost_matrix = make_cost_matrix(matrice_similarite)

        # On fait l'algo hongrois ( munkres ) qui retourne des paires de noeuds apparies
        m = Munkres()
        paires_noeuds = m.compute(cost_matrix)

        # On regarde lez correspondances noeuds a noeuds et on compte les erreurs
        liste_corresponsance = paires.matching
        for corresponsance in liste_corresponsance:
            try :
                noeud_1 = (int)(corresponsance[0])
                noeud_2 = (int)(corresponsance[1])
                for noeuds_associes in paires_noeuds:
                    if  noeuds_associes[0] == noeud_1:
                        cpt_noeud_traites +=1
                        if noeuds_associes[1] != noeud_2:
                            cpt_erreur += 1

            except:
                print "Une valeur de la correpsondance n est pas un entier"




    taux_erreur = float((cpt_erreur*100) / (taille_graphe*len(liste_paires_graphes)))

    print "Taux d erreur = %f\n"%taux_erreur
    print "Temps execution = %f\n"%(time.clock()-chrono)
    print "nb noeuds traite = %f\n"%cpt_noeud_traites




def jouili(liste_paires_graphes):


    # On lance le chrono
    chrono = time.clock()

    # Compteur d'erreur global
    cpt_erreur = 0

    cpt_noeud_traites = 0


    nb_noeuds = 0
    for paire in liste_paires_graphes:

        nb_noeuds += liste_paires_graphes[0].premierGraphe.number_of_nodes()

        signatures_noeuds_graphe1 = obtenir_signatures_noeuds(paire.premierGraphe)
        signatures_noeuds_graphe2 = obtenir_signatures_noeuds(paire.secondGraphe)

        matrice_distance = zeros((len(signatures_noeuds_graphe1),len(signatures_noeuds_graphe2)))
        cpt_ligne = 0

        for signature_noeud in signatures_noeuds_graphe1:
            cpt_colonne = 0
            for signature_noeud2 in signatures_noeuds_graphe2 :
                matrice_distance[cpt_ligne][cpt_colonne] = calcul_distance_signatures(signature_noeud, signature_noeud2)
                cpt_colonne += 1
            cpt_ligne += 1

        m = Munkres()
        paires_noeuds = m.compute(matrice_distance)


        liste_corresponsance = paire.matching
        for corresponsance in liste_corresponsance:
            try:
                noeud_1 = (int)(corresponsance[0])
                noeud_2 = (int)(corresponsance[1])
                for noeuds_associes in paires_noeuds:
                    if  noeuds_associes[0] == noeud_1:
                        cpt_noeud_traites +=1
                        if noeuds_associes[1] != noeud_2:
                            cpt_erreur += 1

            except:
                print "Une valeur de la correpsondance n est pas un entier"

    taux_erreur = float((cpt_erreur * 100) / (nb_noeuds * len(liste_paires_graphes)))

    print "Taux d erreur = %f\n" % taux_erreur
    print "Temps execution = %f\n" % (time.clock() - chrono)
    print "nb noeuds traite = %f\n"%cpt_noeud_traites






def obtenir_signatures_noeuds(graphe):

    signatures_noeuds = []
    for node in graphe.nodes():

        degre = nx.degree(graphe, node)
        degres_noeuds_adjacents = []
        for node in nx.all_neighbors(graphe, node):
            degres_noeuds_adjacents.append(nx.degree(graphe, node))
        attributs = graphe.nodes[node]['label']
        attributs_arretes = []
        arretes_lies_noeuds = []
        arretes_lies_noeuds = nx.edges(graphe)
        for arrete in arretes_lies_noeuds:
            attributs_arretes =  graphe[arrete[0]][arrete[1]]['label']
        signature = signatureNoeud.SignatureNoeud(attributs,degre,degres_noeuds_adjacents,attributs_arretes)
        signatures_noeuds.append(signature)
    return signatures_noeuds


def calcul_distance_signatures(signature1, signature2):

    cpt_distance_attribut = 0
    if len(signature1.attributs) < len(signature2.attributs):
        taille_min_attribut= len(signature1.attributs)

    else: taille_min_attribut= len(signature2.attributs)

    for i in range(0, taille_min_attribut):
        if signature1.attributs[i] not in signature2.attributs:
            cpt_distance_attribut += 1

    cpt_distance_attribut += len(signature1.attributs) - len(signature2.attributs)

    cpt_distance_attribut = math.sqrt(abs(cpt_distance_attribut))

    if signature1.degre != 0 & signature2.degre != 0 :
        cpt_distance_degre = math.sqrt(abs(signature1.degre-signature2.degre)/(signature1.degre+signature2.degre))

    else :
        cpt_distance_degre = math.sqrt(abs(signature1.degre - signature2.degre))

    cpt_distance_degres_noeuds_adjacents = 0

    if len(signature1.degres_noeuds_adjacents) < len(signature2.degres_noeuds_adjacents):
        taille_min_degres_noeuds_adjacents = len(signature1.degres_noeuds_adjacents)

    else: taille_min_degres_noeuds_adjacents = len(signature2.degres_noeuds_adjacents)

    for j in range(0, taille_min_degres_noeuds_adjacents):
        cpt_distance_degres_noeuds_adjacents +=\
            math.pow(abs(signature1.degres_noeuds_adjacents[j]-signature2.degres_noeuds_adjacents[j])
                     / mean(signature1.degres_noeuds_adjacents), 2)

    cpt_distance_degres_noeuds_adjacents +=\
        len(signature1.degres_noeuds_adjacents) - len(signature2.degres_noeuds_adjacents)

    cpt_distance_degres_noeuds_adjacents = math.sqrt((abs)(cpt_distance_degres_noeuds_adjacents))

    cpt_distance_attributs_arretes = 0

    if len(signature1.attributs_arretes) < len(signature2.attributs_arretes):
        taille_min_attributs_arretes = len(signature1.attributs_arretes)

    else:
        taille_min_attributs_arretes = len(signature2.attributs_arretes)

    for k in range(0, taille_min_attributs_arretes):
        if signature1.attributs_arretes[k] not in signature2.attributs_arretes:
            cpt_distance_attributs_arretes += 1

    cpt_distance_attributs_arretes += len(signature1.attributs_arretes) - len(signature2.attributs_arretes)

    cpt_distance_attributs_arretes  = math.sqrt(cpt_distance_attributs_arretes)

    distance_signature = cpt_distance_attribut + cpt_distance_degre + cpt_distance_degres_noeuds_adjacents + cpt_distance_attributs_arretes

    return distance_signature




liste_paires_graphes = []
data = computeData.grecLowLevelInfo('Data/LevelInfo/GREC5-lowlevelinfo.csv')
for cellule in data:
    info_graphe1 = computeData.readGraph(cellule[0])
    info_graphe2 = computeData.readGraph(cellule[1])
    liste_paires_graphes.append(computeData.generatePaireGraph(info_graphe1, info_graphe2 , cellule[3]))

print len(liste_paires_graphes)

umeyama(liste_paires_graphes)
jouili(liste_paires_graphes)


'''
cpt_paire = 1
for paire in liste_paires_graphes:
    nx.draw(paire.premierGraphe)
    plt.savefig('paire_'+str(cpt_paire)+'_1.png')
    plt.close()
    nx.draw(paire.secondGraphe)
    plt.savefig('paire_'+str(cpt_paire)+ '_2.png')
    plt.close()
    cpt_paire +=1
'''













