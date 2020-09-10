# TODO: check_game_won()
#       check_points
#       check_total_points
#       if check_total_points <= 4 && diff <= 2
#       then update_points
#       points_to_score()
# State management : set_wonfor each player
# State management : games_won
# State management : points_won


class Match:

    games_won = []
    points_won = []
    sets_won = []


    def __init__(self, name):
        self._name = name


    def points_won(self, name):
        self.

player1_points = []
player2_points = []

def update_points(player):

    if player == "player1":
        player1_points.append(1)
        player2_points.append(0)
    else:
        player1_points.append(0)
        player2_points.append(1)
    # return player1_points, player2_points



def get_points():
    p1 = player1_points
    p2 = player2_points  
    return p1, p2

total_points = [0,0]
def update_total_points():
    all_p1_points, all_p2_points = get_points()
    last_p1_point = all_p1_points[-1]
    last_p2_point = all_p2_points[-1]
    # if last_p1_point > last_p2_point:
    #     diff_pts = last_p1_point - last_p2_point
    # else:
    #     diff_pts = last_p2_point - last_p1_point

    for i, points in enumerate(total_points):
        if i == 0:
            total_points[0] = points + last_p1_point
        if i == 1:
            total_points[1] = points + last_p2_point
        # if i == 2:
        #     total_points[2] = diff_pts
  
    
    # total_points.
  


    # total_points.append([last_p1_point, last_p2_point, diff_pts])


def get_total_points():
    return total_points

def get_diff_points():
    total_points = get_total_points()
    latest_p1_points = total_points[0]
    latest_p2_points = total_points[1]

    if latest_p1_points > latest_p2_points:
        diff_pts = latest_p1_points - latest_p2_points
    else:
        diff_pts = latest_p2_points - latest_p1_points
    
    return diff_pts

def check_points_n_diff_pts():
    
    p1_points = 0
    p2_points = 0

    # diff_points = get_diff_points()
    while p1_points or p2_points >= 4:
        total_points = get_total_points()
        p1_points = total_points[0]
        p2_points = total_points[1]
        update_total_points()

    # if (p1_points <=4) and (diff_points <=2):
    #     update_total_points()
    # elif (p2_points <=4) and (diff_points <=2):
    #     update_total_points()
    # # if (p1_points <=4) or (p2_points <=4) and (diff_points <=2):
    # #     update_total_points()

    
        # update_points("player1")
        update_total_points()



def main():
    for i in [1,1,1,1,2,1,2,1,1 ]:
        update_points("player"+ str(i))
        # update_total_points()
        check_points_n_diff_pts()
    res1, res2 = get_points()
    checked_total_points = get_total_points()
    diff_in_points = get_diff_points()
    print(f"p1 points: {res1}")
    print(f"p2 points: {res2}")
    print(f"last p1 point: {res1[-1]}")
    print(f"last p2 point: {res2[-1]}")
    print(f"total points: {checked_total_points}")
    print(f"difference in points: {diff_in_points}")


if __name__ == "__main__":
    main()