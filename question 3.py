siblings = ("bittu", "abhilash")
print("My siblings : ", siblings)
print("The no.of siblings I have: ", len(siblings))
# Here we are converting tuple to list in order to add new elements.!
y = list(siblings)
y.append("swaroopa")
y.append("ramesh")
# And converting back to tuple from list in order to print the elements from the tuple
siblings = tuple(y)
print("The updated tuple :", siblings)

