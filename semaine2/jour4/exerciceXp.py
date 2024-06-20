# #Exercice 1 : Qu'apprenez-Vous ?
# Instructions
# Écrivez une fonction appelée display_message()qui imprime une phrase indiquant à tout le monde ce que vous apprenez dans ce cours.
# Appelez la fonction et assurez-vous que le message s'affiche correctement

def display_message():
    print("hello tout le monde")
display_message()
#***********************************************************

# 🌟 Exercice 2 : Quel Est Votre Livre Préféré ?
# Instructions
# Écrivez une fonction appelée favorite_book()qui accepte un paramètre appelé title.
# La fonction doit imprimer un message, tel que "One of my favorite books is <title>".
# Par exemple : « L’un de mes livres préférés est Alice au pays des merveilles »
# Appelez la fonction, assurez-vous d'inclure le titre d'un livre comme argument lors de l'appel de la fonction

def favorite_book(title):
    print(f"one of my favorite book is {title}")
favorite_book("Alice au pays des merveilles")
############################################################################################################
# 🌟 Exercice 3 : Un Peu De Géographie
# Instructions
# Écrivez une fonction appelée describe_city()qui accepte le nom d'une ville et son pays comme paramètres.
# La fonction doit imprimer une phrase simple, telle que "<city> is in <country>".
# Par exemple « Reykjavik est en Islande »
# Donnez au paramètre country une valeur par défaut.
# Appelez votre fonction

def describe_city(ville , pays="cameroun"):
    print(f"{ville} is in {pays}")
    
describe_city("paris")



#Exercice 4 : Aléatoire
#Instructions
# Créez une fonction qui accepte un nombre compris entre 1 et 100 et génère un autre nombre aléatoirement entre 1 et 100. Utilisez le randommodule.
# Comparez les deux nombres, si c'est le même nombre, affichez un message de réussite, sinon affichez un message d'échec et affichez les deux nombres
import random

def nombre_compris (number):
    if number <=1 or number >= 100:
        print("\nplease entera number between 1 and 100\n")
        return number
    else :
        random_number = random.randint(1 ,100)
        if random_number == number:
            print("\n!!!!!!!! bravo !!!!!!!!!(you are success)tu as trouve\n")
        else:
            print(f"\n-----DESOLE-----(you are loss)tu as rate le nombre : {random_number}\n")

nombre_compris(2) 
       

