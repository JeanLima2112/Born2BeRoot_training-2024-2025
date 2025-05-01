patern = {"A":"T","C":"G", "T":"A","G":"C"}

try:

    while True:
        X = input()
        max_size = 0
        start_position= 0
        for i in range(len(X)):
            left = i
            right = i+1
            while  left >= 0 and right < len(X) and patern[X[left]] == X[right]:
                if right - left > max_size:
                    max_size = right- left
                    start_position = left
                left -=1
                right+=1
        if max_size > 1 :
            print(f"{start_position+1} {max_size+1}")
        else:
            print("false")
except EOFError:
    pass
            
