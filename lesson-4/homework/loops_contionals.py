#1 common elements of list

list1 = [1, 1, 2]
list2 = [2, 3, 4]
res = []

for x in list1:
    if list2.count(x) < list1.count(x):
        res += [x] * (list1.count(x) - list2.count(x))
        break

for x in list2:
    if x not in list1:
        res.append(x)

print(res)


#2 squares of less than a number

n = int(input())
for i in range(1, n):
    print(i * i)

#3 underscore after every third character

txt = "abcabcdabcdeabcdefabcdefg"
res = ""
i = 0

while i < len(txt):
    res += txt[i]
    if (i + 1) % 3 == 0 and i != len(txt) - 1:
        if txt[i] in "aeiou" or (i > 0 and res[-2] == "_"):
            res += txt[i + 1] + "_"
            i += 1
        else:
            res += "_"
    i += 1

print(res)

#4 number guessing game

import random

def play():
    num = random.randint(1, 100)
    for i in range(10):
        g = int(input("guess: "))
        if g == num:
            print("you guessed it right!")
            return
        elif g < num:
            print("too low!")
        else:
            print("too high!")
    print("you lost. want to play again?")
    again = input().lower()
    if again in ['y', 'yes', 'ok']:
        play()

play()

#5 password

p = input("password: ")
if len(p) < 8:
    print("password is too short.")
elif not any(x.isupper() for x in p):
    print("password must contain an uppercase letter.")
else:
    print("password is strong.")

#6 prime number

for n in range(2, 101):
    is_prime = True
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            is_prime = False
            break
    if is_prime:
        print(n)
