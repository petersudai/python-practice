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
for i in picture:
    for j in i:
        if j == 0:
            print(" ", end = '')
        elif j == 1:
            print("*", end = '')
    print('')
        