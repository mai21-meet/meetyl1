

class User():
	def __init__ (self,name,email,password,friends_list=[],posts=[]):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]=friends_list=[]
		self.posts=[]=posts=[]

	def add_friends(self):
		email = input("Enter your friend's email")
		friend_list.append(email)
		print(self.name+' has added'+get_email+ ' as a friend')

	def  remove_friend(self):
		email = input("Enter your friend's email")
		friend_list.remove(email)
		print(self.name + 'has removed' + get_email)

	def post (self):
		text =input("give title to your post")
		print(self.name+"has posted"+text)
		

user1 = User('mai',"mai@gmail.com","omer")
user1.add_friends()
