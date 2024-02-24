numbers = [10, 25, 30, 45, 50]

for num in numbers:
    if num < 20:
        print(f"{num} es menor que 20")
    elif num < 40:
        print(f"{num} está entre 20 y 40")
    else:
        print(f"{num} es mayor o igual a 40")