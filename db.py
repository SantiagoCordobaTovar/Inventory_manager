import sqlite3
import csv

def connect():
    return sqlite3.connect("database.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            quantity INTEGER,
            price REAL
        )
    """)
    conn.commit()
    conn.close()

def add_product(name, category, quantity, price):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventory (name, category, quantity, price) VALUES (?, ?, ?, ?)",
                   (name, category, quantity, price))
    conn.commit()
    conn.close()

def get_all_products():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    conn.close()
    return results

def update_product(id, quantity=None, price=None):
    conn = connect()
    cursor = conn.cursor()
    if quantity is not None:
        cursor.execute("UPDATE inventory SET quantity = ? WHERE id = ?", (quantity, id))
    if price is not None:
        cursor.execute("UPDATE inventory SET price = ? WHERE id = ?", (price, id))
    conn.commit()
    conn.close()

def delete_product(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def search_product_by_name(name):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory WHERE name LIKE ?", ('%' + name + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

def get_products_sorted_by_category():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory ORDER BY category ASC")
    results = cursor.fetchall()
    conn.close()
    return results

def export_to_csv(filename):
    data = get_all_products()
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nombre", "Categoría", "Cantidad", "Precio"])
        writer.writerows(data)
