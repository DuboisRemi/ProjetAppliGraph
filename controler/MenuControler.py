import networkx as nx
from numpy import linalg, matmul,transpose



def umeyama(listPairesGraphs):

    for paires in listPairesGraphs :
        # Retourne les matrice d adjacences ( on transforme en array de array )
        adjacency_matrix_un = nx.adjacency_matrix(paires.premierGraphe).toarray()
        adjacency_matrix_deux = nx.adjacency_matrix(paires.secondGraphe).toarray()

        # Recupere les matrices modales issues des matrices d adjacences
        matrice_modale_un = linalg.eig(adjacency_matrix_un)[1]
        matrice_modale_deux = linalg.eig(adjacency_matrix_deux)[1]

        # Pour obtenir la matrice de similarite il faut utiliser les valeurs absolues dans les matrices
        for array in matrice_modale_un:
            for valeur in range(len(array)):
                array[valeur] = abs(array[valeur])

        for array2 in matrice_modale_deux:
            for valeur2 in range(len(array2)):
                array2[valeur2] = abs(array2[valeur2])

        # On calcule ensuite la matrice de similitude

        matrice_similarite = matmul(matrice_modale_un,transpose(matrice_modale_deux))

        # On fait l'algo hongrois ( munkres )

        # Reduction des lignes
        for i in range(len(matrice_similarite)):
            min_val_ligne = matrice_similarite[i][0]
            for val in matrice_similarite[i]:
                if val < min_val_ligne:
                    min_val_ligne = val
            for j in  range(len(matrice_similarite[i])):
                matrice_similarite[i][j] -= min_val_ligne

        # Reduction des colonnes
        for k in range(len(matrice_similarite)):
            min_val_colonne = matrice_similarite[0][k]
            for l in range(len(matrice_similarite)):
                if matrice_similarite[l][k] < min_val_colonne:
                    min_val_colonne = matrice_similarite[l][k]
            for m in range(len(matrice_similarite)):
                matrice_similarite[m][k] -= min_val_colonne











