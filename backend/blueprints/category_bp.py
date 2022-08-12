from flask import Blueprint, request
from config import db
from utils.security_utils import admin_required
from schemas.category_schema import CategorySchema
from models.category import Category
from models.product import Product
from models.product_in_category import ProductInCategory

category = Blueprint('category', __name__)
schema = CategorySchema()

@category.route("/", methods=["GET"])
def get_all_categories():
    categories = Category.query.all()
    return schema.jsonify(categories, many=True)

@category.route("/product/<string:product_id>", methods=["GET"])
def get_categories_by_product(product_id):
    product = Product.query.filter_by(id=product_id).first()
    if not product:
        return "Product not found!", 404

    categories = Category.query.join(ProductInCategory).filter_by(product_id = product_id).all()
    return schema.jsonify(categories, many=True)

@category.route("/<string:id>", methods=["GET"])
def get_category(id):
    category = Category.query.filter_by(id=id).first()
    if not category:
        return "Category not found!", 404

    return schema.jsonify(category)
    
@category.route("/", methods=["POST"])
@admin_required()
def create_category():
    try:
        category = Category(**request.json)
        db.session.add(category)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(category), 201

@category.route("/<string:id>", methods=["PATCH"])
@admin_required()
def update_category(id):
    category = Category.query.filter_by(id=id).first()
    if not category:
        return "Category not found!", 404
    
    new_category = request.json
    try:
        new_category["id"] = new_category["name"].replace(" ", "-").lower()
        Category.query.filter_by(id = id).update(new_category)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(category)

@category.route("/<string:id>", methods=["DELETE"])
@admin_required()
def delete_category(id):
    category = Category.query.filter_by(id = id).first()
    if not category:
        return "Category not found!", 404

    db.session.delete(category)
    db.session.commit()
    return "", 204