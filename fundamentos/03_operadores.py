# Operadores en Python

my_age = 33
my_height = 1.75
num_complex = 3j

# Calcular área del triangulo
print("############ ÁREA DEL TRIANGULO ##############\n")
base = int(input("Ingrese la base del triangulo: "))
height = int(input("Ingrese la altura del triangulo: "))

area_triangle = (base * height) / 2

print("\nEl área del triangulo es", area_triangle)


# Perímetro del triangulo
print("\n\n############ ÁREA DEL TRIANGULO ##############\n")
side_a = int(input("Ingrese el lado a del triangulo: "))
side_b = int(input("Ingrese el lado b del triangulo: "))
side_c = int(input("Ingrese el lado c del triangulo: "))

perimeter_triangle = sum([side_a, side_b, side_c])

print("\nEl perimetro del triangulo es", perimeter_triangle)


# Perímetro y área del rectangulo
print("\n\n############ PERIMETRO Y ÁREA DEL RECTANGULO ##############\n")
length = int(input("Ingrese el largo del rectangulo: "))
width = int(input("Ingrese el ancho del rectangulo: "))

perimeter_rectangle = length * 2 + width * 2
area_rectangle = length * width

print("\nEl perimetro del rectangulo es", perimeter_rectangle)
print("\nEl área del rectangulo es", area_rectangle)


# Circunferencia y área del circulo
print("\n\n############ CIRCUNFERENCIA Y ÁREA DEL CIRCULO ##############\n")
radius = float(input("Ingrese el radio del circulo: "))
pi = 3.1416

circunference = 2 * pi * radius
circle_area = pi * radius ** 2

print("\nLa circunferencia del circulo es", circunference)
print("\nEl área del circulo es", circle_area)


# Comparación de variables
name_a = 'python'
name_b = 'dragon'

print('python > dragon', len(name_a) > len(name_b))

print('\nOn in python y dragon =>', 'on' in name_a and 'on' in name_b)

sentence = 'I hope this course is not full of jargon'
word = 'jargon'

print('\nPalabra en Frase =>', word in sentence)

print('\nNo on en python y dragon =>', not 'on' in name_a and not 'on' in name_b)

len_text = len('python')
len_text_float = float(len_text)
len_text_str = str(len_text)

print('\nValidación matemática =>', int(7 / 3) == int(2.7))

print('\nValidación de tipos =>', type('10') == type(10))

print('\nValidación de número =>', int(float('9.8')) == 10)

hours = float(input('Ingrese sus horas trabajadas: '))
rate_per_hour = float(input('Cual es su tarifa por hora: '))

total_to_pay = hours * rate_per_hour

print('\nSe le debe pagar $', total_to_pay)

years = int(input('\nIngresa el número de años: '))

seconds = 3600 * 24 * 365 * years

print('\nEl número de segundos transcurrido es: ', seconds)

print(' 1 1 1 1 1\n', '2 1 2 4 8\n', '3 1 3 9 27\n', '4 1 4 16 64\n', '5 1 5 25 125')
