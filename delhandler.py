import tornado.web
from product import Product
import json


class DelHandler(tornado.web.RequestHandler):
    def initialize(self, products):
        self.products = products
        
    def get(self):
        product_id = self.get_argument('product_id')
        result = self.products.del_product(product_id)
        if result:
            self.write("Deleted product product_id: {0} successfully".format(product_id))
            self.set_status(200)
        else:
            self.write("Product '{0}' not found".format(product_id))
            self.set_status(404)

