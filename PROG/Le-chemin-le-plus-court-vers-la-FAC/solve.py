import heapq
import json
import pwn

# Process challenge
p = pwn.process(["python3", "chall.py"])

nodes = []
edges = []
tri = 0

def parse(p):
    line = p.recvline().decode().strip()

    while line != "---":
        edges.append(parse_edges(line))
        line = p.recvline().decode().strip()

    path = p.recvline().decode().strip().split("->")
    source = path[0].strip()
    destination = path[1].strip()

    return {
        "nodes": nodes,
        "edges": edges,
        "source": source,
        "destination": destination
    }

def parse_node(name):
    if name not in nodes:
        nodes.append(name)

def parse_edges(line):
    weight = int(line.split(":")[1].strip())
    source = line.split("->")[0].strip()
    target = line.split("->")[1].split(":")[0].strip()

    parse_node(source)
    parse_node(target)

    return {
        "source": source,
        "target": target,
        "weight": weight
    }

def dijkstra(graph, source, destination):
    distances = {node: float('inf') for node in graph["nodes"]}
    distances[source] = 0

    heap = [(0, source)]
    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        if current_node == destination:
            break

        for edge in graph["edges"]:
            if edge["source"] == current_node:
                neighbor = edge["target"]
                distance = current_distance + edge["weight"]
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

    return distances[destination]



def main():
    global tri
    print("Starting...")
    edges.clear()
    graph = parse(p)
    graph_json = json.dumps(graph, indent=2)

    # Send graph to dijkstra
    res = dijkstra({
        "nodes": graph["nodes"],
        "edges": graph["edges"]
    }, graph["source"], graph["destination"])

    # Receive until "Quel est le chemin le plus court ?"
    print(p.recvuntil(b"Quel est le chemin le plus court ?"))

    print(res)
    print(res.to_bytes(4, "big"))

    # Send shortest path as int
    p.sendline(str(res).encode())

    print(p.recvuntil(b'(o/n)'))

    # Send "o"
    p.sendline(b"o")
    tri = tri + 1
    main()



__name__ == "__main__" and main()
