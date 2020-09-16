

import pytest
from pytennis import Match
from docopt import docopt
import sys

def test_print_variables():

    # Setup
    player_name = "Don"
    opponent_name = "Rowena"
    output = 'Name: Rowena Points Won: 0 Games Won: 0  Sets Won: 0'

    # Exercise

    match = Match(player_name, opponent_name)
    # match.print_variables()
    result = match.print_variables()

    # Verify
    assert result == output

    # Clean-up 
    


def test_points_won_by():

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

