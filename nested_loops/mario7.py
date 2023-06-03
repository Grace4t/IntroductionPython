def main():
    print_square(5)

def print_square(size):
    # For para cada fila (row)
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
    
main()