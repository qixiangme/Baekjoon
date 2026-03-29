from collections import *

N,M,V = map(int,input().split())

dict = defaultdict(list)
for x in range(M):
    a,b = map(int,input().split())
    dict[a].append(b)
    dict[b].append(a)

#DFS -> 재귀
visitedDFS = [False for x in range(N+1)]
dfs_result =[]
def DFS(start):
    visitedDFS[start]= True
    dfs_result.append(start)
    for x in sorted(dict[start]):
        if not visitedDFS[x]:
            DFS(x)
        

#BFS -> while
visitedBFS = [False for x in range (N+1)]
def BFS(start):
    q = deque()
    q.append(start)
    visitedBFS[start] = True
    result = []

    while q:
        t = q.popleft()
        result.append(t)


        for x in sorted(dict[t]):
            if(visitedBFS[x]==False):
                q.append(x)
                visitedBFS[x] = True

    return result

DFS(V)

print(*(dfs_result))
print(*(BFS(V)))