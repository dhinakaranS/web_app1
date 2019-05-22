import json

# from basics import

# p1 = Person("John", 36)
# p1.getAge()

# person = {
#     'first_name': "Joshn",
#     "isAlive": True,
# }
# read file
with open('demo.json', 'r') as myfile:
    data=myfile.read()

users = json.loads(data) # reads string and parse dumps: json->string

# for user in users:
#     aUser = users[user]
#     for val in aUser:
#         print(val['first_name'])

for key, user in users.items(): #dic method  
  servletCollection =  user['servlet']   
  for collect in servletCollection:
    print(collect['servlet-name'])

# with open('demo.json', 'w') as f:  # writing JSON object
#     json.dump(person, f)

# # parse file
# obj = json.loads(data)

# stocks = {
#     'IBM': 146.48,
#     'MSFT':44.11,
#     'CSCO':25.54
#     }

# for c in stocks:
#     print(c)

# #sets

# # initialize A and B
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# # use ^ operator
# # Output: {1, 2, 3, 6, 7, 8}
# print(B.union(A))
