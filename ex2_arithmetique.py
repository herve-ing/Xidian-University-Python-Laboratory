"""
Exercice 1.2 : Opérations arithmétiques simples et utilisation du module math.
"""
import math

a, b = 17, 5

# Opérations de base
print("=== Opérations de base ===")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")       # division réelle
print(f"{a} // {b} = {a // b}")     # division entière
print(f"{a} % {b} = {a % b}")       # modulo
print(f"{a} ** {b} = {a ** b}")     # puissance

# Fonctions du module math
print("\n=== Module math ===")
print(f"sqrt({a}) = {math.sqrt(a):.4f}")
print(f"pow({a}, {b}) = {math.pow(a, b)}")
print(f"factorielle({b}) = {math.factorial(b)}")
print(f"log({a}) = {math.log(a):.4f}")
print(f"sin(pi/2) = {math.sin(math.pi / 2)}")
print(f"pi = {math.pi}, e = {math.e}")
