def hello(to="World"):
    print("Hello!, ", to)
hello()
# Ask user for their name and Remove whitespace from str and capitalize use`rs name`
name = input("What`s your name?  ").strip().split()
hello(name)