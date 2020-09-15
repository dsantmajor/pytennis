

import pytest
from pytennis import Match
from docopt import docopt
import sys

def test_print_variables():
    
    match = Match("Don", "Rowena")
    # match.print_variables()
    assert match.print_variables() == None

def test_points_won_by():
    match = Match("Don", "Rowena")
    match.points_won_by("Don")
    match.points_won_by("Rowena")
    match.score()
    match.points_won_by("Don")
    match.points_won_by("Don")
    match.score()
    match.points_won_by("Rowena")
    match.points_won_by("Rowena")
    match.score()
    match.points_won_by("Don")
    match.score()
    match.points_won_by("Don")
    match.score()