#special character
char=input("enter a character")
if char.isdigit():
    print(char,"is a digit")
elif char.islower():
    print(char,"is lower")

#number triangle

for i in range(5):
    print(str(5-i)*(i+1))

###fibonacci series

n=int(input("enter the no of terms"))
a=0
b=1
print(a,b)

count=1
while(count<n):
  c=a+b
  print(c)
  count+=1
  a=b
  b=c

  #### PRIME
f=int(input("enter the 1st character"))
l=int(input("enter the last character"))
print("the prime numbers b/w",f, "and",l,)
for i in range(f,l):
  for j in range(2,i):
    if i%j == 0:
        break
  else:
     print(i) 
     ####  GCD
def gcd(a,b):
    while b!=0:
        a,b=b, a % b 
    return a 

n1= int(input("enter"))
n2= int(input("enter"))
r=gcd(n1,n2)
print(r)

### PALINDROME
def palin(string):
    string=string.replace(" ","").lower()
    return string == string[::-1]
word=input("enter string")
result=palin(word)
print(result)
