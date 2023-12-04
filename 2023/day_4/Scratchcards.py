# cpode inspired by user's FlyingPlatypus5 solution on https://www.reddit.com/r/adventofcode/comments/18actmy/2023_day_4_solutions/

def main():

    with open("example1.txt") as usr_input:
        text = usr_input.readlines()

        numSum = 0
        cards = [1 for _ in text]
        print(cards)

        for index, line in enumerate(text):

            line = line.split(":")[1].replace("\n","")

            win_nums, your_nums = line.split("|")
            win_nums, your_nums = win_nums.split(), your_nums.split()

            winning_numbers = len((set(win_nums) & set(your_nums)))
            print(winning_numbers)

            if winning_numbers > 0:
                numSum += 1 * 2**(winning_numbers-1)


            for i in range(winning_numbers):
                cards[index + i + 1] += cards[index]
                print(cards)

        print(numSum, sum(cards))





if __name__ == "__main__":
    main()