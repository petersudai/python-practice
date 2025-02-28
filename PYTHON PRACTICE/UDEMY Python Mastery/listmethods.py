basket = [1, 2, 3, 4, 5]
print(len(basket))

# List Methods
# adding
basket.append(100)
print(basket)

basket.insert(0, 200)
print(basket)

basket.extend([300, 500, 600, 4])
print(basket)

# removing
basket.pop() #pop by itself, removes the last object in the list
print(basket)

basket.pop(8) # pop with a value, removes the object at that index
print(basket)

basket.remove(100)  # remove, removes the exact object given as an argument
print(basket)

# basket.clear() # removes all objects
# print(basket)