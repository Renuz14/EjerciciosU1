# Convertidor de grados celsius a farenheit
try:
    print("calculadora de grados celsius a farenheit")
    grados_celsius = float(
        input("ingrese los grados celsius que dese convertir a farenheit: "))
    grados_farenheit = (grados_celsius * 9/5) + 32
    print("su temperatura en grados farenheit es: ", grados_farenheit)

except ValueError:
    print("solo puedes ingresar numeros, NO LETRAS")
