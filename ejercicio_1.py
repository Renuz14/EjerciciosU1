# calcular el area de un rectangulo

try:
    print("calculadora de areas de rectangulos")
    base = float(
        input("inserte la base de su rectangulo: "))
    altura = float(
        input("inserte la altura de su rectangulo: "))
    area = base * altura
    print("la area de su rectangulo es: ", area)

except ValueError:
    print("solo puedes ingresar numeros, NO LETRAS")
