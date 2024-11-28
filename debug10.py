#!python3
"""
Debug this program so that it runs correctly

original code:
x = 3
y = 4
if x or y  >= 3 :
    print("at least 1 number is greater than or equal to 3")
elif x >= 3:
    print('only x is greater than or equal to 3')
elif y >= 4:
    print('only y is greater than or equal to 4')
else
    print("Both numbers are less than 3")
"""

x = 3
y = 0
if x >= 3 or y  >= 3:
    print("at least 1 number is greater than or equal to 3")
elif x >= 3:
    print('only x is greater than or equal to 3')
elif y >= 4:
    print('only y is greater than or equal to 4')
else:
    print("Both numbers are less than 3")