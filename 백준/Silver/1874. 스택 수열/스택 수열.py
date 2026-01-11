n = int(input())

count = 1
stack = []
result = []
fail = False

for i in range(1, n + 1):
    data = int(input())
    
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
        
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        fail = True

if fail:
    print('NO')
else: 
    print('\n'.join(result))