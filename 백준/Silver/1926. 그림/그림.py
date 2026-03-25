n, m = map(int, input().split())  # n: 행 개수, m: 열 개수
a4 = []  # 2차원 리스트를 저장할 변수
for i in range(n):
    row = list(map(int, input().split()))  # 한 줄을 숫자로 변환하여 리스트로 저장
    a4.append(row)  # 리스트를 추가
chk = [[False]*m for _ in range(n)]
dy=[0,1,0,-1]
dx=[1,0,-1,0]
cnt = 0
maxv = 0
def BFS(y,x):
    size = 1
    q= [(y,x)]
    while(q):
        ey,ex = q.pop(0)
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if(0<=ny<n and 0 <= nx <m ):
                if(a4[ny][nx] == 1 and chk[ny][nx] == False):
                    q.append((ny,nx))
                    chk[ny][nx] = True
                    size +=1
    return size

for j in range(n):
    for i in range(m):
        if a4[j][i] == 1 and chk[j][i] == False:
            chk[j][i] =True
            cnt = cnt +1
            maxv = max(maxv,BFS(j,i))

print(cnt)
print(maxv)
