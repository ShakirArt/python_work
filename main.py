name='Shakira Islam'
print(name)
print(type(name))
age=22
print(age)
print(type(age))
height=5.2
print(height)
print(type(height))
StudentStatus=True
print(StudentStatus)
print(type(StudentStatus))
fav_color=('black', 'off-white', 'maroon', 'emrald green')
print(fav_color)
print(type(fav_color))


b=7
arithmetic={
    'add':age+b,
    'sub':age-b,
    'mul':age*b,
    'div':age/b,
    'mod':age%b,
    'floor':age//b,
    'exp':age**b,
}
print(arithmetic)
print(type(arithmetic))


comparison={
    'adult':age>=18,
    'greater':age>b,
    'less':age<b,
    'equal':age==b,
    'not equal':age!=b,
    'greater or equal':age>=b,
    'less or equal':age<=b,
}
print(comparison)


a=True
c=False
logical={
    'a and c':a and c,
    'a or c':a or c,
    'not c':not c,
    'and':age>=18 and b>5,
    'or':age>=18 or b>5,
    'not':not age>=18,
}
print(logical)


#assignment operator
roll=41
print(roll)
reg=roll
print(reg)
print(roll)
roll+=6
print(roll)
roll-=5
print(roll)
roll*=6
print(roll)


#identity operator
yr = 2025
t = yr
sec= 54.34
print(age is not yr)
print(yr is not t)
print(sec is yr)


my_hobby=['reading','painting','singing']
# using membership 'in' operator
print(my_hobby)
print(type(my_hobby))
print('reading' in my_hobby)
print('reading' not in my_hobby)