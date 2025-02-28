# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to _____"
# youtuber = "Peter Sudai"

# a few ways to do this
# print("subscribe to " + youtuber)
# print("suscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

# lets now come up with our own madlib

# adj = input("Adjective:")
# verb = input("Verb:")
# madlib = f"I am learning python because it so {adj}, I wish I had learnt it even sooner tbh. \
# I'm going to {verb} when I finally learn python"

# print(madlib)

# Now to create my own madlib from scratch as practice
codinglanguage = input("Codinglanguage: ")
verb = input("verb: ")
adj = input("adjective: ")

madlib = f"I am really enjoying coding in {codinglanguage}. \
I {verb} every time I learn something new with {codinglanguage}. I think its a {adj} language to use"

print(madlib)