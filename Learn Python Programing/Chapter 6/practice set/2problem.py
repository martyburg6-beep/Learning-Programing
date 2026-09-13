
marks1 = int(input("Enter marks 1:"))
marks2= int(input("Enter marks 2:"))
marks3= int(input("Enter marks 3:"))

# Check for total percentage 
total_percentage =(100*(marks1 + marks2 + marks3))/300
if(total_percentage>=40):
    print("you are the pass",total_percentage)
else:
    print("you are the failed, try the next year", total_percentage)