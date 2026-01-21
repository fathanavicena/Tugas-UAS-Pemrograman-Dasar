from flask import Flask, request, jsonify

app = Flask(__name__)

# Data awal di Server (Bobot: 50)
database_toko = [
    {"kode": "L01", "nama": "Laptop Gaming", "harga": 15000000},
    {"kode": "H02", "nama": "Smartphone S23", "harga": 12000000},
    {"kode": "T03", "nama": "Smart TV 4K", "harga": 5000000}
]

@app.route('/api/barang', methods=['GET'])
def ambil_barang():
    return jsonify(database_toko), 200

@app.route('/api/barang', methods=['POST'])
def simpan_barang():
    data_baru = request.json
    database_toko.append(data_baru)
    return jsonify({"pesan": "Berhasil disimpan di Server!"}), 201

if __name__ == '__main__':
    app.run(port=5000)
