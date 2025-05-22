print("Utilize o método da bisseção para achar a raiz aproximada da função 2x² + 6x - 10")

erro = 10**-4
a = float(input("\nDigite o primeiro ponto: "))
b = float(input("Digite o segundo ponto: "))

f_a = 2 * a**2 + 6 * a - 10
f_b = 2 * b**2 + 6 * b - 10

while True:
    if f_a > 0 and f_b > 0 or f_a < 0 and f_b < 0:
        print("Não existe raiz no intervalo selecionado")
        break
    
    media = (a + b) / 2
    f_a = 2 * a**2 + 6 * a - 10
    f_b = 2 * b**2 + 6 * b - 10
    f_media = 2 * media**2 + 6 * media - 10

    if f_media * f_a < 0:
        b = media
    elif f_media * f_b < 0:
        a = media

    if b - a <= erro:
        break    
try:
    print(f"\n {a} | {b} | {f_a} | {f_b} | {media} | {f_media} \n")
    print(f"A raiz aproximada fica no ponto {media:.3f}\n")
except NameError:
    print()
