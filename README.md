# Tennis Scoring

## Approach

We have to initialise Player , Match , Set, Game, 
We need to define `points_won_by` method and `score` method

- `points_won_by` should increment the points by 1
- before it can increment by one it needs to check 
 - games_won method should return ture or fasle
 - sets_won method

what does games_won method do ?
checks if a player has won the game . How?
there are two conditions to check

 1. player points >=4
 2. difference between player 1 and 2 and vice versa is >=2 

how to check if points are greater than /equal to 4 ?
how to check for difference , 

first need to fetch player1s and player2s points? 

how to fetch ?

 by calling Player class and attributes points_won i.e. 
 if p1.points_won >= 4:
    if p1.points_won - p2.points_won >= 2:
        p1.games_won += 1
 elif p2.points_won >= 4:
        if p2.points_won - p1.points_won >= 2:
            p2.games_won += 1


points_won_by( player_name)
 self.player = player_name

### Relationship between Match Set and Games

`Match --1--> Set --*--> Games`

### How does a player win a Game

A player wins a game if that player has

- minimum points = 4 i.e. p1(points) or p2(points) >= 4
  
- difference in points between the two players > 2 `P1(points) -P2(points) >= 2` or `P2(points) -P1(points) >= 2`

### Running score representaton

|Point|Score|
|---|---|
|0|0|
|1|15|
|2|30|
|3|40|

### Solve for Deuce

check if points scored by P1 and P2 >= 3 and P1=P2

### Solve for Advantage

check if points scored by P1 and P2 >=3 and if P1-P2 > 1 or p2-p1 > 1
