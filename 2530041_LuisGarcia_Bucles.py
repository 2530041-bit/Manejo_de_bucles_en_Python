# PORTADA

# Nombre: Luis Garcia
# Matrícula: 2530041
# Grupo: 1-3


# RESUMEN EJECUTIVO
"""
    Este documento muestra el uso de bucles for y while en Python.
    Un bucle for se utiliza cuando conocemos la cantidad de iteraciones.
    Un bucle while se usa cuando no conocemos cuántas iteraciones se necesitarán.
    Se usan contadores y acumuladores para contar o sumar valores dentro de los bucles.
    Se emplean sentinelas para terminar la lectura de datos de manera controlada.
    La tarea cubre sumas, tablas de multiplicar, promedios con sentinelas, intentos de contraseña, menús y patrones de asteriscos.
    Se validan entradas y se evita la creación de ciclos infinitos mediante condiciones claras de salida.
"""

# PRINCIPIOS Y BUENAS PRÁCTICAS
"""
    Usar for cuando se conoce la cantidad de iteraciones.
    Usar while cuando depende de una condición.
    Inicializar contadores y acumuladores antes de los bucles.
    Actualizar variables de control para evitar ciclos infinitos.
    Mantener los bucles simples, extrayendo lógica compleja en funciones si es necesario.
"""
# PROBLEMAS


# PROBLEMA 1: Sum of range with for
# Descripción: Calcula la suma de todos los números enteros desde 1 hasta n 
# y la suma de los números pares dentro del mismo rango usando un bucle for.

# Entradas: n (int)
# Salidas: "Sum 1..n:" total_sum, "Even sum 1..n:" even_sum
# Validaciones: n >=1
# Casos de prueba:
# 1) Normal: n=5 -> sum=15, even_sum=6
# 2) Borde: n=1 -> sum=1, even_sum=0
# 3) Error: n=0

try:
    n = int(input("Enter n: "))
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0
        for i in range(1, n+1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i
        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
except ValueError:
    print("Error: invalid input")


# PROBLEMA 2: Multiplication table with for
# Descripción: Genera e imprime la tabla de multiplicar de un número base 
# desde 1 hasta un límite m.

# Entradas: base, m
# Salidas: cada línea de la tabla
# Validaciones: m >=1
# Casos de prueba:
# 1) Normal: base=3, m=4
# 2) Borde: base=1, m=1
# 3) Error: m=0

try:
    base = int(input("Enter base: "))
    m = int(input("Enter limit m: "))
    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m+1):
            print(f"{base} x {i} = {base*i}")
except ValueError:
    print("Error: invalid input")


# PROBLEMA 3: Average of numbers with while and sentinel
# Descripción: Lee números repetidamente hasta que el usuario ingrese un valor sentinela (-1).
# Calcula el promedio y la cantidad de números válidos ingresados.

# Entradas: número (float)
# Salidas: Count, Average o Error
# Sentinela: -1
# Casos de prueba:
# 1) Normal: 2,4,6,-1 -> count=3, average=4
# 2) Borde: -1 -> Error
# 3) Error: input inválido

sentinel_value = -1
count = 0
total = 0.0
while True:
    user_input = input("Enter number (-1 to stop): ")
    try:
        number = float(user_input)
        if number == sentinel_value:
            break
        total += number
        count += 1
    except ValueError:
        print("Error: invalid input")
if count == 0:
    print("Error: no data")
else:
    average_value = total / count
    print("Count:", count)
    print("Average:", average_value)


# PROBLEMA 4: Password attempts with while
# Descripción: Sistema de intentos de contraseña. Permite un máximo de MAX_ATTEMPTS 
# intentos para ingresar la contraseña correcta.

# Entradas: user_password
# Salidas: Login success o Account locked
# MAX_ATTEMPTS = 3
# Casos de prueba:
# 1) Normal: contraseña correcta en primer intento
# 2) Borde: contraseña correcta en último intento
# 3) Error: falla todos los intentos

MAX_ATTEMPTS = 3
correct_password = "admin123"
attempts = 0
while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ")
    if user_password == correct_password:
        print("Login success")
        break
    attempts += 1
else:
    print("Account locked")


# PROBLEMA 5: Simple menu with while
# Descripción: Menú de opciones que se repite hasta que el usuario elige salir (0).
# Permite mostrar un saludo, ver el valor del contador e incrementarlo.

# Entradas: option
# Salidas: mensajes según opción
# Casos de prueba:
# 1) Normal: elegir 1,2,3,0
# 2) Borde: elegir 0 inmediatamente
# 3) Error: opción inválida como 5

counter = 0
option = None
while option != 0:
    print("Menu:")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")
    try:
        option = int(input("Option: "))
        if option == 1:
            print("Hello!")
        elif option == 2:
            print("Counter:", counter)
        elif option == 3:
            counter += 1
            print("Counter incremented")
        elif option == 0:
            print("Bye!")
        else:
            print("Error: invalid option")
    except ValueError:
        print("Error: invalid option")


# PROBLEMA 6: Pattern printing with nested loops
# Descripción: Imprime un patrón de triángulo rectángulo de asteriscos.
# Se puede agregar opcionalmente un patrón invertido.

# Entradas: n filas
# Salidas: patrón línea por línea
# Casos de prueba:
# 1) Normal: n=4
# 2) Borde: n=1
# 3) Error: n=0

try:
    n = int(input("Enter number of rows: "))
    if n < 1:
        print("Error: invalid input")
    else:
        for i in range(1, n+1):
            print("*" * i)
        # Patrón invertido opcional
        for i in range(n, 0, -1):
            print("*" * i)
except ValueError:
    print("Error: invalid input")


# CONCLUSIONES
"""
    For se usa cuando conocemos la cantidad de iteraciones; while cuando depende de una condición.
    Los contadores y acumuladores permiten sumar o contar elementos dentro de los bucles.
    Los while requieren atención para evitar ciclos infinitos.
    Menús y sistemas de contraseña son ejemplos típicos de uso de while.
    Los bucles anidados permiten generar patrones y estructuras más complejas.
    Aprendimos a combinar validaciones, sentinelas y control de flujo en distintos problemas.
"""

# REFERENCIAS

# 1) Python documentation - for and while loops
# 2) Python official tutorial - Control Flow Tools
# 3) W3Schools Python Loops
# 4) GeeksforGeeks - Python Loops
# 5) Real Python - For and While Loops
# 6) Apuntes en clase