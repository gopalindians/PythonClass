__author__ = 'gopalindians'

# Lists (Like arrays)

print("Exercises on List http://www.afterhoursprogramming.com/tutorial/Python/Lists/\n")

val = [1, 2, 3, 4, 5, 6, 7, 8]
print("Assign val as \"val = [1, 2, 3, 4, 5, 6, 7, 8]\"", )

print("Current elements in val:", val)

print("-------------------------------------------------")

# v2 using for loop

print("Using for loop\n")
print("for a in val:\n\tprint(a)\n")
print("Outputs:")

for a in val:
    print("\t", a)

print("-------------------------------------------------")

# v3 using index

print("Use of index")
print("Example:  val[1:3] - Ouptputs:  2 3")
print("Take care of index(Index starts at 0)")
print("Val[1:5]:", val[1:5])  #prints [2 3 4 5]

print("-------------------------------------------------")

#Common operations on List

print(val)  # List before appending
val.append(12)  #.append(value) - appends element to end of the list

print(val)  #List after appending

print("-----------------------------")
print("COUNT-  .count('x') | .count(int)")
print("val.count(1): ", val.count(1))  #Prints 1  .count('x') - counts the number of occurrences of 'x' in the list
print("val.count(12):", val.count(12))  #Prints 1
print("Current list: ", val)
val.append(12)
print("After appending list with 12 :", val)

print("val.count(12):", val.count(12))  #Prints 2




