# Esta es una pequeña aplicación que verifica si un rut ingresado es válido o no.
# El rut a verificar se puede ingresar con puntos o sin puntos, con guión o sin guión.

from math import ceil

print('Bienvenido al verificador de RUT')

while True:
    rut = list(input('\nIngrese el rut que desea validar: '))
    listaVerificadora = [2,3,4,5,6,7,2,3]

    digitoVerificador = rut[-1]
    digitoVerificadorMayuscula = digitoVerificador.upper()


    # Aquí se obtendrán los números ingresados dentro del rut, excluyendo los puntos y el guión.
    numerosRut = []
    for numero in rut:
        if numero != '.' and numero != '-':
            numerosRut.append(numero)
    numerosRut.pop()

    # La siguiente condición asegura que el rut ingresado tenga más de 7 dígitos.
    if len(numerosRut) > 7:

        # Se realiza la converción de los números ingresados a Int y se invierte el orden para multiplicar
        # los elementos de las listas y obtener el valor para comparar el dígito verificador.
        cuerpoInt = list(map(int, numerosRut))
        cuerpoIntInvertido = list(reversed(cuerpoInt))
        multiplicacion = list(map(lambda x, y: x*y, cuerpoIntInvertido, listaVerificadora))

        resultado = str(11 - ceil(sum(multiplicacion)%11))


        # FIXME: Espagueti de confirmaciones, funciona, pero seguramente hay mejores maneras de hacer
        #        estas confirmaciones...

        if resultado == '10':
            resultado = 'K'
            if resultado == digitoVerificadorMayuscula:
                print('El rut ingresado es válido')
            else:
                print('El rut ingresado no es válido')

        if resultado == '11':
            resultado = '0'
            if resultado == digitoVerificador:
                print('El rut ingresado es válido')
            else:
                print('El rut ingresado no es válido')

        if resultado != '0' and resultado != 'K' and resultado != '10' and resultado != '11':
            if resultado == digitoVerificador:
                print('El rut ingresado es válido')
            else:
                print('El rut ingresado no es válido')
    else:
        print('El rut ingresado no es válido')
