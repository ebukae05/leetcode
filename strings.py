#strings similar to arrays
s = "abc"
print(s[0:2])

# but they are immutable
# s[0] = "d"

#updating string creates new string
s += "def"
print(s)

# valid numeric strings can be converted
print(int("123") + int("456"))

#and numbers can be converted to stings
print(str(123) + str(456))

#combine a list of strings
# (with empy string) delimitor

strings = ["ab", "cd", "ef"]
print("".join(strings))
