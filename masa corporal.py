print("DESEA SABER SU MASA CORPORAL")
nombre=input("favor ingresar nombre: ")
peso=float(input("favor ingresar su peso: "))
altura=float(input("favor ingresar su altura: "))
masa=peso/(altura**2)
print(f"su masa corporal es: {masa:.1f}")