print("selamat datang")
print("masukkan password dan tanggal untuk melanjutkan")
nama = "safri"
guess_count = 0
guess_limit = 3
tgl_lhr = 16
bln_lhr = 5
thn_lhr = 2001
tgl_crn = int(input("tanggal saat ini: "))
bln_crn = int(input("bulan: "))
thn_crn = int(input("tahun: "))
while guess_count < guess_limit:
    guess = str(input("luwak white kopi password nya: "))
    guess_count += 1
    if guess != nama:
        print("type correctly!")
    elif guess == nama:
        print("hello safri")
        status = input("want to know your status? ")
        if status == "yes":
            print(f"Nama: Berlian Safri Prakoso\nNIM: I0320017\nKelas: A")
            print("Tempat Tinggal: Kab Madiun, Kecamatan Balerejo, Desa Sumberbening RT03 RW01. \nsuasana pedesaan yang tenang dan sejuk, jauh dari hiruk pikuk perkotaan")
            if tgl_lhr >> 11:
                print(f"usia mu saat ini adalah {(thn_crn - thn_lhr - 1)} tahun, {(10 - bln_lhr + bln_crn)} bulan, {(28 - tgl_lhr + tgl_crn)} hari. )
            else:
                print(f"usia mu saat ini adalah {(thn_crn - thn_lhr - 1)} tahun, {(11 - bln_lhr + bln_crn)} bulan, {(28 - tgl_lhr + tgl_crn)} hari. )
        else:
            print("understandable, have a nice day :)")
        break
else:
    print("security!")

