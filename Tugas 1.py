print("\t====what do you want?====\n\t\t1. calculate area of rectangle\n\t\t2. calculate area of circle\n\t\t3. calculate surface area of a cube\n\t\t4. convert C to F\n\t\t5. convert R to K")

pilihan = input("select one of them: ")
if pilihan.upper() == "1":
    panjang = float(input("input length: "))
    lebar = float(input("input width: "))
    print(f"Luas adalah {panjang * lebar} meter persegi")
elif pilihan.upper() == "2":
    jari2 = float(input("input radius: "))
    print(f"Luas Lingkaran adalah {3.14 * jari2} meter persegi")
elif pilihan.upper() == "3":
    sisi = float(input("input sisi: "))
    print(f"Luas permukaan kubus adalah {sisi ** 2 * 6} meter persegi")
elif pilihan.upper() == "4":
    ctof = float(input("input value to convert: "))
    print(f"{(ctof * 1.8) + 32} Fahrenheit")
else:
    rtok = float(input("input value to convert: "))
    print(f"{(rtok * 1.25) + 273.15} Kelvin")