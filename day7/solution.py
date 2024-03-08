# to solve this day we have to get familiar with sorting in python

with open("input.txt", "r") as file:
    data = file.read().split("\n")


hands = []
bids = []

# should i do it like that 
for element in data:
    element = element.split()
    hands.append(element[0])
    bids.append(int(element[1]))



order_character = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
hand_types = {}

def categorize_hand(hand):

    # counting original characters in hand
    hand_counter = {}
    for symbol in hand:
        if symbol not in hand_counter:
            hand_counter[symbol] = hand.count(symbol) # useful method list.count(character)

    # sorting original hand to find out TO which character to switch using J wild card
    sorted_hand_counter = dict(sorted(hand_counter.items(), 
                                      key=lambda item: (item[1], [order_character.index(char) for char in item[0]]), reverse=True))
    

    # switching wild cards to most common character
    if "J" in hand:
        most_commmon_character = list(sorted_hand_counter.keys())[0]
        if (most_commmon_character == "J") and len(list(sorted_hand_counter.keys()))>1:
            most_commmon_character = list(sorted_hand_counter.keys())[1]
            new_hand = hand.replace("J", most_commmon_character)
        else:
            new_hand = hand.replace("J", most_commmon_character)

        # counting original characters in hand
        hand_counter = {}
        for symbol in new_hand:
            if symbol not in hand_counter:
                hand_counter[symbol] = new_hand.count(symbol) # useful method list.count(character)

    values = sorted(hand_counter.values(), reverse=True)

    # categorize as if wild cards were used
    if values[0] == 5:
        return "five_of_kind"
    elif values[0] == 4:
        return "four_of_kind"
    elif values == [3,2]:
        return "full_house"
    elif values[:2] == [3,1]:
        return "three_of_kind"
    elif values[:2] == [2,2]:
        return "two_pair"
    elif values[:2] == [2,1]:
        return "one_pair"
    else:
        return "high_card"
    

for hand in hands:
    x = categorize_hand(hand)
    hand_types[hand] = x

# how to create a hierarchy by which by can sort
# create a list [five_of_kind, four_of_kind, full_house, etc.]
# and sort using this list
order = ["five_of_kind", "four_of_kind", "full_house", "three_of_kind", 
         "two_pair", "one_pair", "high_card"]

# sorting for EACH character in given string
sorted_hand_types = dict(sorted(hand_types.items(), 
                                key=lambda item: (order.index(item[1]), [order_character.index(char) for char in item[0]])))


for k,v in sorted_hand_types.items():
    print(k,v)


result = 0

for i,j in enumerate(reversed(sorted_hand_types),1): # 1 as a starting index for enumerate
    result += (i*bids[hands.index(j)])


print(result)