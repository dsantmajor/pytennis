
"""
pytennis

Usage:
  pytennis.py --player-name <player-name>  --opponent-name <opponent-name>

Parameters:
  --player-name <player-name>            Provide name of a player Ex: Federer
  --opponent-name <opponent-name>        Provide name of an Opponent Ex: Nadal
  
Options:
  -h --help                 Show this screen.
  --version                 Show version.
 
"""

from docopt import docopt
import sys


class Player:

    def __init__(self, player_name):
        self._name = player_name
        self._points_won = 0
        self._games_won = 0
        self._sets_won = 0
        self._tiebrk_points_won = 0


class Match(Player):
    """A class used to represent a Tennis match

        ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    print_variables()
        Prints the player's and opponet's name, points_won, games_won, sets_won to the console

    p1_reset_points_games()
        Resets player's and opponet's points_won and games_won values to zero.

    convert_points_to_score()
        Converts points to tennis score representation
            | Point | Score |
            | ----- | ----- |
            | 0     | 0     |
            | 1     | 15    |
            | 2     | 30    |
            | 3     | 40    |
    score()
        prints the current score for each player and opponent

    p2_reset_points_games()
        Resets player's and opponet's points_won and games_won values to zero.

    points_won_by(player_name):
        Increments the points by one for a player / opponent
        Before doing that it checks for games won, sets won, deuce and advantage



    """
    all_players = []

    def __init__(self, player1_name: Player, player2_name: Player):
        self.players = [ Player(player1_name), Player(player2_name)]

    def print_variables(self, given_name):
        """Prints the player's and opponet's name, points_won, games_won, sets_won to the console

        Returns:
            [str]: [the player's and opponet's name, points_won, games_won, sets_won to the console]
        """
        for player in self.players:
            # print (n._name)
            if given_name == player._name:
                print(f"{player._name}")
                print(f"{player._points_won}")
                player._points_won += 1
                print(f"{player._points_won}")
        # print(f"Name: {self._p1._name} Points Won: {self._p1._points_won} Games Won: {self._p1._games_won}  Sets Won: {self._p1._sets_won}")
        # print(f"Name: {self._p2._name} Points Won: {self._p2._points_won} Games Won: {self._p2._games_won}  Sets Won: {self._p2._sets_won}")
        # return f"Name: {self._name} Points Won: {self._points_won} Games Won: {self._games_won}  Sets Won: {self._sets_won}"

    def reset_points_games(self):
        """ Reset points and games

            Resets player's and opponet's points_won and games_won values to zero.
        """
        # self._player = "make a function to get player name " "call by dictionary"
        for player in self.players:
            player._points_won = 0
            player._games_won = 0
            print(f"Name: {player._name}; Points Won: {player._points_won}, Games Won: {player._games_won}")
            
        # return f"Player Name: {player._name} Points_Won: {player._points_won} Games_won: {player._games_won}"
         
    def convert_points_to_score(self, player_name):
        """Converts points to tennis score representation

        Args:
            player_name ([str]): [Name of the player or opponent]

        Returns:
            [int]: [tennis score representation]
        """
        for player in self.players:
            if player_name == player._name:
                if player._points_won == 0:
                    return "Love"
                elif player._points_won == 1:
                    return 15
                elif player._points_won == 2:
                    return 30
                elif player._points_won == 3:
                    return 40
   

    def score(self):
        # pass
        """Provides a summary of the current score
           Games won, points won for each player and opponet

        Returns:
            [empty]: [empty]

            When we call match.score();

            Example outputs:
            this will return "0-0, 15-15"

            this will return "0-0, 40-15"

            this will return "0-0, Deuce"

            this will return "0-0, Advantage player 1"

            this will return "1-0"
        """
        
        print(self.players[0])

        if self.players[0]._points_won >= 3 and self.players[1]._points_won >= 3 and self.players[0]._points_won - self.players[1]._points_won == 0:
            print(f"{self.players[0]._games_won} - {self.players[1]._games_won}, Deuce")
        elif self.players[1]._points_won >= 3 and self.players[0]._points_won >= 3 and self.players[1]._points_won - self.players[0]._points_won == 1:
            print(f"{self.players[0]._games_won} - {self.players[1]._games_won}, Advantage {self.players[1]._name}")
        elif self.players[0]._points_won >= 3 and self.players[1]._points_won >= 3 and self.players[0]._points_won - self.players[1]._points_won == 1:
            print(f"{self.players[0]._games_won} - {self.players[1]._games_won}, Advantage {self.players[0]._name}")
        else:
            # print(f"P1_games_won - P2_games_won, P1_points_won - P2_points_won")
            print(f"{self.players[0]._games_won} - {self.players[1]._games_won}, {match.convert_points_to_score(self.players[0]._name)} - {match.convert_points_to_score(self.players[1]._name)}")

        return


