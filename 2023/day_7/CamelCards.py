def main():

    hands, bids = parser()
    print(cardCounter(hands, bids))
    


def parser():
    
    hands = []
    bids = []

    with open("puzzle_input.txt") as usr_input:
        for line in usr_input:
            hand, bid = line.split(" ")
            hands.append(hand)
            bids.append(int(bid))

    return hands, bids

def cardCounter(hands, bids):

    cards = {"A":14, "K":13, "Q":12, "J":11, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}
    vv = []
    triple = []

    for index, line in enumerate(hands):
        
        vv = [0] * len(cards)
        value = 0

        for card in line:
            if card in cards:
                vv[cards[card] - 2] += 1
                hand_value, card_value = sort(vv)
        triple.append([hand_value, card_value, bids[index]])

    triple.sort()
    triple.reverse()
    f=0

    for index, i in enumerate(triple):
        f += (len(triple) - index) * i[2]
        #print(f)

    return f


def sort(vv):

    tmp = []
    tmp1 = vv.copy()
    
    for index, i in enumerate(vv):
        tmp.append(i*(index+2)) 

    tmp.sort()
    tmp1.sort()
    tmp.reverse()
    tmp1.reverse()


    hand_value = tmp1[0]
    card_value = tmp[0]


    return hand_value, card_value



if __name__ == "__main__":
    main()