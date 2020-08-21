#n represents the number of queries
n=int(input())
#declaring the two stacks
old_stack = list()
new_stack = list()

for i in range(n):
    #taking the queries
    query = list(map(int,input().split()))
    #case 1
    if query[0] == 1:
        if not new_stack :            
            element = query[1]        
        new_stack.append(query[1])
    #case 2
    elif query[0] == 2:
        if not old_stack :
            while new_stack :
                old_stack.append(new_stack.pop())
        old_stack.pop()
    #case 3
    else:
        if old_stack :
            print(old_stack[-1])
        else:
            print(element)
