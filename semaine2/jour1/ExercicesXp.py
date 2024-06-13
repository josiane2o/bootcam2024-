
# Exercice 1 : 
# Bonjour Tout Le Monde
# Imprimez le résultat suivant sur une seule ligne de code :
# Hello world
# Hello world
# Hello world
# Hello world

print("hello world \n" * 10)


# Exercice 2 : Quelques Maths
# Instructions
# Écrivez du code qui calcule le résultat de : (99^3)*8 (c'est-à-dire 99 à la puissance 3, fois 8).

resultat = (99**3) * 8
print(resultat)

# Ex 3
# Prédisez le résultat des extraits de code suivants :
# >>> 5 < 3
# >>> 3 == 3
# >>> 3 == "3"
# >>> "3" > 3
# >>> "Hello" == "hello"

x = 5
y = 3
print(5 < 3)

x = 3
y = 3
print(3 == 3)

x = 3
y = 3
print(3 == "3")

note = float
# x = 3
# y = 3
#print("3" > 3)

# print("Hello" == "hello")


# exercice 4
# Créez une variable appelée computer_branddont la valeur est le nom de marque de votre ordinateur.
# En utilisant la computer_brandvariable, imprimez une phrase qui indique ce qui suit : 
# "I have a <computer_brand> computer".

computer_brand = "Hewett Pakard"
print(f"i have a {computer_brand} computer") 

# exo 5
# Créez une variable appelée nameet définissez sa valeur sur votre nom.
# # Créez une variable appelée ageet définissez sa valeur sur votre âge.
# # Créez une variable appelée shoe_sizeet définissez sa valeur sur votre pointure.
# # Créez une variable appelée infoet définissez sa valeur sur une phrase intéressante sur vous-même. 
# La phrase doit contenir toutes les variables créées dans les parties 1, 2 et 3.
# # Demandez à votre code d'imprimer le infomessage.
# # Exécutez votre code

name = "ndoumbe josiane"
age = 35
shose_size = 39,5
info = f"mon nom c'est {name}, j'ai {age} ans, je chausse du {shose_size}."
print(info)


#ex 6 : A ET B
# Créez deux variables, aet b.
# Chaque valeur de variable doit être un nombre.
# Si ac'est plus grand b, faites imprimer votre code Hello World

a = 5 
b = 10
if a > b:
  print("hello world")
else:
  print("Essayez encore")



# exo 7 : impair ou pair 
# Écrivez du code qui demande à l'utilisateur 
# un nombre et détermine si ce nombre est pair ou impair.

nombre = int(input("entrer un nombre."))
if nombre % 2 == 0:
   print(f"le nombre {nombre} est pair")
else:
   print(f"le nombre{nombre} est impair")


#exo 8 : quel est ton nom 
#Écrivez du code qui demande à l'utilisateur son nom et 
# détermine si vous portez ou non le même nom,
# imprimez un message amusant en fonction du résultat

nom = "josiane"
nom =input("\nquel est ton nom ?\n")
if nom == nom:
   print(f"\nwow nous avons le meme nom, {nom} ! etes vous mon jumeau perdu depuis longtemps ?\n")
else:
   print(f"\nravi de vous rencontrer, {nom} ! desole nous connaissons un seul {nom}.\n") 


    #exo 9
# Écrivez du code qui demandera à 
# l'utilisateur sa taille en centimètres.
# S'ils mesurent plus de 145 cm, imprimez un message 
# indiquant qu'ils sont assez grands pour rouler.
# S'ils ne sont pas assez grands, imprimez un message 
# indiquant qu'ils doivent grandir encore pour rouler. 
     
taille = int(input("veille entrer votre taille en centimetres: ")) 
if taille > 145:
    print("\ntu es assez grande pour rouler !\n")
else :
    print("\nvous devez encore grandir pour rouler.\n")