#esto es un comenteario de python
edad=int(input("Ingrese una edad: "))
saldo=float(input("Ingrese un saldo: "))
t="Años"
print("")
print("")
print(edad, t) #muestra el tipo de dato
print(str(edad)+ " " + t) #muestra el tipo de dato
if edad<18: 
  print("\n\nEs menor de edad")
elif edad>=18:
  print("\n\nEs mayor de edad")
if edad>=18 and saldo>3000:
  print("Puede hacer un préstamo\n")
else:
  if(edad<18):
    print("No puede hacer un préstamo por la edad")
    print("Espere", 18-edad, "años más\n")
  else:
    print("No puede hacer un préstamo por el saldo")
    print("Espere a tener", 3000-saldo, " quetzales más\n")
print("Actualice tu saldo")
saldo2=float(input("Ingrese un saldo a agregar: "))
saldo=saldo+saldo2
print(saldo)