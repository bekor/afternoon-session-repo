# Play with the decorator in debug mode

def ez_decor(func):
    print("WHEREEEE I AM?")
    def wrapper():
        print("--"*5)
        func()
        print("--"*5)
    return wrapper


print("Before init")
@ez_decor
def printingsomething():
    print("BELA")


if __name__ == '__main__':
    printingsomething()