from push_pop_peek import Stack

def is_match(a,b):
    if a == '[' and b == ']':
        return True
    elif a == '{' and b == '}':
        return True
    elif a == '(' and b == ')':
        return True     


def check_matching(paren_string):
    s= Stack()
    index= 0
    is_balanced = True

    while index < len(paren_string) and is_balanced:
        if paren_string[index] in ["[","{","("]:
            s.push(paren_string[index])


        elif s.is_empty():
            is_balanced= False 
            break  

        elif not is_match(s.pop(),paren_string[index]):
            is_balanced = False
            break
        index+=1 

    if not s.is_empty():
        #print(s.get_stack())
        #print('1')
        is_balanced=False    

    return is_balanced

print(check_matching("(((({}))))")) 
print(check_matching("[][]]]")  )       
