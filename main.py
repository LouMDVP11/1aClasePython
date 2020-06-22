from os import system
n1=float(input("Ingrese un número: "))
n2=float(input("Ingrese otro número: "))
op=int(0)
while op!=4:
  print("\n\tM E N U")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. SALIR\n")
  op=int(input("Ingrese una opción: "))
  if op==1:
    print("El resultado de la suma es", n1+n2)
  elif op==2:
    print("El resultado de la resta es", n1-n2)
  elif op==3:
    print("El resultado de la multiplicación es", n1*n2)
  elif op==4:
    print("Vuelva pronto")
  else:
    print("Usted ingresó un número no válido")
  g=input("\nPresione una tecla para continuar...")
  system("clear")