total = 0
for i in range (5):   #It is for loop for Implementing repating similar statements
    marks = int(input("Give the five Subject Marks"))      # Read the input from user
    total += marks                                         # assigining the marks to the single variable
avg = total / 5                                            # find the average
print(avg)                                                 # print the average
if avg >= 95:                                              # checking the particular average
    print("your Grade is A+")                              # if loop is true print the grade
elif avg >= 85:                                            # checking the particular average
    print("Your Grade is A")                               # elif loop is true print the grade
elif avg >= 75:                                            # checking the particular average
    print("Your Grade is B+")                               # elif loop is true print the grade
elif avg >= 65:                                            # checking the particular average
    print("Your Grade is B")                               # elif loop is true print the grade
else:                                                       # checking the particular average
    print("pass")                                          # elif loop is true print the grade