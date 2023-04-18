import math

# Coeficientes da equação

a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C:"))

# Cálculo do discriminante

delta = b**2 - 4*a*c

# Verifica se a equação tem raízes reais

if(delta < 0):
    print("A equação não tem raízes reais.")
elif delta == 0:
    # Uma única raiz real
    x = -b / (2*a)
    print(f"A equação tem uma única raiz real: x = {x}")
else:
    #Duas raízes reais
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

print(f"A equação tem duas raízes reais: x1 = {x1}, x2 = {x2}")