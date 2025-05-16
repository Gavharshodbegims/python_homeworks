#list

#problem1
lst = [1, 2, 3, 2, 4, 2]
x = int(input("element to count: "))
print("count:", lst.count(x))

#problem2
lst = [5, 10, 15, 20]
print("sum:", sum(lst))

#problem3
lst = [10, 2, 33, 4]
print("max:", max(lst))

#problem4
lst = [10, 2, 33, 4]
print("min:", min(lst))

#problem5
lst = [1, 2, 3, 4]
x = int(input("element to check: "))
print("present:", x in lst)

#problem6
lst = [1, 2, 3]
if lst:
    print("first:", lst[0])
else:
    print("empty")

#problem7
lst = [1, 2, 3]
if lst:
    print("last:", lst[-1])
else:
    print("empty")

#problem8
lst = [10, 20, 30, 40]
print("slice:", lst[:3])

#problem9
lst = [1, 2, 3]
rev = lst[::-1]
print("reversed:", rev)

#problem10
lst = [4, 1, 3, 2]
sorted_lst = sorted(lst)
print("sorted:", sorted_lst)

#problem11
lst = [1, 2, 2, 3, 4, 4]
unique = list(set(lst))
print("unique:", unique)

#problem12
lst = [10, 20, 30]
el = int(input("element: "))
i = int(input("index: "))
lst.insert(i, el)
print("updated:", lst)

#problem13
lst = [5, 10, 15, 10]
x = int(input("element: "))
if x in lst:
    print("index:", lst.index(x))
else:
    print("not found")

#problem14
lst = []
print("empty:", len(lst) == 0)

#problem15
lst = [2, 4, 5, 6]
even = sum(1 for n in lst if n % 2 == 0)
print("even:", even)

#problem16
lst = [1, 3, 4, 5]
odd = sum(1 for n in lst if n % 2 != 0)
print("odd:", odd)

#problem17
a = [1, 2]
b = [3, 4]
c = a + b
print("combined:", c)

#problem18
lst = [1, 2, 3, 4, 5]
sub = [2, 3]
print("sublist present:", sub == lst[1:3])

#problem19
lst = [1, 2, 3, 2]
old = int(input("replace: "))
new = int(input("with: "))
if old in lst:
    i = lst.index(old)
    lst[i] = new
print("updated:", lst)

#problem20
lst = [10, 20, 30, 40]
unique = list(set(lst))
unique.sort()
if len(unique) >= 2:
    print("second largest:", unique[-2])
else:
    print("not enough elements")

#problem21

lst = [4, 1, 3, 2]
unique = list(set(lst))
unique.sort()
if len(unique) >= 2:
    print("second smallest:", unique[1])
else:
    print("not enough elements")

#problem22

lst = [1, 2, 3, 4, 5]
even = [x for x in lst if x % 2 == 0]
print("even:", even)

#problem23

lst = [1, 2, 3, 4, 5]
odd = [x for x in lst if x % 2 != 0]
print("odd:", odd)

#problem24

lst = [10, 20, 30]
print("length:", len(lst))

#problem25

lst = [1, 2, 3]
copy = lst[:]
print("copy:", copy)

#problem26

lst = [1, 2, 3, 4, 5]
l = len(lst)
if l % 2 == 0:
    print("middle:", lst[l//2 - 1], lst[l//2])
else:
    print("middle:", lst[l//2])

#problem27

lst = [5, 10, 15, 20, 25]
start = int(input("start: "))
end = int(input("end: "))
if 0 <= start < end <= len(lst):
    print("max in sublist:", max(lst[start:end]))
else:
    print("invalid range")

#problem28

lst = [5, 10, 15, 20, 25]
start = int(input("start: "))
end = int(input("end: "))
if 0 <= start < end <= len(lst):
    print("min in sublist:", min(lst[start:end]))
else:
    print("invalid range")

#problem29

lst = [10, 20, 30, 40]
i = int(input("index: "))
if 0 <= i < len(lst):
    lst.pop(i)
print("updated:", lst)

#problem30

lst = [1, 2, 3, 4]
print("is sorted:", lst == sorted(lst))

#problem31

lst = [1, 2, 3]
n = int(input("repeat count: "))
new_lst = [x for x in lst for _ in range(n)]
print("repeated:", new_lst)

#problem32

a = [3, 1, 4]
b = [2, 5, 0]
merged_sorted = sorted(a + b)
print("merged and sorted:", merged_sorted)

#problem33

lst = [1, 2, 3, 2, 4, 2]
target = int(input("element: "))
indices = [i for i, x in enumerate(lst) if x == target]
print("indices:", indices)

#problem34

lst = [1, 2, 3, 4, 5]
rotated = [lst[-1]] + lst[:-1]
print("rotated:", rotated)

#problem35

start = int(input("start: "))
end = int(input("end: "))
range_list = list(range(start, end + 1))
print("range list:", range_list)

#problem36

lst = [-5, 10, -15, 20]
total = sum(x for x in lst if x > 0)
print("positive sum:", total)

#problem37

lst = [-5, 10, -15, 20]
total = sum(x for x in lst if x < 0)
print("negative sum:", total)

#problem38

lst = [1, 2, 3, 2, 1]
print("palindrome:", lst == lst[::-1])

#problem39

lst = [1, 2, 3, 4, 5, 6]
size = int(input("group size: "))
nested = [lst[i:i+size] for i in range(0, len(lst), size)]
print("nested:", nested)

#problem40

lst = [4, 2, 2, 3, 4, 1]
seen = set()
unique = []
for x in lst:
    if x not in seen:
        unique.append(x)
        seen.add(x)
print("unique in order:", unique)
