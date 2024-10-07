import random

print("Catch The Joker!")
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [f'{rank} of {suit}' for suit in suits for rank in ranks]

deck.append('Joker')
weights = []


def set_probabilities(deck):
    for card in deck:
        if card == 'Joker':
            # Joker should have a probability of 1/53
            weights.append(1/53)
        elif card == 'Ace':
            # Ace should have a probability of 4/53
            weights.append(4/53)
        elif 'Hearts' in card or 'Diamonds' in card:
            # Hearts and Diamonds together should have a probability of 24/53, distributed across 26 cards
            weights.append(24/53)  # Each Heart and Diamonds card gets equal weight
        elif 'Clubs' in card or 'Spades' in card:
            # Clubs and Spades (excluding Ace of Spades) should have a probability of 24/53, distributed across 25 cards
            weights.append(24/53)  # Each Clubs and Spades card gets equal weight
    return weights


def probability_draw(deck, weights, number_of_cards):
    return random.choices(deck, weights=weights, k=number_of_cards)


def draw_card(deck):
    card = random.choice(deck)
    return card


def draw_cards(deck, number_of_cards):
    drawn_cards = []
    for _ in range(number_of_cards):
        card = draw_card(deck)
        if card:
            drawn_cards.append(card)
    return drawn_cards


def winningsTotal(cards):
    RoundEach = []
    total = 0
    for card in cards:
        # Joker rule
        if 'Joker' in card:
            total += 40
            RoundEach.append(40)
        # Ace of Spades rule
        elif 'Ace' in card:
            total += 15
            RoundEach.append(15)
        # Hearts and Diamonds rule
        elif 'Hearts' in card or 'Diamonds' in card:
            total += 3
            RoundEach.append(3)
        # Clubs and Spades rule
        elif 'Clubs' in card or 'Spades' in card:
            total += 2
            RoundEach.append(2)
    return RoundEach

# Main function
def main():
    set_probabilities(deck)  # Set probabilities based on desired distribution

    drawAgain = 'Y'
    while drawAgain == 'Y':
        drawNumber = int(input("How many cards do you want to draw? "))

        # Draw cards with custom probabilities
        cards = probability_draw(deck, weights, drawNumber)

        print("You drew the following cards:")
        #for card in cards:
            #print(card)

        # Calculate and print the total winnings
        total_winnings = winningsTotal(cards)
        for total_winnings in total_winnings:
            print(total_winnings)
        print(f"Your total winnings are: {total_winnings} points")

        drawAgain = input("Would you want to draw again? (Y/N): ").upper()

    if drawAgain == 'N':
        print('Thank You!')

main()
