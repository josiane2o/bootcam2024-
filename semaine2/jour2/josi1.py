
my_name = "jack"
hello = "hello world"
my_age = 27
my_list = [my_name,my_age,hello]    

my_tuples = (my_name,my_age,hello)

#print(my_list[0:3]) # to print all elements in list
#print(my_list[0:2]) # to print first and second elements

#my_list[0] = my_age

#print("\nma nouvelle liste est ", my_list)

#my_list.remove(my_age)
#my_list.pop(1)
#my_list.append("josiane est une eleve")
#my_list2 = ["BABA" ,"sandra","loic","joshyua"]
#my_list_sum = my_list + my_list2
# #print(my_list_sum)

# #my_tuples[0] = "henry"


# #print("\nma nouvelle liste est", my_list)

# Exercice

# Compte tenu de cette liste :

 
# liste1 = [5, 10, 15, 20, 25, 50, 20]


# recherchez la valeur 20 dans la liste, et si elle est présente, remplacez-la par 200. Ne mettez à jour que la première occurrence d'une valeur


# Astuce : Regardez la méthode d'indexation

list1 = [5,10,20,25,50,20]
# check if 20 est dans la liste
if 20 in list1:
 nouvelle_valeur = list1.index(20) 
print(nouvelle_valeur)
# remplace la premiere occurence de 20 avec 200
list1 [nouvelle_valeur] = 200
print(list1)



# Exercice

# Décompressez le tuple suivant en 4 variables


# #my_tuples = (10, 20, 30, 40)
# a,b,c,d = my_tuples

# print(d)
# print(c)
# print(b)
# print(a)




