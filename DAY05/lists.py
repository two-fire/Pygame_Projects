# stuff = [42, 3.14, True, None, "Foo Bar", ['another', 'list'], {'a': 'Dictionary', '\
# language' : 'Python'}]
# print(stuff)

# ------------------------------------------------------

# [42, 3.14, True, None, 'Foo Bar', ['another', 'list'], {'a': 'Dictionary', 'language\
# 2 ': 'Python'}]

# --------------------------------------------------------

# more_stuff = [
# 42,
# 3.14,
# True,
# None,
# "Foo Bar",
# ['another', 'list'],
# {
# 'a': 'Dictionary',
# 'language' : 'Python',
# },
# ]
# print(more_stuff)

# --------------------------------------------------------
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
#
# print(planets) # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
# print(len(planets)) # 6
#
# print(planets[0]) # Mercury
# print(type(planets[0])) # <class 'str'>
# print(planets[3]) # Mars
#
# print(planets[0:1]) # ['Mercury']
# print(type(planets[0:1])) # <class 'list'>
# print(planets[0:2]) # ['Mercury', 'Venus']
# print(planets[1:3]) # ['Venus', 'Earth']
#
# print(planets[2:]) # ['Earth', 'Mars', 'Jupiter', 'Saturn']
# print(planets[:3]) # ['Mercury', 'Venus', 'Earth']
#
# print(planets[:]) # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn\ ']

# --------------------------------------------------------

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# print(letters[::]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# print(letters[::1]) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# print(letters[::2]) # ['a', 'c', 'e', 'g', 'i']
#
# print(letters[1::2]) # ['b', 'd', 'f', 'h', 'j']
#
# print(letters[2:8:2]) # ['c', 'e', 'g']
#
# print(letters[1:20:3]) # ['b', 'e', 'h']

# --------------------------------------------------------
# x = ['abc', 'def', 'ghi', 'jkl']
# x[0] = 'qqrq'
# print(x) # ['qqrq', 'def', 'ghi', 'jkl']
#
# x[1:3] = ['xyz', 'dod']
# print(x) # ['qqrq', 'xyz', 'dod', 'jkl']
#
#
# x[1:3] = ['bla']
# print(x) # ['qqrq', 'bla', 'jkl']
#
# x[1:2] = ['elp', 'free']
# print(x) # ['qqrq', 'elp', 'free', 'jkl']


# x[1] = ['elp', 'free']
# print(x) # ['qqrq', ['elp', 'free'], 'jkl']

# --------------------------------------------------------
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# numbers[1::2] = [0, 0, 0, 0, 0, 0]
# print(numbers) # [1, 0, 3, 0, 5, 0, 7, 0, 9, 0, 11, 0]

# --------------------------------------------------------

# x = ['apple', 'bob', 'cat', 'drone']
# y = x
# x[0] = 'qqrq'
# print(x) # ['qqrq', 'bob', 'cat', 'drone']
# print(y) # ['qqrq', 'bob', 'cat', 'drone']

# --------------------------------------------------------

# a = ["x", "2", "y"]
# b = ["x", 2, "y"]
# print(":".join(a)) # x:2:y
# # print ":".join(b) # TypeError: sequence item 1: expected string, int found
# # convert elements to string using map
# print(":".join( map(str, b) )) # x:2:y

# --------------------------------------------------------

# words = "ab:cd:ef".split(':')
# print(words) # ['ab', 'cd', 'ef']

# # special case: split by spaces
# names = "foo bar baz".split()
# print(names) # ['foo', 'bar', 'baz']

# # special case: split to characters
# chars = list("abcd")
# print(chars) # ['a', 'b', 'c', 'd']

# --------------------------------------------------------

# things = ['apple', 'banana', 'peach', 42]
# for var in things:
#     print(var)

# --------------------------------------------------------
# words = ['apple', 'banana', 'peach', '42']
# if 'apple' in words:
#     print('found apple')

# if 'a' in words:
#     print('found a')
# else:
#     print('NOT found a')

# if 42 in words:
#     print('found 42')
# else:
#     print('NOT found 42')
# --------------------------------------------------------
# words = ['cat', 'dog', 'snake', 'camel']
# print(words.index('snake'))

# print(words.index('python'))
# --------------------------------------------------------

# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
# print(planets) # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
# planets.sort()
# print(planets) # ['Earth', 'Jupiter', 'Mars', 'Mercury', 'Saturn', 'Venus']
#
# planets.sort(reverse=True)
# print(planets) # ['Venus', 'Saturn', 'Mercury', 'Mars', 'Jupiter', 'Earth']