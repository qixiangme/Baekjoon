N,M = map(int,input().split())

visted = [False for _ in range(N+1)]
rst = []
def DFS(start):
    if(len(rst)==M):
        print(*(rst))
        return
    for x in range(1,N+1):
        if(start <= x):
            rst.append(x)
            DFS(x)
            rst.pop()
            visted[x] == False

DFS(1)
