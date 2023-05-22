def main():
    print_square(5)

def print_square(size):
    # For para cada fila (row)
    for i in range(size):
        for j in range(size):
            # For para cada bloque
            print("#", end="")
        # el print() manda una linea en blanco o un punto y aparte
        print()
main()