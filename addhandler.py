import tornado.web
from product import Product
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self, products):
        self.products = products
        
    def get(self):
        product_id = self.get_argument('product_id')
        product_name = self.get_argument('product_name')
        result = self.products.add_product(product_id, product_name)
        self.write(result)