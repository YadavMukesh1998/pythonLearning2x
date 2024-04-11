# strings
# bunch of char
# "" or ''
name = "Mukesh"
name2 = 'Mukesh '
print(name)
print(name2)
print(type (name2))
print(type (name))

# raw String
# this will be helpful in dir path

dir = "C:\abc\abc.txt"
dir = 'C:\abc\abc.txt'
print(dir)
print(dir)

# from abc a will be missing bcz \a is a special char, to solve this we have to use raw string.
dir = r'C:\abc\abc.txt'
print(dir)