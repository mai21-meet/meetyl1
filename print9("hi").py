class animal(object):
	def __init__ (self,sound,name,age,fav_color):
		self.sound=sound
		self.name=name
		self.age=age
		self.fav_color+fav_color
	def eat(self,food):
		print("yumm!!"+self.name+"is eating"+food)
	def description(self):
		prnt(self.name+'is'+self.age+"years old and love color"+self.fav_color)
