# TODO:
# - tier-breaker
# - duece
# - advantage
# - game_won
# - set_won
# - point_won


class Player:

    def __init__(self, player_name, points_won=0, games_won=0, sets_won=0):
        self.player_name = player_name
        self.points_won = points_won
        self.games_won = games_won
        self.sets_won = sets_won

    # def games_won(self):


# class GamesWon(Player):

#     def __init__(self, player_name, points_won = 0, games_won =0, sets_won = 0):
#         Player.__init__(player_name, points_won, games_won, sets_won)
#     def calculate_games_won(self):


class Match:

    counter = 0

    def __init__(self, player_name_1, player_name_2, points_won=0, tiebrk_points_won=0, games_won=0, sets_won=0):
        self._p1_name = player_name_1
        self._p1_points_won = points_won
        self._p1_games_won = games_won
        self._p1_sets_won = sets_won
        self._p1_tiebrk_points_won = tiebrk_points_won
        self._p2_name = player_name_2
        self._p2_points_won = points_won
        self._p2_games_won = games_won
        self._p2_sets_won = sets_won
        self._p2_tiebrk_points_won = tiebrk_points_won

    def print_variables(self):
        print(f"Name: {self._p1_name} Points Won: {self._p1_points_won} Games Won: {self._p1_games_won}  Sets Won: {self._p1_sets_won}")
        print(f"Name: {self._p2_name} Points Won: {self._p2_points_won} Games Won: {self._p2_games_won}  Sets Won: {self._p2_sets_won}")
        return f"Name: {self._p1_name} Points Won: {self._p1_points_won} Games Won: {self._p1_games_won}  Sets Won: {self._p1_sets_won}"

    def p1_reset_points_games(self):
        print(f"Count {Match.counter}: Set WinCondition: Name: {self._p1_name} Points Won: {self._p1_points_won}  Name: {self._p2_name} Points Won: {self._p2_points_won} Games P1 Won: {self._p1_games_won} Game Difference P1 - P2 : {self._p1_games_won - self._p2_games_won} P1 Sets won: {self._p1_sets_won} Sets Difference P1 -P2: {self._p1_sets_won - self._p2_sets_won}")
        self._p1_points_won = 0
        print(f"Player 1 points reset : {self._p1_points_won}")
        self._p2_points_won = 0
        print(f"Player 2 points reset : {self._p2_points_won}")
        # print("out
        self._p1_games_won = 0
        print(f"Player 1 Games won reset : {self._p1_games_won}")
        self._p2_games_won = 0
        print(f"Player 2 Games won reset : {self._p2_games_won}")
        return

    def convert_points_to_score(self, player_name):
        if player_name == self._p1_name:
            if self._p1_points_won == 0:
                return "nil"
            elif self._p1_points_won == 1:
                return 15
            elif self._p1_points_won == 2:
                return 30
            elif self._p1_points_won == 3:
                return 40
        else:
            if player_name == self._p2_name:
                if self._p2_points_won == 0:
                    return "nil"
                elif self._p2_points_won == 1:
                    return 15
                elif self._p2_points_won == 2:
                    return 30
                elif self._p2_points_won == 3:
                    return 40



    def score(self):
        """Score

            match.score();
             // this will return "0-0, 15-15"
             p1-games won - p2-games won, p1points - p2 points
            // this will return "0-0, 40-15"

            // this will return "0-0, Deuce"

            // this will return "0-0, Advantage player 1"

            // this will return "1-0"

        """
        if self._p1_points_won >= 3 and self._p2_points_won >= 3 and self._p1_points_won - self._p2_points_won == 0:
            print(f"{self._p1_games_won} - {self._p2_games_won}, Deuce")
        elif self._p2_points_won >= 3 and self._p1_points_won >= 3 and self._p2_points_won - self._p1_points_won == 1:
            print(f"{self._p1_games_won} - {self._p2_games_won}, Advantage {self._p2_name}")
        elif self._p1_points_won >= 3 and self._p2_points_won >= 3 and self._p1_points_won - self._p2_points_won == 1:
            print(f"{self._p1_games_won} - {self._p2_games_won}, Advantage {self._p1_name}")
        else:
            print(f"P1_games_won - P2_games_won, P1_points_won - P2_points_won")
            print(f"{self._p1_games_won} - {self._p2_games_won}, {match.convert_points_to_score(self._p1_name)} - {match.convert_points_to_score(self._p2_name)}")
        
        return
    

    # @classmethod
    def p2_reset_points_games(self):
        print(f"Count {Match.counter}: Set WinCondition: Name: {self._p2_name} Points Won: {self._p2_points_won}  Name: {self._p1_name} Points Won: {self._p1_points_won} Games P2 Won: {self._p2_games_won} Game Difference P2 - P1 : {self._p2_games_won - self._p1_games_won} P2 Sets won: {self._p2_sets_won} Sets Difference P2 - P1: {self._p2_sets_won - self._p1_sets_won}")
        self._p2_points_won = 0
        print(f"Player 2 points reset : {self._p2_points_won}")
        self._p1_points_won = 0
        print(f"Player 2 points reset : {self._p1_points_won}")
        # print("out
        self._p2_games_won = 0
        print(f"Player 2 Games won reset : {self._p2_games_won}")
        self._p1_games_won = 0
        print(f"Player 1 Games won reset : {self._p1_games_won}")
        return

    def points_won_by(self, player_name):

        print(f"Outer Counter set to {Match.counter}")
        if player_name == self._p1_name:

            # print(f"Count {Match.counter}: Set WinCondition: Name: {self._p1_name} Points Won: {self._p1_points_won}  Name: {self._p2_name} Points Won: {self._p2_points_won} Games P1 Won: {self._p1_games_won} Game Difference P1 - P2 : {self._p1_games_won - self._p2_games_won} P1 Sets won: {self._p1_sets_won} Sets Difference P1 -P2: {self._p1_sets_won - self._p2_sets_won}")
            # self._p1_points_won = 0
            # print(f"Player 1 points reset : {self._p1_points_won}")
            # self._p2_points_won = 0
            # print(f"Player 2 points reset : {self._p2_points_won}")
            # # print("out
            # self._p1_games_won = 0
            # print(f"Player 1 Games won reset : {self._p1_games_won}")
            # self._p2_games_won = 0
            # print(f"Player 2 Games won reset : {self._p2_games_won}")

            if self._p1_games_won == 6 and self._p2_games_won == 5:
                self._p1_games_won += 1
                print(
                    f"Player1 won Set {self._p1_games_won} - {self._p2_games_won} ")
                match.p1_reset_points_games()
                # Solve for Tie-Breaker
            elif self._p1_games_won == 6 and self._p2_games_won == 6:
                print(
                    f"Tie Break: {self._p1_games_won} - {self._p1_games_won} ")
                self._p1_tiebrk_points_won += 1
                if self._p1_tiebrk_points_won >= 7 and self._p1_tiebrk_points_won - self._p2_tiebrk_points_won >= 2:
                    self._p1_sets_won += 1
                    match.p1_reset_points_games()
                    self._p1_tiebrk_points_won = 0
                    print(
                        f"Player 1 tie break points reset : {self._p1_tiebrk_points_won }")
                    self._p2_tiebrk_points_won = 0
                    print(
                        f"Player 2 tie break points reset : {self._p2_tiebrk_points_won}")

            elif self._p1_games_won >= 6 and self._p1_games_won - self._p2_games_won >= 2:
                self._p1_sets_won += 1
                match.p1_reset_points_games()
            else:
                print(f"P1 Counter set to {Match.counter}")
                print(f"Starting P1 Points Won: {self._p1_points_won}")
                self._p1_points_won += 1
                Match.counter += 1
                print(
                    f"Count {Match.counter}: P1 Points Won: {self._p1_points_won}")
                if self._p1_points_won >= 3 and self._p2_points_won >= 3 and self._p1_points_won - self._p2_points_won == 0:
                    print(f"We are in points = 3 Deuce mode")
                    print(
                        f"Its a Deuce: P1: {self._p1_points_won} - P2: {self._p2_points_won}")

                elif self._p1_points_won >= 3 and self._p2_points_won >= 3 and self._p1_points_won - self._p2_points_won == 1:
                    print(f"we are in advantage mode")
                    print(f"Advantage P1: {self._p1_points_won }")

                else:
                    print(f"Checking for point above 4")
                    if self._p1_points_won >= 4 and self._p1_points_won - self._p2_points_won >= 2:
                        self._p1_games_won += 1

                        print(f"Count {Match.counter}: Game WinCondition: Name:{self._p1_name} Points Won:{self._p1_points_won} | Name:{self._p2_name} Points Won:{self._p2_points_won} | Games P1 Won:{self._p1_games_won} | Game Difference P1 - P2 :{self._p1_games_won - self._p2_games_won}")
                        self._p1_points_won = 0
                        print(f"Player 1 points reset : {self._p1_points_won}")
                        self._p2_points_won = 0
                        print(f"Player 2 points reset : {self._p2_points_won}")
                        # print("out

            print(
                f"Count {Match.counter}: Outer: Name: {self._p1_name} Points Won: {self._p1_points_won} Games Won: {self._p1_games_won}")

        elif player_name == self._p2_name:

            if self._p2_games_won == 6 and self._p1_games_won == 5:
                self._p2_games_won += 1
                print(
                    f"Player2 won Set {self._p2_games_won} - {self._p1_games_won}")
                match.p2_reset_points_games()
                # Solve for Tie-Breaker
            elif self._p2_games_won == 6 and self._p1_games_won == 6:
                print(
                    f"Tie Break: {self._p2_games_won} - {self._p1_games_won} ")
                self._p2_tiebrk_points_won += 1
                if self._p2_tiebrk_points_won >= 7 and self._p2_tiebrk_points_won - self._p1_tiebrk_points_won >= 2:
                    self._p2_sets_won += 1
                    match.p2_reset_points_games()
                    self._p1_tiebrk_points_won = 0
                    print(
                        f"Player 1 tie break points reset : {self._p1_tiebrk_points_won }")
                    self._p2_tiebrk_points_won = 0
                    print(
                        f"Player 2 tie break points reset : {self._p2_tiebrk_points_won}")

            elif self._p2_games_won >= 6 and self._p2_games_won - self._p1_games_won >= 2:
                self._p2_sets_won += 1
                match.p2_reset_points_games()
            else:
                print(f"P2 Counter set to {Match.counter}")
                print(f"Starting P2 Points Won: {self._p2_points_won}")
                self._p2_points_won += 1
                Match.counter += 1
                print(
                    f"Count {Match.counter}: P2 Points Won: {self._p2_points_won}")
                if self._p2_points_won >= 3 and self._p1_points_won >= 3 and self._p2_points_won - self._p1_points_won == 0:
                    print(f"We are in points = 3 Deuce mode")
                    print(
                        f"Its a Deuce: P1: {self._p1_points_won} - P2: {self._p2_points_won}")

                elif self._p2_points_won >= 3 and self._p1_points_won >= 3 and self._p2_points_won - self._p1_points_won == 1:
                    print(f"we are in advantage mode")
                    print(f"Advantage P2: {self._p2_points_won }")

                else:
                    print(f"Checking for point above 4")
                    if self._p2_points_won >= 4 and self._p2_points_won - self._p1_points_won >= 2:
                        self._p2_games_won += 1

                        print(f"Count {Match.counter}: Game WinCondition: Name:{self._p2_name} Points Won:{self._p2_points_won} | Name:{self._p1_name} Points Won:{self._p1_points_won} | Games P2 Won:{self._p2_games_won} | Game Difference P2 - P1 :{self._p2_games_won - self._p1_games_won}")
                        self._p2_points_won = 0
                        print(f"Player 1 points reset : {self._p1_points_won}")
                        self._p2_points_won = 0
                        print(f"Player 2 points reset : {self._p2_points_won}")
                        # print("out

            print(
                f"Count {Match.counter}: Outer: Name: {self._p2_name} Points Won: {self._p2_points_won} Games Won: {self._p2_games_won}")

            # print(f"P2 Counter set to {Match.counter}")
            # print(f"Starting P2 Points Won: {self._p2_points_won}")
            # self._p2_points_won += 1
            # Match.counter += 1
            # print(f"Count {Match.counter}: P2 Points Won: {self._p2_points_won}")
            # if self._p2_points_won >= 4 and self._p2_points_won - self._p1_points_won >= 2:
            #     self._p2_games_won += 1

            #     print(f"Count {Match.counter}: WinCondition: Name: {self._p2_name} Points Won: {self._p2_points_won}  Name: {self._p1_name} Points Won: {self._p1_points_won} Games P2 Won: {self._p2_games_won} Difference of: {self._p2_points_won - self._p1_points_won}")
            #     # print("out
            #     self._p2_points_won = 0
            #     print(f"Player 2 points reset : {self._p2_points_won}")
            #     self._p1_points_won = 0
            #     print(f"Player 1 points reset : {self._p2_points_won}")
        else:
            print(f"{player_name} is not registered")

        # self._p2_games_won = games_won

        # while self._p1_games_won
        # self.

    # def print_name(self):
    #     return f"FirstPlayer: {self._player1}, SecondPlayer: {self._player2}, P1_points_won: {self._player1._points_won}, P2_points_won:{self._player2._points_won}, P1_sets_won: {self._player1._sets_won}"

    # def point_won_by(self, player_name):
    #     self._player_name = player_name
    #     self._p1_points_won = 0
    #     self._p2_points_won = 0
    #     self.game_won_counter = 0
    #     while (self._p1_points_won <= 4) and (self._p1_points_won - self._p2_points_won >=2):
    #         self._p1_games_won += 1

        # while self.game_won_counter < 1:

        #     if self._player_name == self._player1:
        #         # self._p1_points_won += 1
        #         if self._p1_points_won >=4:
        #             if self._p1_points_won - self._p2_points_won >=2:
        #                     self._p1_games_won += 1
        #                     self.game_won_counter += 1
        #         else:
        #             self._p1_points_won += 1

        #     else:
        #         if self._p2_points_won >=4:
        #             if self._p2_points_won - self._p1_points_won >=2:
        #                     self._p2_games_won += 1
        #                     self.game_won_counter += 1
        #         else:
        #             self._p2_points_won += 1

    # def games_won_by(self, player_name):
    #     if self._player_name == self._player1:
    #         self._other_player = self._player2
    #     else:
    #         self._player_name = self._player2
    #         self._other_player = self._player1

    # def points_to_score(self, player_name):
    #     self._player_name = player_name

    #     if self._player_name == 0:
    #         return 0
    #     elif self._player_name == 1:
    #         return 15
    #     elif self._player_name == 2:
    #         return 30
    #     elif self._player_name == 3:
    #         return 40
    # def score(self):
    #     # return self._p1_points_won, self._p2_points_won
    #     return self._p1_games_won, self._p2_games_won, self._p1_points_won, self._p2_points_won, self.points_to_score(self._p1_points_won), self.points_to_score(self._p2_points_won)
if __name__ == "__main__":

    match = Match("Player 1", "Player 2")
    match.print_variables()
    # for i in range(1,30):
    #     match.points_won_by("Player 1")
    #     match.points_won_by("Player 2")
    # for x in range(0):
    #     match.points_won_by("Player 2")
    # match.points_won_by("Player 1")
    match.points_won_by("Player 1")
    match.points_won_by("Player 2")
    match.score()
    match.points_won_by("Player 1")
    match.points_won_by("Player 1")
    match.score()
    match.points_won_by("Player 2")
    match.points_won_by("Player 2")
    match.score()
    match.points_won_by("Player 1")
    match.score()
    match.points_won_by("Player 1")
    match.score()

 