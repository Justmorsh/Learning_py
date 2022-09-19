import random


def game(p1, p2):
    if p1 == p2:
        return None
    if p1 == 's':
        if p2 == 'w':
            return False
        elif p2 == 'g':
            return True
    if p1 == 'w':
        if p2 == 's':
            return True
        elif p2 == 'g':
            return False
    if p1 == 'g':
        if p2 == 's':
            return False
        elif p2 == 'w':
            return True


# eeoeoeec
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

user = input("your turn: Snake(s) Water(w) or Gun(g): ")
print("comp =", comp, "\nuser =", user, "\n")
a = game(comp, user)
if a == None:
    print("It's a Tie :)")
elif a == True:
    print("You Won the game!")
else:
    print("You Lost!")
