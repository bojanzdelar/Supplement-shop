from app import app, mysql
import flask

@app.route("/api/product", methods=["GET"])
def get_all_product():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM product")
    return flask.jsonify(cursor.fetchall())

@app.route("/api/product/<int:id>", methods=["GET"])
def get_product(id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM product WHERE id=%s", (id,))
    product = cursor.fetchone()
    return flask.jsonify(product) if product else ("", 404)

@app.route("/api/product", methods=["POST"])
def create_product():
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO product(name, description, price, quantity, image, category_id) "
            "VALUES(%(name)s, %(description)s, %(price)s, %(quantity)s, %(image)s, %(category_id)s)", flask.request.json)
    db.commit()
    return flask.jsonify(flask.request.json), 201

@app.route("/api/product/<int:id>", methods=["PUT"])
def update_product(id):
    product = flask.request.json
    product["id"] = id
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE product SET name=%(name)s, description=%(description)s, price=%(price)s, quantity=%(quantity)s, image=%(image)s, category_id=%(category_id)s "
            "WHERE id=%(id)s", product)
    db.commit()
    cursor.execute("SELECT * FROM product WHERE id=%s", (id,))
    return flask.jsonify(cursor.fetchone()), 200

@app.route("/api/product/<int:id>", methods=["DELETE"])
def delete_product(id):
    db = mysql.get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM product WHERE id=%s", (id,))
    db.commit()
    return ""