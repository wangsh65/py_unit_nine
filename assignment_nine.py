
#https://gist.github.com/JenkinsDev/1e4bff898c72ec55df6f
#https://chat.openai.com/c/97a28349-28dc-46db-bd07-f49f264d65bc

import random
class Card:


    def __init__(self,rank_orders, suit):
        self.rank_orders = rank_orders
        self.sult = suit

    def _lt_(self,c2):
        if self.rank_orders < c2.rank_orders:
            return True
        if self.rank_orders == c2.rank_orders:
            if self. suits <c2.suit:
                return True
            else: return False

        return False

class Deck:
    def __init__(self):
        # Initialize a standard deck of cards
        self.suits = ['Hearts', 'Spades', 'Diamond', 'Clubs']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [{'suit': suit, 'value': value} for suit in self.suits for value in self.values]

    def shuffle_deck(self):
        # Fisher-Yates shuffle algorithm
        n = len(self.deck)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]


    def deal_cards(self, num_cards):
        # Deal a specified number of random cards
        dealt_cards = self.deck[:num_cards]
        self.deck = self.deck[num_cards:]
        return dealt_cards

    def display_cards(self, cards):
        # Convert card objects to human-readable format
        return [f"{card['value']} of {card['suit']}" for card in cards]





def main():
    deck = Deck()
    deck.shuffle_deck()

    print(deck)

    ask_user = int(input("How many cards should each player get? Enter a number between 1 and 26"))
    if ask_user > 1 or ask_user <26 :
        print("Dealer deals",ask_user,"cards to each player")
    else:
        print("Invalid input. Please enter a number between 1 and 26")



    player1_hand = deck.deal_cards(ask_user)
    player2_hand = deck.deal_cards(ask_user)
    print(player1_hand)
    print(player2_hand)

    suits_order = ['Hearts', 'Spades', 'Diamond', 'Clubs']
    values_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']



    if values_order.index(player1_hand['values']) >values_order.index(player2_hand['values']):
        print("player 1 won")
        return 1
    elif values_order.index(player1_hand['values']) < values_order.index(player2_hand['values']):
        print("player 2 won")
        return -1
    else:
        print("tie")
        return suits_order .index(player1_hand['suits']) - suits_order.index(player2_hand['suits'])

if __name__ == '__main__':
    main()
