import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False
    if comp=='p':
        if you=='s':
            return True
        elif you=='r':
            return False
print("comp turn:Rock(r),Paper(p),Scissors(s)?")
Randomno=random.randint(1,3)
if Randomno==1:
    comp='r'
elif Randomno==2:
    comp='p'
elif Randomno==3:
    comp='s'
you=input("your turn:Rock(r),Paper(p),Scissors(s)?")
yourscore=0
compscore=0
a=gamewin(comp,you)
print(f"computer chose :{comp}")
print(f"you chose :{you}")
if a==None:
    print("the match is tie!")
elif a:
    print("you win")
    yourscore+=1
else:
    print("you lose")
    compscore+=1
print(f"Your score is:{yourscore}")
print(f"Comp score is:{compscore}")
while(True):
    wlcm='''Press 1 for play another round
Press 2 for exit the game'''
    print(wlcm)
    c=int(input("You want to play another round:"))
    if c==1:
        def gamewin(comp,you):
            if comp==you:
                return None
            elif comp=='r':
                if you=='s':
                    return False
                elif you=='p':
                    return True
            elif comp=='s':
                if you=='r':
                    return True
                elif you=='p':
                    return False
            if comp=='p':
                if you=='s':
                    return True
                elif you=='r':
                    return False
        print("comp turn:Rock(r),Paper(p),Scissors(s)?")
        Randomno=random.randint(1,3)
        if Randomno==1:
            comp='r'
        elif Randomno==2:
            comp='p'
        elif Randomno==3:
            comp='s'
        you=input("your turn:Rock(r),Paper(p),Scissors(s)?")
        yourscore=0
        compscore=0
    a=gamewin(comp,you)
    print(f"computer chose :{comp}")
    print(f"you chose :{you}")
    if a==None:
        print("the match is tie!")
    elif a:
        print("you win")
        yourscore+=1
    else:
        print("you lose")
        compscore+=1
    print(f"Your score is:{yourscore}")
    print(f"Comp score is:{compscore}")
    if c==2:
        print("Thank for playing the game!")
        break