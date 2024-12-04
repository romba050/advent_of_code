with open('inputs/01.in', 'r') as file:
# with open('inputs/01.example', 'r') as file:
    col1, col2 = zip(*(map(int, line.split()) for line in file))
    
# Convert to lists if needed (zip creates tuples)
list1 = list(col1)
list2 = list(col2)

print(list1[:5])
print(list2[:5])

list1.sort()
list2.sort()

print(list1[:5])
print(list2[:5])

assert(len(list1) == len(list2))

sum_of_differences = 0
for i in range(len(list1)):
    sum_of_differences += abs(list1[i] - list2[i])

print(sum_of_differences)

similarity_score = 0
for i in range(len(list1)):
    similarity_score += list1[i] * list2.count(list1[i])

print(similarity_score)