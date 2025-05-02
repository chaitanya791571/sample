def greet_user(name, callback):
    print(f"Hello, {name}!")
    callback()  
def say_goodbye():
    print("Goodbye!")


greet_user("chaitu", say_goodbye)
