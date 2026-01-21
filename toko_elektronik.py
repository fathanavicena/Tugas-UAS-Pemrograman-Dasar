import streamlit as st

# --- KRITERIA: OOP ---
class Produk:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

# --- KRITERIA: FUNCTION & STRING ---
def format_rupiah(nominal):
    return f"Rp{nominal:,}"

# Inisialisasi List (KRITERIA: LIST)
if 'katalog' not in st.session_state:
    st.session_state.katalog = [
        Produk("L01", "Laptop Gaming", 15000000),
        Produk("H02", "Smartphone S23", 12000000),
        Produk("T03", "Smart TV 4K", 5000000)
    ]

st.title("🏪 UAS Toko Elektronik")

# --- KRITERIA: PERCABANGAN (Menu via Sidebar) ---
menu = st.sidebar.selectbox("Navigasi Menu", ["Lihat Katalog", "Tambah Produk Baru"])

if menu == "Lihat Katalog":
    st.header("Katalog Produk Saat Ini")
    
    # Menampilkan data dalam bentuk tabel agar rapi
    data_tabel = []
    # --- KRITERIA: PERULANGAN ---
    for p in st.session_state.katalog:
        data_tabel.append({
            "Kode": p.kode.upper(), # KRITERIA: STRING
            "Nama Produk": p.nama,
            "Harga": format_rupiah(p.harga)
        })
    st.table(data_tabel)

elif menu == "Tambah Produk Baru":
    st.header("Input Data Elektronik")
    
    # Mengganti input() terminal dengan widget Streamlit
    with st.form("form_input"):
        new_kode = st.text_input("Masukkan Kode (Contoh: B01)")
        new_nama = st.text_input("Nama Barang")
        new_harga = st.number_input("Harga Barang", min_value=0)
        
        submit = st.form_submit_button("Simpan Barang")
        
        if submit:
            if new_kode and new_nama:
                # Membuat objek baru (OOP)
                produk_baru = Produk(new_kode, new_nama, new_harga)
                # Menambah ke list
                st.session_state.katalog.append(produk_baru)
                st.success(f"Barang '{new_nama}' berhasil ditambahkan!")
            else:
                st.error("Semua kolom harus diisi!")
