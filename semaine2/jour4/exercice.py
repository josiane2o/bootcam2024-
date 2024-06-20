# #Exercice
# Écrivez une fonction calculation()telle qu'elle puisse accepter deux variables et en calculer l'addition et la soustraction. Et il doit également renvoyer à la fois l'addition et la soustraction en un seul appel de retour

def calulation(a, b):
    som =(a + b)
    sub =(a - b )
    res = som,sub
    return res

Res = calulation(5 , 1 )

print("somme : ",Res[0],"soustraction :",Res[1])

# Res = calulation(100 , 75)
print( Res)
