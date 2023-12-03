def main():
    # open file
    # loop through the symbols unit end of line
    with open("example1.txt", "r") as usr_input:
        text = usr_input.read()
        test_1(text)




def test_1(text):
    
    numList = []
    numSum = 0
    

    for symbol in text:
        if symbol == "\n" or text is None:
            numSum += int(numList[0]) * 10 + int(numList[-1])
            numList.clear()
        elif symbol.isnumeric() == True:
            numList.append(symbol) 

    print(numSum)

if __name__ == "__main__":
    main()