from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
INT_CHANCE_CAR = 6


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()  # prevent a turtle being generated on super().__init__
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def random_car(self):
        chance = random.randint(1, INT_CHANCE_CAR)
        if chance == 1:
            new_car = Turtle("square")
            # new_car.setheading(180)
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            new_car.goto(x= 300, y= rand_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT