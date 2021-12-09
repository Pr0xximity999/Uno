import random
from time import sleep
from os import system
proceed = False
playerCount = 0
deck = []
turnDone = False

#This array of lists define how the deck is shaped
colors = ["green", "red", "yellow", "blue"]
nums = "0112233445566778899"
takeTwoCards = [2, "Take two"]
reverseCards = [2, "reverse"]
skipCards = [2, "skip"]
wildCards = [4, "wild"]
takeFourCards = [4, "take four"]
blackCards = [wildCards, takeFourCards]
coloredCards = [takeTwoCards, reverseCards, skipCards]
opencard = ""

nameList = ["Thomas", "Martin", "Harry", "Jane", "Matt", "Joe", "Lucy", "Gabe", "Mark", "Chris", "Mary", "Anna", "Mike", "Josey"]
playerList = [["you", []]]
finishedPlayers = 0

def chechIfWholeNum(checkNum): #Checks if the inputted number's a whole number and contains no letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    checkNum = str(checkNum)
    #If the input contains letters
    for i in range(len(checkNum)):
        if checkNum[i] in alphabet: print("Please dont add letters, only number"); return False
    
    #If the user enters a decimal number
    if float(checkNum) % 1 != 0: print(f"Please give a whole number"); return False
    else: checkNum = int(checkNum)

    #If the user enters zero
    if checkNum <= 0:print(f"Choose at least one player"); return False



def MakeDeck(): #Makes the deck and then shuffles it
    global deck, colors,nums, takeTwoCards, reverseCards, skipCards, wildCards, takeTwoCards, coloredCards
    for i in range(len(colors)): #First, it makes all the colored cards
        for x in range(len(nums)):#Number cards
            deck.append(colors[i] + " " + nums[x]) #Adds the cards to the deck
        
        for x in range(len(coloredCards)):#Non-number cards
            for y in range(coloredCards[x][0]): #executes it how many times it has been noted in the fist index of the cardtype
                deck.append(colors[i] + " " + coloredCards[x][1])#Adds the cards to the deck
    
    for i in range(len(blackCards)): #Then, it adds the black(special) cards
        for x in range(blackCards[i][0]):#executes it how many times it has been noted in the fist index of the cardtype
            deck.append(blackCards[i][1])#Adds the cards to the deck

    random.shuffle(deck) #Shuffles the deck


#The program starts here
MakeDeck()
sleep(1)
print("Welcome")
sleep(1)
print("To")
sleep(1)
print("⠐⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠂");sleep(0.05)
print("⠄⠄⣰⣾⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠄⠄");sleep(0.05)
print("⠄⠄⣿⣿⣿⡿⠋⠄⡀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⣉⣉⣉⡉⠙⠻⣿⣿⠄⠄");sleep(0.05)
print("⠄⠄⣿⣿⣿⣇⠔⠈⣿⣿⣿⣿⣿⡿⠛⢉⣤⣶⣾⣿⣿⣿⣿⣿⣿⣦⡀⠹⠄⠄");sleep(0.05)
print("⠄⠄⣿⣿⠃⠄⢠⣾⣿⣿⣿⠟⢁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄⠄");sleep(0.05)
print("⠄⠄⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⠄");sleep(0.05)
print("⠄⠄⣿⣿⣿⣿⣿⡟⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄");sleep(0.05)
print("⠄⠄⣿⣿⣿⣿⠋⢠⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄");sleep(0.05)
print("⠄⠄⣿⣿⡿⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⠗⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⡟⠄⠄");sleep(0.05)
print("⠄⠄⣿⡿⠁⣼⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⠄⣠⣄⢰⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄");sleep(0.05)
print("⠄⠄⡿⠁⣼⣿⣿⣿⣿⣿⣿⣿⡇⠄⢀⡴⠚⢿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⠄⠄");sleep(0.05)
print("⠄⠄⠃⢰⣿⣿⣿⣿⣿⣿⡿⣿⣿⠴⠋⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⠄⠄");sleep(0.05)
print("⠄⠄⢀⣿⣿⣿⣿⣿⣿⣿⠃⠈⠁⠄⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⣿⠄⠄");sleep(0.05)
print("⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⢶⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀⣾⣿⣿⠄⠄");sleep(0.05)
print("⠄⠄⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⠋⣠⣿⣿⣿⣿⠄⠄");sleep(0.05)
print("⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣼⣿⣿⣿⣿⣿⠄⠄");sleep(0.05)
print("⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⠄⠄");sleep(0.05)
print("⠄⠄⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢁⣴⣿⣿⣿⣿⠗⠄⠄⣿⣿⠄⠄");sleep(0.05)
print("⠄⠄⣆⠈⠻⢿⣿⣿⣿⣿⣿⣿⠿⠛⣉⣤⣾⣿⣿⣿⣿⣿⣇⠠⠺⣷⣿⣿⠄⠄");sleep(0.05)
print("⠄⠄⣿⣿⣦⣄⣈⣉⣉⣉⣡⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⠉⠁⣀⣼⣿⣿⣿⠄⠄");sleep(0.05)
print("⠄⠄⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⡿⠟⠄⠄");sleep(0.05)
print("⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄.")
sleep(0.2)
print("UNO!")


while proceed == False:
    sleep(1)
    playerCount = input("How many players do you wanna play with? >>")
    proceed = chechIfWholeNum(playerCount)
    playerCount = int(playerCount)

for i in range(playerCount): #Adds players with random names
    ranNum = random.randint(0, len(nameList) - 1)
    player = [nameList[ranNum], []]
    playerList.append(player)

for i in range(7): #Gives the cards to the players
    for x in range(len(playerList)):
        playerList[x][1] = playerList[x][1] + [(deck[0])]
        deck.remove(deck[0])


#The real game starts
finished = False
turn = 1
playerTurn = 0
opencard = deck[0].split(' ') 
deck.remove(deck[0])

while finished == False:
    system('cls') #Clears the screen
    print(f"Turn {turn} |{4 - finishedPlayers} players remaining") #Shows the turn and players remaining(A.k.A. aren't finished)
    sleep(0.3)
    
    print(f"{opencard[0]} {opencard[1]} is now on top")

    if playerTurn == 0: #If its the user's turn
        print(f"YOUR TURN")
        sleep(0.3)
        print()
        print("Your cards:")
        playerList[0][1].sort()
        for i in range(len(playerList[0][1])): #Displays the available cards
            print(f"{i + 1}|{playerList[0][1][i]}")
            sleep(0.05)
        
        print("Enter the number of the card that you want to draw, or enter 'take card' if you want to take a card off the pile")
        proceed = False
        while proceed == False:
            action = input(">>")
            if action.lower() == "take card":
                sleep(0.1)
                print(f"You took a card from the deck \nIt's a {deck[0]}")
                playerList[0][1] = playerList[0][1] + [deck[0]]
                deck.remove(deck[0])
                turnDone = True
                proceed = True
                continue

                

    else: #If it is the computer's turn
        print(f"{playerList[0][0].upper()}'S TURN")