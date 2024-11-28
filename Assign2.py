"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
repeatForever = True
tryagain = True
while repeatForever:
    try:
        x = float(input("Enter a number: "))
        repeatForever = False
    except:
        print("Please only enter numbers")
while tryagain:
    try: 
        y = float(input("Enter a second number: "))
        tryagain = False
    except: 
        print("Please only enter numbers")
Question = True
while Question == True:
    Q = input("Is one of the numbers the hypotenuse?(Yes/No): ")
    if Q in "Yes yes":
        c = max(x,y)
        a = min(x,y)
        Mside = c**2 - a**2
        Question = False
    elif Q in "No no":
        Mside = x**2 + y**2 
        Question = False
    else:
        print("Please enter a valid response (Yes/No).")

print(f"The missing side has a length of {Mside}")