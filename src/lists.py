from collections import deque

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# print(len(fruits),fruits.count('apple'))

# print(fruits.index('banana'))
# print(fruits.index('banana',4))

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

# print(queue.popleft())

squares = [x**2 for x in range(10)]
# print(squares)



matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = []
for i in range(4):
    tmp = []
    for row in matrix:
       tmp.append(row[i])
    transposed.append(tmp)

print(transposed)

transposed = [[row[i] for row in matrix] for i in range(4)]

print(transposed)

transposed = list(zip(*matrix))

print(transposed)

t = 12345, 54321, 'hello!'
print(t)