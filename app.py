from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('textile_shop.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Sample data for the database
def seed_db():
    conn = sqlite3.connect('textile_shop.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, description, price) VALUES ('Бавовняна тканина', 'Тканина високої якості з бавовни', 10.99)")
    cursor.execute("INSERT INTO products (name, description, price) VALUES ('Шовкова тканина', 'Преміум тканина з шовку', 29.99)")
    cursor.execute("INSERT INTO products (name, description, price) VALUES ('Вовняна тканина', 'Тепла тканина з вовни', 15.99)")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('textile_shop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/products')
def products():
    conn = sqlite3.connect('textile_shop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return render_template('products.html', products=products)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission (this is a placeholder)
        return redirect(url_for('index'))
    return render_template('contact.html')

if __name__ == '__main__':
    init_db()
    #seed_db()  # Comment this out after the first run to avoid duplicating data
    app.run(debug=True)
