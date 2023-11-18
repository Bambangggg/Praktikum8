def pangkat(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return x * pangkat(x, n - 1)
    else:
        return 1 / (x * pangkat(x, -n - 1))

while True:
    print("Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")
    angka = input("Masukkan Angka: ")

    if angka == "":
        print("Program Selesai")
        break

    pangkatnya = int(input("Masukkan Pangkatnya: "))
    hasil = pangkat(int(angka), pangkatnya)
    print(f"Hasilnya adalah: {hasil}\n")
