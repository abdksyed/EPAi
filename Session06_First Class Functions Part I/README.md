# Assignemt 6 - First Class Functions Part I

## Topics Covered:

* Default Values

* Docstrings and Annotations

* Lambda Expressions

* Fucntional Introspection

* Callables

* Map, Filter and Zip

## Link to Class Notebook (along with Notes)

[Class Notebook with extra Notes.](https://github.com/abdksyed/EPAi/blob/master/Session06_First%20Class%20Functions%20Part%20I/notebooks/Session06_Notes.ipynb)


# Pokers

This is a fun assignment, where we need to check, according to the rules of Pokers, which of the player hand of cards wins. The winner is decided on the basis of rank allotted according to the following sequence:

![](poker.jpg)

But first we need to create a deck of cards, right? Let's start from the beginning.

## Creating the deck


Method 1:

```python
deck_lam = list(map(lambda x: (x[0], x[1]), zip(vals*4, suits*13)))
```

Method 2:

```python
def create_deck(vals: 'List/Set of Values',
                suits: 'List/Set of Suits',
                number_of_decks: 'Total Number of Decks to be Used' = 1) -> 'Set of Deck':
    '''
    A function which creates a deck of playing cards.
    Inputs:
    vals: The values of cards of each suit.
    suits: The diffrent suits of cards.
    number_of_decks: Number of decks to be used.
    Returns:
    deck: Set of Cards.
    '''
    deck = set()
    for _ in range(number_of_decks):
        for suit in suits:
            for val in vals:
                deck.add((val, suit))
    return deck
```

## Checking the rank

Next, to declare a winner, we need to find the rank of the card sets with each player and then decide on the winner. To reduce the complexity, in this section, we discuss the function whose task is to just return the rank according to the rules. All the checks on the cards will be performed by the function which calls this and we would discuss that one in the coming section.

Let's look at the function.

```python
def royal_flush(hand):
    '''
    Check if hand is a Royal Flush.
    Input: The set of card - hand
    Output:
    If True, Return (Rank:1, string), (14)
    If False, Return False, None
    '''
    val = [x[0] for x in hand]
    suit = [x[1] for x in hand]
    royal_flush = ['ace', 'king', 'queen', 'jack', '10']
    if len(set(suit)) != 1:
        return False, None
    k = 0
    for i in range(len(hand)):
        if val[i] in royal_flush[:len(hand)]:
            k += 1
    if k == len(hand):
        return (1, 'WOW!!!!. You got a "ROYALLLLLLL FLUSH!"(Rank:1)'), (14,)
    return False, None


def straight_flush(hand):
    '''
    Check if hand is a Straight Flush.
    Input: The set of card - hand
    Output:
    If True, Return (Rank:2, string), (Descending Order of Card Values)
    If False, Return False, None
    '''
    flu, _ = flush(hand)
    stra, num = straight(hand)
    if flu and stra:
        return (2, 'You are Amazing, its a "STRAIGHT FLUSH!!!!"(Rank:2)'), (num,)
    return False, None


def four_kind(hand):
    '''
    Check if hand is a Four of a Kind.
    Input: The set of card - hand
    Output:
    If True, Return (Rank:3, string), (Card Value)
    If False, Return False, None
    '''
    val = [conv_card_to_num(x[0]) for x in hand]
    suit = [x[1] for x in hand]
    if len(set(suit)) != 4:
        return False, None
    dict_val = {i: val.count(i) for i in val}
    for k, v in dict_val.items():
        if v == 4:
            return (3, 'You have all suits of a card, "FOUR OF A KIND"(Rank:3)'), (k,)
    return False, None


def full_house(hand):
    '''
    Check if hand is a Full House.
    Input: The set of card - hand
    Output:
    If True, Return (Rank:4, string), (Three Kind Card Value, Pair Card Value)
    If False, Return False, None
    '''
    thr, num_3 = three_kind(hand)
    op, num_2 = one_pair(hand)
    if thr and op:
        return (4, 'That is a "FULL HOUSE(Rank:4)"'), (num_3[0], num_2[0])
    return False, None


def flush(hand):
    '''
    Check if hand is a Flush.
    Input: The set of card - hand
    Output:
    If True, Return (Rank:5, string), (Three Kind Card Value, Pair Card Value)
    If False, Return False, None
    '''
    val = [conv_card_to_num(x[0]) for x in hand]
    val.sort()
    suit = [x[1] for x in hand]
    if len(set(suit)) != 1:
        return False, None
    return (5, 'You "FLUSHed it"(Rank:5)'), tuple(val[::-1])


def straight(hand):
    '''
    Check if hand is a Straight.
    Input: The set of card - hand
    Output:
    If True, Return (Rank:6, string), (Descending Order of Card Values)
    If False, Return False, None
    '''
    val = [conv_card_to_num(x[0]) for x in hand]
    val.sort()
    k = 0
    for i in range(len(hand)-1):
        if val[i] == val[i+1]-1:
            k += 1
    if k == len(hand)-1:
        return (6, 'What a "STRAIGHT" drive(RANK:6)'), tuple(val[::-1])
    return False, None


def three_kind(hand):
    '''
    Check if hand is a Three of a Kind.
    Input: The set of card - hand
    Output:
    If True, Return (Rank:7, string), (Three Kind Card Value,)
    If False, Return False, None
    '''
    val = [conv_card_to_num(x[0]) for x in hand]
    suit = [x[1] for x in hand]
    if len(set(suit)) < 3:
        return False, None
    dict_val = {i: val.count(i) for i in val}
    for k, v in dict_val.items():
        if v == 3:
            return (7, 'Go for 3, "THREE OF A KIND"(Rank:7)'), (k,)
    return False, None


def two_pair(hand):
    '''
    Check if hand is a Two Pairs.
    Input: The set of card - hand
    Output:
    If True, Return (Rank:8, string), (Higher Pair Value, Lower Pair Value, Final Card Value)
    If False, Return False, None
    '''
    p1, n1 = one_pair(hand)
    if not p1:
        return False, None
    left_over_hand = [x for x in hand if conv_card_to_num(x[0]) != n1[0]]
    p2, n2 = one_pair(left_over_hand)
    if p1 and p2:
        final_card_val = [conv_card_to_num(
            x[0]) for x in left_over_hand if conv_card_to_num(x[0]) != n2[0]]
        return (8, 'This is good, "TWO PAIRS" haan (Rank:8)'), (max(n1[0], n2[0]), min(n1[0], n2[0]), *final_card_val)
    return False, None


def one_pair(hand):
    '''
    Check if hand is a One Pair.
    Input: The set of card - hand
    Output:
    If True, Return (Rank:9, string), (Pair Card Value, Descending Order of Remaining Card Values)
    If False, Return False, None
    '''
    val = [conv_card_to_num(x[0]) for x in hand]
    val.sort()
    dict_val = {i: val.count(i) for i in val}
    for k, v in dict_val.items():
        if v == 2:
            left_over_val = [conv_card_to_num(
                x[0]) for x in hand if conv_card_to_num(x[0]) != k]
            left_over_val.sort()
            return (9, 'Good! It is a "PAIR"(Rank:9)'), (k, *left_over_val[::-1])
    return False, None


def high_card(hand):
    '''
    Input: The set of card - hand
    Output:
    Return (Rank:10, string), (Descending Order of Card Values)
    '''
    val = [conv_card_to_num(x[0]) for x in hand]
    val.sort()
    return (10, f'Only hope is your High Card must be good enough(Rank:10)'), tuple(val[::-1])
```

This function not only returns the rank, but also returns the card values oin proper orders in the set to help in tie braking, if required.

## Misc Functions:

This function converts the Jack, Quen, King and Ace to respective values of 11, 12, 13 and 14.
```python
def conv_card_to_num(card: 'Value of the Card in String') -> 'Value of Card in int':
    if card == 'ace':
        return 14
    if card == 'king':
        return 13
    if card == 'queen':
        return 12
    if card == 'jack':
        return 11
    return int(card)
```

This function creates two random players, with each player holding either 3/4/5 cards.
```python
def create_player(deck, cards_per_player=5):
    print('----SHUFFLING---')
    p1_hand = random.sample(tuple(deck), cards_per_player)
    p2_hand = random.sample(tuple(deck-set(p1_hand)), cards_per_player)
    print('----Lightening Speed Distribution Later---')
    print('Hey P1, you got: ', p1_hand)
    print('Hey P2, you got: ', p2_hand)
    print('------------------------------------------')

    return p1_hand, p2_hand
```

## Who's the winner!

The Final function, to check who is the winner based on the hand (set of cards) the player gets.  
The function first sets the win cases according to the number fo cards per player.  
Then for each rank in win cases, the hand is passed and checked if it holds the patterns from Rank 1 to 10, and it stops checking if it find the rank, or else at last Rank 10 is assigned.

```python
def winner(p1_hand, p2_hand):
    win_cases = {
        5: [royal_flush, straight_flush, four_kind, full_house, flush, straight, three_kind, two_pair, one_pair, high_card],
        4: [royal_flush, straight_flush, four_kind, flush, straight, three_kind, two_pair, one_pair, high_card],
        3: [royal_flush, straight_flush, flush, straight, three_kind, one_pair, high_card]
    }
    if len(p1_hand) != len(p2_hand):
        raise ValueError('Unequal Number of Cards for P1 and P2')
    cards_per_player = len(p1_hand)
    win_case = win_cases[cards_per_player]
    p1_rank, p2_rank = 0, 0

    for case in win_case:
        if not p1_rank:
            p1_res = case(p1_hand)
            if p1_res[0]:
                p1_rank = p1_res[0][0]
                p1_stat = p1_res[0][1]
                p1_high = p1_res[1]
        if not p2_rank:
            p2_res = case(p2_hand)
            if p2_res[0]:
                p2_rank = p2_res[0][0]
                p2_stat = p2_res[0][1]
                p2_high = p2_res[1]

    print(f'Hey P1: {p1_stat}, with order of highest cards as: {p1_high}')
    print(f'Hey P2: {p2_stat}, with order of highest cards as: {p2_high}')
    print('------------------------------------------')
    if p1_rank < p2_rank:
        return f'Congratulations Player 1, you WON! as you had better hand.'
    elif p1_rank > p2_rank:
        return f'Congratulations Player 2, you WON! as you had better hand.'
    else:
        print('---TIE BREAKER CHECK:---')
        for p1_c, p2_c in zip(p1_high, p2_high):
            if p1_c > p2_c:
                return f'Congratulations Player 1, you have Won! as you had better high card {p1_c} than {p2_c}'
            elif p1_c < p2_c:
                return f'Congratulations Player 2, you have Won! as you had better high card {p2_c} than {p1_c}'
        else:
            return 'MAN....this is very rare....Its a TOTAL TIE!'
```