#march: hacer el codigo mas compacto
name = input("What`s your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffidor")
    
    case "Draco":
        print("Gryffidor") 
    case _:
        print("You are not a wizard")
    