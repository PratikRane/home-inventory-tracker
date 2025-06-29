from flask import Flask, render_template, request, redirect
from db_config import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM item")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    purchase_date = request.form['purchase_date']
    position = request.form.get('position')
    related_item_id = request.form.get('related_item_id') or None
    relative_position = request.form.get('relative_position') or None
    is_consumable = bool(request.form.get('is_consumable'))
    expiry_date = request.form.get('expiry_date') or None

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO item (name, purchase_date, position, related_item_id,
                          relative_position, is_consumable, expiry_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (name, purchase_date, position, related_item_id,
          relative_position, is_consumable, expiry_date))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