#     def p2_reset_points_games(self):
#         """ Reset points and games

#             Resets player's and opponet's points_won and games_won values to zero.
#         """
#         # This code can be deleted in refactoring
#         self._p2_points_won = 0
#         self._p1_points_won = 0
#         self._p2_games_won = 0
#         self._p1_games_won = 0
#         return

    def points_won_by(self, player_name):
        pass
#         """Increment points by one
#             Increments the points by one for a player / opponent
#             Before doing that it checks for games won, sets won, deuce and advantage

#         Args:
#             player_name ([str]): Name of the player or opponent
#         """

#         if player_name == self._p1_name:
#             if self._p1_games_won == 6 and self._p2_games_won == 5:
#                 self._p1_games_won += 1
#                 match.p1_reset_points_games()
#                 # Solving for Tie-Breaker
#             elif self._p1_games_won == 6 and self._p2_games_won == 6:
#                 ## have another function for tiebreak and call it here...
#                 self._p1_tiebrk_points_won += 1
#                 if self._p1_tiebrk_points_won >= 7 and self._p1_tiebrk_points_won - self._p2_tiebrk_points_won >= 2:
#                     self._p1_sets_won += 1
#                     match.p1_reset_points_games()
#                     self._p1_tiebrk_points_won = 0
#                     self._p2_tiebrk_points_won = 0

#             elif self._p1_games_won >= 6 and self._p1_games_won - self._p2_games_won >= 2:
#                 self._p1_sets_won += 1
#                 match.p1_reset_points_games()
#             else:
#                 self._p1_points_won += 1
#                 # if self._p1_points_won >= 3 and self._p2_points_won >= 3 and self._p1_points_won - self._p2_points_won == 0:

#                 # elif self._p1_points_won >= 3 and self._p2_points_won >= 3 and self._p1_points_won - self._p2_points_won == 1:

#                 # else:
#                 if self._p1_points_won >= 4 and self._p1_points_won - self._p2_points_won >= 2:
#                     self._p1_games_won += 1
#                     self._p1_points_won = 0
#                     self._p2_points_won = 0

#             print(
#                 f"Name: {self._p1_name} --> (Points Won: {self._p1_points_won} Games Won: {self._p1_games_won})")

#         elif player_name == self._p2_name:

#             if self._p2_games_won == 6 and self._p1_games_won == 5:
#                 self._p2_games_won += 1
#                 match.p2_reset_points_games()
#                 # Solve for Tie-Breaker
#             elif self._p2_games_won == 6 and self._p1_games_won == 6:
#                 self._p2_tiebrk_points_won += 1
#                 if self._p2_tiebrk_points_won >= 7 and self._p2_tiebrk_points_won - self._p1_tiebrk_points_won >= 2:
#                     self._p2_sets_won += 1
#                     match.p2_reset_points_games()
#                     self._p1_tiebrk_points_won = 0
#                     self._p2_tiebrk_points_won = 0

#             elif self._p2_games_won >= 6 and self._p2_games_won - self._p1_games_won >= 2:
#                 self._p2_sets_won += 1
#                 match.p2_reset_points_games()
#             else:
#                 self._p2_points_won += 1
#                 # if self._p2_points_won >= 3 and self._p1_points_won >= 3 and self._p2_points_won - self._p1_points_won == 0:
#                 # elif self._p2_points_won >= 3 and self._p1_points_won >= 3 and self._p2_points_won - self._p1_points_won == 1:


#                 # else:
#                 if self._p2_points_won >= 4 and self._p2_points_won - self._p1_points_won >= 2:
#                     self._p2_games_won += 1
#                     self._p2_points_won = 0
#                     self._p2_points_won = 0

#             print(
#                 f"Name: {self._p2_name} --> (Points Won: {self._p2_points_won} Games Won: {self._p2_games_won})")
#         else:
#             print(f"{player_name} is not registered")


# if __name__ == "__main__":
#     arguments = docopt(__doc__, version='1.0')
#     print(arguments, file=sys.stderr)

#     match = Match(arguments["--player-name"], arguments["--opponent-name"])
#     # match.print_variables()

#     # Sample implementation showing how pytennis works

#     match.points_won_by(arguments["--player-name"])
#     match.points_won_by(arguments["--opponent-name"])
#     match.score()
#     match.points_won_by(arguments["--player-name"])
#     match.points_won_by(arguments["--player-name"])
#     match.score()
#     match.points_won_by(arguments["--opponent-name"])
#     match.points_won_by(arguments["--opponent-name"])
#     match.score()
#     match.points_won_by(arguments["--player-name"])
#     match.score()
#     match.points_won_by(arguments["--player-name"])
#     match.score()
if __name__ == "__main__":
    match = Match("Donny", "Rowena")
    match.print_variables("Donny")
    match.reset_points_games()
    print( "check")
    match.score()
 
