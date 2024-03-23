def parcours_largeur(G):
    # Initialisation des structures de données
    table_pere = {}  # Dictionnaire pour stocker les pères de chaque sommet dans l'arborescence de recherche
    table_atteint = {}  # Dictionnaire pour marquer les sommets atteints
    table_profondeur = {}  # Dictionnaire pour stocker la profondeur de chaque sommet par rapport au sommet de départ
    début = 0  # Indice du début de la file de sommets à explorer
    fin = 0  # Indice de la fin de la file de sommets à explorer

    # Initialisation des pères de tous les sommets à 0
    for sommet in G.keys():
        table_pere[sommet] = 0  # Affectation de la valeur 0 à chaque sommet

    # Parcours en largeur
    while not all(table_pere[S0] for S0 in table_pere.keys()):  # Tant que tous les sommets n'ont pas de père
        for S0 in table_pere.keys():
            if table_pere[S0] == 0:  # Si le sommet n'a pas encore de père
                table_pere[S0] = S0  # Marquer le sommet comme visité, son propre père est lui-même
                fin += 1  # Augmenter l'indice de la fin de la file
                table_atteint[fin] = S0  # Ajout du sommet à la liste des sommets atteints
                table_profondeur[S0] = 0  # Initialiser la profondeur à 0 pour le sommet racine
                # Parcours des voisins du sommet actuel
                while début < fin:
                    début += 1  # Avancer l'indice du début de la file
                    S = table_atteint[début]  # Sélectionner le sommet à explorer
                    for t in G[S]:  # Parcourir les voisins du sommet S
                        if table_pere[t] == 0:  # Si le voisin n'a pas encore de père
                            fin += 1  # Augmenter l'indice de la fin de la file
                            table_atteint[fin] = t  # Ajouter le voisin à la file pour exploration
                            table_pere[t] = S  # Définir le père du voisin
                            table_profondeur[t] = table_profondeur[S] + 1  # Profondeur du voisin = profondeur de S + 1

    return table_pere, table_profondeur  # Retourner à la fois la table des pères et la table des profondeurs


if __name__ == "__main__":
    # Exemple de graphe de test
    graphe = {
        1: [2, 3],
        2: [4, 1, 3],
        3: [1, 2, 5],
        4: [2],
        5: [3],
        6: []

    }

    # Appel de la fonction pour le graphe de test
    result = parcours_largeur(graphe)
    print(result)  # Afficher le résultat du parcours en largeur
