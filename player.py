from turtle import Turtle
STARTING_POSITION = (-280, 0)
MOVE_DISTANCE = 10
FINISH_LINE_X = 279


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("red")
        self.go_to_start()

    def go_forward(self):
        if self.xcor() < 280:
            self.forward(MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > -280:
            x_cor = self.xcor()
            y_cor = self.ycor() - MOVE_DISTANCE
            self.goto((x_cor, y_cor))

    def go_up(self):
        if self.ycor() < 280:
            x_cor = self.xcor()
            y_cor = self.ycor() + MOVE_DISTANCE
            self.goto((x_cor, y_cor))

    def go_back(self):
        if self.xcor() > -280:
            self.back(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.xcor() > FINISH_LINE_X:
            return True
        else:
            return False

