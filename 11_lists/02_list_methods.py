'''List Methods in Python are some built-in functions that operate on Python Lists and help modify, sort, search, or perform other operations on Lists.'''

marks = [1, 2, 3, 4, 5]
extra_marks = [6, 7, 8]

print(marks)

# marks.append(63) # This will change the original list and .append(63) means — Add the number 63 to the end of the (marks) list. .append() is a Python list method that adds new items to the end of the list. This modifies the original marks list.

# marks.pop() #.pop() removes the last item. .pop(i) removes the item at position i
# marks.pop(2)

# marks.extend(extra_marks) # Here, the .extend() method adds all the items of the extra_marks list to the end of the marks list, one by one. That is, each element of extra_marks will be included in the marks list separately, but not as another list.

# marks.insert(0, 9) # Here index = 0, meaning 9 will be placed in the 1st position (index 0). Previous list: [1, 2, 3, 4, 5]. 9 will now be placed where 1 was, and all subsequent ones including 1 will be moved one space.

# marks.remove(5) # .remove(value) → Removes a specific value from the list. Here, the number 5 will be removed. List: [1, 2, 3, 4, 5]. 5 is in the 5th position (index 4), that will be removed.

# marks.reverse() # .reverse() → Reverses the entire list, meaning the last item comes first, the first goes last. Output: List before: [1, 2, 3, 4, 5]. List after: [5, 4, 3, 2, 1].

# marks.sort() # .sort() → Sorts the list in ascending order. e.g. Output: List before: [5, 4, 3, 2, 1]. List after: [1, 2, 3, 4, 5]

marks.sort(reverse=True) # .sort(reverse=True) → Sorts the list in descending order.  e.g. Output: List before: [1, 2, 3, 4, 5]. List after: [5, 4, 3, 2, 1].

print(marks)