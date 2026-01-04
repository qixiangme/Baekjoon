from sys import stdin

coin = []
count = 0


N, M = map(int,stdin.readline().split())

for i in range(N): 
    coin.append(int(stdin.readline()))

coin.sort(reverse=True) # 내림차순 정렬

#-- 수행 --#
for value in coin:
    count = count + (M//value) 
    M = M % value # 쓰고 남은 돈 
    if(M <=0):
        break

print(count)