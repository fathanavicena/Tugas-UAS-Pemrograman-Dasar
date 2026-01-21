import streamlit as st
import requests

# URL Server API (Soal No. 2)
URL_API = "http://127.0.0.1:5000/api/barang"

st.title("🏪 UAS Toko Elektronik (Client Side)")

# Fungsi mengambil data dari server
def fetch_data():
    try:
        response = requests.get(URL_API)
        return response.json()
    except:
        return None

menu = st.sidebar.selectbox("Navigasi", ["Katalog Server", "Tambah ke Server"])

if menu == "Katalog Server":
    st.header("Data Produk dari Server")
    data = fetch_data()
    if data:
        st.table(data)
    else:
        st.error("Server belum jalan! Jalankan server.py di terminal dulu.")

elif menu == "Tambah ke Server":
    st.header("Input Barang Baru")
    with st.form("form_input"):
        kode = st.text_input("Kode")
        nama = st.text_input("Nama")
        harga = st.number_input("Harga", min_value=0)
        if st.form_submit_button("Kirim ke Server"):
            payload = {"kode": kode, "nama": nama, "harga": harga}
            res = requests.post(URL_API, json=payload)
            st.success(res.json()['pesan'])
