# Given an input n print out a triangle of height n

def print_triangle(n):
    for row in range(1, n+1):
        print("*" * row)
    
print_triangle(10)