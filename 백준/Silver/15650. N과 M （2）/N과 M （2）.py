N,M= map(int,input().split())
visited = [False for x in range(N+1)]
result = []


def DFS(start):
    if(len(result) == M):
        print(*(result))
        return
    for x in range(start,N+1):
        if(visited[x]== False):
            visited[x] = True
            result.append(x)
            DFS(x+1)

            result.pop()
            visited[x] = False


DFS(1)