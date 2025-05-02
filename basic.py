my_number = 8
i=0
limit=3
while i < limit :
    guess=int(input("enter the your guess number"))
    i += 1
    if my_number == guess:
        print("you won!")
        break
else:
    print("you lost")
    


