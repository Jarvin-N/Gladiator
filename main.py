from tkinter import *
import random
#Variables
battle = "false"
move_select = ""
thiefMove = ""
thiefDMG = ""
playerHP = 100
thiefHP = 100
damage = 0
turn = 1
#MainScreen
gameGUI = Tk()
gameGUI.title('Gladiators')
menuSCR = Frame(gameGUI)
menuSCR.pack(fill=BOTH)
title_WELCOME = PhotoImage(file='WELC.png')
title_WEL = Label(menuSCR, image=title_WELCOME)
title_WEL.pack(fill=X)
playIM = PhotoImage(file='PLAY.png')
charIM = PhotoImage(file='CHAR.png')
#Menu Music

#BattleSCR Stuff
battleSCR = Frame(gameGUI)

def playfunction(event):
    global battle
    battleSCR.pack(fill=BOTH)
    battle = "true"
    menuSCR.pack_forget()
    battleSYS(event)
    global thiefHP
    global playerHP
    #Resets Health, Displays, Turns
    global turn
    turn = 1
    thiefHP = 100
    playerHP = 100
    healthDisplay = Label(battleSCR, text="Your health " + str(playerHP), fg="red", font=('Impact', 15), width=20)
    healthDisplay.grid(row=1, column=2)
    thiefHealthDisplay = Label(battleSCR, text="Thief's health " + str(thiefHP), fg="blue", font=('Impact', 15),width=20)
    thiefHealthDisplay.grid(row=2, column=2)
    info_tag = Label(battleSCR, text="Please choose an attack", font=('Impact', 25), width=50)
    info_tag.grid(row=0, columnspan=50, sticky=W)



playB = Button(menuSCR, image=playIM)
playB.pack(fill=X)
playB.bind("<Button-1>", playfunction)

characterB = Button(menuSCR, image=charIM)
characterB.pack(fill=X)

war = PhotoImage(file="glad.png")
warLAB = Label(menuSCR, image=war, width=500, height=439)
warLAB.pack()




def mace():
    global move_select
    global damage
    move_select = "Mace"
    damage = random.randrange(15, 30)


def sword():
    global move_select
    global damage
    move_select = "Sword"
    damage = random.randrange(20, 25)


def dagger():
    global move_select
    global damage
    move_select = "Dagger"
    damage = damage = random.randrange(15, 17)


def shield_bash():
    global move_select
    global damage
    move_select = "Shield Bash"
    damage = damage = random.randrange(5, 10)


def end_game():
    game = 0
    def time_wait():
        if game == 1:
            menu_B = Button(battleSCR, text="Menu", font=('Impact', 25))
            menu_B.grid(row=0, column=0, sticky=W)

            def menuB(event):
                battleSCR.pack_forget()
                menuSCR.pack(fill=BOTH)
                pygame.mixer.music.play(-1)


            menu_B.bind("<Button-1>", menuB)
    if thiefHP <= 0:
        info_tag = Label(battleSCR, text="Please choose an attack", font=('Impact', 25), width=50)
        info_tag.grid(row=0, columnspan=50, sticky=W)
        info_tag.config(text="The thief has died and you win")
        game = 1
    if playerHP <= 0:
        info_tag = Label(battleSCR, text="Please choose an attack", font=('Impact', 25), width=50)
        info_tag.grid(row=0, columnspan=50, sticky=W)
        info_tag.config(text="You have died and have loss the battle")
        game = 1
    time_wait()

def plyr_turn(event):
    global thiefHP
    global move_select
    global turn
    global damage
    global thiefHealthDisplay
    info_tag = Label(battleSCR, text="Please choose an attack", font=('Impact', 25), width=50)
    info_tag.grid(row=0, columnspan=50, sticky=W)
    if turn == 1:
        if move_select == "Mace":
            thiefHP = thiefHP - damage
            info_tag.config(text="You whip your mace at the thief and do " + str(damage) + " damage")
            turn = 0
        if move_select == "Sword":
            thiefHP = thiefHP - damage
            info_tag.config(text="You stab the thief and do " + str(damage) + " damage")
            turn = 0
        if move_select == "Dagger":
            thiefHP = thiefHP - damage
            info_tag.config(text="You throw your dagger at the thief and do " + str(damage) + " damage")
            turn = 0
        if move_select == "Shield Bash":
            thiefHP = thiefHP - damage
            info_tag.config(text="You shield bash the thief and do " + str(damage) + " damage")
            turn = 0
    thiefHealthDisplay = Label(battleSCR, text="Thief's health " + str(thiefHP), fg="blue", font=('Impact', 15), width=20)
    thiefHealthDisplay.grid(row=2, column=2)
    end_game()
def thief_turn(event):
    global thiefMove
    global thiefDMG
    global playerHP
    global healthDisplay
    global turn
    info_tag = Label(battleSCR, text="Please choose an attack", font=('Impact', 25), width=50)
    info_tag.grid(row=0, columnspan=50, sticky=W)
    if turn == 0:
        thiefMove = random.randrange(1, 4)
        if thiefMove == 1:
            thiefDMG = random.randrange(15, 30)
            playerHP = playerHP - thiefDMG
            info_tag.config(text="The Thief whips his mace at you and does " + str(thiefDMG) + " damage")
            turn = 1
        if thiefMove == 2:
            thiefDMG = random.randrange(20, 25)
            playerHP = playerHP - thiefDMG
            info_tag.config(text="The Thief stabs you does " + str(thiefDMG) + " damage")
            turn = 1
        if thiefMove == 3:
            thiefDMG = random.randrange(15, 17)
            playerHP = playerHP - thiefDMG
            info_tag.config(text="The Thief throws his dagger at you and does " + str(thiefDMG) + " damage")
            turn = 1
        if thiefMove == 4:
            thiefDMG = random.randrange(5, 10)
            playerHP = playerHP - thiefDMG
            info_tag.config(text="The Thief bashes you and does " + str(thiefDMG) + " damage")
            turn = 1
    healthDisplay = Label(battleSCR, text="Your health " + str(playerHP), fg="red", font=('Impact', 15), width=20)
    healthDisplay.grid(row=1, column=2)
    end_game()
#BattleSCR
def battleSYS(event):
    global battle
    battleSCR.pack(fill=BOTH)
    battle = "true"
    menuSCR.pack_forget()
    if battle == "true":
        thief_turn(event)
        plyr_turn(event)
    #Attack Buttons
    move_1 = Button(battleSCR, text="Mace", fg="black", font=('Impact', 15), command=mace, width=15)
    move_2 = Button(battleSCR, text="Sword", fg="black", font=('Impact', 15), command=sword, width=15)
    move_3 = Button(battleSCR, text="Dagger", fg="black", font=('Impact', 15), command=dagger, width=15)
    move_4 = Button(battleSCR, text="Shield Bash", fg="black", font=('Impact', 15), command=shield_bash, width=15)
    next_B = Button(battleSCR, text="Next", fg="black", font=('Impact', 15), width=15)
    next_B.grid(row=5, columnspan=2)
    move_1.grid(row=1, column=0)
    move_2.grid(row=1, column=1)
    move_3.grid(row=2, column=0)
    move_4.grid(row=2, column=1)
    move_1.bind("<Button-1>", plyr_turn)
    move_2.bind("<Button-1>", plyr_turn)
    move_3.bind("<Button-1>", plyr_turn)
    move_4.bind("<Button-1>", plyr_turn)
    next_B.bind("<Button-1>", thief_turn)




gameGUI.mainloop()
