#adding 5 to the original value (x) using functions

def main():
    x = int(input("Please enter a value: "))
    x = plus_five(x)
    print('x =',x)

def plus_five(x):
    x += 5
    return x

if __name__ == '__main__':
    main()
