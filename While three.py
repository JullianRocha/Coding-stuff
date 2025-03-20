import os
os.system ('cls')
i = 0
print("Q"*-1)
while i<5:
    j = 0
   
    while j<5:  
        j = j+1 
        if i>0:
            print(3,end="")
            print("2"*(i-1),end="")
            print(j-1,end=" ")
        else:
            print(j,end=" ")
    i = i+1
    print("\n")