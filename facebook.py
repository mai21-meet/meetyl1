class Post():
	def __init__(self,name,date,text):
		self.name=name
		self.date=date
		self.text=text

class User():
	def __init__ (self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list = []
		self.post = []

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
		self.post.append(post1)
		print(self.name+"has posted"+text)

	def get_userinfo(self):
		print("name: " + self.name)
		print("Email: " + self.email)
		print("passwors: " +self.password)
		print("friends list: " + str(self.friends_list))
		print("posts: " + str(self.post))

class Comment(Post):
	def __init__ (self,text,likes,date):
		self.likes=likes
		self.date=date

	def writecomment(self):
		print(input("write your comment"))
		print(self.text)

user1 = User('Mai',"mai@gmail.com","omer")
user1.add_friends()
user1.posts()
user1.remove_friend()

user2=User('omer','omer@gmail.com','mai')
user2.add_friends()
user2.posts()
user2.remove_friend()

#my stomek hets so lets practis my writing on the computer. i am bored,we have 33 minutes to the end of the saaion. i think tha evry one thinks im working,when ectully i am writing this.

