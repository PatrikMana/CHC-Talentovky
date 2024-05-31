import random

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

# Funkce create_deck() vytváří nový balíček karet
def create_deck():
    deck = []
    for card in cards:
        for _ in range(4):
          deck.append(card)
    return deck

# Funkce get_card(deck) získává jednu kartu z balíčku
def get_card(deck):
  index = random.randint(0, len(deck) - 1)
  card = deck[index]
  del deck[index]
  return card

# Zapne 1 hru Black Jacku
def play_21():
    deck = create_deck()
    player_cards = []
    dealer_cards = []
    player_cards.append(get_card(deck))
    player_cards.append(get_card(deck))
    dealer_cards.append(get_card(deck))
    dealer_cards.append(get_card(deck))

    # Skóre krupiéra a hráče
    player_score = sum([card_values[card] for card in player_cards])
    dealer_score = sum([card_values[card] for card in dealer_cards])

    print("--------------------------")
    print("Hráč:", " ".join(player_cards), "(" + str(player_score) + ")")
    print("Krupiér:", dealer_cards[0], "XX")

    # Kolo hráče
    while player_score < 21:
        print("--------------------------")
        choice = input("Chcete si nechat přidat další kartu (ano/ne)? ")
        if choice.lower() == "ano":
            player_cards.append(get_card(deck))
            player_score = sum([card_values[card] for card in player_cards])
            print("--------------------------")
            print("Hráč:", " ".join(player_cards), "(" + str(player_score) + ")")
            print("Krupiér:", dealer_cards[0], "XX")
        elif choice.lower() == "ne":
            break
        else:
            print("--------------------------")
            print("Neplatná Odpověď")   
    
    #Hráč přebral a automaticky prohrál
    if player_score > 21:
        print("--------------------------")
        print("Hráč prohrál!")
        return
    
    print("--------------------------")
    print("Hráč skončil, na řadě je krupiér.")

    #Krupiérovo kolo
    while dealer_score < 17:
        dealer_cards.append(get_card(deck))
        dealer_score = sum([card_values[card] for card in dealer_cards])

    print("--------------------------")
    print("Hráč:", " ".join(player_cards), "(" + str(player_score) + ")")
    print("Krupiér:", " ".join(dealer_cards), "(" + str(dealer_score) + ")")

    #Porovnání výsledků    
    if dealer_score >= 22:
        print("--------------------------")
        print("Hráč vyhrál!")
    elif player_score > dealer_score:
        print("--------------------------")
        print("Hráč vyhrál!")
    elif player_score == dealer_score:
        print("--------------------------")
        print("Remíza!")
    elif player_score < dealer_score:
        print("--------------------------")
        print("Hráč prohrál!")

# Opakování hry
def play_round():
    
    play_21()
    print("--------------------------")
    play_again = input("Chcete zahrát znovu? (ano/ne) ")
    if play_again.lower() == "ano":
        play_round()
        
play_round()