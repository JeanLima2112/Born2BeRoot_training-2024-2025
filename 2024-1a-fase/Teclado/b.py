pattern = {
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "Q", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y", "Z"]
}
for _ in range(int(input())):
    X = input()
    for i in X:
        for key, value in pattern.items():
            if i in value:
                print(key, end="")
    print()
    
