mot = "crocodile"
lettre = "i"
liste_position = list()

def trouve(letter,debut,fin):
    if debut > fin:
        return liste_position
    else:
        position = mot.find(letter,debut,fin) 
        if position != -1:
            liste_position.append(position)
            trouve(letter,position+1,fin)

trouve("k",0,len(mot))
print(liste_position)

trouve("c",0,len(mot))
print(liste_position)

trouve("e",0,len(mot))
print(liste_position)






