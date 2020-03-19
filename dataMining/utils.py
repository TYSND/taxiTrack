# function controls all print,pass debug or not as first parameter
def log(*args):
    if args[0]==True: # if is debug
        for string in args:
            print(string,end=' ')
        print()

