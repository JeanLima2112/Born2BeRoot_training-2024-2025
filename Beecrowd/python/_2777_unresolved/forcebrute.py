enters = {}
try:
    index = 0
    while True:
        N = int(input())
        enters[index] = N
        index += 1
except EOFError:
    pass

sorted_enters = {k: v for k, v in sorted(enters.items(), key=lambda item: item[1])}

c, b, a = 1, 2, 2
last_calculated = 3
new_value = 0

for key, value in sorted_enters.items():
    if value == 1: 
        sorted_enters[key] = 1
    elif value == 2: 
        sorted_enters[key] = 2
    elif value == 3: 
        sorted_enters[key] = 2
    else:
        while last_calculated + 1 <= value:  
            new_value = (b + c) % (10**9 + 7)
            c, b, a = b, a, new_value
            last_calculated += 1
        sorted_enters[key] = new_value  

sorted_enters = {k: v for k, v in sorted(sorted_enters.items())}

for key, value in sorted_enters.items():
    print(value)
