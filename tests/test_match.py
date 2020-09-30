import pytest
from match import Match
 
def test_PlayerOnePointsCheck():
    match = Match("player 1", "player 2")
    match.pointWonBy("player 1")
    assert match.score() == "games: 0-0, points: 15-love"
    match.pointWonBy("player 1")
    assert match.score() == "games: 0-0, points: 30-love"
    match.pointWonBy("player 1")
    assert match.score() == "games: 0-0, points: 40-love"
    match.pointWonBy("player 1")
    assert match.score() == "games: 1-0"

def test_PlayerTwoPointsCheck():
    match = Match("player 1", "player 2")
    match.pointWonBy("player 2")
    assert match.score() == "games: 0-0, points: 15-love"
    match.pointWonBy("player 2")
    assert match.score() == "games: 0-0, points: 30-love"
    match.pointWonBy("player 2")
    assert match.score() == "games: 0-0, points: 40-love"
    match.pointWonBy("player 2")
    assert match.score() == "games: 1-0"

def test_DeuceAdvantageCheck():
    match = Match("player 1", "player 2", 3, 4, 4, 3)
    match.pointWonBy("player 2")
    assert match.score() == "games: 3-4, points: deuce"
    match.pointWonBy("player 1")
    assert match.score() == 
        "games: 3-4, points: advantage player 1"

    match.pointWonBy("player 2")
    assert match.score() == "games: 3-4, points: deuce"
    match.pointWonBy("player 2")
    assert match.score() == 
        "games: 3-4, points: advantage player 2"
    )
    match.pointWonBy("player 2")
    assert match.score()) == "games: 3-5")

def test_Tiebreak():
    match = Match("player 1", "player 2", 6, 6, 4, 3)
    match.pointWonBy("player 2")
    assert match.score()) == "games: 6-6, points: tiebreak 4-4")
    match.pointWonBy("player 1")
    assert match.score()) == "games: 6-6, points: tiebreak 5-4")
    match.pointWonBy("player 2")
    assert match.score()) == "games: 6-6, points: tiebreak 5-5")
    match.pointWonBy("player 2")
    assert match.score()) == "games: 6-6, points: tiebreak 5-6")
    match.pointWonBy("player 2")
    assert match.score()) == "games: 6-7")