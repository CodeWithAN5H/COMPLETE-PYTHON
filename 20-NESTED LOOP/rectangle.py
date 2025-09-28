
rows = int(input("How many rows? "))
cols = int(input("How many columns? "))
symbol = input("What is your symbol? ")

for x in range(rows):
    for y in range(cols):
        print(symbol, end="")
    print()