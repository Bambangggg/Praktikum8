def penjumlahan_rekursif(jumlah, index=1):
    if index > jumlah:
        return 0
    else:
        angka = float(input(f"Masukkan angka ke-{index}: "))
        return angka + penjumlahan_rekursif(jumlah, index + 1)

def main():
    jumlahh = int(input("Masukkan Jumlah: "))
    hasil = penjumlahan_rekursif(jumlahh, 1)
    print(f"Hasil penjumlahan: {hasil}")

if __name__ == "__main__":
    main()