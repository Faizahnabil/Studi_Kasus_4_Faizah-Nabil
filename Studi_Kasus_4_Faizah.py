Buku = {
    "Buku1" : {
        "Judul" : "Hans",
        "Penulis" : "Risa Saraswati",
        "Tahun Terbit" : "2017"
    },

    "Buku2" :{
        "Judul" : "Tomie",
        "Penulis" : "Junji Ito",
        "Tahun Terbit" : "1997"
    }
}

while True:
    print("1. Tampilkan Data Buku")
    print("2. Tambah Data Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("5. Keluar")

    pilih = input("pilih: ")

# Menampilkan Data Buku
    if pilih == "1":
        print("Data Buku")
        print(Buku)

# Menambahkan Data Penerbit
    elif pilih == "2" :
        penerbit = input("Masukkan nama penerbit: ")
        Buku["penerbit"] = penerbit
        print("Data penerbit ditambahkan")

#Mengubah Data Penulis
    elif pilih == "3" :
        penulis = input("Masukkan nama penulis: ")
        Buku["penulis"] = penulis
        print("Data penulis diubah")

#Menghapus Data Penerbit
    elif pilih == "4" :
        if "penerbit" in Buku:
            del Buku["penerbit"]
            print("Data penerbit dihapus")
        else:
            print("Data penerbit belum ada")

#Keluar
    elif pilih == "5" :
        print("Program Selesai")
        print("Data Buku Setelah Perubahan")
        print(Buku)
        break
    else:
        print("Pilihan Tidak Ada")