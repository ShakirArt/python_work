name = input("Enter your name: ")
print("Welcome,",name,"!")
age=input("Enter your age: ")
print("You are", age, "years old.")
roll, reg= input("Enter your roll and registration number: ").split()
'''We are taking multiple input from the user in a single line,
 splitting the values entered by the user into separate variables for each value using the split() method.'''
print("Your roll number:", roll, "and registration number:", reg)

# Taking input from the user
num = int(input("Enter a value: "))

add = num + 5

# Output
print("The sum is %d" %add)

