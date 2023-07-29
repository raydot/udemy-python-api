# function that takes any number of args
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total

print(multiply(1, 3, 5))

def multiply2(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total

def apply(*args, operator): #collect all position arguments with a required named argument at the end
    if operator == "*":
        return multiply2(*args) #need this or else you'll return a tuple
    elif operator == "+":
        return (sum(args))
    else: 
        return "No valid operator passed"


print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 6, 7, operator="*")) 


def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums)) # passes one value for each parameter


def addParams(x, y):
    return x + y

nums2 = {"x": 15, "y": 25}
# here's one way to match the dictionary to the function:
print(add(x=nums2["x"], y=nums2["y"]))
# or this:
print(add(**nums2)) # pass values as named arguments