# usando str, se contatenan en lugar de sumarse
x = input("Valor de x ? ")
y = input("Valor de y ? ")
z= x + y
print(z)


#Forma de sumar dos numeros
a = input("Valor de x ? ")
b = input("Valor de y ? ")
c= int(a) + int(b)
print(c)

#Forma de sumar dos numeros
d = int(input("Valor de x ? "))
r = int(input("Valor de y ? "))
print(d+r)

#Forma de sumar dos numeros
print(int(input("Valor de x ? "))+int(input("Valor de x ? ")) )

#Float
e = float(input("Valor de x ? "))
f = float(input("Valor de y ? "))
print(e+f)

#Como separamos con comas

g = float(input("Valor de x ? "))
h = float(input("Valor de y ? "))
i = round(g + h)
print(f"{i:,}")


j = float(input("Valor de x ? "))
k = float(input("Valor de y ? "))
l = x / y
l = round(j / k, 2)
print(f"{l:,}")

#Si queremos n=2 digitos
m = float(input("Valor de x ? "))
n = float(input("Valor de y ? "))
o = m / n
print(f"{o:.2f}")
