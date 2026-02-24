"""Check if the user is above 18 or not."""

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"You can vote {name}")
else:
    print("Grow up kid")
