def BFS(y,x):
    size=1
    q = [(y,x)]
    chk[y][x] = True
    while(q):
        ey,ex = q.pop(0)
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if (0<=ny<n and 0<=nx<n):
                if(maap[ny][nx] == 1 and chk[ny][nx]== False):
                    size=size+1
                    q.append((ny,nx))
                    chk[ny][nx] = True
    return size
        
n = int(input())
cnt = 0
rsList = []
maap = [list(map(int,input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)] 
dy = [0,1,0,-1]
dx = [1,0,-1,0]
for y in range(n):
    for x in range(n):
        if(maap[y][x] == 1 and chk[y][x] == False):
            cnt = cnt+1
            rsList.append(BFS(y,x))
print(cnt)
rsList.sort()
for k in rsList:
    print(k)