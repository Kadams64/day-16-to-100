import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

PLAYER_COLLISION = 20
SLEEP_TIMER = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score_board = Scoreboard()


game_is_on = True
screen.listen()
screen.onkey(fun= player.move_up, key="Up")

timer = SLEEP_TIMER

while game_is_on:
    time.sleep(timer)
    screen.update()

    car_manager.random_car()
    car_manager.move_cars()

    # detect car collision
    for car in car_manager.cars:
        if car.distance(player) < PLAYER_COLLISION:
            game_is_on = False
            score_board.game_over()

    # detect player has reached the other side
    if player.at_finish_line():
        print("Player reached the other side")
        player.restart()
        car_manager.speed_up()
        score_board.increment_score()


screen.exitonclick()