# calcular iva de un producto

try:
    producto = float(
        input("ingrese el precio de su producto: "))
    iva = float(
        input("ingrese el iva que quiere aplicarle a su producto: "))

    iva_del_producto = (producto * iva) / 100
    producto_final = producto + iva_del_producto

    print("el iva es: ", round(iva_del_producto, 2))
    print("el precio final con iva es: ", round(producto_final, 2))

except ValueError:
    print("solo puedes ingresar numeros, NO LETRAS")
