import pytest
import random
import session6
import os
import inspect
import re
import test_session6

README_CONTENT_CHECK_FOR = [
    'royal_flush',
    'straight_flush',
    'four_kind',
    'full_house',
    'flush',
    'straight',
    'three_kind',
    'two_pair',
    'one_pair',
    'high_card',
    'lambda',
    'map',
    'zip',
]

deck = [('6', 'hearts'), ('7', 'diamonds'), ('9', 'diamonds'), ('king', 'diamonds'), ('5', 'diamonds'), ('3', 'diamonds'), ('10', 'hearts'), ('2', 'hearts'), ('6', 'clubs'), ('10', 'clubs'), ('jack', 'diamonds'), ('king', 'spades'), ('ace', 'hearts'), ('2', 'clubs'), ('8', 'clubs'), ('jack', 'hearts'), ('7', 'clubs'), ('2', 'diamonds'), ('10', 'diamonds'), ('jack', 'clubs'), ('ace', 'clubs'), ('9', 'spades'), ('8', 'hearts'), ('5', 'spades'), ('6', 'diamonds'), ('7', 'hearts'),
        ('8', 'diamonds'), ('4', 'spades'), ('10', 'spades'), ('queen', 'diamonds'), ('6', 'spades'), ('4', 'hearts'), ('3', 'clubs'), ('ace', 'diamonds'), ('queen', 'spades'), ('9', 'clubs'), ('4', 'clubs'), ('5', 'clubs'), ('3', 'hearts'), ('jack', 'spades'), ('5', 'hearts'), ('8', 'spades'), ('king', 'hearts'), ('4', 'diamonds'), ('ace', 'spades'), ('7', 'spades'), ('9', 'hearts'), ('king', 'clubs'), ('queen', 'hearts'), ('3', 'spades'), ('queen', 'clubs'), ('2', 'spades')]
