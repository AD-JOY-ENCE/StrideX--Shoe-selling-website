from flask import Flask, render_template, abort

app = Flask(__name__)

# --- THE DATABASE ---
products_db = [
    { "id": 1, "name": "Jordan 1 Retro High", "desc": "Dark Mocha", "price": 385, "sku": "555088-105", "image": "jordan1.png" },
    { "id": 2, "name": "Nike Dunk Low", "desc": "White Black (Panda)", "price": 150, "sku": "DD1391-100", "image": "panda.png" },
    { "id": 3, "name": "adidas Yeezy Boost 350", "desc": "Zebra", "price": 280, "sku": "CP9654", "image": "yeezy350.png" },
    { "id": 4, "name": "New Balance 550", "desc": "White Green", "price": 120, "sku": "BB550WT1", "image": "nb550.png" },
    { "id": 5, "name": "Jordan 4 Retro", "desc": "Military Black", "price": 410, "sku": "DH6927-111", "image": "jordan4.png" },
    { "id": 6, "name": "Adidas Samba OG", "desc": "Cloud White", "price": 110, "sku": "B75806", "image": "samba.png" },
    { "id": 7, "name": "Travis Scott x Jordan 1", "desc": "Low Olive", "price": 850, "sku": "DZ4137-106", "image": "travis.png" },
    { "id": 8, "name": "Nike Kobe 6", "desc": "Protro Grinch", "price": 780, "sku": "CW2190-300", "image": "kobe6.png" },
    { "id": 9, "name": "Air Jordan 11 Retro", "desc": "Cool Grey", "price": 290, "sku": "CT8012-005", "image": "jordan11.png" },
    { "id": 10, "name": "Nike Air Max 1", "desc": "'86 Big Bubble", "price": 140, "sku": "DQ3989-100", "image": "airmax1.png" },
    { "id": 11, "name": "New Balance 9060", "desc": "Rain Cloud", "price": 160, "sku": "U9060GRY", "image": "nb9060.png" },
    { "id": 12, "name": "Off-White x Nike Presto", "desc": "The Ten", "price": 1800, "sku": "AA3830-001", "image": "presto.png" }
]

@app.route('/')
def home():
    return render_template('home.html', products=products_db)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Find product by ID
    product = next((item for item in products_db if item["id"] == product_id), None)
    if product is None:
        return abort(404)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)