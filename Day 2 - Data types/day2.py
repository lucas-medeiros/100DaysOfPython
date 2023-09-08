# Tip calculator
if __name__ == '__main__':
    print("Welcome to the tip calculator.")
    bill = float(input("What was the total bill?\n"))
    people = int(input("How many people to split the bill?\n"))
    percent = int(input("What percentage tip would you like to give?\n"))
    total = round((bill * (1 + (percent/100))) / people, 2)
    print(f"Each person should pay: {total}")
