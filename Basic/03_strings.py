### Strings ###

my_string = "Mi strings"
my_other_string = 'Mi otro strings'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\tEste es un String con\nescapado"
print(my_scape_string)


### Formateo ###

name , surname , age = "Harold" , "Sabogal" , 18

print("Mi nombre es {} {} y mi edad es {}".format(name , surname , age))
print("Mi nombre es %s %s y mi edad es %d" %(name , surname , age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


### Desempaquetado de caracteres ###

language = "python" 
a , b , c , d , e , f= language
print(b)
print(d)
print(f)

### Division ###

language_slices = language[1:4]
print(language_slices)

language_slices = language[1:]
print(language_slices)

language_slices = language[-2]
print(language_slices)

language_slices = language[0:6:2]
print(language_slices)

### Reverse ####

reversed_language = language[::-1]
print(reversed_language)

### Metodos ###

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("2".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith("py"))
print(language.startswith("th"))