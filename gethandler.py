import tornado.web
from product import Product
import json


class GetHandler(tornado.web.RequestHandler):
    def initialize(self, products):
        self.products = products
        
    def get(self):
        self.write(self.products.json_list())