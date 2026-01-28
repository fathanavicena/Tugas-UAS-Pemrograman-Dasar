from flask import Flask, request, jsonify

app = Flask(__name__)

# Database sementara dengan struktur data lengkap
database_toko = [
    {
        "kode": "L01", 
        "nama": "LAPTOP GAMING ASUS", 
        "harga": 15000000, 
        "kategori": "Laptop",
        "foto": [] 
    },
    {
        "kode": "H02", 
        "nama": "SMARTPHONE S23", 
        "harga": 12000000, 
        "kategori": "Handphone",
        "foto": []
    }
]

@app.route('/api/barang', methods=['GET'])
def ambil_barang():
    # Mengirim data ke Client
    return jsonify(database_toko), 200

@app.route('/api/barang', methods=['POST'])
def simpan_barang():
    # Menerima data baru dari Client
    data_baru = request.json
    database_toko.append(data_baru)
    return jsonify({"pesan": "Berhasil disimpan di Server!"}), 201

if __name__ == '__main__':
    # Debug mode ON agar perubahan kode langsung terbaca
    app.run(port=5000, debug=True)
