# promedio de calificaciones
try:
    print("caluladora de promedios de calificaciones")
    matematicas = float(
        input("ingrese su calificacion de matematicas:"))
    programacion = float(
        input("ingrese su calificacion de programacion: "))
    ingles = float(
        input("ingrese su calificacion de ingles: "))

    promedio_final = (programacion + ingles + matematicas) / 3

    if (
            promedio_final > 7):
        print("has aprobado")
    else:
        print("has reprobado")

    print("tu promedio final es: ", round(promedio_final, 1))

except ValueError:
    print("solo puedes ingresar numeros, NO LETRAS")
