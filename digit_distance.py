a=input("Enter 1st number: ")
b=input("Enter 2nd number: ")
n=len(a)
num1=[]
num2=[]
dist=[]
for i in a:
    num1.append(int(i))
for i in b:
    num2.append(int(i))

for i in range(len(num1)):
    dist.append(abs(num1[i] - num2[i]))

print ("Distance between two numbers:", sum(dist))
