def trapezio(n, base, x1):
    area = 0
    for i in range(n):
        partes = ((((2 * (x1 + (i * base))) + ((x1 + (i * base)) ** 2)) + ((2 * (x1 + ((i + 1) * base))) + ((x1 + ((i + 1) * base)) ** 2))) * base) / 2
        area += partes
    return area

print("Utilize o método do trapézio para achar a área aproximada da função 2x + x² no intervalo escolhido")

x1 = int(input("\nQual o primeiro valor do intervalo? "))
x2 = int(input("E o último? "))
n = int(input("Quantos trapézios você quer utilizar? "))

base = (x2 - x1) / n

area = trapezio(n, base, x1)

print(f"\nA área aproximada da função no intervalo de {x1} até {x2} é {area:.2f}\n")
