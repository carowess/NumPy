import numpy as np
import random

# two-dimensional ray because it has rows and columns
# each of these numbers separated by a comma makes a new row, and within each element, each of those represent a column
# this example has three columns and two rows
arr01 = np.array([[1,2,3],[4,5,6]])
# one-dimensional ray
arr02 = np.array([0.0,0.1,0.2,0.3,0.4])

for row in arr01:
    print(row)
    for col in row:
        print(col, end=' ')
    print()

for i in arr01.flat:
    print(i)

arr03 = np.zeros(5)

arr04 = np.ones((2,4), dtype=int)

arr05 = np.full((3,5),13)


# EXERCISE
#############

# create a 2 dimensional array of 5 integer elements each using the random module
# and list comprehension 

a = np.array([[random.randint(1,10) for i in range(5)],[random.randint(1,10) for i in range(5)]])
print(a)

b = np.array(np.random.randint(1,10,size=(2,5)))
print(b)

arr06 = np.arange(5)

arr07 = np.arange(5,10)

arr08 = np.arange(10,1,-2)


print()