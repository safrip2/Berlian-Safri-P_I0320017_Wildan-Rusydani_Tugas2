def greet_user():
    print("Welcome")
    print("You can convert any temperature unit to any other unit you want")

def hasilnya():
    print("hasil konversi adalah: ")
greet_user()
satuan = input("satuan yang ingin di konversi: (c f r k) ")
if satuan.upper() == "C":
    konversi1 = input("konversi ke: (f r k) ")
    if konversi1.upper() == "F":
        hasil1 = float(input("nilai yang ingin di konversi: "))
        hasilnya()
        print(f"{(hasil1 * 1.8) + 32} Fahrenheit")
    elif konversi1.upper() == "R":
        hasil2 = float(input("nilai yang ingin di konversi: "))
        hasilnya()
        print(f"{hasil2 * 0.8} Reamur")
    elif konversi1.upper() == "K":
        hasil3 = float(input("nilai yang ingin di konversi: "))
        hasilnya()
        print(f"{(hasil3 + 273.15)} Kelvin")
    else:
        print("oke")

elif satuan.upper() == "F":
    konversi2 = input("konversi ke:  (c r k) ")
    if konversi2.upper() == "C":
        hasil4 = float(input("nilai yang ingin di konversi: "))
        hasilnya()
        print(f"{(hasil4 - 32) * 0.56} Celcius")
    elif konversi2.upper() == "R":
        hasil2 = float(input("nilai yang ingin di konversi: "))
        hasilnya()
        print(f"{(hasil5 - 32) * 0.4} Reamur")
    elif konversi2.upper() == "K":
        hasil6 = float(input("nilai yang ingin di konversi: "))
        hasilnya()
        print(f"{(hasil6 - 32) * 0.5 + 273.15} Kelvin")
    else:
        print("oke")

elif satuan.upper() == "R":
    konversi3 = input("konversi ke:  (c f k) ")
    if konversi3.upper() == "C":
        hasil7 = float(input("nilai yang ingin di konversi: "))
        hasilnya()
        print(f"{text + str(hasil7 * 1.25)} Celcius")
    elif konversi3.upper() == "F":
        hasil8 = float(input("nilai yang ingin di konversi: "))
        hasilnya()
        print(f"{(hasil8 * 2.25) + 32} Fahrenheit")
    elif konversi3.upper() == "K":
        hasil9 = float(input("nilai yang ingin di konversi: "))
        hasilnya()
        print(f"{(hasil9 * 1.25) + 273.15} Kelvin")
    else:
        print("oke")

elif satuan.upper() == "K":
    konversi4 = input("konversi ke:  (c r f) ")
    if konversi4.upper() == "C":
        hasil10 = float(input("nilai yang ingin di konversi: "))
        hasilnya()
        print(f"{hasil10 - 273.15} Celcius")
    elif konversi4.upper() == "F":
        hasil11 = float(input("nilai yang ingin di konversi: "))
        hasilnya()
        print(f"{(hasil11 - 273.15) * 1.8 + 32} Fahrenheit")
    elif konversi4.upper() == "R":
        hasil12 = float(input("nilai yang ingin di konversi: "))
        hasilnya()
        print(f"{(hasil12 - 273.15) * 0.8} Reamur")
    else:
        print("hmmmmm 10 jam")
#Kelvin ke Fahrenheit sudah benar, yg lainnya mungkin banyak yang salah

else:
    print("oke")