# #🌟 Exercice 1 : Numéros Favoris
# Instructions
# Créez un ensemble/set appelé my_fav_numbers avec tous vos numéros favoris.
# Ajoutez deux nouveaux numéros à l'ensemble.
# Supprimez le dernier numéro.
# Créez un ensemble appelé friend_fav_numbers avec les numéros favoris de votre ami.
# Concaténer my_fav_numbers et friend_fav_numbers à une nouvelle variable appelée our_fav_numbers


# Créez un ensemble/set appelé my_fav_numbers avec tous vos numéros favoris.
my_fav_numbers = {3, 40, 70, 30, 10, 50, 100}

# Ajoutez deux nouveaux numéros à l'ensemble.
my_fav_numbers.add(90)
my_fav_numbers.add(200)



# Supprimez le dernier numéro.
my_fav_numbers.remove(50)
print(my_fav_numbers)

# Créez un ensemble appelé friend_fav_numbers avec les numéros favoris de votre ami.
friend_fav_numbers = {2, 34, 66, 54, 78, 89, 44 }

# Concaténer my_fav_numbers et friend_fav_numbers à une nouvelle variable appelée our_fav_numbers
# our_fav_numbers = my_fav_numbers | friend_fav_numbers. OR
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)

