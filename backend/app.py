from config import app

from api.address import address
from api.cart import cart
from api.category import category
from api.comment import comment
from api.orders import orders
from api.payment_method import payment_method
from api.product_in_category import product_in_category
from api.product_in_order import product_in_order
from api.product import product
from api.shipping_method import shipping_method
from api.user import user

from api.auth import auth
from api.mail import mail_bp

app.register_blueprint(address, url_prefix="/api/address")
app.register_blueprint(cart, url_prefix="/api/cart")
app.register_blueprint(category, url_prefix="/api/category")
app.register_blueprint(comment, url_prefix="/api/comment")
app.register_blueprint(orders, url_prefix="/api/orders")
app.register_blueprint(payment_method, url_prefix="/api/payment-method")
app.register_blueprint(product_in_category, url_prefix="/api/product-in-category")
app.register_blueprint(product_in_order, url_prefix="/api/product-in-order")
app.register_blueprint(product, url_prefix="/api/product")
app.register_blueprint(shipping_method, url_prefix="/api/shipping-method")
app.register_blueprint(user, url_prefix="/api/user")
app.register_blueprint(auth, url_prefix="/api")
app.register_blueprint(mail_bp, url_prefix="/api/mail")

if __name__ == "__main__":
    app.run()