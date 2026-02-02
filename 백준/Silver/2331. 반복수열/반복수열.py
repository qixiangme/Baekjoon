import sys

a, p = map(int, sys.stdin.readline().split())
seq = [a] 
link = [0]*250000
link[a] = 1

while True:
    t = seq[-1]
    val = 0
    while t:
        val += ((t%10) ** p)
        t //= 10

    if not link[val]:
        seq.append(val)
        link[val] = 1
    else:
        seq = seq[:seq.index(val)]
        break

sys.stdout.write(str(len(seq)))
