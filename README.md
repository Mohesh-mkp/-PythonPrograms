# Interview key concepts related to Python
### Window popup in Selenium (windows level not browser)
### MRO
### Memory management in Python
### sorting dictionary 
### File handling
### float division
### Delete in dictionary and list (removing multiple elements)
```python
'''
############################################################################################ Concepts of Set ################################################################################
my_list = [1, 2, 2, 3, 4, 4, 5]

unique_set = set(my_list)

## To add element in set
unique_set.add(8)
print(unique_set)

unique_set.update([9,7,14])
print(unique_set)

## To remove element in set
unique_set.remove(9)
print(unique_set)

unique_set.discard(9) # will not throw error if the element is not visible
print(unique_set)

unique_set.discard(7)
print(unique_set)

popped_element = unique_set.pop() # will remove a random element [will not take any arguments]
print(popped_element, unique_set)

'''
# Set Operations:

set1 = {1,2,3,4,5}
set2 = {3,5,7,9,2}

### Union

Union_set = set1 | set2
union_set = set1.union(set2)

print(Union_set, union_set)

### Intersection 

Intersection_set = set1 & set2
inter_set = set1.intersection(set2)

print(Intersection_set, inter_set)

### Difference 

Difference_Set = set1 - set2
diff_Set = set1.difference(set2)

print(Difference_Set,diff_Set)

### Symmetric Difference

Symm_diff_set = set1 ^ set2
symm_set = set1.symmetric_difference(set2)

print(Symm_diff_set, symm_set)


# Set Methods

# Check if an element is in the set
print(3 in set1)

# Get the length of the set
print(len(set1))

# Copy a set
copied_set = {(1,2,3)}

# Clear all elements from a set
set1.clear()

print(copied_set, set1)
```
