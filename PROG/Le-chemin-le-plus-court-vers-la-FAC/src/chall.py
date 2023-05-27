import random
import json

def generate_random_graph(num_nodes, min_weight, max_weight):
    nodes = [chr(ord('A') + i) for i in range(num_nodes)]  # Génère des noms de nœuds de A à Z
    edges = []
    
    # Génère des arêtes aléatoires entre les nœuds avec des poids aléatoires
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            weight = random.randint(min_weight, max_weight)
            edge = {
                "source": nodes[i],
                "target": nodes[j],
                "weight": weight
            }
            edges.append(edge)
    
    graph = {
        "nodes": nodes,
        "edges": edges
    }
    
    return graph

def generate_random_challenge(num_nodes, min_weight, max_weight):
    graph = generate_random_graph(num_nodes, min_weight, max_weight)
    source = random.choice(graph["nodes"])
    destination = random.choice(graph["nodes"])
    
    # Assurez-vous que la source et la destination sont différentes
    while source == destination:
        destination = random.choice(graph["nodes"])
    
    challenge = {
        "graph": graph,
        "source": source,
        "destination": destination
    }
    
    return challenge

# Exemple d'utilisation
random_challenge = generate_random_challenge(26, 1, 10)
challenge_json = json.dumps(random_challenge, indent=2)
print(challenge_json)