import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
STARTING_X = 300
Y_LIMIT = 220
X_LIMIT = 320
CAR_ODDS = 6


class CarManager:

    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []

    def generate_car(self):
        """Has a 1/6 chance of creating a new car"""
        if random.randint(1, CAR_ODDS) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(STARTING_X, random.randint(-Y_LIMIT, Y_LIMIT))
            self.cars.append(new_car)

    def move_cars(self):
        """Move all the cars to the left by the move distance attribute"""
        for car in self.cars:
            car.goto(car.xcor() - self.move_distance, car.ycor())
            if car.xcor() < -X_LIMIT:
                self.cars.pop(self.cars.index(car))

    def is_crashed(self, turtle):
        """Returns True if turtle crashed with any car"""
        for car in self.cars:
            if car.distance(turtle) < 15:
                return True
        return False

    def reset_level(self):
        """Resets turtle position and goes to next level"""
        self.cars = []
        self.move_distance += 10
        for i in range(random.randint(3, 5)):
            self.generate_car()
