#dictionary

#get value
d = {"a": 1, "b": 2}
key = input("key: ")
print(d.get(key, "not found"))

#check key
d = {"a": 1, "b": 2}
key = input("key: ")
print(key in d)

#count keys
d = {"a": 1, "b": 2}
print(len(d))

#get all keys
d = {"a": 1, "b": 2}
print(list(d.keys()))

#get all values
d = {"a": 1, "b": 2}
print(list(d.values()))

#merge dictionaries
d1 = {"a": 1}
d2 = {"b": 2}
d3 = {**d1, **d2}
print(d3)

#remove key
d = {"a": 1, "b": 2}
key = input("key to remove: ")
if key in d:
    del d[key]
    print("removed")
else:
    print("key not found")

#clear dictionary
d = {"a": 1, "b": 2}
d.clear()
print(d)

#check if dictionary is empty
d = {}
print(not bool(d))

#get key-value pair
d = {"a": 1, "b": 2}
key = input("key: ")
if key in d:
    print((key, d[key]))
else:
    print("not found")

#update value
d = {"a": 1, "b": 2}
key = input("key: ")
value = input("new value: ")
if key in d:
    d[key] = value
    print("updated")
else:
    print("key not found")

#count value occurrences
d = {"a": 1, "b": 2, "c": 1}
val = input("value to count: ")
val = int(val) if val.isdigit() else val
print(list(d.values()).count(val))

#invert dictionary
d = {"a": 1, "b": 2}
inv = {v: k for k, v in d.items()}
print(inv)

#find keys with value
d = {"a": 1, "b": 2, "c": 1}
val = int(input("value: "))
keys = [k for k, v in d.items() if v == val]
print(keys)

#create dict from lists
keys = ["a", "b"]
vals = [1, 2]
d = dict(zip(keys, vals))
print(d)

#check for nested dictionaries
d = {"a": 1, "b": {"x": 10}}
print(any(isinstance(v, dict) for v in d.values()))

#get nested value
d = {"a": 1, "b": {"x": 10}}
key1 = input("outer key: ")
key2 = input("inner key: ")
if key1 in d and isinstance(d[key1], dict) and key2 in d[key1]:
    print(d[key1][key2])
else:
    print("not found")

#create default dictionary
from collections import defaultdict
d = defaultdict(lambda: "default")
d["a"] = 1
print(d["a"])
print(d["b"])

#count unique values
d = {"a": 1, "b": 2, "c": 1}
print(len(set(d.values())))

#sort dictionary by key
d = {"b": 2, "a": 1}
sorted_d = dict(sorted(d.items()))
print(sorted_d)

#sort dictionary by value
d = {"b": 2, "a": 1}
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_d)

#filter by value
d = {"a": 1, "b": 2, "c": 3}
filtered = {k: v for k, v in d.items() if v > 1}
print(filtered)

#check for common keys
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
common = any(k in d1 for k in d2)
print(common)

#create dict from tuple
t = (("a", 1), ("b", 2))
d = dict(t)
print(d)

#get first key-value pair
d = {"a": 1, "b": 2}
if d:
    print(next(iter(d.items())))
else:
    print("empty")

# remove key safely with pop
d = {"a": 1, "b": 2}
key = input("key to pop: ")
val = d.pop(key, "key not found")
print(val)

# merge dictionaries with update
d1 = {"a": 1}
d2 = {"b": 2}
d1.update(d2)
print(d1)

# get all items as list of tuples
d = {"a": 1, "b": 2}
print(list(d.items()))

# check if any value meets condition
d = {"a": 1, "b": 5}
print(any(v > 3 for v in d.values()))

# get all keys with string type values
d = {"a": "x", "b": 3, "c": "y"}
keys = [k for k, v in d.items() if isinstance(v, str)]
print(keys)

# count how many keys start with a given prefix
d = {"apple": 1, "banana": 2, "apricot": 3}
prefix = input("prefix: ")
count = sum(1 for k in d if k.startswith(prefix))
print(count)

# safely get nested value with default
d = {"a": {"x": 1}}
val = d.get("a", {}).get("x", "not found")
print(val)

# swap keys and values (only if values are unique)
d = {"a": 1, "b": 2}
inv = {v: k for k, v in d.items()}
print(inv)

# update multiple keys
d = {"a": 1, "b": 2}
updates = {"a": 10, "c": 3}
d.update(updates)
print(d)

# create dictionary with keys from list and default value
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
print(d)

# get dictionary keys sorted as list
d = {"b": 2, "a": 1}
print(sorted(d.keys()))

# filter dictionary by keys starting with a letter
d = {"apple": 1, "banana": 2, "apricot": 3}
filtered = {k: v for k, v in d.items() if k.startswith("a")}
print(filtered)

#clear dictionary
d = {"a":1, "b":2}
d.clear()
print(d)  # {}

#check if dictionary is empty
d = {}
print(len(d) == 0)  # True

#get key-value pair if key exists
d = {"a":1, "b":2}
k = "a"
if k in d:
    print((k, d[k]))
else:
    print("key not found")

#update value for a specified key
d = {"a":1, "b":2}
d["a"] = 10
print(d)

#count how many times a value appears
d = {"a":1, "b":2, "c":1}
v = 1
count = list(d.values()).count(v)
print(count)

#invert dictionary (swap keys and values)
d = {"a":1, "b":2, "c":1}
inverted = {}
for key, val in d.items():
    inverted[val] = key
print(inverted)

#find keys with a specific value
d = {"a":1, "b":2, "c":1}
v = 1
keys = [k for k, val in d.items() if val == v]
print(keys)

#create dictionary from two lists
keys = ["a", "b", "c"]
vals = [1, 2, 3]
d = dict(zip(keys, vals))
print(d)

#check if dictionary has nested dictionaries
d = {"a":1, "b":{"x":10}, "c":3}
has_nested = any(isinstance(v, dict) for v in d.values())
print(has_nested)

#get nested value safely
d = {"a":1, "b":{"x":10}, "c":3}
nested_val = d.get("b", {}).get("x", None)
print(nested_val)

#create default dictionary (default value for missing keys)
from collections import defaultdict
d = defaultdict(lambda: "default")
d["a"] = 1
print(d["a"])  # 1
print(d["b"])  # default

#count unique values
d = {"a":1, "b":2, "c":1}
unique_count = len(set(d.values()))
print(unique_count)

#sort dictionary by key
d = {"b":2, "a":1, "c":3}
sorted_by_key = dict(sorted(d.items()))
print(sorted_by_key)

#sort dictionary by value
d = {"b":2, "a":1, "c":3}
sorted_by_val = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_by_val)

#filter dictionary by value condition (value > 1)
d = {"a":1, "b":2, "c":3}
filtered = {k:v for k,v in d.items() if v > 1}
print(filtered)

#check for common keys between two dictionaries
d1 = {"a":1, "b":2}
d2 = {"b":3, "c":4}
common = bool(set(d1.keys()) & set(d2.keys()))
print(common)

#create dictionary from tuple of key-value pairs
t = (("a",1), ("b",2), ("c",3))
d = dict(t)
print(d)

#get first key-value pair
d = {"a":1, "b":2, "c":3}
if d:
    first_pair = next(iter(d.items()))
    print(first_pair)
else:
    print("empty dict")
