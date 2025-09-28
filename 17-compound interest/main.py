# Python compound interest calculator
# FORMULA:
# A = P(1+r/n)^t
# A = final amount
# P = initial principal balance
# r = rate of interest
# t = no of time periods elapsed

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount must be greater than 0")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("Rate of Interest must be greater than 0")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time period elapsed must be greater than 0")
    else:
        break

total = principle*pow((1 + rate/100), time)

print(f"Balance after {time} year/s: ${total:.2f}")