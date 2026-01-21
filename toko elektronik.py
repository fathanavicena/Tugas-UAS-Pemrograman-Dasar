# --- KRITERIA: OOP (Object-Oriented Programming) ---
class ProdukElektronik:
    def __init__(self, kode, nama, kategori, harga):
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.harga = harga

    # Method untuk memformat data produk (KRITERIA: STRING & FUNCTION)
    def detail_produk(self):
        # Menggunakan f-string dan method string .upper() serta .title()
        return f"[{self.kode.upper()}] {self.nama.title()} ({self.kategori}) - Rp{self.harga:,}"

# --- KRITERIA: FUNCTION (Fungsi Mandiri) ---
def cetak_garis():
    print("-" * 50)

def main():
    # --- KRITERIA: LIST (Menyimpan objek produk) ---
    katalog = [
        ProdukElektronik("L01", "Laptop Gaming ASUS", "Laptop", 15000000),
        ProdukElektronik("H02", "Smartphone Samsung S23", "Handphone", 12000000),
        ProdukElektronik("T03", "Smart TV LG 43 Inch", "Elektronik Rumah", 5000000)
    ]
    
    keranjang = []

    # --- KRITERIA: PERULANGAN (While Loop) ---
    berjalan = True
    while berjalan:
        print("\n=== AMIKOM ELECTRONIC STORE ===")
        print("1. Lihat Katalog Produk")
        print("2. Tambah Barang ke Keranjang")
        print("3. Checkout & Keluar")
        
        # --- KRITERIA: PERCABANGAN (If-Else) ---
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            print("\nDAFTAR PRODUK:")
            cetak_garis()
            # Perulangan (For Loop) untuk list
            for produk in katalog:
                print(produk.detail_produk())
            cetak_garis()

        elif pilihan == "2":
            cari_kode = input("Masukkan Kode Produk (contoh: L01): ").strip().upper()
            ditemukan = False
            for produk in katalog:
                if produk.kode == cari_kode:
                    keranjang.append(produk)
                    print(f"Berhasil menambahkan {produk.nama} ke keranjang!")
                    ditemukan = True
                    break
            if not ditemukan:
                print("Maaf, kode produk tidak ditemukan.")

        elif pilihan == "3":
            if not keranjang:
                print("Keranjang kosong. Terima kasih!")
            else:
                print("\nRINGKASAN BELANJA ANDA:")
                total = 0
                for item in keranjang:
                    print(f"- {item.nama} : Rp{item.harga:,}")
                    total += item.harga
                print(f"TOTAL PEMBAYARAN: Rp{total:,}")
                print("Terima kasih telah berbelanja!")
            berjalan = False # Menghentikan perulangan

        else:
            print("Pilihan menu tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
