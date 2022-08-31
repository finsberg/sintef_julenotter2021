def dfs(node, visited, graph):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(neighbour, visited, graph)


if __name__ == "__main__":
    N = int(input().strip())
    graph = {}
    for _ in range(N):
        value, *edges = map(int, input().strip().split(" "))
        graph[value] = set(edges)

    all_subgraphs = set()
    for value in graph:
        visited = set()
        dfs(value, visited, graph)
        all_subgraphs.add(tuple(visited))

    cleaned_subgraphs = []
    sorted_subgraphs = sorted(list(all_subgraphs), key=lambda x: len(x), reverse=True)
    for i, subgraph in enumerate(sorted_subgraphs):
        current_subgraph = set(subgraph)
        for j, smaller_subgraph in enumerate(sorted_subgraphs[i + 1 :]):
            current_subgraph.difference_update(set(smaller_subgraph))
        cleaned_subgraphs.append(tuple(sorted(current_subgraph)))

    for subgraph in sorted(cleaned_subgraphs, key=lambda x: x[0]):
        print(" ".join(map(str, subgraph)))
