
def main():

    gameSum = 0
    cubePower = 0
    # get the input from the user:
    with open("puzzle_input.txt", "r") as usrInput:
        # iterate over each line
        for line in usrInput:
            gameSum += CubeCounter(line)
            cubePower += CubeCounter2(line)

    print(gameSum)
    print(cubePower)
        
    
def CubeCounter(line):
    gameNum, ball= line.split(":")

    gameNum = gameNum.replace("Game ","")
    ballSet = ball.replace(";" , ",")
    
    colorBall = ballSet.split(",")

    for i in colorBall:  # 1st i = ['7 blue']
        value, color = i.strip().split(" ")
        value = int(value)

        # 1st part check 
        if color == "red" and value > 12:
            return 0
        elif color == "green" and value > 13:
            return 0
        elif color == "blue" and value > 14:
            return 0

    return int(gameNum)

def CubeCounter2(line):
    gameNum, ball= line.split(":")

    gameNum = gameNum.replace("Game ","")
    ballSet = ball.replace(";" , ",")
    
    colorBall = ballSet.split(",")

    redList = []
    greenList = []
    blueList = []

    for i in colorBall:  # 1st i = ['7 blue']
        value, color = i.strip().split(" ")
        value = int(value)

        # 2nd part check
        if color == "red":
            redList.append(value) 
        elif color == "green":
            greenList.append(value) 
        elif color == "blue":
            blueList.append(value)

    redSet = set(redList)
    greenSet = set(greenList)
    blueSet = set(blueList)

    redSet = sorted(redSet)
    greenSet = sorted(greenSet)
    blueSet = sorted(blueSet)

    cubePower = redSet[-1] * greenSet[-1] * blueSet[-1]

    return cubePower

if __name__ == "__main__":
    main()