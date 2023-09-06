import heapq

def dijkstra(start, distance, graph):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(queue, (dist + i[1], i[0]))
    return distance
            
def solution(N, road, K):
    distance = [ 1e9 for _ in range(N+1) ]
    graph = [ [] for _ in range(N+1) ]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    distance = dijkstra(1, distance, graph)
    return len([ True for val in distance if val <= K ])