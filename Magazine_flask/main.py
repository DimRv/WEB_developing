from flask import Flask, render_template, session, request, redirect
from database import *
import json


web = Flask(__name__)
web.secret_key = "aslfpohskdfh23r)_!fsdf"


@web.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if 'username' not in session:
            session['username'] = 'Гость'
        username = session['username']
        content = {'username': username}

        sql = f'SELECT * FROM category'
        cursor.execute(sql)
        categories = cursor.fetchall()
        content['categories'] = categories

        sql = f'SELECT * FROM products'
        cursor.execute(sql)
        products = cursor.fetchall()
        content['products'] = products

        sql = f"SELECT * FROM carts WHERE cart_user='{username}'"
        cursor.execute(sql)
        carts = cursor.fetchall()
        if carts:
            count = 0
            for cart in carts:
                count += cart['cart_count']
            content['cart'] = count

        return render_template('index.html', content=content)
    product = request.form.get('product_id')
    user_name = request.form.get('username')
    count = 1
    sql = f"SELECT * from carts WHERE cart_product ={product} and cart_user='{user_name}'"
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        count = data['cart_count']
        sql = f"UPDATE carts SET cart_count={count + 1} WHERE cart_product ={product} and cart_user='{user_name}'"
        cursor.execute(sql)
        connection.commit()
    else:
        sql = f"INSERT INTO carts (cart_product, cart_user, cart_count) VALUES ({product}, '{user_name}', {count})"
        cursor.execute(sql)
        connection.commit()
    return redirect('/', code=302)


@web.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        content = {'username': session['username']}
        username = session['username']
        if 'error' in request.args:
            content["error"] = True
        sql = f"SELECT * FROM carts WHERE cart_user='{username}'"
        cursor.execute(sql)
        carts = cursor.fetchall()
        if carts:
            count = 0
            for cart in carts:
                count += cart['cart_count']
            content['cart'] = count

        return render_template('login.html', content=content)
    username = request.form.get('login')
    password = request.form.get('password')
    sql = f"SELECT user_id FROM users WHERE user_login='{username}' AND user_password='{password}'"
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        session['username'] = username
        return redirect('/', code=302)
    else:
        return redirect('/login?error', code=302)


@web.route('/logout')
def logout():
    session.pop('username')
    return redirect('/', code=302)


@web.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        content = {'username': session['username']}
        if 'error' in request.args:
            content["error"] = True
        return render_template('registration.html', content=content)
    username = request.form.get('login')
    password = request.form.get('password')
    sql = f"SAVEPOINT snapshot; INSERT INTO users (user_login, user_password) VALUES ('{username}', '{password}');"
    try:
        cursor.execute(sql)
    except psycopg2.errors.UniqueViolation:
        sql = "ROLLBACK TO SAVEPOINT snapshot;"
        cursor.execute(sql)
        return redirect('/registration?error', code=302)
    sql = "RELEASE SAVEPOINT snapshot;"
    cursor.execute(sql)
    session['username'] = username
    connection.commit()
    return redirect('/', code=302)


@web.route('/admin', methods=["GET", "POST"])
def admin():
    if request.method == 'GET':
        username = session['username']
        content = {"username": username}
        sql = f"SELECT user_role FROM users WHERE user_login='{username}'"
        cursor.execute(sql)
        data = cursor.fetchone()
        if data['user_role'] == 0:
            content['error'] = "1"
        else:
            sql = f"SELECT user_login, user_role FROM users ORDER BY user_login"
            cursor.execute(sql)
            users = cursor.fetchall()
            content['users'] = users

            sql = f"SELECT * FROM category;"
            cursor.execute(sql)
            category = cursor.fetchall()
            content['category'] = category

            sql = f"SELECT * FROM products;"
            cursor.execute(sql)
            products = cursor.fetchall()
            content['products'] = products

            sql = f'SELECT * FROM carts'
            cursor.execute(sql)
            carts = cursor.fetchall()
            content['carts'] = carts

            sql = f'SELECT * FROM orders'
            cursor.execute(sql)
            orders = cursor.fetchall()
            content['orders'] = orders

        return render_template("admin.html", content=content)
    print(request.form.keys())
    if 'user_rights' in request.form:
        user = request.form.get('user_rights')
        role = request.form.get(user)
        sql = f"UPDATE users SET user_role='{role}' WHERE user_login='{user}'"
        cursor.execute(sql)
        connection.commit()

    if 'category' in request.form:
        category_id = request.form.get('category')
        category_title = request.form.get(category_id)
        sql = f"UPDATE category SET category_title='{category_title}' WHERE category_id='{category_id}'"
        cursor.execute(sql)
        connection.commit()

    if 'category_title' in request.form:
        category_title = request.form.get('category_title')
        sql = f"INSERT INTO category (category_title) VALUES ('{category_title}')"
        cursor.execute(sql)
        connection.commit()

    if 'product_title' in request.form:
        product_title = request.form.get('product_title')
        product_description = request.form.get('product_description')
        product_price = request.form.get('product_price')
        product_category = request.form.get('product_category')
        product_photo = request.form.get('product_photo')
        sql = (f"INSERT INTO products(product_title, product_description, product_price, product_category, product_photo)"
               f" VALUES ('{product_title}', '{product_description}', '{product_price}' ,'{product_category}' ,'{product_photo}')")
        cursor.execute(sql)
        connection.commit()

    return redirect('/admin', code=302)


@web.route('/cart', methods=['GET', "POST"])
def cart():
    if request.method == 'GET':
        if 'username' not in session:
            session['username'] = 'Гость'
        username = session['username']
        content = {'username': username}

        sql = f"SELECT c.cart_id, c.cart_count, p.product_title, p.product_price from carts c INNER JOIN products p ON c.cart_product = p.product_id WHERE c.cart_user = '{username}'"
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        if data:
            content['products'] = data
        return render_template("cart.html", content=content)
    if 'cart_id' in request.form:
        cart_id = request.form.get("cart_id")
        product_count = int(request.form.get("product_count"))
        if product_count <= 0:
            sql = f"DELETE FROM carts WHERE cart_id='{cart_id}';"
        else:
            sql = f"UPDATE carts SET cart_count='{product_count}' WHERE cart_id='{cart_id}';"
        cursor.execute(sql)
        connection.commit()
        return redirect('/cart', code=302)
    if 'submit' in request.form:
        user_name = request.form.get('submit')
        sql = f"INSERT INTO orders (order_user, order_product, order_count) SELECT cart_user, cart_product, cart_count FROM carts WHERE cart_user='{user_name}';"
        sql += f"DELETE from carts WHERE cart_user='{user_name}'"
        cursor.execute(sql)
        connection.commit()
        return redirect('/cart', code=302)


if __name__ == "__main__":
    web.run(debug=True, host='localhost', port=8084)
