# while loop
i = 0
while i < 50:
    print(i)
    i = i + 5
else:
    print("done with all this")
    
    
#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# print(picture[i][j])
for row in picture:
    for pixel in row:
        if pixel == 0:
            print(" ", end = '')
        elif pixel == 1:
            print("*", end = '')
    print('')
        