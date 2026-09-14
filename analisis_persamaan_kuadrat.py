print("Analisis Persamaan Kuadrat")

a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    diskriminan = b ** 2 - 4 * a * c
    print(f"Diskriminan = {diskriminan:.2f}")

    # Menentukan jenis akar berdasarkan diskriminan
    if diskriminan > 0:
        print("Persamaan memiliki dua akar real berbeda.")
        
        x1 = (-b + diskriminan ** 0.5) / (2 * a)
        x2 = (-b - diskriminan ** 0.5) / (2 * a)
        
        print(f"Akar pertama = {x1:.2f}")
        print(f"Akar kedua = {x2:.2f}")

    elif diskriminan == 0:
        print("Persamaan memiliki satu akar real kembar.")
        
        x = -b / (2 * a)
        print(f"Akar kembar = {x:.2f}")

    else:
        print("Persamaan tidak memiliki akar real.")
