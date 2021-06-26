# # map
# nums = [1, 2, 3, 4]

# doubles = map(lambda x: x*2, nums)
# print(doubles)


# map in Action

# get lastname for each item

names = [
    {'first':'Rusty',
    'last': 'Steele'},
    {'first':'Colt',
    'last': 'Steele'},
    {'first':'Blue',
    'last': 'Steele'}
]

first_name = list(map(lambda x: x['first'], names))

print(first_name)