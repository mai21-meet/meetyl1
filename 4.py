import Turtle

class Ball(Turtle):
	def__init__(self,radius,color,dx ,dy):
		Turtle._init_(self)
		self.radius=radius
		self.dx = dx
		self.dy = dy
		self.color=color
		self.penup()
		self.shape('circle')
		self.size(radius/10)
	def move(self,screen_width,screen_hight)
		currenr_x=X
		new_x=current_x+1dx
		current_y=Y
		new_y=current_y+dy
		right_side_ball=new_x + radius
