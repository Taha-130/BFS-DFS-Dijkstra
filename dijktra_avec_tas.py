import math
import heapq

def dijkstra_avec_poids(graphe):
    distances_minimales = {}
    
    for sommet in graphe:
        distances = {s: math.inf for s in graphe}  # Initialiser toutes les distances à l'infini
        distances[sommet] = 0  # Distance du sommet à lui-même est 0
        
        # Initialisation du tas avec le tuple (distance, sommet)
        tas = [(0, sommet)]
        
        while tas:
            # Extraire le sommet avec la distance minimale du tas
            distance, sommet_courant = heapq.heappop(tas)
            
            # Si le sommet a déjà été visité, passer au suivant
            if sommet_courant in distances_minimales:
                continue
            
            # Marquer le sommet comme visité
            distances_minimales[sommet_courant] = distance
            
            # Mettre à jour les distances des voisins non visités
            for voisin, poids in graphe[sommet_courant].items():
                if voisin not in distances_minimales:
                    nouvelle_distance = distance + poids
                    heapq.heappush(tas, (nouvelle_distance, voisin))
                    
    return distances_minimales

if __name__ == "__main__":
    graphe_avec_poids = {
        'A': {'B': 3, 'C': 1},
        'B': {'A': 3, 'C': 2, 'D': 1},
        'C': {'A': 1, 'B': 2, 'D': 4},
        'D': {'B': 1, 'C': 4}
    }
    
    distances_minimales = dijkstra_avec_poids(graphe_avec_poids)
    for sommet, distance in distances_minimales.items():
        print("Distance minimale depuis le sommet", sommet, ":", distance)
