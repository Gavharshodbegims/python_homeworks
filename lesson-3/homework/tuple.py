#tuples
#problem1
t = tuple(input("tuple elements (space): ").split())
e = input("element: ")
print("count:", t.count(e))

#problem2
t = tuple(map(int, input("tuple: ").split()))
print("max:", max(t))

#problem3
t = tuple(map(int, input("tuple: ").split()))
print("min:", min(t))

#problem4
t = tuple(input("tuple elements (space): ").split())
e = input("element: ")
print(e in t)

#problem5
t = tuple(input("tuple: ").split())
if t:
    print("first:", t[0])
else:
    print("empty")

#problem6
t = tuple(input("tuple: ").split())
if t:
    print("last:", t[-1])
else:
    print("empty")

#problem7
t = tuple(input("tuple: ").split())
print("length:", len(t))

#problem8
t = tuple(input("tuple: ").split())
print("slice:", t[:3])

#problem9
t1 = tuple(input("tuple1: ").split())
t2 = tuple(input("tuple2: ").split())
print("combined:", t1 + t2)

#problem10
t = tuple(input("tuple: ").split())
print("empty:", len(t) == 0)

#problem11
t = tuple(input("tuple: ").split())
e = input("element: ")
indices = [i for i, x in enumerate(t) if x == e]
print("indices:", indices)

#problem12
t = tuple(map(int, input("tuple: ").split()))
if len(t) >= 2:
    print("second max:", sorted(set(t))[-2])
else:
    print("not enough elements")

#problem13
t = tuple(map(int, input("tuple: ").split()))
if len(t) >= 2:
    print("second min:", sorted(set(t))[1])
else:
    print("not enough elements")

#problem14
e = input("element: ")
t = (e,)
print("tuple:", t)

#problem15
l = input("list: ").split()
print("tuple:", tuple(l))

#problem16
t = tuple(map(int, input("tuple: ").split()))
print("sorted:", t == tuple(sorted(t)))

#problem17
t = tuple(map(int, input("tuple: ").split()))
a = int(input("start index: "))
b = int(input("end index: "))
print("max in sub:", max(t[a:b]))

#problem18
t = tuple(map(int, input("tuple: ").split()))
a = int(input("start index: "))
b = int(input("end index: "))
print("min in sub:", min(t[a:b]))

#problem19
t = tuple(input("tuple: ").split())
e = input("element to remove: ")
if e in t:
    i = t.index(e)
    t = t[:i] + t[i+1:]
print("new tuple:", t)

#problem20
t = tuple(input("tuple: ").split())
n = int(input("subtuple size: "))
nt = tuple(tuple(t[i:i+n]) for i in range(0, len(t), n))
print("nested:", nt)

#problem21
t = tuple(input("tuple: ").split())
n = int(input("repeat: "))
print("repeated:", tuple(x for x in t for _ in range(n)))

#problem22
a = int(input("start: "))
b = int(input("end: "))
print("range tuple:", tuple(range(a, b+1)))

#problem23
t = tuple(input("tuple: ").split())
print("reversed:", t[::-1])

#problem24
t = tuple(input("tuple: ").split())
print("palindrome:", t == t[::-1])

#problem25
t = tuple(input("tuple: ").split())
seen = set()
u = tuple(x for x in t if x not in seen and not seen.add(x))
print("unique:", u)