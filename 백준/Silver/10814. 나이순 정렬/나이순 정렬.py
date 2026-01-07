import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    a.append([age, name])

a.sort(key = lambda x : x[0])

for i in range(len(a)):
    print(a[i][0], a[i][1])
