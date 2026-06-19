"""
Python Data Structure Exercises
List | Dictionary | Tuple | Set
Each exercise prints the question first, then runs the code and shows the output.
"""

from collections import Counter, defaultdict


def show(title):
    print("\n" + "=" * 65)
    print(title)
    print("=" * 65)


# ===========================================================
# LIST EXERCISES
# ===========================================================

show("List Exercise 1: Perform Basic List Operations")
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)
fruits.append("orange")
print("After append('orange'):", fruits)
fruits.remove("banana")
print("After remove('banana'):", fruits)
print("Element at index 1:", fruits[1])
fruits.insert(1, "mango")
print("After insert(1, 'mango'):", fruits)
print("Length of list:", len(fruits))


show("List Exercise 2: Perform List Manipulation")
numbers = [5, 3, 8, 1, 9, 2]
print("Original list:", numbers)
numbers.extend([10, 20])
print("After extend([10, 20]):", numbers)
numbers.sort()
print("After sort() (ascending):", numbers)
numbers.sort(reverse=True)
print("After sort(reverse=True) (descending):", numbers)
print("Slice [1:4]:", numbers[1:4])
numbers.reverse()
print("After reverse():", numbers)


show("List Exercise 3: Sum and average of all numbers in a list")
nums = [10, 20, 30, 40, 50]
total = sum(nums)
average = total / len(nums)
print("List:", nums)
print("Sum:", total)
print("Average:", average)


show("List Exercise 4: Reverse a list")
lst = [1, 2, 3, 4, 5]
reversed_lst = lst[::-1]
print("Original list:", lst)
print("Reversed list:", reversed_lst)


show("List Exercise 5: Turn every item of a list into its square")
nums = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in nums]
print("Original list:", nums)
print("Squared list:", squares)


show("List Exercise 6: Find Maximum and Minimum")
nums = [4, 9, 2, 7, 1, 8]
print("List:", nums)
print("Maximum:", max(nums))
print("Minimum:", min(nums))


show("List Exercise 7: Count Occurrences")
lst = [1, 2, 2, 3, 2, 4, 5, 2]
print("List:", lst)
print("Occurrences of 2:", lst.count(2))


show("List Exercise 8: Sort a list of numbers")
nums = [5, 2, 9, 1, 7]
print("Original list:", nums)
print("Sorted ascending:", sorted(nums))
print("Sorted descending:", sorted(nums, reverse=True))


show("List Exercise 9: Create a copy of a list")
original = [1, 2, 3]
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]
copy1.append(4)
print("Original list:", original)
print("copy1 (using .copy(), then modified):", copy1)
print("copy2 (using list()):", copy2)
print("copy3 (using slicing):", copy3)


show("List Exercise 10: Combine two lists")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("list1:", list1)
print("list2:", list2)
print("Combined list:", combined)


show("List Exercise 11: Remove empty strings from the list of strings")
strings = ["Hello", "", "World", "", "Python", ""]
filtered = [s for s in strings if s != ""]
print("Original list:", strings)
print("After removing empty strings:", filtered)


show("List Exercise 12: Remove Duplicates from list")
lst = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(dict.fromkeys(lst))
print("Original list:", lst)
print("List after removing duplicates (order preserved):", unique_list)


show("List Exercise 13: Remove all occurrences of a specific item from a list")
lst = [2, 4, 2, 5, 2, 6, 2]
item_to_remove = 2
result = [x for x in lst if x != item_to_remove]
print("Original list:", lst)
print(f"After removing all occurrences of {item_to_remove}:", result)


show("List Exercise 14: List Comprehension for Numbers")
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers from 1 to 10 using list comprehension:", evens)


show("List Exercise 15: Access Nested Lists")
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list:", nested)
print("Element at nested[1][2]:", nested[1][2])
for row in nested:
    print("Row:", row)


show("List Exercise 16: Flatten Nested List")
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print("Nested list:", nested)
print("Flattened list:", flat)


show("List Exercise 17: Concatenate two lists index-wise")
list1 = [[1, 3], [5, 7], [9, 11]]
list2 = [[2, 4], [6, 8], [10, 12]]
result = [list1[i] + list2[i] for i in range(len(list1))]
print("list1:", list1)
print("list2:", list2)
print("Concatenated index-wise:", result)


show("List Exercise 18: Concatenate two lists in the following order")
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
# Order required: list2 elements first, then list1 elements
result = list2 + list1
print("list1:", list1)
print("list2:", list2)
print("Concatenated (list2 then list1):", result)


show("List Exercise 19: Iterate both lists simultaneously")
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for x, y in zip(list1, list2):
    print(f"{x} -> {y}")


