nilai1 = 75
nilai2 = 60

# Menggunakan fungsinya ==
if nilai1 == 75:
    print("nilai Anda :", nilai1)

# Menggunakan fungsinya !=
if nilai1 != 85:
    print("nilai Anda Bukan: 85")

# Menggunakan is fungsinya sama seperti ==
if nilai1 is 75:
    print("nilai Anda :", nilai1)

# Menggunakan is not fungsinya sama seperti !=
if nilai1 is not 85:
    print("nilai Anda Bukan: 85")

# Menggunakan fungsi elif
nilai = 79


if 80 <= nilai <= 100:
    print("Nilai Anda Adalah A")
elif 70 <= nilai <= 80:
    print("Nilai Anda Adalah B")
elif 60 <= nilai <= 70:
    print("Nilai Anda Adalah C")
else:
    print("Maaf Anda Tidak Lulus Ujian MAtakuliah ini")


# Find Data tanpa harus menggunakan looping  /  for
gorengan = ["bakwan","cireng","bala-bala","gedang goreng"]
beli = "gedang goreng"

if beli in gorengan:
    print('Tukang Gorengan :"Iya mas Saya Jualan',beli,'"')
else:
    print('Tukang Gorengan :"Maaf mas Saya Tidak Jualan',beli,'"')


# Nesting If
if nilai1 == 85:
    print("nilai Anda :", nilai1)
    if nilai2 == 80:
        print("nilai Anda :", nilai2)
