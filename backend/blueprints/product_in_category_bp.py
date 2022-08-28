from flask import Blueprint, request
from config import db
from utils.security_utils import admin_required
from schemas.product_in_category_schema import ProductInCategorySchema
from models.product_in_category import ProductInCategory
from models.product import Product

product_in_category = Blueprint('product_in_category', __name__)
schema = ProductInCategorySchema()

@product_in_category.route("/", methods=["GET"])
def get_all_products_in_category():
    products_in_category = ProductInCategory.query.all()
    return schema.jsonify(products_in_category, many=True)
   
@product_in_category.route("/<string:product_id>/<string:category_id>", methods=["GET"])
def get_product_in_category(product_id, category_id):
    product_in_category = ProductInCategory.query.filter_by(product_id=product_id, category_id=category_id).first()
    if not product_in_category:
        return "Product in category not found!", 404

    return schema.jsonify(product_in_category)

@product_in_category.route("/", methods=["POST"])
@admin_required()
def create_product_in_category():
    try:
        product_in_category = ProductInCategory(**request.json)
        db.session.add(product_in_category)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(product_in_category), 201

@product_in_category.route("/<string:product_id>/<string:category_id>", methods=["PATCH"])
@admin_required()
def update_product_in_category(product_id, category_id):
    product_in_category = ProductInCategory.query.filter_by(product_id=product_id, category_id=category_id).first()
    if not product_in_category:
        return "Product in category not found!", 404
    
    new_product_in_category = request.json
    new_product_in_category["product_id"] = product_id
    new_product_in_category["category_id"] = category_id
    try:
        ProductInCategory.query.filter_by(product_id=product_id, category_id=category_id).update(new_product_in_category)
        db.session.commit()
    except Exception as e:
        print(e)
        return "Bad request!", 400
    return schema.jsonify(product_in_category)

@product_in_category.route("/<string:product_id>/<string:category_id>", methods=["DELETE"])
@admin_required()
def delete_product_in_category(product_id, category_id):
    product_in_category = ProductInCategory.query.filter_by(product_id=product_id, category_id=category_id).first()
    if not product_in_category:
        return "Product in category not found!", 404

    db.session.delete(product_in_category)
    db.session.commit()
    return "", 204

@product_in_category.route("/<string:product_id>", methods=["DELETE"])
@admin_required()
def delete_product_categories(product_id):
    product = Product.query.filter_by(id=product_id).first()
    if not product:
        return "Product not found!", 404

    ProductInCategory.query.filter_by(product_id=product_id).delete()
    db.session.commit()
    return "", 204