N = int(input())
casas = N **2
if N % 2 == 0:
    print(f"{casas/2:.0f} casas brancas e {casas/2:.0f} casas pretas")
else:
    print(f"{(casas// 2) + 1:.0f} casas brancas e {casas // 2:.0f} casas pretas")
