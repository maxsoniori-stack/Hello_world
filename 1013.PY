numero = input().split()
a = int(numero[0])
b = int(numero[1])
c = int(numero[2])
d = int(((a+b+abs(a-b))/2))
if d < c:
    print(f"{c} eh o maior")
else: 
    print(f"{d} eh o maior") 
  