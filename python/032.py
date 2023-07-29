def named(**kwargs):  # *args and **kwargs are standard
    print(kwargs)

named(name="Jim", age=25)

details = {"name": "Sue", "age": 25}
named(**details) # dereference, or else details will be passed in as the lone piece of data


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

    
print_nicely(name="Hong", age=27)

def both(*args, **kwargs): #why not both?
    print(f"args: {args}") # tuple
    print(f"kwargs: {kwargs}") # dictionary

both(1, 3, 5, name="Bob", age=25)

def myfunction(**kwargs):
    print(kwargs)

myfunction(**"Bob") # error, not a dictionary so can't deference
myfunction(**None) # error, not a dictionary, so can't encode