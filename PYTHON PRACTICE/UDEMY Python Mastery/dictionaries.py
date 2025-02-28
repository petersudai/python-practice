# Dictionary
# this is also a data structure just like lists

dictionary = {
    'a': 1,
    'b': 2,
    'x': 3,
    'c': 4
}

print(dictionary.get('t', 90))

print(dictionary.values())

# Exercise Dictionary Methods
# Scroll to see answers.

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {
    'age': 30,
    'username': ' ',
    'weapons': None,
    'is_active': True,
    'clan': None
}
# 2 iterate and print all the keys in the above user.
print(user_profile.keys())

# 3 Add a new weapon to your user
user_profile.update({'weapons': 'machete'})
print(user_profile)

# 4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({'is_banned': False})
print(user_profile)

# 5 Ban the user by setting the previous key to True
user_profile.update({'is_banned': True})
print(user_profile)
# 6 create a new user2 my copying the previous user and update the age value and username value.

user2 = user_profile.copy()
print(user2)
user2.update({'age': 30, 'username': 'Peter'})
print(user2)