def find_average():
    total = 0
    count = 0

    print("Enter numbers one by one. Type 'done' when you are finished:")

    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        
        if user_input.lower() == 'done':
            break
        
        try:
            number = float(user_input)
            total += number
            count += 1
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish.")
    
    if count == 0:
        print("No numbers were entered.")
    else:
        average = total / count
        print(f"The average of the entered numbers is: {average:.2f}")

find_average()
