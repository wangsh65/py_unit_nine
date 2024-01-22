# name : Shelly.W
# date : 1/21/2024
# purpose : to make a compare  nums card game
# link : https://gist.github.com/JenkinsDev/1e4bff898c72ec55df6f
#link: https://chat.openai.com/c/97a28349-28dc-46db-bd07-f49f264d65bc

import random
class Deck:                                                                                                     # create a deck of normal playing cards

    def __init__(self):
        self.suits = ['Clubs','Diamonds','Hearts','Spades']                                                     # Initialize a standard deck of cards
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        self.deck = [{'suit': suit, 'value': value} for suit in self.suits for value in self.values]            # use for to make a loop, and it can have a loopn for values and suits


    def shuffle_deck(self):                                                                                     # Fisher-Yates shuffle algorithm
        n = len(self.deck)                                                                                      #  it can good to list the cards numbers
        for i in range(n - 1, 0, -1):                                                                           # use a loop to shuffle the cards,
            j = random.randint(0, i)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]                                             #return to a self


    def deal_cards(self, num_cards):                                                                            # Deal a specified number of random cards
        if num_cards <= 0 or num_cards > len(self.deck):
            raise ValueError("Invalid number of cards to deal")                                                 # to check deal the card whether valid

        dealt_cards = self.deck[:num_cards]                                                                     # Use list it can a good way to list every shot
        self.deck = self.deck[num_cards:]
        return dealt_cards                                                                                      # return the dealt cards



    def display_cards(self, cards):
        return[f"{card['value']} of {card['suit']}" for card in cards]                                          # Convert card objects to human-readable format

    def compare_card(self,card1,card2):                                                                         # Compare the values of two cards

        suits_order = ['Clubs','Diamonds','Hearts','Spades']                                                    #create a deck of normal playing cards
        values_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        if values_order.index(card1['value']) > values_order.index(card2['value']):                             # use values and suits to compare the two cards numbers, and it can know
            return 1                                                                                            # return 1
        elif values_order.index(card1['value']) < values_order.index(card2['value']):
            return -1
        else:
            return suits_order.index(card1['suit']) - suits_order.index(card2['suit'])



def is_integer(user_input):
    try:
                                                                                                                # Try to convert the user input to an integer
        int_value = int(user_input)                                                                             # it can to cause the next one 'ask user' function that can don't use int, so it can to write down anythings
        return True
    except ValueError:
                                                                                                                # If conversion fails, it's not an integer
        return False

def print_card(card):                                                                                           # to change the 'suit' to be a symbol, it can good to see
    if card["suit"] == "Clubs":
        return str(card["value"]) + "♣️"
    if card["suit"] == "Diamonds":
        return str(card["value"]) + "♦️"
    if card["suit"] == "Spades":
        return str(card["value"]) + "♠️"
    if card["suit"] == "Hearts":
        return str(card["value"]) + "♥️"

def main():


    print("Welcome to the game of Compare. You will decide how many cards we get and then we'll play them one by one. ")
    print("Whoever has the higher card wins that round. Whoever wins the most rounds wins the game")

    while True:                                                                                                #it need while true to have a loop
        ask_user = input("How many cards should each player get? Enter a number between 1 and 26")

        if is_integer(ask_user):
            ask_user = int(ask_user)
            if ask_user >= 1 and ask_user <= 26:
                print("Dealer deals", ask_user, "cards to each player")
                break                                                                                          #if input is a correct answer,break the loop
            else:
                print("Invalid input. Please enter a number between 1 and 26")                                 #  If ask_user function input isn't nums, it should try again,

    deck = Deck()
    deck.shuffle_deck()

    player1_hand = deck.deal_cards(ask_user)
    player2_hand = deck.deal_cards(ask_user)
    print("Player 1 Hand:", end=" ")
    for card in player1_hand:                                                                                  # to deal every cards in a desk, and according to the cards numbers make a loop
        print(print_card(card), end=" ")
    print("")
    print("Player 2 Hand:", end=" ")
    for card in player2_hand:
        print(print_card(card), end=" ")
    print("")
    print("")

    player1_wins = 0
    player2_wins = 0                                                                                          # It's easy to count the number of wins for both sides

    for i in range(ask_user):
        print("Round " + str(i+1))
        card1 = player1_hand[i]
        card2 = player2_hand[i]
        print("Player 1:", end=" ")
        print(print_card(card1))
        print("Player 2:", end=" ")
        print(print_card(card2))
        play = deck.compare_card(card1,card2)                                                               # transfer compare _card functin

        if play > 0:
            print("Player 1 wins this round!")
            player1_wins = player1_wins + 1                                                                 # add 1 to the variable keeping track of duplicates
        else:
            print("Player 2 wins this round!")
            player2_wins = player2_wins + 1
        print("")

    print("Game over!")

    print("player 1 wins:", player1_wins, "rounds")                                                         # to count the number of wins for both sides
    print("player 2 wins:", player2_wins, "rounds")
    if player1_wins > player2_wins:
        print("Player 1 wins the game!")
    if player2_wins > player1_wins:
        print("Player 2 wins the game!")
    if player1_wins == player2_wins:
        print("It is a tie!")




if __name__ == '__main__':
    main()