suits = ['spades', 'clubs', 'hearts', 'diamonds']
cards = ['2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'jack', 'queen', 'king', 'ace']

CHECK_FOR_THINGS_NOT_ALLOWED = []


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r", encoding="utf8")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_count():
    functions = inspect.getmembers(test_session6, inspect.isfunction)
    assert len(functions) > 20, 'Test cases seems to be low. Work harder man...'


def test_function_repeatations():
    functions = inspect.getmembers(test_session6, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'


def test_deck_lam():
    assert set(session6.deck_lam) == set(
        deck), 'Incorrect cards using Lambda operation'
    assert len(
        session6.deck_lam) == 52, 'Incorrect number of cards using Lambda operation'


def test_deck_func():
    assert set(session6.create_deck(
        cards, suits)) == set(deck), 'Incorrect cards using normal function'
    assert len(session6.create_deck(suits, cards)
               ) == 52, 'Incorrect number of cards using normal function'


def test_royal_flush():
    hand = [('ace', 'hearts'), ('king', 'hearts'),
            ('queen', 'hearts'), ('10', 'hearts'), ('jack', 'hearts')]
    assert session6.royal_flush(
        hand)[0][0] == 1, 'royal_flush hand check failed'


def test_straight_flush():
    hand = [('9', 'spades'), ('8', 'spades'), ('queen', 'spades'),
            ('jack', 'spades'), ('10', 'spades')]
    assert session6.straight_flush(
        hand)[0][0] == 2, 'straight_flush hand check failed'


def test_four_kind():
    hand = [('7', 'hearts'), ('7', 'diamonds'),
            ('7', 'spades'), ('7', 'clubs'), ('10', 'spades')]
    assert session6.four_kind(hand)[0][0] == 3, 'four_kind hand check failed'


def test_full_house():
    hand = [('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'),
            ('king', 'spades'), ('king', 'diamonds')]
    assert session6.full_house(hand)[0][0] == 4, 'full_house hand check failed'


def test_flush():
    hand = [('9', 'spades'), ('2', 'spades'), ('3', 'spades'),
            ('4', 'spades'), ('7', 'spades')]
    assert session6.flush(hand)[0][0] == 5, 'flush hand check failed'


def test_straight():
    hand = [('9', 'clubs'), ('king', 'diamonds'), ('queen', 'spades'),
            ('jack', 'spades'), ('10', 'hearts')]
    assert session6.straight(hand)[0][0] == 6, 'straight hand check failed'


def test_three_kind():
    hand = [('queen', 'hearts'), ('queen', 'spades'),
            ('queen', 'clubs'), ('jack', 'spades'), ('10', 'spades')]
    assert session6.three_kind(hand)[0][0] == 7, 'three_kind hand check failed'


def test_two_pair():
    hand = [('king', 'hearts'), ('king', 'spades'),
            ('queen', 'spades'), ('queen', 'hearts'), ('10', 'spades')]
    assert session6.two_pair(hand)[0][0] == 8, 'two_pair hand check failed'


def test_one_pair():
    hand = [('king', 'clubs'), ('king', 'spades'),
            ('jack', 'spades'), ('queen', 'clubs'), ('10', 'spades')]
    assert session6.one_pair(hand)[0][0] == 9, 'one_pair hand check failed'


def test_high_card():
    hand = [('9', 'spades'), ('queen', 'diamonds'),
            ('5', 'spades'), ('jack', 'clubs'), ('10', 'clubs')]
    assert session6.high_card(hand)[0][0] == 10, 'high_card hand check failed'


def test_20_combos():

    # 1
    p1 = [('3', 'diamonds'), ('ace', 'hearts'),
          ('3', 'hearts'), ('9', 'spades'), ('4', 'diamonds')]
    p2 = [('queen', 'spades'), ('queen', 'hearts'),
          ('8', 'clubs'), ('5', 'spades'), ('7', 'hearts')]
    assert 'Player 2' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 2
    p1 = [('6', 'hearts'), ('7', 'spades'), ('9', 'spades')]
    p2 = [('2', 'clubs'), ('ace', 'clubs'), ('5', 'clubs')]
    assert 'Player 2' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 3
    p1 = [('3', 'diamonds'), ('4', 'diamonds'), ('2', 'spades')]
    p2 = [('2', 'clubs'), ('ace', 'clubs'), ('5', 'clubs')]
    assert 'Player 2' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 4
    p1 = [('3', 'spades'), ('2', 'hearts'), ('3', 'hearts'),
          ('2', 'clubs'), ('queen', 'hearts')]
    p2 = [('king', 'diamonds'), ('7', 'spades'),
          ('8', 'diamonds'), ('8', 'spades'), ('ace', 'hearts')]
    assert 'Player 1' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 5
    p1 = [('jack', 'diamonds'), ('8', 'diamonds'), ('10', 'diamonds')]
    p2 = [('8', 'clubs'), ('6', 'diamonds'), ('7', 'diamonds')]
    assert 'Player 1' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 6
    p1 = [('3', 'clubs'), ('10', 'diamonds'),
          ('king', 'hearts'), ('ace', 'diamonds')]
    p2 = [('queen', 'clubs'), ('king', 'diamonds'),
          ('queen', 'hearts'), ('9', 'spades')]
    assert 'Player 2' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 7
    p1 = [('5', 'spades'), ('6', 'spades'), ('4', 'diamonds'), ('3', 'clubs')]
    p2 = [('8', 'spades'), ('8', 'hearts'), ('2', 'hearts'), ('5', 'diamonds')]
    assert 'Player 1' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 8
    p1 = [('8', 'spades'), ('8', 'diamonds'),
          ('6', 'hearts'), ('6', 'clubs'), ('4', 'spades')]
    p2 = [('ace', 'diamonds'), ('queen', 'diamonds'),
          ('queen', 'clubs'), ('queen', 'hearts'), ('4', 'diamonds')]
    assert 'Player 2' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 9
    p1 = [('ace', 'spades'), ('ace', 'diamonds'),
          ('jack', 'spades'), ('ace', 'clubs')]
    p2 = [('jack', 'hearts'), ('5', 'diamonds'),
          ('7', 'hearts'), ('8', 'diamonds')]
    assert 'Player 1' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 10
    p1 = [('3', 'clubs'), ('2', 'spades'), ('10', 'hearts'),
          ('6', 'clubs'), ('9', 'diamonds')]
    p2 = [('6', 'diamonds'), ('7', 'spades'), ('7', 'clubs'),
          ('jack', 'hearts'), ('7', 'diamonds')]
    assert 'Player 2' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 11
    p1 = [('jack', 'clubs'), ('queen', 'clubs'),
          ('10', 'clubs'), ('king', 'clubs'), ('ace', 'clubs')]
    p2 = [('jack', 'hearts'), ('5', 'diamonds'),
          ('7', 'hearts'), ('8', 'diamonds'), ('7', 'clubs')]
    assert 'Player 1' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 12
    p1 = [('jack', 'clubs'), ('queen', 'clubs'),
          ('10', 'clubs'), ('king', 'clubs'), ('9', 'clubs')]
    p2 = [('jack', 'hearts'), ('5', 'diamonds'),
          ('7', 'hearts'), ('8', 'diamonds'), ('7', 'clubs')]
    assert 'Player 1' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 13
    p1 = [('3', 'hearts'), ('10', 'hearts'),
          ('king', 'hearts'), ('8', 'hearts')]
    p2 = [('4', 'clubs'), ('jack', 'hearts'),
          ('9', 'diamonds'), ('6', 'hearts')]
    assert 'Player 1' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 14
    p1 = [('9', 'hearts'), ('7', 'spades'), ('6', 'hearts'), ('2', 'diamonds')]
    p2 = [('jack', 'hearts'), ('8', 'diamonds'),
          ('jack', 'spades'), ('8', 'clubs')]
    assert 'Player 2' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 15
    p1 = [('7', 'clubs'), ('4', 'hearts'), ('6', 'hearts'), ('ace', 'clubs')]
    p2 = [('jack', 'clubs'), ('jack', 'hearts'),
          ('jack', 'spades'), ('3', 'clubs')]
    assert 'Player 2' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 16
    p1 = [('queen', 'hearts'), ('king', 'hearts'),
          ('ace', 'hearts'), ('jack', 'hearts')]
    p2 = [('4', 'diamonds'), ('9', 'spades'),
          ('6', 'clubs'), ('king', 'clubs')]
    assert 'Player 1' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 17
    p1 = [('5', 'clubs'), ('6', 'clubs'), ('4', 'clubs')]
    p2 = [('king', 'spades'), ('2', 'spades'), ('jack', 'spades')]
    assert 'Player 1' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 18
    p1 = [('6', 'hearts'), ('6', 'spades'), ('6', 'clubs')]
    p2 = [('2', 'spades'), ('5', 'diamonds'), ('jack', 'clubs')]
    assert 'Player 1' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 19
    p1 = [('4', 'spades'), ('9', 'spades'), ('9', 'hearts'),
          ('3', 'spades'), ('6', 'diamonds')]
    p2 = [('5', 'clubs'), ('6', 'clubs'), ('2', 'clubs'),
          ('3', 'clubs'), ('4', 'clubs')]
    assert 'Player 2' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."

    # 20
    p1 = [('4', 'diamonds'), ('3', 'diamonds'), ('2', 'diamonds'),
          ('6', 'diamonds'), ('5', 'diamonds')]
    p2 = [('5', 'clubs'), ('9', 'spades'), ('queen', 'clubs'),
          ('2', 'spades'), ('ace', 'hearts')]
    assert 'Player 1' in session6.winner(
        p1, p2), "Your function has taken bribe, declaring incorrect winners."
