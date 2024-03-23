# Lists (Array) in Python []

list = [1, 2, 3, 4, 5]
print(list)

# append()  method is used to add an element at the end of a list.

list.append(6)  
print("After appending: ", list)

# insert() method is used to add an element at any given position in the list.

list.insert(2,7)    # Inserting 7 at index 2
print("After inserting: ", list)

# remove() method is used to delete an element from the list.

list.remove(7)      # Removing 4 from the list
print("After removing: ", list)

#  pop() method removes and returns an element at the specified position from the list.
# If no index is  provided then it removes and returns the last item in
# pop() method removes and returns the last item in the list by default.

list.pop(1)         # Removes and returns the first element i.e., 1
print("After popping out the first element: ", list)

# index()  method returns the index of the specified element in the list.
# It returns the index of the first occurrence of the element.

index_of_element = list.index(3)     # Returns the index of 2 which is 1
print("Index of 2 :", index_of_element)

# count() method returns the number of times an element appears in the list.
number_count = list.count(1)        # Counts how many times 1 occurs in the list
print("Number of times 1 comes in the list: ", number_count)

# sort() method sorts all the elements in the list in ascending order.
# The sort() method modifies the original list.

list.sort()          # Sorting the list
print("Sorted List: ", list)

# reverse() method reverses the list.
# The reverse() method also modifies the original list.

list.reverse()       # Reversing the list
print("Reversed List: ", list)

# Adding elements using extend() method
another_list = [7, 8, 9]
list.extend(another_list)   
print("After extending with another list: ", list)