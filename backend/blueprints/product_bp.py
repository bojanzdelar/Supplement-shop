from uuid import uuid1
from flask import Blueprint, request
from config import db
from utils.security_utils import admin_required
from schemas.product_schema import ProductSchema
from models.product import Product
from models.category import Category
from models.product_in_category import ProductInCategory

product = Blueprint('product', __name__)
schema = ProductSchema()

@product.route("/", methods=["GET"])
def get_all_products():
    search = request.args.get("search")
    if not search:
        products = Product.query.filter_by(deleted = False).all()
        return schema.jsonify(products, many=True)

    search = f"%{search}%"
    products = Product.query.filter((Product.name.ilike(search)) | (Product.description.ilike(search))).all()
    return schema.jsonify(products, many=True)

@product.route("/popular/<int:limit>", methods=["GET"])
def get_popular_products(limit):
    products = Product.query.filter_by(deleted = False).order_by(Product.views.desc()).limit(limit).all()
    return schema.jsonify(products, many=True)

@product.route("/category/<string:category_id>", methods=["GET"])
def get_products_by_category(category_id):
    category = Category.query.filter_by(id = category_id).first()
    if not category:
        return "Category not found!", 404

    products = Product.query.join(ProductInCategory).filter((Product.deleted == False) & (ProductInCategory.category_id == category_id)).all() 
    return schema.jsonify(products, many=True)

@product.route("/<string:id>", methods=["GET"])
def get_product(id):
    product = Product.query.filter_by(id = id).first()
    if not product:
        return "Product not found!", 404

    product.views += 1
    db.session.commit()
    return schema.jsonify(product)
 
@product.route("/", methods=["POST"])
@admin_required()
def create_product():
    product = request.json 
    try:
        product["id"] = product["name"].replace(" ", "-").lower()
        product = Product(**product)
        db.session.add(product)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(product), 201

@product.route("/<string:id>", methods=["PATCH"])
@admin_required()
def update_product(id):
    product = Product.query.filter_by(id = id).first()
    if not product:
        return "Product not found!", 404

    new_product = request.json
    try:
        new_product["id"] = new_product["name"].replace(" ", "-").lower()
        Product.query.filter_by(id = id).update(new_product)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400

    product = Product.query.filter_by(id = new_product["id"]).first()
    return schema.jsonify(product)

@product.route("/<string:id>", methods=["DELETE"])
@admin_required()
def delete_product(id):
    product = Product.query.filter_by(id = id).first()
    if not product:
        return "Product not found!", 404

    product.id = uuid1()
    product.deleted = True
    db.session.commit()
    return "", 204