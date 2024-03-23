def parcours_profondeur(G):
    table_pere = {}  # Dictionnaire pour stocker les pères de chaque sommet dans l'arborescence de recherche
    table_profondeur = {}  # Dictionnaire pour stocker la table_profondeur de chaque sommet par rapport au sommet de départ
    
    # Initialisation des pères et des table_profondeurs
    for sommet in G:
        table_pere[sommet] = 0  # Initialiser tous les pères à 0 (non visité)
        table_profondeur[sommet] = 0  # Initialiser toutes les table_profondeurs à 0

    # Parcours en table_profondeur
    for sommet in G:
        if table_pere[sommet] == 0:  # Si le sommet n'a pas encore de père assigné
            table_pere[sommet] = sommet  # Définir le père du sommet comme lui-même (racine)
            table_profondeur[sommet] = 0  # La table_profondeur de la racine est 0
            sous_programme_table_profondeur(G, sommet, table_pere, table_profondeur)  # Appeler le sous-programme pour explorer en table_profondeur
    
    return table_pere, table_profondeur  # Retourner à la fois la table des pères et la table des table_profondeurs


def sous_programme_table_profondeur(G, s, table_pere, table_profondeur):
    for t in G[s]:  # Parcourir tous les voisins du sommet s
        if table_pere[t] == 0:  # Si le voisin n'a pas encore de père assigné
            table_pere[t] = s  # Définir le père du voisin comme le sommet s
            table_profondeur[t] = table_profondeur[s] + 1  # La table_profondeur du voisin est la table_profondeur de son père + 1
            sous_programme_table_profondeur(G, t, table_pere, table_profondeur)  # Appeler récursivement pour explorer en table_profondeur à partir du voisin


if __name__ == "__main__":
    graphe = {
        1: [2, 3],
        2: [4, 1, 3],
        3: [1, 2, 5],
        4: [2],
        5: [3],
        6: []
    }
    
    # Appel de la fonction pour le graphe donné
    table_pere, table_profondeur = parcours_profondeur(graphe)
    print("Table des pères:", table_pere)  # Afficher la table des pères
    print("Table de profondeurs:", table_profondeur)  # Afficher la table des table_profondeurs
