import heapq

def dijkstra(start):
    distances = [float('inf') for _ in range(N+1)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue,[0,start])

    while queue:
        cur_distance, cur_destination = heapq.heappop(queue)

        if distances[cur_destination] < cur_distance : continue

        for new_destination, new_distance in graph[cur_destination] :
            d = cur_distance + new_distance
            if distances[new_destination] > d:
                distances[new_destination] = d
                heapq.heappush(queue,[d,new_destination])

    return distances


def solve():
    if r1 == r2 : 
        print(0)
        return
    
    r1_lst = dijkstra(r1)
    r2_lst = dijkstra(r2)

    answer = float('inf')
    for cur in range(1,N+1):
        for nxt,_ in graph[cur]:
            sum = r1_lst[cur] + r2_lst[nxt]
            if answer > sum : answer = sum

    print(answer)
        


N,r1,r2 = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))

solve()