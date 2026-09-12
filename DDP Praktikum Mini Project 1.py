# 1. Inisialisasi Data
# Tuple berisi data awal board game
daftar_boardgame = (
    ("Catan", "Strategy", 4),
    ("Carcassonne", "Tile Placement", 5),
    ("Uno Stacko", "Party", 10)
)

# List kosong untuk menyimpan koleksi board game
koleksi_boardgame = []

# Menambahkan data dari tuple ke dalam list koleksi_boardgame
for game in daftar_boardgame:
    koleksi_boardgame.append(game)

while True:
    print("\nPENDATAAN KOLEKSI BOARD GAME PRIBADI")
    print("1. Tampilkan Daftar Koleksi (Read)")
    print("2. Tambah Board Game Baru (Create)")
    print("3. Ubah Data Board Game (Update)")
    print("4. Hapus Board Game (Delete)")
    print("5. Keluar Program")
    
    pilihan = input("Pilih menu (1-5): ")
    
    # 2. Conditional Statement untuk Menu
    if pilihan == "1":
        # READ DATA
        print("\nDAFTAR KOLEKSI BOARD GAME")
        if not koleksi_boardgame:
            print("Belum ada data board game.")
        else:
            print("-" * 40)
            i = 1
            for game in koleksi_boardgame:
                nama = game[0]
                genre = game[1]
                pemain = game[2]
                print(f"{i}.", "Nama Game     :", nama)
                print("   Genre         :", genre)
                print("   Max Pemain    :", pemain, "Orang")
                print("-" * 40)
                i = i + 1
            
    elif pilihan == "2":
        # CREATE DATA
        print("\nTAMBAH BOARD GAME BARU")
        nama = input("Masukkan Nama Game: ")
        genre = input("Masukkan Genre Game: ")
        pemain = int(input("Masukkan Maksimal Jumlah Pemain: "))
        
        # Membuat tuple baru dan menambahkannya ke list
        game_baru = (nama, genre, pemain)
        koleksi_boardgame.append(game_baru)
        print("\nBoard game berhasil ditambahkan.")
        
    elif pilihan == "3":
        # UPDATE DATA
        print("\nUBAH DATA BOARD GAME")
        if not koleksi_boardgame:
            print("Belum ada data board game yang bisa diubah.")
        else:
            i = 1
            for game in koleksi_boardgame:
                print(f"{i}.", game[0], "(", game[1], ")")
                i = i + 1
                
            nomor = int(input("Pilih nomor game yang ingin diubah: "))
            indeks = nomor - 1
            
            print("\nMasukkan data baru untuk:", koleksi_boardgame[indeks][0])
            nama_baru = input("Nama Baru: ")
            genre_baru = input("Genre Baru: ")
            pemain_baru = int(input("Jumlah Pemain Baru: "))
            
            # Mengubah data di dalam list berdasarkan indeks
            koleksi_boardgame[indeks] = (nama_baru, genre_baru, pemain_baru)
            print("\nData board game berhasil diperbarui.")
            
    elif pilihan == "4":
        # DELETE DATA
        print("\nHAPUS BOARD GAME DARI KOLEKSI")
        if not koleksi_boardgame:
            print("Belum ada data board game yang bisa dihapus.")
        else:
            i = 1
            for game in koleksi_boardgame:
                print(f"{i}.", game[0], "(", game[1], ")")
                i = i + 1
                
            nomor = int(input("Pilih nomor game yang ingin dihapus: "))
            indeks = nomor - 1
            
            # Menghapus data dari list menggunakan pop
            game_dihapus = koleksi_boardgame.pop(indeks)
            print("\nBoard game berhasil dihapus dari koleksi.")
            
    elif pilihan == "5":
        # KELUAR PROGRAM
        print("\nProgram selesai.")
        break
        
    else:
        print("\nPilihan tidak valid. Silakan masukkan angka 1 sampai 5.")