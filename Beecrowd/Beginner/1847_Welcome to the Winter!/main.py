A, B, C = map(int, input().split())

print(":)" if C > B and (A <= B or C - B >= B - A) or C < B and A > B and C - B > B - A or A == B else ":(")
