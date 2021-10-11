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

arr09 = np.linspace(0.0,1.0,num=5)

arr10 = np.arange(1,21).reshape(4,5) #makes 4 rows with 5 columns each


num01 = np.arange(1,6)

num02 = num01*2 #doesn't affect original array

num03 = num01*3    #doesn't affect original array #broadcasting- takes the number and applies it to every number in the array

num01 += 10 #DOES affect original array (it changed)

num04 = num01 * num02 #must be the same size

num05 = num01 > 13 #shows True or False

num06 = num03 > num01 #shows True or False

#Here we have an array of 4 students grades on 3 exams
#row = student
#col = exam
grades = np.array([[87,96,70],[100,87,90],
                    [94,77,90],[100,81,82]])

print(grades.sum())
print(grades.mean())
print(grades.std())
print(grades.var())

# calculate average on all rows for each column
grades_by_exam = grades.mean(axis=0) #one-dimensinal ray of 3 elements

#calculate average on all cols for each row
grades_by_student = grades.mean(axis=1) #one-dimensional ray for 4 values

num07 = np.array([1,4,9,16,25,36])
num08 = np.sqrt(num07)

num09 = np.array([10,20,30,40,50,60])
num10 = np.add(num07,num09)
#same as
num10 = num07 +num09

num11 = np.multiply(num09,5)
#same as
num11 = num09 * 5 #broadcasting

num12 = num09.reshape(2,3)
num13 = np.array([2,4,6])

num14 = np.multiply(num12,num13) #DIFFERENT SHAPES, # of rows DON'T have to match up, but number of columns DO

print()