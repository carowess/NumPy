import numpy as np

# ROWS - Each student (student0, student1, student2, student3)
# COLS - Each Test (Test0, Test1, Test2)
grades = np.array([[87,96,70],[100,87,90],
                    [94,77,90],[100,81,82]])


student1 = grades[1]
print(student1)

student0_test1 = grades[0,1]
print(student0_test1)

students0_1 = grades[0:2] #colon represents sequential values, the UPPER BOUND is NOT included (only 0 and 1 are included in this case)
print(students0_1)

students1and3 = grades[[1,3]] #represents the row part, not the column part, this gives us all the grades for students 1 and 3
print(students1and3)

#to select students 1 and 3 but only test 2
students1and3_test2 = grades[[1,3],2]

all_students_test0 = grades[:,0]

all_students_test1_2 = grades[:,1:3]

all_students_test0and2 = grades[:,[0,2]]

'''
Use NumPy random-number generation to create an array of twelve 
random grades in the range 60 through 100, then reshape the result 
into a 3-by-4 array. Calculate the average of all the grades, 
the averages of the grades for each test, and the averages of the 
grades for each student
'''

arr_random = np.random.randint(60,101,12).reshape(3,4)

grades.mean()

#avg by col
grades.mean(axis=0) #represents average by TEST SCORE (column)

#avg by row
grades.mean(axis=1) #represents average by STUDENT (row)


numbers = np.arange(1,6)

####SHALLOW COPY####
numbers_view = numbers.view() #creating a SHALLOW copy

numbers[1] *= 10 #copy is affected when the original is changed

numbers_view[1] /= 10 #original is affected when the copy is changed

numbers_slice = numbers[0:3] #shallow copy

numbers[1] *= 20

####DEEP COPIES####
numbers_copy = numbers.copy()

numbers[1] *= 10 #the copy is NOT changed when the original is changed

grades = np.array([[87,96,70],[100,87,90]])

#RESHAPE METHOD produces a SHALLOW COPY
grades_reshaped = grades.reshape(1,6)

grades.resize(1,6)

#FLATTEN METHOD creates a DEEP copy
flattened = grades.flatten()

#RAVEL creats a shallow copy
raveled = grades.ravel()

raveled[0] = 100

flattened[1] = 100

grades = np.array([[87,96,70],[100,87,90]])

grades.T #flips the array

grades2 = np.array([[94,77,90],[100,81,82]])


h_grades = np.hstack((grades,grades2)) ##adds more columns (exam)

v_grades = np.vstack((grades,grades2)) ##adds more rows (students)

print()



