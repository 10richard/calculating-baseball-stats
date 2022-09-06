#Baseball stats calculator

def getPlayerName(): 
    print (" ")
    print (" ")
    playerName = input("Player name: ")
    getPlayerPosition(playerName)

def getPlayerPosition(name):
    upperName = name.upper()
    print (" ")
    print ("Name: {}".format(upperName))
    print (" ")
    print ("""Pitcher = 1 | Batter = 2""")
    playerPosition = int(input("Pitcher or Batter: "))

    for x in range(5):
        if playerPosition == 1 or playerPosition == 2:
            getCategory(playerPosition)
        else: 
            print ("Invalid input. Please try again.")
            playerPosition = int(input("Pitcher or Batter: "))

def getCategory(position):
    print (" ")
    if position == 1:
        print ("Strikeouts = 1 | Pitches Thrown 1st Inning = 2 | ")
        category = int(input("What category: "))
        for x in range(5):
            if category == 1:
                print ("Category chosen: Strikeouts")
                getStrikeouts()
            elif category == 2:
                print ("Category: Pitches Thrown 1st Inning")
                getERA()
            else:
                print ("Invalid input. Please try again.")
                category = int(input("What category: "))

    elif position == 2:
        print ("Hitter Fantasy Score = 1 | Total Bases = 2")
        category = int(input("WHat category: "))
        for x in range(5):
            if category == 1:
                print ("Category chosen: Hitter Fantasy Score")
                getBattingAvg()
            elif category == 2:
                print ("Category: Total Bases")
                getBattingAvg()
            else:
                print ("Invalid input. Please try again.")
                category = int(input("What category: "))

def getStrikeouts():
    print (" ")
    while True:
        strikeouts = input("Strikeouts: ")
        try:
            validate_strikeouts = int(strikeouts)
            print("Total number of strikeouts: ", validate_strikeouts)
            break;
        except ValueError:
            try:
                float(strikeouts)
                print("Input is a float number.")
                print("Total number of strikeouts: ", validate_strikeouts)
                break;
            except ValueError:
                print("This is not a number. Please enter a valid number")
    getGames(int(strikeouts))

def getGames(strikeouts):
    print (" ")
    while True:
        games = input("Games: ")
        try:
            validate_games = int(games)
            print("Total number of games: ", validate_games)
            break;
        except ValueError:
            try:
                float(games)
                print("Input is a float number.")
                print("Total number of games: ", validate_games)
                break;
            except ValueError:
                print("This is not a number. Please enter a valid number")
    
    calcStrikeouts(strikeouts, int(games))

def calcStrikeouts(strikeouts, games):
    print (" ")
    avg = strikeouts / games
    print ("Average amount of strikeouts per {} games: {}".format(games, avg))
    checkRepeat()

def getERA():
    print (" ")
    while True:
        era = input("Pitcher's ERA: ")
        try:
            validate_era = int(era)
            print("ERA: ", validate_era)
            break;
        except ValueError:
            try:
                float(era)
                print("Input is a float number.")
                print("Pitcher's ERA: ", validate_era)
                break;
            except ValueError:
                print("This is not a number. Please enter a valid number")

def getBattingAvg():
    print (" ")
    while True:
        battingAverage = input("Batting average: ")
        try:
            validate_battingAverage = int(battingAverage)
            print("Batting average: ", validate_battingAverage)
            break;
        except ValueError:
            try:
                float(battingAverage)
                print("Input is a float number.")
                print("Batting average: ", validate_battingAverage)
                break;
            except ValueError:
                print("This is not a number. Please enter a valid number")

def getBookLine():
    print (" ")
    while True:
        bookLine = input("Sportsbook line: ")
        try:
            validate_bookLine = int(bookLine)
            print("Sportsbook line: ", validate_bookLine)
            break;
        except ValueError:
            try:
                float(bookLine)
                print("Sportsbook line: ", validate_bookLine)
                break;
            except ValueError:
                print("This is not a number. Please enter a valid number")

def calcERA():
    x =  "placeholder"

def calcBatter():
    x = "placeholder"

def checkRepeat():
    print(" ")
    print ("Yes = 1 | No = 2")
    repeatAnswer = int(input("Would you like to do more calculations: "))
    for x in range(5):
        if repeatAnswer == 1:
            checkPlayer()
        elif repeatAnswer == 2:
            exit()
        else:
            print ("Invalid input. Please Try Again")
            print ("Yes = 1 | No = 2")
            repeatAnswer = int(input("Would you like to do more calculations: "))
            
def checkPlayer():
    print (" ")
    print ("Same = 1 | New = 2")
    checkPlayer = int(input("Same player or new player: "))
    for x in range(5):
        if checkPlayer == 1:
            getStrikeouts()
        elif checkPlayer == 2:
            getPlayerName()
        else:
            print ("Invalid input. Please try again.")
            checkPlayer = int(input("Same player = 1 | New player = 2"))

getPlayerName()