import sys
input = sys.stdin.readline


list = []
t = int(input())
for _ in range(t):
    n = int(input())
    list.append(n)
    
dp = [[0, 0] for _ in range(max(list)+1)]  
dp[0] = [1, 0]  
if max(list) >= 1:
    dp[1] = [0, 1]
for i in range(2,max(list)+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for t in list:
    print(str(dp[t][0]) + " " + str(dp[t][1]))