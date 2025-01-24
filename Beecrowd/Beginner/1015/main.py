def distance(x1,x2,y1,y2):
    value = (((x2 - x1)**2) + ((y2-y1)**2))**0.5
    return value
X1, Y1 = map(float, input().split())
X2, Y2 = map(float, input().split())

print(f"{distance(X1,X2,Y1,Y2):.4f}")