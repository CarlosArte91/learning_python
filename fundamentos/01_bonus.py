# Funciones integradas de Python

""" Estas son algunas de las funciones integradas
que tiene el lenguaje de programación Python, las
cuales no requieren ser importadas ni declaradas,
es decir, están listas para su uso."""

# Función abs() para hallar el valor absoluto de un número.
print(abs(-15))
print(abs(-7))

# Función all() devuelve True si todos los elementos de un iterable
# se evaluan como verdadero o si el iterable está vacío.
print("[True, True, False] ==========>", all([True, True, False]))
print("[True, True, True] ===========>", all([True, True, True]))
print("[1, 2, 3] ====================>", all([1, 2, 3]))
print("[1, 2, 3] ====================>", all([1, 2, 0]))
print("['python', 'java', ''] =======>", all(["python", "java", ""]))
print("['python', 'java', 'rust'] ===>", all(["python", "java", "rust"]))
print("[] ===========================>", all([]))

# Función any() devuelve True si almenos uno de los elementos de un
# iterable se evalua como True, si está vacío, devuelve False.
print("\n\n[] =======================>", any([]))
print("[False, False, True] =====>", any([False, False, True]))
print("[0, '', 1] ===============>", any([0, '', 1]))
print("[False, False] ===========>", any([False, False]))
