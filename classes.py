class Animal(object):
	def __init__ (self,sound,name,age,fav_color,fav_food):
		self.sound=sound
		self.name=name
		self.age=age
		self.fav_color=fav_color
		self.fav_food = fav_food
	def eat(self,fav_food):
		print("yumm!!"+self.name+"is eating"+fav_food)
	def description(self):
		print(self.name + 'is' +str(self.age) + "years old and love the color "+self.fav_color)


dog = Animal("Hav","Milka",1,"brown","Beef")
dog.eat("fav_food")
dog.description()

class Man(self):
	def __init__ (self,name,eat,gender):
		self.name=name
		self.eat=eat
		self.gender=gender
	def eat_nothing (self):
		print(self.name + " is eating nothing")
	def unknown (self):
		print(self.gender + "unknown")

omer =Man('omer','nothing','unknown')
omer.eat_nothing('self')
