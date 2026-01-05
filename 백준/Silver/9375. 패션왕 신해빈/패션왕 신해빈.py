t = int(input())

for i in range(t):
    n = int(input())
    dict = {}
    for j in range(n):
        wear = list(input().split())
        if wear[1] in dict:
            dict[wear[1]].append(wear[0])
        else:
            dict[wear[1]] = [wear[0]]

    cnt = 1 

    for k in dict:
        cnt *= (len(dict[k])+1)
    print(cnt-1)