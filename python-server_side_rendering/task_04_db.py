from flask import Flask, render_template, request # type: ignore
import sqlite3
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open("items.json", "r") as file:
        data = json.load(file)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)
    

@app.route('/products')
def products():
    source = request.args.get('source')
    productId = request.args.get('id')
    filtred = []

    if source == 'json':
        with open("products.json", "r") as file:
            filtred = json.load(file)
    elif source == 'csv':
        with open("products.csv", mode="r") as file:
            filtred = csv.DictReader(file)
            filtred = list(filtred)

    elif source == 'sql':
        with sqlite3.connect('products.db') as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT * FROM Products")
            rows = cursor.fetchall()
            filtred = [dict(row) for row in rows]

    else:
        return render_template('product_display.html', error="Wrong source")
    if productId:
        filtred = [p for p in filtred if str(p.get('id') or p['id']) == str(productId)]
        if not filtred:
            return render_template('product_display.html', error='Product not found')
    return render_template('product_display.html', products=filtred)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
