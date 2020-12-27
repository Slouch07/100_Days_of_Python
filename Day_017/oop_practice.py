class User:  # Class creation
    # Constructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # default value
        self.following = 0

    def follow(self, user):  # 'self' tells the method which object called it.
        user.followers += 1
        self.following += 1


user_1 = User("001", "Ryan")  # object creation using constructor.
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)