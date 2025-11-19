contraseña = []


for grupo in grupos:
contraseña.append(random.choice(grupo))


todos = "".join(grupos)
resto = longitud - len(contraseña)
for _ in range(resto):
contraseña.append(random.choice(todos))


random.shuffle(contraseña)


return ''.join(contraseña)




def guardar_contrasena(contrasena: str, nombre_archivo: str = 'contraseñas.txt') -> None:
"""Guarda la contraseña en un archivo (modo append).
Nota: Este almacenamiento es **texto plano**. Para uso real en producción,
considere cifrar el archivo o usar un gestor de contraseñas.
"""
try:
with open(nombre_archivo, 'a', encoding='utf-8') as f:
timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
f.write(f"{timestamp} - {contrasena}\n")
except Exception as e:
print(f"Error al guardar la contraseña: {e}")




def leer_entero(prompt: str) -> int:
while True:
try:
valor = int(input(prompt))
return valor
except ValueError:
print("Por favor ingresa un número entero válido.")




def menu_interactivo():
print("Bienvenido al generador de contraseñas seguras")


while True:
print('\nOpciones:')
print('1) Generar contraseña')
print('2) Salir')
opcion = input('Selecciona una opción (1-2): ').strip()


if opcion == '1':
longitud = leer_entero('¿Cuántos caracteres quieres que tenga la contraseña?: ')


usar_mayus = input('Incluir mayúsculas? (S/n): ').strip().lower() != 'n'
usar_minus = input('Incluir minúsculas? (S/n): ').strip().lower() != 'n'
usar_numeros = input('Incluir números? (S/n): ').strip().lower() != 'n'
usar_simbolos = input('Incluir símbolos? (S/n): ').strip().lower() != 'n'


try:
contrasena = generar_contrasena(longitud, usar_mayus, usar_minus, usar_numeros, usar_simbolos)
except ValueError as e:
print(f"Error: {e}")
continue


print('\nContraseña generada:')
print(contrasena)


guardar = input('¿Deseas guardar la contraseña en un archivo?
