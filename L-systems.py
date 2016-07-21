import turtle
from matplotlib.pyplot import *
from math import cos,sin,radians
from random import *


def maison():
    wn = turtle.Screen()
    alex = turtle.Turtle()
    alex.forward(100)
    alex.left(90)
    alex.forward(100)
    alex.left(30)
    alex.forward(100)
    alex.left(120)
    alex.forward(100)
    alex.left(30)
    alex.forward(100)
    turtle.exitonclick()
    return

# maison() # test de la fonction maison



def dessiner(l,a,m):
    turtle.setup(width=800, height=600, startx=None, starty=None)
    wn = turtle.Screen()
    mike = turtle.Turtle()
    mike.speed(200)
    for c in m:
        if c=='F':
            mike.forward(l)
        elif c=='+':
            mike.left(a)
        elif c=='-':
            mike.right(a)
        else:
            break
    turtle.exitonclick()

# dessiner(100,30,'F+++F+F++++F+F') # test de la maison avec la fonction déssiner

def suivant(m,R):
    nouveau_motif=''
    for c in m:
        if c=='F':
            nouveau_motif += R
        else:
            nouveau_motif += c
    return nouveau_motif

# print(suivant('F--F--F','F+F--F+F')) # test de la fonction suivant avec le motif de l'exercice

def evolution(A,R,etape):
    m=A
    for n in range(etape):
        m=suivant(m,R)
    return m

# print(evolution('F','F+',4)) # test de la fonction evolution avec le motif de l'exercice

# dessiner(5,60,evolution('F--F--F','F+F--F+F',4)) # FLOCON DE VON KOCH
# dessiner(10,90,evolution('F+F+F+F','F+F-F-F+F',3)) # FLOCON CARRE
# dessiner(10,60,evolution('F+F+F+F+F+F','F++F--FF+F-F++F',3)) # FLOCON CARRE

# test de matplot
# X=[0,4,4,2,0,0]
# Y=[0,0,4,8,4,0]
# plot(X,Y,"k-")
# show()

def dessiner_plot(l,a,m):
    X=[0]
    Y=[0]
    D=[0]
    for c in m:
        if c=='F':
            X.append(X[-1]+l*cos(radians(D[-1])))
            Y.append(Y[-1] + l * sin(radians(D[-1])))
            D.append(D[-1])
        elif c=='+':
            X.append(X[-1])
            Y.append(Y[-1])
            D.append(D[-1]+a)
        elif c=='-':
            X.append(X[-1])
            Y.append(Y[-1])
            D.append(D[-1]-a)
    plot(X,Y,"k-")
    return show()

# Flocon de Von-Koch avec plot
# dessiner_plot(5,60,evolution('F--F--F','F+F--F+F',5))

def dessiner(l,a,m,azimut=0):
    wn = turtle.Screen()
    mike = turtle.Turtle()
    mike.left(azimut)
    coordonneesX=[]
    coordonneesY = []
    coordonneesA = []
    for c in m:
        if c=='F':
            mike.forward(l)
        elif c=='+':
            mike.left(a)
        elif c=='-':
            mike.right(a)
        elif c=='[':
            coordonneesX.append(mike.xcor())
            coordonneesY.append(mike.ycor())
            coordonneesA.append(mike.heading())
        elif c==']':
            mike.penup()
            mike.goto(coordonneesX[-1],coordonneesY[-1])
            mike.setheading(coordonneesA[-1])
            mike.pendown()
            coordonneesX.pop(-1)
            coordonneesY.pop(-1)
            coordonneesA.pop(-1)
        else:
            break
    turtle.exitonclick()

# dessiner(5,60,evolution('F--F--F','F+F--F+F',3),90) # FLOCON DE VON KOCH
# dessiner(10,20,evolution('F','F[+F]F[-F]F',4),90) # Arbre

def geneRegle():
    alphabet = ['F','-','+','[',']']
    regle = "F"
    for i in range(randint(15,20)):
        regle += choice(alphabet)
    return regle

# Test de geneRegle
# print(geneRegle())

def verifie(regle):
    score=0 # score qui doit être nul à la fin du parcour et jamais négatif
    # print(regle)
    for i in regle:
        # print(score)
        if i == '[':
            score = score + 1
        elif i == ']':
            score = score - 1
            if score < 0:
                return 'invalide'
                break
    if score==0:
        return 'valide'
    else :
        return 'invalide'


# Tests de la fonction verifie
# print(verifie( 'F[-F][F]' )) # Valide
# print(verifie( '-[+]-+-[+][[-++++F+F-'))  #invalide
# print(verifie( 'F[-F[F]F]' )) # Valide
# print(verifie( ']F[-F[F]F]' )) # invalide
# print(verifie( '-[+]-+-[+]-++++F+F-'))  #valide
# print(verifie(geneRegle()))



def simplifie(regle):
    """
    Fonction qui recoit une règle sous forme d'une chaine de caratères et qui retourne une regle simplifiée
    On pourrais aussi simplifier les []
    :param regle:
    :return:
    """
    i=0
    reponse = ""
    while i < len(regle)-1:
        double = regle[i] + regle[i+1]
        if double == "+-" or double == "-+" or double == "[]":
            i=i+2
        elif double == '-]' or double == '+]':
            reponse = reponse + double[-1]
            i=i+2
        else:
            reponse = reponse + double[0]
            i=i+1
    reponse = reponse + regle[-1]
    if len(reponse) != len(regle):
        reponse = simplifie(reponse)
    return reponse

# print(simplifie('F+-[F-F]+F[F-]-F'))
# print(simplifie('F+-[F-+F]+F[F-]-F'))

def genePopulation(n):
    """
    :param n: nombre d'individus a générer
    :return: un fichier txt avec n plantes dont la syntaxe est corecte
    """
    fichier_population = open("population.txt",'w')
    plante_a_tester=[]
    while n != 0:
        plante_a_tester.append(simplifie(geneRegle()))
        if verifie(plante_a_tester[-1])=='valide' and plante_a_tester[-1].count('[') >= 3 and plante_a_tester[-1].count('+')+plante_a_tester[-1].count('-')>=2 and plante_a_tester[-1] not in plante_a_tester[0:-2]:
            fichier_population.write(plante_a_tester[-1]+'\n')
            n=n-1
    fichier_population.close()
    return fichier_population

# Test de la fonction genePopulation
# genePopulation(100)

population=open("population.txt",'r')
regles = population.read().splitlines()
# print(regles[1])
# dessiner(10,20,evolution('F',regles[5],4),90)
population.close()

# dessiner(10,20,evolution('F','F[-FF]+[FFF]-FF[-F-F]',3),90) # fougere1
# dessiner(10,20,evolution('F','F[+F]+[-F-F]-FF[+F][-F][F]',5),90) # fougere2

parent='F[-FF]+[FFF]-FF[-F-F]'
enfant='F[+F]+[-F-F]-FF[+F][-F][F]'

def extraitBranche(regle) :
    index1 = 0
    index2 = 0
    dico_crochets={}
    while index1 <= len(regle) and index2 <= len(regle) :
        index1 = regle.find("[", index1)
        index2 = regle.find("]", index2)
        dico_crochets[index1] = regle[index1]
        dico_crochets[index2] = regle[index2]
        # Break if not found.
        if index1 == -1:
            break
        if index2 == -1:
            break
        index1 += 1
        index2 += 1
    del dico_crochets[-1]
    return


print(extraitBranche('F[-FF]+[FFF]-FF[-F-F]'))
