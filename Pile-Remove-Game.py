from random import randrange

def playerMove(player, checkPile):
    remove = 0
    while remove == 0:
        try:
            remove = eval(input(str(player)+ ' removes: '))
            print()
            if remove>0 and remove<4 and remove<=checkPile and remove == int(remove):
                checkPile -= remove
                print('There are', checkPile,'items left in the pile.\n')
                if gameOver(checkPile):
                    print(player, 'wins!!!')
                return checkPile
            else:
                print('Invalid input, please try again...\n')
                remove = 0
            
        except:
            print('\nInvalid input, please try again...\n')
            remove = 0

            
#Spits Out Pile In The Begining#
def pileCreate():
    newPile = 0
    while newPile == 0: 
        try:
            newPile = eval(input('How many items would you like in the pile: '))
            print()
            if newPile > 0:
                return newPile
            else:
                print('Invalid input, please try again...\n')
                newPile = 0
        except:
            print('\nInvalid input, please try again...\n')
            newPile = 0
    
    
def hardCpu(newpile):
    if newpile < 4:
        remove = newpile
        newpile -= remove
        print('The cpu removed', remove,'objects.\n')
        print('There are', newpile,'objects left.\n')
        print('CPU wins!!\n')
        return newpile
    elif newpile % 4 == 3:
        newpile -= 3
        print('The cpu removed 3 objects.\n')
        print('There are', newpile,'objects left.\n')
        return newpile
    elif newpile % 4 == 2:
        newpile -= 2
        print('The cpu removed 2 object.\n')
        print('There are', newpile,'objects left.\n')
        return newpile
    elif newpile % 4 ==  1 or newpile % 4 == 0:
        newpile -= 1
        print('The cpu removed 1 object.\n')
        print('There are', newpile,'objects left.\n')
        return newpile
      
          
def easyCpu(newpile):
    remove = randrange(1,3)
    if remove > newpile:
        remove = newpile
    newpile -= remove
    print("CPU removes: ", remove)
    print()
    print('There are', newpile,'object left.\n')
    if gameOver(newpile):
        print('CPU wins!!!')
    return newpile

    
def dificulty(choice):
    for i in range(len(choice)):
        if choice[i] == 'e' or choice[i] == 'E':
            return 'cpuEasy'
        elif choice[i] == 'h' or choice[i] == 'H':
            return 'cpuHard'

def Intro():
    print('\nWelcome to the countdown game!\n')
    print('The objective of this game is to remove the last items from the pile, leaving\n')
    print('the other player with nothing to pick from, making you the Winner!.\n')
  
def rules(pilenum):
    print('Rules: You can only remove 1-3 items from the pile during your turn,\n')
    print('there are', pilenum,' items in the pile.\n')

def gameOver(checkPile):
    if checkPile > 0:
        return False
    else:
        return True


def main():
    stop = "go"
    while stop != "":
        p1 = 'Player 1'
        p2 = 'Player 2'
        Intro()
        cpu = input('Enter "T" for two player\nor enter an "E" for easy mode for easy mode against the computer\nor "H" for hard mode against the computer: ')
        print()
        level = dificulty(cpu)
        pile = pileCreate()
        rules(pile)
        while not gameOver(pile):
            pile = playerMove(p1 , pile)
            if level == 'cpuEasy' and not gameOver(pile):
                pile = easyCpu(pile)
            elif level == 'cpuHard' and not gameOver(pile):
                pile = hardCpu(pile)
            elif not gameOver(pile):
                pile = playerMove(p2, pile)
        stop = input("\nPress Enter to Quit, or input anything to continue playing: ")
    
        
        
        
main()
