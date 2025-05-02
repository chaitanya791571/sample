'''phone = input("enter the phone number")
digits_mapping = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
}
output = ""
for char in phone:
   output += digits_mapping.get(char,"!")+ " "
print(output)'''


##classes
'''class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point = Point(10,20)
point.x=11
print(point.x)'''

'''class Person:
    def ___init__(self,x):
        self.x = self
    def talk(self):
        print("talk")

hi = Person("chaitanya")
print(hi.x)
hi.talk()'''

'''n1,n2,n3,n4,n5=input( ),input( ),input( ),input( ),input( )
print(n1 + n2 + n3 + n4 + n5 ,".")'''

''''numbers = input("enter the five single digit numbers separated with commas")
x = numbers.split(',')
product = 1
for x in numbers :
        x = int(numbers)   
        product += product * x
        
    
        
print(product)'''

'''B = input("enter the branch code of length 2")
D = input("enter your degree")
Y = int(input("enter the year"))
R = int(input(" enter the roll "))
I = input("enter the institude name of length 4")
print(f'{B}_{D}_{Y}_{R}@student.onlinedegree.{I}.ac.in')'''

y = input()
part = y.split('_')
if len(part) == 3:
    branch = part[0]
    degree = part[1]
    year = part[2]
    roll  = part[3]
    institute = part[4].split('@')[0]
    
    print(f"Branch : {branch}")
    print(f"Degree : {degree}")
    print(f"Year : {year}")
    print(f"Roll no : {roll}")
    print(f"Institute : {institute}")
    
else:
    print("in valid")
