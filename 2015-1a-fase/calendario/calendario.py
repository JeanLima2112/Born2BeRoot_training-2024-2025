def quantos_dias(valor):
    quantos = abs(valor)// 4
    result = (abs(valor) * 365)+(quantos)
    print(result)
def convert_year(year):
    distance = (-3113 - year)
    quantos_dias(distance)
    
# data_inicio = "11/08/-3113"
try: 
    while True:
        day, month, year = map(int, input().split('/'))
        
        print(day, month, year)
        convert_year(year)


except EOFError:
    pass

# 2597747