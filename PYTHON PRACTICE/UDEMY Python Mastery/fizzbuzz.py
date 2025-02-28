# FizzBuzz

for i in range(1, 51):
    if i % 3 == 0 and i % 4 == 0:
        print("FizzBuzz")
    elif i % 4 == 0:
        print("Buzz")
    elif i % 3 == 0 :
        print("Fizz")
    else:
        print(i)