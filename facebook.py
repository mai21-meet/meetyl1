class Post():
	def __init__(self,name,date,text):
		self.name=name
		self.date=date
		self.text=text

class User():
	def __init__ (self,name,email,password,friends_list=[],posts=[]):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list = []
		self.posts = []

	def add_friends(self):
		email = input("Enter your friend's email")
		self.friends_list.append(email)
		print(self.name+' has added'+ self.email+ ' as a friend')

	def remove_friend(self):
		email = input("Enter your friend's email")
		self.friends_list.remove(email)
		print(self.name + 'has removed' + self.email)

	def posts(self):
		text =input("give title to your post")
		post1=Post(self.name, "17/11", text)
		self.posts.append(post1)
		print(self.name+"has posted"+text)

	def get_userinfo(self):
		print("name: " + self.name)
		print("Email: " + self.email)
		print("passwors: " +self.password)
		print("friends list: " + str(self.friends_list))
		print("posts: " + str(self.posts))

user1 = User('Mai',"mai@gmail.com","omer")
user1.add_friends()
user1.posts()
user1.remove_friend()

user2=User('omer','omer@gmail.com','mai')
user2.add_friends()
user2.posts()
user2.remove_friend()

