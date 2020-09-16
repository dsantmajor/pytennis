

import pytest
from pytennis import Match
from docopt import docopt
import sys

def test_print_variables():

    # Setup
    player_name = "Don"
    opponent_name = "Rowena"
    output_player_name = 'Name: Don Points Won: 0 Games Won: 0  Sets Won: 0'
    output_opponent_name = 'Name: Rowena Points Won: 0 Games Won: 0  Sets Won: 0'

    # Exercise

    match = Match(player_name, opponent_name)
    # match.print_variables()
    result_player_name = match.print_variables(player_name)
    result_opponent_name = match.print_variables(opponent_name)

    # Verify
    assert result_player_name == output_player_name
    assert result_opponent_name == output_opponent_name

    # Clean-up 
    


def notest_points_won_by():

    # Setup
    player_name = "Don"
    opponent_name = "Rowena"
    output = " "

    # Exercise
    match = Match(player_name, opponent_name)
    match.points_won_by("Don")
    result = match.score()

    # Verify
    
    assert result == output

    # Cleanup

def notest_reset_points_games():
    
    # Setup
    player_name = "Don"
    opponent_name = "Rowena"

    # Exercise
    match = Match(player_name, opponent_name)
    actual = match.reset_points_games(player_name)
    expected = 'Player Name: Don Points_Won: 0 Games_won: 0'

    # Verify
    
    assert actual == expected

    # Cleanup




