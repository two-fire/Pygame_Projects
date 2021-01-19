# Loop over keys
# user = {
#     'fname': 'Foo',
#     'lname': 'Bar',
# }
#
# for k in user.keys():
#     print(k)
#
# # lname
# # fname
#
# for k in user.keys():
#     print("{} -> {}".format(k, user[k]))
#
#     # lname -> Bar
#     # fname -> Foo

##########################
# Loop using items
people = {
    "foo" : "123",
    "bar" : "456",
    "qux" : "789",
}

for name, uid in people.items():
    print("{} => {}".format(name, uid))
# foo => 123
# bar => 456
# qux => 789
user = {
    'fname': 'Foo',
    'lname': 'Bar',
}

for t in user.items(): # returns tuples
    print("{} -> {}".format(t[0], t[1]))
#print("{} -> {}".format(*t))

# lname -> Bar
# fname -> Foo