show("List Exercise 21: Add new item to list after a specified item")
lst = [10, 20, 30, 40]
target = 20
new_item = 25
idx = lst.index(target)
lst.insert(idx + 1, new_item)
print(f"List after inserting {new_item} right after {target}:", lst)


show("List Exercise 22: Extend nested list by adding the sublist")
nested_list = [[1, 2], [3, 4]]
sub_list = [5, 6]
print("Original nested list:", nested_list)
nested_list.extend([sub_list])
print("After extending with the sublist as a new element:", nested_list)


show("List Exercise 23: Replace list's item with new value if found")
lst = [10, 20, 30, 40, 50]
old_value, new_value = 30, 35
print("Original list:", lst)
if old_value in lst:
    lst[lst.index(old_value)] = new_value
print(f"After replacing {old_value} with {new_value}:", lst)


# ===========================================================
# DICTIONARY EXERCISES
# ===========================================================

show("Dictionary Exercise 1: Perform basic dictionary operations")
d = {"name": "John", "age": 25, "city": "NYC"}
print("Original dict:", d)
print("Access 'name':", d["name"])
d["email"] = "john@example.com"
print("After adding 'email':", d)
d["age"] = 26
print("After updating 'age':", d)
del d["city"]
print("After deleting 'city':", d)


show("Dictionary Exercise 2: Perform dictionary operations")
d = {"a": 1, "b": 2, "c": 3}
print("Dict:", d)
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
print("Items:", list(d.items()))
popped = d.pop("b")
print(f"After pop('b') -> removed value {popped}:", d)
print("get('z', 'Not Found'):", d.get("z", "Not Found"))


show("Dictionary Exercise 3: Dictionary from Lists")
keys = ["name", "age", "city"]
values = ["Alice", 30, "Los Angeles"]
d = dict(zip(keys, values))
print("Keys list:", keys)
print("Values list:", values)
print("Resulting dictionary:", d)


show("Dictionary Exercise 4: Clear Dictionary")
d = {"x": 1, "y": 2}
print("Before clear():", d)
d.clear()
print("After clear():", d)


show("Dictionary Exercise 5: Merge two Python dictionaries into one")
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {**d1, **d2}
print("d1:", d1)
print("d2:", d2)
print("Merged dict:", merged)


show("Dictionary Exercise 6: Count Character Frequencies")
s = "programming"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print("String:", s)
print("Character frequencies:", freq)


show("Dictionary Exercise 7: Access Nested Dictionary")
student = {"name": "Tom", "marks": {"math": 90, "science": 85}}
print("Nested dictionary:", student)
print("Access marks -> math:", student["marks"]["math"])


show("Dictionary Exercise 8: Print the value of key 'history' from nested dict")
sample_dict = {
    'class': {
        'student': {
            'name': 'Mike',
            'marks': {'physics': 70, 'history': 80}
        }
    }
}
print("Nested dictionary:", sample_dict)
print("Value of 'history':", sample_dict['class']['student']['marks']['history'])


show("Dictionary Exercise 9: Modify Nested Dictionary")
print("Before modification:", sample_dict)
sample_dict['class']['student']['marks']['history'] = 95
print("After setting 'history' to 95:", sample_dict)


show("Dictionary Exercise 10: Initialize dictionary with default values")
keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, 0)
print("Keys:", keys)
print("Dictionary with default value 0:", default_dict)


show("Dictionary Exercise 11: Create a dictionary by extracting the keys from a given dictionary")
d = {"a": 1, "b": 2, "c": 3, "d": 4}
keys_needed = ["a", "c"]
new_d = {k: d[k] for k in keys_needed if k in d}
print("Original dict:", d)
print("Keys needed:", keys_needed)
print("Extracted dictionary:", new_d)


show("Dictionary Exercise 12: Delete a list of keys from a dictionary")
d = {"a": 1, "b": 2, "c": 3, "d": 4}
keys_to_delete = ["b", "d"]
print("Original dict:", d)
for k in keys_to_delete:
    d.pop(k, None)
print(f"After deleting keys {keys_to_delete}:", d)


show("Dictionary Exercise 13: Check if a value exists in a dictionary")
d = {"a": 1, "b": 2, "c": 3}
value_to_check = 2
exists = value_to_check in d.values()
print("Dict:", d)
print(f"Does value {value_to_check} exist? {exists}")


show("Dictionary Exercise 14: Rename key of a dictionary")
d = {"name": "Alice", "age": 25}
print("Before rename:", d)
d["full_name"] = d.pop("name")
print("After renaming 'name' to 'full_name':", d)


