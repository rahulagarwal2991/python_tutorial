# mathematical operations
# union() : 

# intersection()
# difference()
# symmetric difference()

# Union: it is used to return all elements present in both the set
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}
# 1,2,3,4,5,6,7,8,9 -> union
print(set1.union(set2)) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

print(set1 | set2)


# intersection() : it is used to return common elements in both the sets

set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}
# 5 -> intersection
print(set1.intersection(set2)) #{5}
print(set1 & set2) #{5}


# difference() :it will return elements present in set1 but not in set2

set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}

print(set1.difference(set2))

print(set1 - set2)

# it will return elements present in set1 but not in set2
# {1,2,3,4}

print(set2.difference(set1)) # {6,7,8,9}
print(set2 - set1)

# Symmetric difference : it will return element present in set1 and set2 but not common in both

set1 = {1,2,3,4,5, 5,5}
set2 = {5,6,7,8,9}

print(set1.symmetric_difference(set2))
#{1, 2, 3, 4, 6, 7, 8, 9}

print(set1 ^ set2)
#{1, 2, 3, 4, 6, 7, 8, 9}
print(set1) # {1, 2, 3, 4, 5}