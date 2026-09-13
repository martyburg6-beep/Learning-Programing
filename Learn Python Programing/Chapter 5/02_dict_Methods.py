marks = {
    "hanzka":100,
    "life" :13,
    "Money": 84,

}
# print(marks,type(marks))

# print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"hanzka":99})
print(marks)
print(marks.get("hanzka")) # prints None 
print(marks["hanzka"]) # prints Keyerror


