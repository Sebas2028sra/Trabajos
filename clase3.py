#uso de string


#dividir cadenas

# new_user = "Sebastian Rojas Araya"

# user_name = new_user.split()

# print(user_name)

# user = "Sebas, 20, M, est"
# user_1 = user.split(",")

# print(user)

# #actualizaciones de cadenas

# special = "Today's special is Pasta"

# new_special = special.replace("pasta","pizza")



# vaule = "44,000"
# fix_vaule = vaule.replace(",",".")





#casting de variables 

# print(type("Hello"))
# print(type(10.5))
# print(type(10))
# print(type(True))

# #cambiar un tipo de dato a otro(Convercion de tipos)

# age = "17"
# if int (age) < 18:
#     print("You are too young")


# position = 3
# update = "You are now number"+str (position)+"in the queue."

# print(update)


# price = 9.99
# print(int(price))


# member = True
# vaule = int(member)
# print(vaule)

#listas como list(), dict(), set() y  tuple() para la convercion de estructuras 

# choices = ["pizza", "kebab", "burger", "pizza"]
# unique = set(choices)

# print(unique)

#Funciones de codigo para hacer el codigo reutilizable y mas facil de leer y usar


#Reutilizacion de codigo con funciones

# def greet_user():
#     print("Good morning Sebastian")
#     print("welcome back")
# greet_user()

# #creacion de parametros

# def greet_ron():
#     name = "Ron"
#     print(f"Hello, {name}")

# greet_ron()


# def greet(name):
#     print(f"hello, {name} ")

# greet("Chris")
# greet("Sebas")
# greet("Freddy")


# def user_status(status):
#     user_name = "Sebas"
#     print(f"{user_name} is {status}")

# user_status("active")

# def double_number(number):
#     result = number * 2
#     print(result)

# double_number(5)

# #devolver valores con RETURN

# def age_label(age):
#     label = "user age: "+age
#     return label

# print(age_label("18"))

# def half_twice(number):
#     half = number/2
#     half_again = half / 2
#     return half_again


# result = half_twice(12)
# print(result)

# #Uso de multiples parametros

# def show_winner(first, second, third):
#     print("First place: "+first)
#     print("Second place: "+second)
#     print("Third place: "+third)

# show_winner("Sebas","Cris","Paul")

# def create_email(name, year):
#     return name, year + "@gmail.com"

# email = create_email("Sebas2028","2002")
# print(email)


# #vamos a apreneder a comprender las funciones 
# #Funciones de nomenclatura 

# def get_final_price(price, tax):
#     return price + tax
# price = get_final_price(30,1.5)
# print(price)

# #Alcance de las funciones las variables ceradas dento de una funcion tienen un alcance local

# def add_bonus(salary):
#     bonus = 100
#     bonus = 200
#     print(salary + bonus)


# add_bonus(1900)

# #Alcance global e las funciones 

# shipping = 10

# def calclate_total(cart):
#     print(cart + shipping)

# print(shipping)
# calclate_total(54)


#agregar condiciones en funciones 

# def add_shipping(cart):
#     if cart < 100:
#         print(f"total: {cart+10}")
#     else:
#         print(f"total: {cart}")

# add_shipping(45)
# add_shipping(200)

#hola

#tambien podemos anidar declaraciones (elfi)

# def calculate(operator,x,y):
#     if operator == "+":
#         print(x+y)
#     elif operator == "-":
#         print(x-y)
#     else:
#         print(f"unknown: {operator }")

# calculate ("+",40,30 )


#cualquier tipo de valor puede servir como entrada o salida de una funcion de esta manera las funciones pueden hacer uso de las listas


# def is_mltiplayer(players):
#     print(len(players)== 2)


# players = ["Freddy","Paul","Sebastian"]
# is_mltiplayer(players)


#funciones con bucles


# def onboard_passengers(bookings):
#     counter = 1
#     while counter <= bookings:
#         print(f"Passenger {counter} on board")
#         counter+= 1

# onboard_passengers(15)

# def display_progress(total_files):
#     for i in range(total_files):
#         i+= 1
#         print(f"downloading file {i} out of {total_files}")

# display_progress(20)


#la utilizacione de un bucle itera a  traves de una lista.


# def halve_price(cart):
#     for price in cart:
#         print(f"New price: {price/2}")


# cart_list = [5, 20, 8]
# halve_price(cart_list)

