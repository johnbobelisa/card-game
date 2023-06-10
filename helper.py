from cards import Rank, Suit, Card

def int_input(prompt="", restricted_to=None):
    """
    Helper function that modifies the regular input method,
    and keeps asking for input until a valid one is entered. Input 
    can also be restricted to a set of integers.

    Arguments:
        - prompt: String representing the message to display for input
        - restricted: List of integers for when the input must be restricted
                    to a certain set of numbers

    Returns the input in integer type.
    """
    while True:
        player_input = input(prompt)
        try:                           
            int_player_input = int(player_input)
        except ValueError:
            continue
        if restricted_to is None:
            break
        elif int_player_input in restricted_to:
            break

    return int_player_input

# create deck
def deck() :
    deck=[]
    for suit in Suit:
        for rank in Rank:
            deck.append(Card(rank,suit))
    return (deck)