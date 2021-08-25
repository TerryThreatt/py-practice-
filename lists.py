# similar to Arrays in Javascript
colors = ["purple", "teal", "green"]

# for color in colors:
#     print(color)

# numbers = [1, 2, 3, 5]
# index = 0

# while index < len(numbers):
#     print(numbers[index])
#     index += 1

# index = 0

# while index < len(colors):
#     print(f"{index}: {colors[index]}")
#     index += 1

data = [1, 2, 3]

data_squared = [x for x in data]
print(data_squared)

# add to the list on the end
data.append("purple")

# adds all items to the end
data.extend([4, 5, 6])

# add to the list at the index
data.insert(1, "hi")
data.pop()
data.remove("hi")

print(data)

# names data set
names = ["terry", "buster", "kristal", "buster"]
print(names.index("terry", 0))
print(names.count("buster"))
