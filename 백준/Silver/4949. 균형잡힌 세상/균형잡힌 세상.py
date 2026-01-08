import sys
while True:
    sen = sys.stdin.readline().rstrip()
    flag = 0
    stack = []
    if sen == '.':
        break
    for i in sen:
        if i == "(" or i == "[": 
            stack.append(i)
        elif i == ")": 
            if not stack or stack[-1] == "[": 
                print("no")
                flag = 1
                break
            else:
                stack.pop()
        elif i == "]": 
            if not stack or stack[-1] == "(": 
                print("no")
                flag = 1
                break
            else:
                stack.pop()
    if flag == 0:   
        if not stack :  
            print("yes")
        else:
            print("no")