#strings
#problem1

name = input("enter ur name: ")
yearofBirth = int(input("enter ur year of birth: "))
age = 2025 - yearofBirth
print(f"{name}, ur age is {age}")

#problem2

txt = 'LMaasleitbtui'
carname1 = txt[::2]
carname2 =  txt[1::2]
print("car name(s):", carname1, carname2)

#problem3

str = input("enter a str: ")
print("length: ", len(str))
print("uppercase: ", str.upper())
print("lowercase: ", str.lower())

#problem4

text = input("enter a text: ")
if text == text[::-1]:
  print("palindrome")
else:
  print("not palindrome")

#problem5

s = input("str: ").lower()
vowels = "aeiou"
vowelcount = sum(1 for char in s if char in vowels)
consonantcount = sum(1 for char in s if char.isalpha() and char not in vowels)
print("Vowels:", vowelcount)
print("Consonants:", consonantcount)

#problem6
str1 = input("enter first str: ")
str2 = input("enter second string: ")
print(str2 in str1)

#problem7

sentence = input("input string ")
oldword = input("which word should i replace: ")
newword = input("what should i replace with: ")
print(sentence.replace(oldword, newword))

#problem8

s = input("enter string ")
if len(s) > 0:
  print("first char:", s[0])
  print("last char:", s[-1])
else:
  print("empty")

#problem9

s = input("string to be reversed: ")
print("reversed:", s[::-1])

#problem10

sentence = input("sentence: ")
wordcount = len(sentence.split())
print("Number of words:", wordcount)

#problem11

s = input("Enter a string: ")
hasdigit = any(char.isdigit() for char in s)
print("digits avalaible: t/f", hasdigit)

#problem12

words = input("words split by space: ").split()
separator = input("seperator for choice: - ,: ")
joined = separator.join(words)
print("Joined string:", joined)

#problem13

s = input("string: ")
nospaces = s.replace(" ", "")
print("no spaces:", nospaces)

#problem14

s1 = input("string one: ")
s2 = input("string two: ")
print("equal t/f" , s1 == s2)

#problem15

sentence = input("sentence to make acronym: ")
acronym = ''.join(word[0].upper() for word in sentence.split() if word)
print("acronym:", acronym)

#problem16

s = input("string: ")
char = input("char to remove: ")
print("removed:", s.replace(char, ''))

#problem17

s = input("string: ")
vowels = "aeiouAEIOU"
result = ''.join('*' if c in vowels else c for c in s)
print("replaced:", result)

#problem18

s = input("string: ")
start = input("start: ")
end = input("end: ")
print("start is", s.startswith(start))
print("end is", s.endswith(end))
