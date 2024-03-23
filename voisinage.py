def parcours_voisinage(G):
    # Initialisation des structures de données
    Atteint = {}  # Dictionnaire pour marquer les sommets atteints
    table_pere = {}     # Dictionnaire pour stocker les pères de chaque sommet dans l'arborescence de recherche
    table_profondeur = {}  # Dictionnaire pour stocker la profondeur de chaque sommet par rapport au sommet de départ
    for sommet in G:
        # Initialisation de chaque sommet
        table_pere[sommet] = 0  # Le père de chaque sommet est initialisé à 0 (non visité)
        Atteint[sommet] = False  # Marquer chaque sommet comme non atteint

    # Parcours en profondeur
    for sommet in G:
        if Atteint[sommet] == False:  # Si le sommet n'a pas encore été atteint
            s0 = sommet  # Définir le sommet de départ pour le parcours en profondeur
            Atteint[s0] = True  # Marquer le sommet de départ comme atteint
            table_pere[s0] = s0  # Le père du sommet de départ est lui-même
            table_profondeur[sommet] = 0  # La profondeur du sommet de départ est 0
            E = [s0]  # File pour stocker les sommets à explorer
            while E:  # Tant qu'il y a des sommets à explorer
                for s in E:  # Pour chaque sommet dans la file E
                    E.remove(s)  # Retirer le sommet de la file
                    for t in G[s]:  # Pour chaque voisin du sommet s
                        if table_pere[t] == 0:  # Si le voisin n'a pas encore de père
                            Atteint[t] = True  # Marquer le voisin comme atteint
                            table_profondeur[t] = table_profondeur[s] + 1  # Calculer la profondeur du voisin
                            table_pere[t] = s  # Définir le père du voisin
                            E.append(t)  # Ajouter le voisin à la file pour exploration

    return table_pere, table_profondeur  # Retourner à la fois la table des pères et la table des profondeurs


if __name__ == "__main__":
    # Exemple de graphes de test
    graph = {
        1: [2, 5],
        2: [1, 3, 4, 5],
        3: [2, 4, 9],
        4: [2, 3],
        5: [1, 2],
        6: [7, 8],
        7: [6, 8],
        8: [6, 7],
        9: [3]
    }
    
    graph2 = {
        1: [2, 3],
        2: [4, 1, 3],
        3: [1, 2, 5],
        4: [2],
        5: [3],
        6: []

    }

    # Appel de la fonction pour le graphe 2
    result = parcours_voisinage(graph2)
    print(result)  # Afficher le résultat du parcours en profondeur