show("Dictionary Exercise 15: Get the key of a minimum value")
d = {"a": 10, "b": 3, "c": 7}
min_key = min(d, key=d.get)
print("Dict:", d)
print("Key with minimum value:", min_key)


show("Dictionary Exercise 16: Change value of a key in a nested dictionary")
nested = {"x": {"y": {"z": 5}}}
print("Before change:", nested)
nested["x"]["y"]["z"] = 50
print("After change:", nested)


show("Dictionary Exercise 17: Invert Dictionary")
d = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in d.items()}
print("Original dict:", d)
print("Inverted dict:", inverted)


show("Dictionary Exercise 18: Sort Dictionary by Keys")
d = {"banana": 3, "apple": 5, "cherry": 1}
sorted_by_key = dict(sorted(d.items()))
print("Original dict:", d)
print("Sorted by keys:", sorted_by_key)


show("Dictionary Exercise 19: Sort Dictionary by Values")
sorted_by_value = dict(sorted(d.items(), key=lambda item: item[1]))
print("Original dict:", d)
print("Sorted by values:", sorted_by_value)


show("Dictionary Exercise 20: Check if All Values are Unique")
d = {"a": 1, "b": 2, "c": 3}
values = list(d.values())
all_unique = len(values) == len(set(values))
print("Dict:", d)
print("Are all values unique?", all_unique)


# ===========================================================
# TUPLE EXERCISES
# ===========================================================

show("Tuple Exercise 1: Perform Basic Tuple Operations")
t = (10, 20, 30, 40)
print("Tuple:", t)
print("Element at index 2:", t[2])
print("Length:", len(t))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))
print("Concatenation with (50, 60):", t + (50, 60))


show("Tuple Exercise 2: Tuple Repetition")
t = (1, 2, 3)
repeated = t * 3
print("Original tuple:", t)
print("Repeated 3 times:", repeated)


show("Tuple Exercise 3: Slicing Tuples")
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Tuple:", t)
print("Slice t[2:7]:", t[2:7])


show("Tuple Exercise 4: Reverse the tuple")
t = (1, 2, 3, 4, 5)
reversed_t = t[::-1]
print("Original tuple:", t)
print("Reversed tuple:", reversed_t)


show("Tuple Exercise 5: Access Nested Tuples")
nested = (1, 2, (3, 4, (5, 6)))
print("Nested tuple:", nested)
print("Access nested[2][2][1]:", nested[2][2][1])


show("Tuple Exercise 6: Create a tuple with single item 50")
t = (50,)
print("Single item tuple:", t)
print("Type:", type(t))


show("Tuple Exercise 7: Unpack the tuple into 4 variables")
t = (1, 2, 3, 4)
a, b, c, d = t
print("Tuple:", t)
print("a =", a, ", b =", b, ", c =", c, ", d =", d)


show("Tuple Exercise 8: Swap two tuples in Python")
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print("Before swap -> t1:", t1, "t2:", t2)
t1, t2 = t2, t1
print("After swap  -> t1:", t1, "t2:", t2)


show("Tuple Exercise 9: Copy Specific Elements From Tuple")
t = (10, 20, 30, 40, 50)
sub = t[1:4]
print("Original tuple:", t)
print("Copied elements (index 1 to 3):", sub)


show("Tuple Exercise 10: List to Tuple")
lst = [1, 2, 3]
t = tuple(lst)
print("List:", lst)
print("Converted tuple:", t)


show("Tuple Exercise 11: Function Returning Tuple")
def min_max(values):
    return min(values), max(values)

result = min_max([3, 1, 4, 1, 5, 9])
print("Input list: [3, 1, 4, 1, 5, 9]")
print("Function returns (min, max):", result)


show("Tuple Exercise 12: Comparing Tuples")
t1 = (1, 2, 3)
t2 = (1, 2, 4)
print("t1:", t1, ", t2:", t2)
print("t1 == t2:", t1 == t2)
print("t1 < t2:", t1 < t2)


show("Tuple Exercise 13: Removing Duplicates from Tuple")
t = (1, 2, 2, 3, 4, 4, 5)
unique_t = tuple(set(t))
print("Original tuple:", t)
print("Tuple without duplicates:", unique_t)


show("Tuple Exercise 14: Filter Tuples")
t = (1, 2, 3, 4, 5, 6, 7, 8)
even_t = tuple(filter(lambda x: x % 2 == 0, t))
print("Original tuple:", t)
print("Filtered tuple (even numbers only):", even_t)


