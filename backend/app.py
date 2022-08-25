from config import app

from blueprints.address_bp import address
from blueprints.cart_bp import cart
from blueprints.category_bp import category
from blueprints.order_bp import order
from blueprints.payment_method_bp import payment_method
from blueprints.product_in_category_bp import product_in_category
from blueprints.product_in_order_bp import product_in_order
from blueprints.product_bp import product
from blueprints.shipping_method_bp import shipping_method
from blueprints.user_bp import user
from blueprints.user_type_bp import user_type

from blueprints.auth_bp import auth
from blueprints.mail_bp import mail_bp

app.register_blueprint(address, url_prefix="/api/addresses")
app.register_blueprint(cart, url_prefix="/api/carts")
app.register_blueprint(category, url_prefix="/api/categories")
app.register_blueprint(order, url_prefix="/api/orders")
app.register_blueprint(payment_method, url_prefix="/api/payment-methods")
app.register_blueprint(product_in_category, url_prefix="/api/products-in-category")
app.register_blueprint(product_in_order, url_prefix="/api/products-in-order")
app.register_blueprint(product, url_prefix="/api/products")
app.register_blueprint(shipping_method, url_prefix="/api/shipping-methods")
app.register_blueprint(user, url_prefix="/api/users")
app.register_blueprint(user_type, url_prefix="/api/user-types")

app.register_blueprint(auth, url_prefix="/api")
app.register_blueprint(mail_bp, url_prefix="/api/mail")