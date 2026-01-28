from flask import Flask, request, jsonify

app = Flask(__name__)

# Database sementara di sisi Server
database_toko = [
    {
        "kode": "L01", 
        "nama": "LAPTOP GAMING ASUS", 
        "harga": 15000000, 
        "kategori": "Laptop",
        "foto": [] # Tempat menyimpan string Base64 foto
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
    # Mengirim seluruh data ke Client
    return jsonify(database_toko), 200

@app.route('/api/barang', methods=['POST'])
def simpan_barang():
    # Menerima data produk baru dari Client
    data_baru = request.json
    database_toko.append(data_baru)
    return jsonify({"pesan": "Berhasil disimpan di Server!"}), 201

if __name__ == '__main__':
    # Berjalan di port 5000 (Default Flask)
    app.run(port=5000, debug=True)
