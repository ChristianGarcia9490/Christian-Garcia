def convertir_a_binario(numero):
    if numero <= 1:
        return str(numero)
    else:
        return convertir_a_binario(numero // 2) + str(numero % 2)

def contar_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)

def calcular_raiz_cuadrada(numero, estimacion=1):
    if abs(estimacion ** 2 - numero) < 0.1:
        return int(estimacion)
    else:
        return calcular_raiz_cuadrada(numero, (estimacion + numero / estimacion) / 2)

def raiz_cuadrada_entera(numero):
    return calcular_raiz_cuadrada(numero)

def convertir_a_decimal(numero_romano):
    romano_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(numero_romano) == 1:
        return romano_decimal[numero_romano]
    else:
        if romano_decimal[numero_romano[0]] < romano_decimal[numero_romano[1]]:
            return -romano_decimal[numero_romano[0]] + convertir_a_decimal(numero_romano[1:])
        else:
            return romano_decimal[numero_romano[0]] + convertir_a_decimal(numero_romano[1:])

def suma_numeros_enteros(numero):
    if numero == 0:
        return 0
    else:
        return numero + suma_numeros_enteros(numero - 1)

def menu():
    print("1. Convertir a binario")
    print("2. Contar dígitos")
    print("3. Raíz cuadrada entera")
    print("4. Convertir a decimal desde romano")
    print("5. Suma de números enteros")
    print("6. Salir")

def main():
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            numero = int(input("Ingresa un número entero: "))
            print("El número binario es:", convertir_a_binario(numero))
        elif opcion == '2':
            numero = int(input("Ingresa un número entero: "))
            print("La cantidad de dígitos es:", contar_digitos(numero))
        elif opcion == '3':
            numero = int(input("Ingresa un número entero: "))
            print("La raíz cuadrada entera es:", raiz_cuadrada_entera(numero))
        elif opcion == '4':
            numero_romano = input("Ingresa un número romano: ")
            print("El número decimal equivalente es:", convertir_a_decimal(numero_romano))
        elif opcion == '5':
            numero = int(input("Ingresa un número entero positivo: "))
            print("La suma de los números enteros hasta", numero, "es:", suma_numeros_enteros(numero))
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
