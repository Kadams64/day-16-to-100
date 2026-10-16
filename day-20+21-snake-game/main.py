from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    # turn off tracer, skip intermediate drawing steps
                    # call update to redraw screen
screen.update()
snake = Snake()
food = Food()
score = Scoreboard()

# Listen for directional keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_running = True
food_eaten = 0
# make the snake longer to help test snake collisions
# for _ in range(20):
#     snake.extend()

while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 25:
        food_eaten += 1
        food.refresh()
        snake.extend()
        score.write_score(food_eaten)

    # detect collision with wall
    x_cor = snake.head.xcor()
    y_cor = snake.head.ycor()
    if x_cor > 290 or x_cor < -290 or y_cor > 290 or y_cor < -290:
        game_running = False
        score.game_over()

    # detect collision with tail
    for segment in snake.snake_parts[1:]:
        if snake.head.distance(segment) < 10:
            # trigger game over
            game_running = False
            score.game_over()


screen.exitonclick()
