from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_car = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            ran_y = random.randint(-250, 250)
            new_car.goto(300, ran_y)
            self.all_car.append(new_car)

    def move(self):
        for car in self.all_car:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.car_speed += 10



