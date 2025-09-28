# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

while name == "":
    print("your name can't be blank")
    name = input("Enter your name: ")

print(f"Hello {name}")