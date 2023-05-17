def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Is even")
    else:
        print("Is odd")

def is_even(n):
    return n % 2 == 0
#Si nos va a regresar un valor boleano (T o F)
main()