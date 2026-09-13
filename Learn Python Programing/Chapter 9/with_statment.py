f =open("file.txt")
print=(f.read())

# the same can be written using with statment like this:
with open("file.txt") as f:
    print=(f.read())