import random

def create_deck():
    suits = ["Spades","Hearts","Diamonds","Clubs"]
    ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    
    deck = []
    
    for suit in suits:
        for rank in ranks:
            deck.append((suit,rank))
            
    return deck

def final_winner(card1, card2):
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    rank_one = card1.split()[0]
    rank_two = card2.split()[0]
    
    if ranks.index(rank_one) > ranks.index(rank_two):
        return "Player One"
    elif ranks.index(rank_two) > ranks.index(rank_one):
        return "Player Two"
    else:
        return "No one won"


def main():
    deck = create_deck()
    random.shuffle(deck)
    
    while len(deck)>=2:
        player_one = deck.pop(0) 
        player_two = deck.pop(0) 
        
        winner  = final_winner(player_one,player_two)
        
        print("Player one draws the card", player_one)
        print("Player two draws the card", player_two)
        print(winner, "wins")
        
        input("Press enter to play again\n")
        
    print("Deck empty. Goodbye")

main()