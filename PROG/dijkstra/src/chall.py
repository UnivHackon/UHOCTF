import datetime
from random import *
import heapq
import networkx as nx
import matplotlib.pyplot as plt

NODES_NAMES = open("stations.txt").read().splitlines()

def save_graph_as_image(graph, filename):
    """
    Save a graph to a file

    Content of image:
    - nodes are labeled
    - edges have a weight
    """
    pos = nx.spring_layout(graph, k=1)
    nx.draw_networkx(graph, pos, with_labels=True, node_size=10, font_size=5)
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.savefig(filename)

def random(n, p, max_weight=10, min_weight=1):
    """
    Crée un graphe aléatoire de n sommets et de probabilité p

    les poids des arêtes sont des entiers aléatoires entre min_weight et max_weight
    les nodes sont nommés aves des noms de la liste NODES_NAMES
    """
    graph = nx.erdos_renyi_graph(n, p)

    # Renomme les labels des nodes avec des noms de la liste NODES_NAMES
    mapping = { i: NODES_NAMES[i] for i in range(n) }
    graph = nx.relabel_nodes(graph, mapping)

    # Assigne des poids aléatoires aux arêtes
    for u, v in graph.edges:
        graph.edges[u, v]["weight"] = randint(min_weight, max_weight)

    return graph

def generate_random_graph_json(min_weight, max_weight, n):
    """
    Crée un graphe aléatoire de n sommets et de probabilité p
    """

    # Crée un graphe aléatoire de n sommets et de probabilité p
    graph = random(n, n/100, max_weight, min_weight)

    #save_graph_as_image(graph, "random.png")

    graph_dict = {
        "nodes": list(graph.nodes),
        "edges": [
            { "source": u, "target": v, "weight": graph.edges[u, v]["weight"] }
            for u, v in graph.edges
        ]
    }

    return graph_dict

def generate_random_challenge(num_nodes, min_weight, max_weight):
    """
    Génère un challenge aléatoire
    """

    # Crée un graphe aléatoire de n sommets et de probabilité p
    graph = generate_random_graph_json(min_weight, max_weight, num_nodes)

    source = choice(graph["nodes"])
    destination = choice(graph["nodes"])

    # Assurez-vous que la source et la destination sont différentes
    while source == destination:
        destination = choice(graph["nodes"])

    challenge = {
        "graph": graph,
        "source": source,
        "destination": destination
    }
    
    return challenge

def dijkstra(graph, source, destination):
    """
    Calcule le chemin le plus court entre la source et la destination
    """

    # Initialise les distances à l'infini
    distances = {node: float('inf') for node in graph["nodes"]}
    # Initialise la distance de la source à 0
    distances[source] = 0

    # Initialise la file de priorité
    heap = [(0, source)]
    while heap:
        # Récupère le noeud avec la plus petite distance
        current_distance, current_node = heapq.heappop(heap)

        # Si la distance est plus grande que la distance actuelle, on passe au noeud suivant
        if current_distance > distances[current_node]:
            continue

        # Si on a atteint la destination, on arrête
        if current_node == destination:
            break

        # Pour chaque voisin du noeud courant
        for edge in graph["edges"]:
            # Si le noeud courant est la source de l'arête
            if edge["source"] == current_node:
                # Récupère le noeud voisin
                neighbor = edge["target"]
                # Calcule la distance entre la source et le voisin
                distance = current_distance + edge["weight"]
                # Si la distance est plus petite que la distance actuelle
                if distance < distances[neighbor]:
                    # Met à jour la distance
                    distances[neighbor] = distance
                    # Ajoute le voisin à la file de priorité
                    heapq.heappush(heap, (distance, neighbor))

    # Retourne la distance entre la source et la destination
    return distances[destination]

def transform_json_to_shell_output(graph_json):
    """
    Transforme un graphe au format JSON en une chaîne de caractères
    qui peut être affichée dans un terminal
    """
    edges = graph_json["graph"]["edges"]
    shell_output = ""
    for edge in edges:
        shell_output += f"{edge['source']} -> {edge['target']} : {edge['weight']}\n"

    shell_output += "---\n"
    shell_output += f"{graph_json['source']} -> {graph_json['destination']}\n"

    return shell_output

score = 0;

def main():
    global score

    nb_nodes = randint(20, 30)

    # Crée un challenge aléatoire
    random_challenge = generate_random_challenge(nb_nodes, 1, 10)
    resp = dijkstra(random_challenge["graph"], random_challenge["source"], random_challenge["destination"])

    while resp == float("inf"):
        random_challenge = generate_random_challenge(nb_nodes, 1, 10)
        resp = dijkstra(random_challenge["graph"], random_challenge["source"], random_challenge["destination"])

    # Affiche le challenge
    print(transform_json_to_shell_output(random_challenge))

    # Demande à l'utilisateur de saisir le chemin le plus court
    user_answer = int(input("Quel est le chemin le plus court ? "))

    with open("log.txt", "a") as f:
        # log the time, the score and the user answer
        f.write(f"{datetime.now()}\t{score}\t{user_answer}\n")

    # Vérifie si la réponse est correcte
    if user_answer == resp:
        score += 1
        print(f"Bonne réponse !")
    else:
        exit()

    if score == 10:
        # Send the flag
        with open("flag.txt", "r") as f:
            print(f"Flag : {f.read()}")
        print("Voulez-vous continuer ? (o/n) ")
        exit()
        return

    # Demande à l'utilisateur s'il veut continuer
    elif input("Voulez-vous continuer ? (o/n) ") == "o":
        main()

__name__ == "__main__" and main()

