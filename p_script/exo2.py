# recuperer 3 notes de l'utilisateur
## les notes sont 12, 15, 19
from email import message_from_binary_file

grade1 = input("enter first grade:")
grade2 =input("entrer second grade:")
grade3 = input("entrer third grade:")

#calculer la somme des 3 notes
## somme des notes
somme = float(grade1) + float(grade2) + float(grade3)

# pour faire la moyenne sans afficher "la somme est"
print (somme)
#pour faire la somme avec deux chiffres après la virgule et afficher "la somme est"
print(f"la somme est : {somme: .2f}")

## divise par 3 pour obtenir un nombre entier
moy = int(somme/3)
## pour avoir un nombre decimal
moy = float(somme/3)

#afficher la moyenne
print(moy)

# si la somme est plus grand ou egal à 16
if moy >= 16 :
    message = "very good"

# si la somme est plus grand ou egale à 14

elif moy >= 14 :
    message = "good"

# si la moyenne est plus grand ou egal à 12
elif moy >= 12 :
    message = "fairly good"

# si la moyenne est plus grand ou egal à 10
elif moy >= 10 and moy <=12
    message = "passable"

# Si la moyenne est moins que 10, ecrit "failed"
elif moy < 10 :
    message = "failed"

else:
    message = "retry"
print(message)





