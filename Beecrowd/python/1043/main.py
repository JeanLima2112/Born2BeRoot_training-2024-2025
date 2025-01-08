A,B,C= map(float, input().split())

if C < A + B and A < C + B and B < C + A:
    print(f"Perimetro = {A + B +C}")
  
else:print(f"Area = {((A + B) * C) /2  }")