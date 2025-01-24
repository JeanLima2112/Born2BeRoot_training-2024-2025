from collections import deque

try:
    while True:
        line = input()  
        result = deque()
        current = []
        at_home = False
        
        for char in line:
            if char == '[': 
                if at_home:
                    result.appendleft(''.join(current))
                else:
                    result.append(''.join(current))
                current = []
                at_home = True
            elif char == ']':  
                if at_home:
                    result.appendleft(''.join(current))
                else:
                    result.append(''.join(current))
                current = []
                at_home = False
            else:
                current.append(char)
        
        if at_home:
            result.appendleft(''.join(current))
        else:
            result.append(''.join(current))
        
        print(''.join(result))
except EOFError:
    pass
