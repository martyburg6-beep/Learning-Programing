a = int(input("Enter your age:"))

# if statement no 1
if(a%2==0):
    print("it is even")
# End of if statement no 1


# if statement no 2
if (a>18):
    print ("you are above the age of consent")
elif(a<0):
    print("you are add the nagetive age number")
elif(a==0):
    print("you are the enter the invaild number 0")

#End of if statement no 2

else:
    print ("you are below the age of consent")

print("End the program")