# def demannder_info():
#     noms = []
#     while True: 
#         nom = input("Nom de la personne :")
#         if nom=="":
#             break
#         noms.append(nom)
#     return noms
    
# noms = demannder_info()
# # sort= trier
# noms.sort 

# print(noms)

nom_chauffeur = [  "Mark ",  "Paul ","Raoul ", "Jean " , " Jamal ", "Zava" ]
distance_chauff_km= [1.5    , 2.2   ,0.8      ,2.6          ,4.7     ,0.6]
index_min= 0 
distance_min = 10000
 
for i  in range(len(nom_chauffeur)) : 
    distance = distance_chauff_km[i]
    if distance < distance_min :
        distance_min = distance
        index_min= i 
         

# index_min =distance_chauff_km.index(distance_min)  

print(f"la distance minimal est {distance_min} Km le chaufeur le plus proche est {nom_chauffeur [index_min]}")

