def readInt():
    wrong = True
    value = 0
    while(wrong):
        try:
            value = int(input())
            if value < 0:
                print("No se admiten valores negativos")
            else:
                wrong = False
        except Exception:
            print("Valor incorrecto")
    return value

def simplexPrint(n: int, m: int, res: list, beneficio: list):
    print("Z =", end=" ")
    for i in range(1, n+1):
        print(f"{beneficio[i-1]}x_{i} ", end=" ")
    print()
    for i in range(1, m+1):
        for j in range(1,n+1):
            print(f"{res[i-1][j-1]}x_{j}", end=" ")
        print(f"< {res[i-1][-1]}")

print("Numero de variables (n > 0)")
n = readInt()
m = int(input("Numero de reestricciones (m > 0)"))
res = []
beneficio = input("Funcion objetivo").split(",")


for i in range(1, m+1):
    print("Formato restricciones: x_1, x_2, b")
    res.append(input(f"Introduce la restriccion {i}").split(","))

simplexPrint(n, m, res, beneficio)

