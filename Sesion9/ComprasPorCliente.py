## Actividad: Compras por Cliente
# - Crear un programa que permita al usuario ingresar los montos de las 
#       compras de un cliente (se desconoce la cantidad de datos que se cargarán, 
#       que pueden cambiar en cada ejecución), cortando el ingreso de datos cuando
#        el usuario ingresa el monto 0.
# - Si ingresa una cantidad negativa, no debe procesarse y se le debe solicitar 
#       que ingrese una nueva cantidad. Al finalizar, informar el total a pagar 
#       teniendo en cuenta que, si las ventas superan el total de $1000, se debe 
#       aplicar un 10% de descuento.

print("Calculadora de monto total a pagar. Ingrese el monto de cada artículo y presione 'Enter'.\nAl finalizar ingresar 0.")

# Se inicializa condicional de bucle
montoArticulo=float(input("Monto de artículo 1: "))
subTotal=0
articulo=1
while montoArticulo!=0:
    articulo+=1
    if montoArticulo<0:
        print("No se permite el ingreso de montos negativos, intente nuevamente:")
        articulo-=1
    else:
        subTotal+=montoArticulo
    montoArticulo=float(input("Monto de artículo "+str(articulo)+": "))

if subTotal>1000:
    descuento=0.1*subTotal
    total=subTotal-descuento
    print("El costo total de los artículos es $",subTotal)
    print("Se aplicó un descuento de: $",descuento)
    print("El monto total a pagar es $",total)
else:
    total=subTotal
    print("El monto total a pagar es $",total)
