value = (365,30,1)
data=('ano(s)','mes(es)','dia(s)')
N = int(input())
resto = N

for c in range(0,3):
    print(f"{resto//value[c]} {data[c]}") 
    resto = resto % value[c]


