"""
File: birthday.py
-----------------
Program to show an example of using dictionaries with functions.
We have a dictionary representing people's ages and then 
increment the ages when they have a birthday.
"""


def have_birthday(dict, name):
    """
    Print a birthday message and increment the age of the person
    with the given name in the dictionary passed in.
    """
    print("You're one year older, " + name + "!")
    dict[name] += 1


def main():
    ages = {'Chris': 33, 'Julie': 22, 'Mehran': 50}
    print(ages)
    have_birthday(ages, 'Chris')
    print(ages)
    have_birthday(ages, 'Mehran')
    print(ages)


# Python boilerplate.
if __name__ == '__main__':
    main()
