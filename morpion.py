
import turtle as t

def grille():
    t.speed(0)
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.forward(600)
    t.forward(-200)
    t.left(90)
    t.forward(-200)
    t.forward(600)
    t.forward(-200)
    t.left(90)
    t.forward(-200)
    t.forward(600)
    t.forward(-200)
    t.left(90)
    t.forward(-200)
    t.forward(600)
    t.penup()
    t.goto(0,0)
    t.left(90)
    t.goto(-100,-100)
    t.pendown()
    t.write("C", align="center",font=('Arial',30,'normal'))
    t.penup()
    t.goto(-100,100)
    t.pendown()
    t.write("B", align="center",font=('Arial',30,'normal'))
    t.penup()
    t.goto(-100,300)
    t.pendown()
    t.write("A", align="center",font=('Arial',30,'normal'))
    t.penup()
    t.goto(100,500)
    t.pendown()
    t.write("1", align="center",font=('Arial',30,'normal'))
    t.penup()
    t.goto(300,500)
    t.pendown()
    t.write("2", align="center",font=('Arial',30,'normal'))
    t.penup()
    t.goto(500,500)
    t.pendown()
    t.write("3", align="center",font=('Arial',30,'normal'))
    
def croix(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.left(45)
    t.forward(-50)
    t.forward(100)
    t.forward(-50)
    t.left(90)
    t.forward(-50)
    t.forward(100)
    
def cercle(x,y):
    t.penup()
    t.home()
    t.goto(x,y-50)
    t.pendown()
    t.circle(50)
      

A1 = [100,300]
A2 = [300,300]
A3 = [500,300]
B1 = [100,100]
B2 = [300,100]
B3 = [500,100]
C1 = [100,-100]
C2 = [300,-100]
C3 = [500,-100]

def test_case(str):
    if str == "A1":
        return A1
    elif str == "A2":
        return A2
    elif str == "A3":
        return A3
    elif str == "B1":
        return B1
    elif str == "B2":
        return B2
    elif str == "B3":
        return B3
    elif str == "C1":
        return C1
    elif str == "C2":
        return C2
    elif str == "C3":
        return C3

        

def play():
    grille()  
    deja_joue= []
    print("Entrez play pour jouer :")
    last_input = input()
    while 1==1:
        if last_input=="play":
            print("Les règles sont celles d'un morpion de base, vous jouez à deux joueurs, rentrez les informations des cases quand cela est demandé(ligne en MAJ et chiffre collé, exemple : A1), le joueur 1 à pour défaut les croix et le joueur 2 à pour défaut les cercles. Si un de vous deux gagne ou qu'il y a un match nul tapez la commande : finish(apparaît une fois par tour à partir du troisième tour); à vous de jouer !")
            print("Joueur 1 à toi choisi ta case :")
            last_input = input()
            deja_joue.append(last_input)
            if last_input in {"A1","A2","A3","B1","B2","B3","C1","C2","C3"}:
                list(last_input)
                croix(test_case(last_input)[0],test_case(last_input)[1])
            else:
                print("erreur recommencez, tapez play")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            print("Joueur 2 à toi choisi ta case : (sauf parmi "+str(deja_joue)+"sinon ça marche po)")
            last_input = input()
            if last_input in deja_joue:
                print("tu le fais exprès je t'ai remis la liste en haut, pour la peine recommence")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            else:
                list(last_input)
                cercle(test_case(last_input)[0],test_case(last_input)[1])
            deja_joue.append(last_input)
            print("Joueur 1 à toi choisi ta case : (sauf parmi "+str(deja_joue)+"sinon ça marche po") 
            last_input = input()
            if last_input in deja_joue:
                print("tu le fais exprès je t'ai remis la liste en haut, pour la peine recommence")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            else:
                list(last_input)
                croix(test_case(last_input)[0],test_case(last_input)[1])
            deja_joue.append(last_input)
            print("Joueur 2 à toi choisi ta case : (sauf parmi "+str(deja_joue)+"sinon ça marche po") 
            last_input = input()
            if last_input in deja_joue:
                print("tu le fais exprès je t'ai remis la liste en haut, pour la peine recommence")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            else:
                list(last_input)
                cercle(test_case(last_input)[0],test_case(last_input)[1])
            deja_joue.append(last_input)
            print("Joueur 1 à toi choisi ta case ou écris finish si terminé : (sauf parmi "+str(deja_joue)+"sinon ça marche po") 
            last_input = input()
            if last_input in deja_joue:
                print("tu le fais exprès je t'ai remis la liste en haut, pour la peine recommence")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            elif last_input == "finish":
                print("Voilà... Que dire de plus à pars une autre partie ? Aller je la relance si jamais")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            else:
                list(last_input)
                croix(test_case(last_input)[0],test_case(last_input)[1])
            deja_joue.append(last_input)
            print("Joueur 2 à toi choisi ta case ou écris finish si terminé : (sauf parmi "+str(deja_joue)+"sinon ça marche po") 
            last_input = input()
            if last_input in deja_joue:
                print("tu le fais exprès je t'ai remis la liste en haut, pour la peine recommence")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            elif last_input == "finish":
                print("Voilà... Que dire de plus à pars une autre partie ? Aller je la relance si jamais")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            else:
                list(last_input)
                cercle(test_case(last_input)[0],test_case(last_input)[1])
            deja_joue.append(last_input)
            print("Joueur 1 à toi choisi ta case ou écris finish si terminé : (sauf parmi "+str(deja_joue)+"sinon ça marche po") 
            last_input = input()
            if last_input in deja_joue:
                print("tu le fais exprès je t'ai remis la liste en haut, pour la peine recommence")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            elif last_input == "finish":
                print("Voilà... Que dire de plus à pars une autre partie ? Aller je la relance si jamais")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            else:
                list(last_input)
                croix(test_case(last_input)[0],test_case(last_input)[1])
            deja_joue.append(last_input)
            print("Joueur 2 à toi choisi ta case ou écris finish si terminé : (sauf parmi "+str(deja_joue)+"sinon ça marche po") 
            last_input = input()
            if last_input in deja_joue:
                print("tu le fais exprès je t'ai remis la liste en haut, pour la peine recommence")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            elif last_input == "finish":
                print("Voilà... Que dire de plus à pars une autre partie ? Aller je la relance si jamais")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            else:
                list(last_input)
                cercle(test_case(last_input)[0],test_case(last_input)[1])
            deja_joue.append(last_input)
            print("Joueur 2 à toi choisi ta case ou écris finish si terminé : (sauf parmi "+str(deja_joue)+"sinon ça marche po") 
            last_input = input()
            if last_input in deja_joue:
                print("tu le fais exprès je t'ai remis la liste en haut, pour la peine recommence")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            elif last_input == "finish":
                print("Voilà... Que dire de plus à pars une autre partie ? Aller je la relance si jamais")
                t.clear()
                t.penup()
                t.home()
                play()
                break
            else:
                list(last_input)
                cercle(test_case(last_input)[0],test_case(last_input)[1])
            deja_joue.append(last_input)
            print("Bon là tu as essayé de voir si j'avais tous prévu, et en tout cas ça oui. J'imagine que tu joues avec personne du coup triste. Aller je le relance")
            t.clear()
            t.penup()
            t.home()
            play()
            break
            
               
            
            
play()
t.exitonclick()