show("Tuple Exercise 15: Map Tuples")
t = (1, 2, 3, 4)
squared_t = tuple(map(lambda x: x ** 2, t))
print("Original tuple:", t)
print("Tuple after mapping (squares):", squared_t)


show("Tuple Exercise 16: Modify Tuple")
t = (1, 2, 3, 4)
print("Original tuple:", t)
temp_list = list(t)
temp_list[1] = 20
t = tuple(temp_list)
print("Modified tuple (index 1 changed to 20):", t)


show("Tuple Exercise 17: Sort a tuple of tuples by 2nd item")
t = ((1, 3), (4, 1), (2, 2))
sorted_t = tuple(sorted(t, key=lambda x: x[1]))
print("Original tuple of tuples:", t)
print("Sorted by 2nd item:", sorted_t)


show("Tuple Exercise 18: Count Elements")
t = (1, 2, 2, 3, 3, 3, 4)
counts = Counter(t)
print("Tuple:", t)
print("Element counts:", counts)


show("Tuple Exercise 19: Check if all items in the tuple are the same")
t1 = (5, 5, 5, 5)
t2 = (5, 5, 6, 5)
print("t1:", t1, "-> all same?", len(set(t1)) == 1)
print("t2:", t2, "-> all same?", len(set(t2)) == 1)


# ===========================================================
# SET EXERCISES
# ===========================================================

show("Set Exercise 1: Perform Basic Set Operations")
s = {1, 2, 3, 4}
print("Original set:", s)
s.add(5)
print("After add(5):", s)
s.remove(2)
print("After remove(2):", s)
print("Is 3 in set?", 3 in s)
print("Length of set:", len(s))


show("Set Exercise 2: Union of Sets")
a = {1, 2, 3}
b = {3, 4, 5}
print("a:", a, ", b:", b)
print("Union (a | b):", a | b)


show("Set Exercise 3: Intersection of Sets")
print("a:", a, ", b:", b)
print("Intersection (a & b):", a & b)


show("Set Exercise 4: Difference of Sets")
print("a:", a, ", b:", b)
print("Difference (a - b):", a - b)


show("Set Exercise 5: Symmetric Difference")
print("a:", a, ", b:", b)
print("Symmetric Difference (a ^ b):", a ^ b)


show("Set Exercise 6: Add a list of Elements to a Set")
s = {1, 2, 3}
print("Original set:", s)
s.update([4, 5, 6])
print("After update([4, 5, 6]):", s)


show("Set Exercise 7: Set Difference Update")
a = {1, 2, 3, 4}
b = {3, 4}
print("Before -> a:", a, ", b:", b)
a.difference_update(b)
print("After a.difference_update(b):", a)


show("Set Exercise 8: Remove Items From Set Simultaneously")
s = {1, 2, 3, 4, 5}
items_to_remove = {2, 4}
print("Original set:", s)
s.difference_update(items_to_remove)
print(f"After removing {items_to_remove} simultaneously:", s)


show("Set Exercise 9: Check Subset")
a = {1, 2}
b = {1, 2, 3, 4}
print("a:", a, ", b:", b)
print("Is a a subset of b?", a.issubset(b))


show("Set Exercise 10: Check Superset")
print("b:", b, ", a:", a)
print("Is b a superset of a?", b.issuperset(a))


show("Set Exercise 11: Set Intersection Check")
a = {1, 2, 3}
b = {4, 5, 6}
print("a:", a, ", b:", b)
print("Are a and b disjoint (no intersection)?", a.isdisjoint(b))


show("Set Exercise 12: Set Symmetric Difference Update")
a = {1, 2, 3}
b = {3, 4, 5}
print("Before -> a:", a, ", b:", b)
a.symmetric_difference_update(b)
print("After a.symmetric_difference_update(b):", a)


show("Set Exercise 13: Set Intersection Update")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Before -> a:", a, ", b:", b)
a.intersection_update(b)
print("After a.intersection_update(b):", a)


show("Set Exercise 14: Find Common Elements in Two Lists")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print("list1:", list1)
print("list2:", list2)
print("Common elements:", common)


show("Set Exercise 15: Frozen Set")
fs = frozenset([1, 2, 3, 4])
print("Frozen set:", fs)
try:
    fs.add(5)
except AttributeError as e:
    print("Cannot modify a frozenset! Error:", e)


show("Set Exercise 16: Count Unique Words")
text = "the quick brown fox jumps over the lazy dog the fox runs"
words = text.split()
unique_words = set(words)
print("Text:", text)
print("Unique words:", unique_words)
print("Count of unique words:", len(unique_words))

print("\n" + "=" * 65)
print("All exercises completed successfully!")
print("=" * 65)
