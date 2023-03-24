#podemos usar una lista para almacenar  una marca de tienda pero no su sede tendriamos que usar 2 listas 

location_list = ["NY","Paris"]


#Creacion de diccionario 

locations = {
    "Sede": "NY",
    "Marca": "Paris"
}


car_data = {
    "Marca": "Nissan",
    "Anno" : "2010",
    "Restauraciones" : ["2011","2018"],
    "Rentado" : False
}

actor_bio = {
    "nombre": "Sebastian",
    "Conocido_por" : ["Todos los hombres van al cielo","todas las mujeres mientes"]

}

print(actor_bio["nombre"])
actor_name = actor_bio["nombre"]

print(actor_name)


#Ejemplo de recorrer un diccionario con un bucle

player_score = {
    "Esteban" : 13,
    "Raymond" : 20,
    "Sebastian" : 34
}


for player in player_score:
    print(player_score[player])

#Actualizar el valor de un diccionario

ticket = {
    "asiento" : 25,
    "primera clase" : False 
}

ticket["primera clase"] = True

print(ticket)



#Para agregar una clave codificamos el nombre del diccionario y luego el nombre de la clave


ticket = {
    "asiento" : 25,
    "primera clase" : False 
}

ticket["windows"] = True

print(ticket)

#comprobar que un diccionario tiene una clave

datos_personales = {
    "Nombre" : "Sebastian Rojas",
    "Telefono" : 6189023837
}

print("Nombre" in datos_personales)
name = "Nombre" in datos_personales


#eliminar una clave de un diccionario

ticket = {
    "asiento" : 25,
    "primera clase" : False, 
    "windowas" : True
}

if "windows" in ticket:
    windows =ticket.pop("windows")
    print(windows)




