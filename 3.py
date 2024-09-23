'''
There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
'''

x = int(input()) 
y = int(input()) 
z = int(input())  
n = int(input()) 
suitable_lab = None
max_capacity = -1
if x >= n and x > max_capacity:
    suitable_lab = "L1"
    max_capacity = x
if y >= n and y > max_capacity:
    suitable_lab = "L2"
    max_capacity = y
if z >= n and z > max_capacity:
    suitable_lab = "L3"
    max_capacity = z
if suitable_lab:
    print(suitable_lab)
else:
    print("No suitable lab")  # Optional: In case no lab can accommodate n students

