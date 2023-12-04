

# what should I know 
# 


def main():

    cardSum = 0

    with open("puzzle_input.txt", "r") as usrInput:
        for line in usrInput:
            cardSum += scratchCardCounter(line)
    
    #print()
    print(cardSum)



def scratchCardCounter(line):

    cardNum, number = line.split(":")
    winNum, yourNum = number.split("|")

    winNumList = winNum.strip().replace("\n", "").replace("  ", " ").split(" ")
    yourNumList = yourNum.strip().replace("\n","").replace("  ", " ").split(" ")

    winCounter = 0
    #print(f"winNumList: {winNumList}")
    #print(f"youNumList: {yourNumList}")
    for i in yourNumList:
        if i in winNumList:
            winCounter += 1
        else:
            continue

    if winCounter >= 1:
        gameCounter = 1 * 2**(winCounter-1)
    else:
        gameCounter = 0

    #print(gameCounter)
    return gameCounter
    

if __name__ == "__main__":
    main()