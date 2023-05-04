print("Zadanie 1")
print()

a=b=c=10

print("a =",a,"ID a =",id(a),"\n""b =",b,"ID b =",id(b),"\n""c =",c,"ID c =",id(c) )
print()
print ("### Zmiana danych ###")
print()
a = 20
print("a =",a,"ID a =",id(a),"\n""b =",b,"ID b =",id(b),"\n""c =",c,"ID c =",id(c))
print()
print("Zadanie 2")
print()
a=b=c = [1,2,3]
print("a =",a,"ID a =",id(a),"\n""b =",b,"ID b =",id(b),"\n""c =",c,"ID c =",id(c))
print()
print ("### Zmiana danych ###")
print()
a = [1,2,3,4]
print("a =",a,"ID a =",id(a),"\n""b =",b,"ID b =",id(b),"\n""c =",c,"ID c =",id(c))
print()
print("Zadanie 3")
print()
x=10
y=10
print(id(x), id(y))
y = y + 1 - 1
print(id(x), id(y))
y = y + 1234567890 - 1234567890
print(id(x), id(y))