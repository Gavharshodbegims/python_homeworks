#problem1

#num = float(input("enter a num: "))
#roundedNum = round(num, 2)
#print("your number has been rounded to 2 dec places: ", roundedNum)

#problem2

#num1 = float(input("enter a num: "))
#num2 = float(input("enter a num: "))
#num3 = float(input("enter a num: "))
#print("largest num: ", max(num1, num2, num3))
#print("smallest num: ", min(num1, num2, num3))

#problem3

#km = float(input("enter distance in km: "))
#m = km * 1000
#cm = km * 1000000
#print(f"ur km in meters is {m} and in centimeters {cm}")

#problem4

#numOne = int(input("enter a num: "))
#numTwo = int(input("enter a num: "))
#
#if numTwo != 0: 
#    print("quotient: ", numOne // numTwo)
#    print("remainder: ", numOne % numTwo)
#else: 
#    print("math error: unable to divide by 0")

#problem5

#celsius = float(input("enter temp in Celsius: "))
#fahrenheit = (celsius * 9/5) + 32
#print(f"{celsius}°C is {fahrenheit}°F")

#problem6

#number = int(input("num: "))
#last_digit = abs(number) % 10
#print("last digit:", last_digit)

#problem7

numEO = int(input("enter a num: "))

if numEO % 2 == 0:
    print("even")
else:
    print("odd")