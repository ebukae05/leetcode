#funtion
def myFunc(n, m):
    return n * m

print(myFunc(3,4))


#nested functions
def outer(a,b):
    c = "c"

    def inner():
        return a + b + c
    return inner()

print(outer("a", "b"))
