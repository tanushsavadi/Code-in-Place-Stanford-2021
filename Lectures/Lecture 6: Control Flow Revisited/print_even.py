"""
Print Even Numbers
Write a program to print the first 100 even numbers


Example of using the index variable of a for loop
"""

def main():
    for i in range(1,101):
        if i % 2 == 0:
            print(i, "Even number")

if __name__ == '__main__':
    main()
