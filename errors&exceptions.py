def f():
    try:
        1/0
    finally:
        return 42
print f()

while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "OOps! That was no valid number!"
    except(RuntimeError, TypeError, NameError):
        pass