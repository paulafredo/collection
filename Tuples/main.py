# COLLECTION 
# Tuple  ():  immutable (non modifiable )
# liste [] : mutable -> modifiable : rajout / suprimer des élement ou modifier 


# a = 5 
# b = "Toto"

# personnes = ("Melanie ", "Jean ", "Martin ", "Alice "  ) 
# print(personnes)
# print(len(personnes))
# for i in range(0 , len(personnes)):
#     print(personnes[i])
   

# for i in personnes:
#     print(i)
#     print(len(i))
#     print(i [-1])


# function et tuples 

def obtenir_info_personne():
    return "Melanie", 37, 1.64 

# infos = obtenir_info_personne()
# print(f"nom :  {infos[0]}")
# print(f"age :  {infos[1]}")
# print(f"taille :  {infos[2]}")


# nom, age , taille = obtenir_info_personne()

# info = (nom , age , taille )
# print (info)


# ''''''''SLICE (De :  a ) '''
personnes = ("Melanie ", "Jean ", "Martin ", "Alice "  ) 

for i in personnes[1: 3 ]: 
    print(i)


