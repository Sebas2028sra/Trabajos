# movies = ["Vertigo", "Chucky", 1958, 2019]

# #Las tuplas son agrupar datos relacionados

# movies_tupla = ("Vertigo", 1958),("Chucky",2019)

# print(movies_tupla)


#podemos almacenar tuplas en una lista

# movies_tupla1 = [("Vertigo", 1958),("Chucky",2019),("Cars", 2006)]
# favorite = movies_tupla1[2]
# print(favorite)

# #las tuplas son utiles porque nos permiten devolver multiples valores de una funcion


# def get_score_datos(score_list):
#     highest_score = max(score_list)
#     lowest_score = min(score_list)
#     return highest_score, lowest_score

# scores = [31, 17, 80]
# data = get_score_datos(scores)
# print(data)

# highest = data[0]
# smallest = data[1]

# print(f"Samllest score: {smallest}")
# print(f"Highest score: {highest}")


# #ordenamiento de datos

# def get_score_datos(score_list):
#     orden_menor_mayor = sorted(score_list)
#     orden_mayor_menor = sorted(score_list, reverse=True )
#     return orden_menor_mayor#,orden_mayor_menor

# scores = [31, 17, 80]
# data = get_score_datos(scores)
# print(data)
# first = data[0]
# second = data[1]
# third = data[2]


# print(f"First: {first}")
# print(f"Second: {second}")
# print(f"third: {third}")


