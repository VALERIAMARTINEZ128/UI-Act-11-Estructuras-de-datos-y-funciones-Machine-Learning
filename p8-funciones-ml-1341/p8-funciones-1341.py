# ==========================================================
# valeria yaretzi NC = 1341
# FUNCIONES EN PYTHON
# Número de lista: 36
# Ejemplos basados en Pythones
# ==========================================================


# ==========================================================
# EJEMPLO 1 - FUNCIÓN SIN PARÁMETROS
# ==========================================================

def saludo():
    print("Hola, soy estudiante de Inteligencia Artificial")


saludo()


# ==========================================================
# EJEMPLO 2 - FUNCIÓN CON PARÁMETROS
# ==========================================================

def saludar_persona(nombre):
    print("Hola", nombre)


saludar_persona("Valeria")


# ==========================================================
# EJEMPLO 3 - FUNCIÓN CON DOS PARÁMETROS Y RETURN
# ==========================================================

def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado


resultado_suma = sumar(10, 20)

print("Ejemplo 3")
print("Resultado de la suma:", resultado_suma)


# ==========================================================
# EJEMPLO 4 - FUNCIÓN PARA CALCULAR ÁREA
# ==========================================================

def calcular_area(base, altura):
    area = base * altura
    return area


base = 8
altura = 5

area = calcular_area(base, altura)

print("Ejemplo 4")
print("Base:", base)
print("Altura:", altura)
print("Área del rectángulo:", area)


# ==========================================================
# EJEMPLO 5 - CALCULADORA CON FUNCIONES
# ==========================================================

def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


numero1 = 20
numero2 = 5

print("Ejemplo 5 - Calculadora")

print("Suma:", suma(numero1, numero2))
print("Resta:", resta(numero1, numero2))
print("Multiplicación:", multiplicacion(numero1, numero2))
print("División:", division(numero1, numero2))
print("valeria yaretzi NC = 1341")