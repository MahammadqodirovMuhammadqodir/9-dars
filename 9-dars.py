import math

a = int(input("Kvadratning tomonini kiriting: "))
P = 4*a
print(f"Peremetr {P}")



a = int(input("Kvadratning tomonini kiriting: "))
S = a**2
print(f"Yuzasi {S}")




a = int(input("1-to`rt burchakning tomonini kiriting: "))
b = int(input("2-to`rt burchakning tomonini kiriting: "))
S = a*b
P = 2*(a+b)
print(f"Peremtri {S, P}")





a = int(input("Aylananing deametrini kiriting: "))
math.pi
L = math.pi * a
print(f"Aylanani uzunligi {L}")


a = int(input("Aylananing deametrini kiriting: "))
V = a**3
S = 6*a**2
print(f"To`la sirti {V, S}")


a = int(input("1-Parala pepedning tomonlarini kiriting: "))
b = int(input("2-Parala pepedning tomonlarini kiriting: "))
c = int(input("3-Parala pepedning tomonlarini kiriting: "))
V = a*b*c
S = 2*(a*b+b*c+a*c)
print(f"To`la sirti {V, S} ")



R =int(input("Doirani radiusini kiriting: "))
L = 2*math.pi*R
S = math.pi*R**2
print(f"Yuzasi {L, S}")


a =int(input("1-sonni kiriting: "))
b =int(input("2-sonni kiriting: "))
S = (a+b)/2
print(f"Arfmetigi {S}")




a =int(input("1-sonni kiriting: "))
b =int(input("2-sonni kiriting: "))
L = a*b
print(f"o`rta geometrigi{L}")



a =int(input("1-sonni kiriting: "))
b =int(input("2-sonni kiriting: "))
print(f"Yig`indisi{a+b}, \nKo`paytmasi{a*b}, \nAning kvadrati{a**2}, \nb ning kvadrati{b**2}")


a =int(input("1-sonni kiriting: "))
b =int(input("2-sonni kiriting: "))
print(f"Yig`indisi{a+b}, \nKo`paytmasi{a*b}, \nAning moduli{abs(a)}, \nb ning moduli {abs(b)}")


a =int(input("1-Tog`ri uchburchakning katetlarini kiriting: "))
b =int(input("2-Tog`ri uchburchakning katetlarini kiriting: "))
c = a**2*b**2
L = a+b+c
print(f"Peremtri { c, L}")


a =int(input("1-Radiusni kiriting: "))
b =int(input("2-Radiusni kiriting: "))
S_1 = math.pi*a
S_2 = math.pi*b
S_3 = math.pi*(a-b)
print(F"Ayirmasi{S_1, S_2, S_3}")


L =int(input("1-Uzunlikni kiriting: "))
R = 2*math.pi/L
S = math.pi*R**2
print(f"yuzasi{S}, Radius{R}")


S =int(input("1-Uzunlikni kiriting: "))
R = math.sqrt(S/math.pi)
D = 2*R
print(f"Diametr{D}, \nRadius{R}")



a =int(input("1-Sonlar o`qini kiriting: "))
b =int(input("2-Sonlar o`qini kiriting: "))
S = abs(b-a)
print(f"Kesmani uzunligi {S}")



a =int(input("1-nuqtani kiriting: "))
b =int(input("2-nuqtani kiriting: "))
c =int(input("2-nuqtani kiriting: "))
S = abs(c-b)
D = abs(c-b)
print(f"Uzunligini yig`indisi{S+D}")


a =int(input("1-nuqtani kiriting: "))
b =int(input("2-nuqtani kiriting: "))
c =int(input("2-nuqtani kiriting: "))
S = abs(c-b)
D = abs(c-b)
print(f"Uzunligini yig`indisi{S*D}")


x_1 = int(input("1-sonni kiriting: "))
x_2 = int(input("2-sonni kiriting: "))
y_1 = int(input("3-sonni kiriting: "))
y_2 = int(input("4-sonni kiriting: "))
D = math.sqrt(x_2-x_1)**2+(y_2-y_1)**2
print(f"Orasidagi masofa {D}")


a =int(input("A-sonni kiriting: "))
b =int(input("B-sonni kiriting: "))
print(f"A soni{b}, B soni{a}")


a =int(input("A-sonni kiriting: "))
b =int(input("B-sonni kiriting: "))
c =int(input("C-sonni kiriting: "))
print(f"A soni{b}, B soni{c}, C soni{a}")



a =int(input("A-sonni kiriting: "))
b =int(input("B-sonni kiriting: "))
c =int(input("C-sonni kiriting: "))
print(f"A soni{c}, B soni{a}, C soni{b}")


x =int(input("sonni kiriting: "))
y =x**6-x**2-7
print(f"Funksiya qiymati {y}")



x =input("sonni kiriting: ")
y =4(x-3)**6-7(x-3)**3+2
print(type("Funksiya qiymati ", y))