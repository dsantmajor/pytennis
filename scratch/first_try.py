# TODO:
#     - method to store player name and points for each serve
#     - retrieve player name and players latest points
#     - check if player1 or Player2's points are equal to or greater than 4
#     - if above is true, then 
#           - check which player has higher points
#           - check the difference in points , if difference is >= 2
#           - then that player won the game
          
points_card = []
def update_points(player_name: str):
    points_card.append({'name': player_name, 'score': 1 })
    return points_card

score = update_score('p1')
print(score)
score = update_score('p2')
score = update_score('p2')
score = update_score('p2')
score = update_score('p2')
print(score)
print(len(score))
p1_total = [p1['score'] for p1 in score if p1['name'] == 'p1' ]
p2_total = [p2['score'] for p2 in score if p2['name'] == 'p2' ]
total = sum(x for x in p1_total)
print(total)
# def convert_points_to_score():
#     for player in points_card if player['name'] == 'p1'





# def start_game(player_name):
#     score_sheet= update_score(player_name)
    

