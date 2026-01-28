import streamlit as st
import requests
import base64

# OOP - Kriteria Penilaian UAS
class Elektronik:
    def __init__(self, kode, nama, harga, kategori, foto_list):
        self.kode = kode
        self.nama = nama.upper() # Manipulasi String
        self.harga = harga
        self.kategori = kategori
        self.foto_list = foto_list

URL_API = "http://127.0.0.1:5000/api/barang"

def fetch_data():
    try:
        response = requests.get(URL_API)
        return response.json()
    except:
        return None

st.set_page_config(page_title="UAS Toko Elektronik", page_icon="🏪")
st.title("🏪 UAS Toko Elektronik (Client Side)")

menu = st.sidebar.selectbox("Navigasi", ["Katalog Server", "Tambah ke Server"])

if menu == "Katalog Server":
    st.header("Daftar Produk di Toko")
    data = fetch_data()
    
    if data is None:
        st.error("Gagal terhubung ke Server! Pastikan server.py sudah jalan.")
    elif len(data) == 0:
        st.info("Belum ada data.")
    else:
        for produk in data:
            with st.container():
                col1, col2 = st.columns([1, 2])
                with col1:
                    if produk.get("foto"):
                        for img_base64 in produk["foto"]:
                            st.image(img_base64, use_container_width=True)
                    else:
                        st.caption("Tidak ada foto")
                
                with col2:
                    # PERBAIKAN: Menggunakan .get() agar tidak KeyError
                    st.subheader(produk.get('nama', 'Tanpa Nama'))
                    st.write(f"**Kode:** {produk.get('kode', '-')}")
                    st.write(f"**Kategori:** {produk.get('kategori', 'Umum')}")
                    st.write(f"**Harga:** Rp{produk.get('harga', 0):,}")
                st.divider()

elif menu == "Tambah ke Server":
    st.header("Input Barang Baru")
    with st.form("form_input", clear_on_submit=True):
        kode = st.text_input("Kode Produk")
        nama = st.text_input("Nama Produk")
        kategori = st.selectbox("Kategori", ["Laptop", "Smart TV", "Handphone", "Aksesoris"])
        harga = st.number_input("Harga", min_value=0, step=1000)
        uploaded_files = st.file_uploader("Upload Foto PNG", type=['png'], accept_multiple_files=True)
        
        submit = st.form_submit_button("Kirim ke Server")
        
        if submit:
            if kode and nama:
                list_foto_base64 = []
                for f in uploaded_files:
                    encoded = base64.b64encode(f.read()).decode()
                    list_foto_base64.append(f"data:image/png;base64,{encoded}")
                
                obj_produk = Elektronik(kode, nama, harga, kategori, list_foto_base64)
                
                payload = {
                    "kode": obj_produk.kode,
                    "nama": obj_produk.nama,
                    "harga": obj_produk.harga,
                    "kategori": obj_produk.kategori,
                    "foto": obj_produk.foto_list
                }
                
                try:
                    res = requests.post(URL_API, json=payload)
                    st.success(res.json()['pesan'])
                except:
                    st.error("Gagal kirim ke server!")
