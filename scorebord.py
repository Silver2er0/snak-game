from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 15, "normal")

class Scorebord(Turtle):
	"""docstring for Scorebord"""
	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("white")
		self.penup()
		self.goto(0,270)
		self.update_score_board()
		self.hideturtle()

	def update_score_board(self):
		self.write(f"your score is: {self.score}", align = ALIGN, font = FONT)

	def game_over(self):
		self.goto(0, 0)
		self.write("GAME OVER", align = ALIGN, font = FONT)


	def inc_score(self):
		self.score += 1
		self.clear()
		self.update_score_board()
		