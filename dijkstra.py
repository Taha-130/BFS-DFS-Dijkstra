import math

def dijkstra_sans_etiquette(graphe):
    distances_minimales = {}  # Dictionnaire pour stocker les distances minimales pour chaque sommet
    
    for sommet in graphe:  # Parcourir tous les sommets du graphe
        distances = {s: math.inf for s in graphe}  # Initialiser toutes les distances à l'infini
        distances[sommet] = 0  # La distance du sommet à lui-même est 0
        visite = set()  # Ensemble des sommets visités
        
        while len(visite) < len(graphe):  # Tant que tous les sommets n'ont pas été visités
            sommet_courant = trouver_prochain_sommet(distances, visite)  # Trouver le prochain sommet à visiter
            visite.add(sommet_courant)  # Ajouter le sommet courant à l'ensemble des sommets visités
            
            for voisin in graphe[sommet_courant]:  # Parcourir les voisins du sommet courant
                nouvelle_distance = distances[sommet_courant] + 1  # Coût uniforme pour un graphe sans étiquette
                if nouvelle_distance < distances[voisin]:  # Si la nouvelle distance est plus courte que la distance actuelle
                    distances[voisin] = nouvelle_distance  # Mettre à jour la distance du voisin
                    
        distances_minimales[sommet] = distances  # Enregistrer les distances minimales pour ce sommet
        
    return distances_minimales  # Retourner les distances minimales pour tous les sommets


def trouver_prochain_sommet(distances, visite):
    min_distance = math.inf  # Initialiser la distance minimale à l'infini
    sommet_prochain = None  # Initialiser le prochain sommet à None
    for sommet, distance in distances.items():  # Parcourir tous les sommets et leurs distances
        if distance < min_distance and sommet not in visite:  # Si la distance est plus courte et le sommet n'a pas été visité
            min_distance = distance  # Mettre à jour la distance minimale
            sommet_prochain = sommet  # Mettre à jour le prochain sommet à visiter
    return sommet_prochain  # Retourner le prochain sommet à visiter


if __name__ == "__main__":
    graphe_sans_etiquette = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D'],
        'D': ['B', 'C']
    }
    
    distances_minimales = dijkstra_sans_etiquette(graphe_sans_etiquette)  # Appliquer l'algorithme de Dijkstra
    for sommet, distances in distances_minimales.items():  # Parcourir les distances minimales pour chaque sommet
        print("Distances minimales depuis le sommet", sommet, ":", distances)  # Afficher les distances minimales
