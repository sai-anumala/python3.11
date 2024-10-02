
# Get the number of chocolates from the user
choco = int(input("Enter number of chocolates: "))

# Get the number of students from the user
stu = int(input('Enter number of students: '))

# Initialize a list to count chocolates for each student
students = [0] * stu 

# Set the starting index for the student
i = 0

# Distribute chocolates until none are left
while choco >= 1: 
    
    # Give one chocolate to the current student
    students[i] += 1   
    
    # Move to the next student
    i += 1  
    
    # Wrap around if the end of the list is reached
    i = (i % stu)
    
    # Decrease the chocolate count
    choco -= 1

# Initialize a list for student names
names = [] 

# Create names using letters A, B, C, ...
for i in range(stu):
    names.append(chr(i + 65))  # Convert numbers to letters

# Print each student's name and the number of chocolates received
for i, j in zip(names, students):
    print(i, "=", j, end=' ')
