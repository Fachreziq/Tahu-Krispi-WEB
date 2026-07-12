from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

import sqlite3
import os

app = Flask(__name__)
app.secret_key = "tahu_krispi_secret_key"

# ==========================
# DATABASE
# ==========================

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATABASE = os.path.join(
    BASE_DIR,
    "database",
    "tahu_krispi.db"
)


def get_db():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn


# ==========================
# SESSION CART
# ==========================

def get_cart():

    if "cart" not in session:

        session["cart"] = []

    return session["cart"]


def save_cart(cart):

    session["cart"] = cart

    session.modified = True


# ==========================
# HOME
# ==========================

@app.route("/")
def home():

    conn = get_db()

    products = conn.execute(
        """
        SELECT *
        FROM products
        """
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        products=products
    )


# ==========================
# PRODUCT LIST
# ==========================

@app.route("/products")
def product_list():

    conn = get_db()

    products = conn.execute(
        """
        SELECT *
        FROM products
        """
    ).fetchall()

    conn.close()

    return render_template(
        "products.html",
        products=products
    )
# ==========================
# DETAIL PRODUK
# ==========================

@app.route("/product/<int:id>")
def product_detail(id):

    conn = get_db()

    product = conn.execute(
        """
        SELECT *
        FROM products
        WHERE id = ?
        """,
        (id,)
    ).fetchone()

    conn.close()

    if product is None:

        flash("Produk tidak ditemukan.", "danger")

        return redirect(url_for("product_list"))

    return render_template(
        "detail.html",
        product=product
    )


# ==========================
# TAMBAH KE KERANJANG
# ==========================

@app.route("/add-to-cart/<int:id>")
def add_to_cart(id):

    conn = get_db()

    product = conn.execute(
        """
        SELECT *
        FROM products
        WHERE id = ?
        """,
        (id,)
    ).fetchone()

    conn.close()

    if product is None:

        flash("Produk tidak ditemukan.", "danger")

        return redirect(url_for("product_list"))

    cart = get_cart()

    found = False

    for item in cart:

        if item["id"] == id:

            item["qty"] += 1

            found = True

            break

    if not found:

        cart.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "image": product["image"],
            "qty": 1
        })

    save_cart(cart)

    flash("Produk berhasil ditambahkan ke keranjang.", "success")

    return redirect(url_for("checkout"))


# ==========================
# HAPUS ITEM
# ==========================

@app.route("/remove-cart/<int:id>")
def remove_cart(id):

    cart = get_cart()

    cart = [
        item
        for item in cart
        if item["id"] != id
    ]

    save_cart(cart)

    flash("Produk dihapus dari keranjang.", "warning")

    return redirect(url_for("checkout"))


# ==========================
# TAMBAH JUMLAH
# ==========================

@app.route("/increase/<int:id>")
def increase_qty(id):

    cart = get_cart()

    for item in cart:

        if item["id"] == id:

            item["qty"] += 1

            break

    save_cart(cart)

    return redirect(url_for("checkout"))


# ==========================
# KURANGI JUMLAH
# ==========================

@app.route("/decrease/<int:id>")
def decrease_qty(id):

    cart = get_cart()

    for item in cart:

        if item["id"] == id:

            item["qty"] -= 1

            if item["qty"] <= 0:

                cart.remove(item)

            break

    save_cart(cart)

    return redirect(url_for("checkout"))
# ==========================
# CHECKOUT
# ==========================

@app.route("/checkout", methods=["GET", "POST"])
def checkout():

    cart = get_cart()

    total = sum(item["price"] * item["qty"] for item in cart)

    if request.method == "POST":

        name = request.form.get("name")
        phone = request.form.get("phone")
        address = request.form.get("address")

        if not name or not phone or not address:

            flash("Semua data wajib diisi.", "danger")

            return render_template(
                "checkout.html",
                cart=cart,
                total=total
            )

        conn = get_db()

        conn.execute(
            """
            INSERT INTO orders
            (
                customer_name,
                phone,
                address,
                total
            )
            VALUES
            (?,?,?,?)
            """,
            (
                name,
                phone,
                address,
                total
            )
        )

        conn.commit()
        conn.close()

        session["cart"] = []

        flash(
            "Pesanan berhasil dibuat.",
            "success"
        )

        return redirect(
            url_for("success")
        )

    return render_template(
        "checkout.html",
        cart=cart,
        total=total
    )


# ==========================
# SUCCESS PAGE
# ==========================

@app.route("/success")
def success():

    return render_template(
        "success.html"
    )


# ==========================
# 404 ERROR
# ==========================

@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for("home"))


# ==========================
# RUN APP
# ==========================

if __name__ == "__main__":

    app.run(debug=True)