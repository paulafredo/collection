def demannder_info():
    noms = []
    while(True): 
        nom = input("Nom de la personne :")
        if nom=="":
            break
        noms.append(nom)
    return noms
    
nom = demannder_info()
print(nom)
