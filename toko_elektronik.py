import streamlit as st
import requests
import base64

# 1. Konsep OOP (Object Oriented Programming)
class Elektronik:
    def __init__(self, kode, nama, harga, kategori, foto_list):
        self.kode = kode
        self.nama = nama.upper() # Manipulasi String
        self.harga = harga
        self.kategori = kategori
        self.foto_list = foto_list

# URL API Server (Pastikan server.py jalan di port 5000)
URL_API = "http://127.0.0.1:5000/api/barang"

# 2. Function untuk mengambil data dari Server
def fetch_data():
    try:
        response = requests.get(URL_API)
        return response.json()
    except:
        return None

# Konfigurasi Tampilan
st.set_page_config(page_title="UAS Toko Elektronik", page_icon="🏪")
st.title("🏪 UAS Toko Elektronik (Client Side)")

# Navigasi menggunakan Sidebar
menu = st.sidebar.selectbox("Navigasi", ["Katalog Server", "Tambah ke Server"])

# --- HALAMAN KATALOG (Menampilkan Data) ---
if menu == "Katalog Server":
    st.header("Daftar Produk di Toko")
    data = fetch_data()
    
    # 3. Percabangan & Perulangan untuk menampilkan data
    if data is None:
        st.error("Gagal terhubung ke Server! Pastikan server.py sudah dijalankan di terminal.")
    elif len(data) == 0:
        st.info("Belum ada data produk di server.")
    else:
        # Perulangan (Looping) untuk setiap produk
        for produk in data:
            with st.container():
                col1, col2 = st.columns([1, 2])
                with col1:
                    # Menampilkan foto jika ada (Handling List)
                    if produk.get("foto"):
                        for img_base64 in produk["foto"]:
                            st.image(img_base64, use_container_width=True)
                    else:
                        st.caption("Tidak ada foto")
                
                with col2:
                    st.subheader(produk['nama'])
                    st.write(f"**Kode:** {produk['kode']}")
                    st.write(f"**Kategori:** {produk['kategori']}")
                    st.write(f"**Harga:** Rp{produk['harga']:,}")
                st.divider()

# --- HALAMAN TAMBAH DATA (Input ke Server) ---
elif menu == "Tambah ke Server":
    st.header("Input Barang Baru")
    with st.form("form_input", clear_on_submit=True):
        kode = st.text_input("Kode Produk (Contoh: L03)")
        nama = st.text_input("Nama Produk")
        kategori = st.selectbox("Kategori", ["Laptop", "Smart TV", "Handphone", "Aksesoris"])
        harga = st.number_input("Harga", min_value=0, step=1000)
        
        # Fitur Upload Foto: Hanya menerima PNG & Bisa banyak sekaligus
        uploaded_files = st.file_uploader("Upload Foto Produk (Format .PNG)", type=['png'], accept_multiple_files=True)
        
        submit = st.form_submit_button("Kirim ke Server")
        
        if submit:
            if kode and nama:
                # Proses konversi gambar ke Base64
                list_foto_base64 = []
                for uploaded_file in uploaded_files:
                    encoded = base64.b64encode(uploaded_file.read()).decode()
                    list_foto_base64.append(f"data:image/png;base64,{encoded}")
                
                # Menginisialisasi Object dari Class (OOP)
                produk_baru = Elektronik(kode, nama, harga, kategori, list_foto_base64)
                
                # Data dikirim dalam format JSON
                payload = {
                    "kode": produk_baru.kode,
                    "nama": produk_baru.nama,
                    "harga": produk_baru.harga,
                    "kategori": produk_baru.kategori,
                    "foto": produk_baru.foto_list
                }
                
                try:
                    res = requests.post(URL_API, json=payload)
                    if res.status_code == 201:
                        st.success(res.json()['pesan'])
                    else:
                        st.error("Gagal mengirim data.")
                except:
                    st.error("Koneksi ke Server terputus!")
            else:
                st.warning("Mohon isi Kode dan Nama produk.")
