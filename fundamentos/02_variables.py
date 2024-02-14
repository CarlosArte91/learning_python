""" Variable en Python """

first_name = "Carlos"
last_name = "Cruz"
full_name = "Arturo Gutierrez"
country = "Colombia"
city = "Bogotá"
age = 33
year = "2024"
is_married = False
is_true = True
is_light_on = True
amount = 253.65
is_active = True
languajes = ["Python", "Java", "JavaScript", "Rust"]

person_info = {
  "first_name": first_name,
  "last_name": last_name,
  "age": age,
  "country": "Colombia",
}

# Imprimiendo valores

print("\nvariable first_name: ", first_name)
print("Tipo de dato:", type(first_name))
print("Longitud de la variable:", len(first_name), "\n")

print("\nvariable age: ", age)
print("Tipo de dato:", type(age), "\n")

print("\nvariable amount: ", amount)
print("Tipo de dato:", type(amount), "\n")

print("\nvariable is_active: ", is_active)
print("Tipo de dato:", type(is_active), "\n")

print("\nvariable languajes: ", languajes)
print("Tipo de dato:", type(languajes), "\n")

print("\nvariable person_info: ", person_info)
print("Tipo de dato:", type(person_info), "\n\n")

print("Comparar longitud", len(first_name) == len(last_name), "\n\n")

user_name = input("What is your name? ")
user_age = input("How old are you? ")

print("Your name is", user_name)
print("You are", user_age, "years old\n\n")


""" Casteo de variables """
# De entero a flotante
num_int = 15
print("num_int", num_int, "\n")

num_float = float(num_int)
print("num_float", num_float, "\n\n")

# De flotante a entero
gravity = 9.1
print("gravity int", int(gravity), "\n\n")

# De entero a string
num_int = 12
print("num_int", num_int, "\n")
print("num_str", str(num_int), "\n\n")

# De string a entero y a flotante
num_str = '25'
print("int_str", int(num_str), "\n")
print("float_str", float(num_str), "\n\n")

# De string a lista
my_string = 'Aprendiendo python'
print("my_string", my_string, "\n")
print("my_string_list", list(my_string), "\n\n")

# Calcular medidas del circulo
radius = float(input("Ingresa el radio del circulo: "))
pi = 3.1416

# Calcular area
area_of_circle = pi * radius ** 2

# Calcular la circunferencia
circum_of_circle = 2 * pi * radius

print("\nEl area del circulo es", area_of_circle)
print("La circunferencia es", circum_of_circle)
