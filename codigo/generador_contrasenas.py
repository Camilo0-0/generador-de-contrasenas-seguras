import random

print("Generador de contraseñas")

usar_mayus = input("¿Quieres mayúsculas? (s/n): ")
usar_minus = input("¿Quieres minúsculas? (s/n): ")
usar_numeros = input("¿Quieres números? (s/n): ")
usar_simbolos = input("¿Quieres símbolos? (s/n): ")

mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minus = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%&*()_-+=[]{};:,.<>?/"

caracteres = ""

if usar_mayus == "s":
    caracteres += mayus
if usar_minus == "s":
    caracteres += minus
if usar_numeros == "s":
    caracteres += numeros
if usar_simbolos == "s":
    caracteres += simbolos

if caracteres == "":
    print("No elegiste ningún tipo de carácter. No se puede generar contraseña.")
    exit()

longitud = int(input("¿Cuántos caracteres quieres que tenga la contraseña?: "))
contrasena = ""

for i in range(longitud):
    contrasena += random.choice(caracteres)

print("Tu contraseña es:", contrasena)

guardar = input("¿Quieres guardarla en un archivo? (s/n): ")

if guardar == "s":
    archivo = open("contrasenas.txt", "a")
    archivo.write(contrasena + "\n")
    archivo.close()
    print("Contraseña guardada en contrasenas.txt")
else:
    print("Contraseña NO guardada")
