from collections import *
def bfs(start_node,end,count):
    #x-1 or x+1 // 2x
    q = deque([start_node])
    check[start_node] = 0

    while q:
        t = q.popleft()
        
        if t == end:
            return check[t]
        


        if 0<=t+1<=100000 and check[t+1] == -1:
            check[t+1] = check[t] + 1
            q.append(t+1)
        
        if 0<=t-1<=100000 and check[t-1] == -1:
            check[t-1] = check[t] + 1
            q.append(t-1)
        
        if 0<=t*2<=100000 and check[t*2] == -1:
            check[t*2] = check[t] + 1
            q.append(t*2)


check = [-1] * 100001

start, end = map(int,input().split())
print(bfs(start,end,0))