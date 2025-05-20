#1 temperature 
def convert_cel_to_far(c):
    return round(c * 9/5 + 32, 2)

def convert_far_to_cel(f):
    return round((f - 32) * 5/9, 2)

f = float(input("Enter a temperature in degrees F: "))
print(f"{f} degrees F = {convert_far_to_cel(f)} degrees C")

c = float(input("Enter a temperature in degrees C: "))
print(f"{c} degrees C = {convert_cel_to_far(c)} degrees F")

#2 calculator
def invest(amount, rate, years):
    for i in range(1, years + 1):
        amount += amount * rate
        print(f"year {i}: ${amount:.2f}")

amt = float(input("Initial amount: "))
rate = float(input("Annual rate (as decimal): "))
yrs = int(input("Number of years: "))
invest(amt, rate, yrs)

#3 factor finder
n = int(input("Enter a positive integer: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(f"{i} is a factor of {n}")

#4 university statistics
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(data):
    students = [row[1] for row in data]
    tuition = [row[2] for row in data]
    return students, tuition

def mean(lst):
    return sum(lst) / len(lst)

def median(lst):
    s = sorted(lst)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2

students, tuition = enrollment_stats(universities)

print("******************************")
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuition):,}")
print()
print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {int(median(students)):,}")
print()
print(f"Tuition mean: $ {mean(tuition):,.2f}")
print(f"Tuition median: $ {int(median(tuition)):,}")
print("******************************")

#5 prime checker
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

x = int(input("Enter a number: "))
print("Prime" if is_prime(x) else "Not prime")

