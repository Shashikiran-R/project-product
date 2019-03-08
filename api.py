import tornado.ioloop
import tornado.web
from product import Product
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler

products = Product()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Products Microservice v1")

def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addproduct", AddHandler, dict(products = products)),
        (r"/v1/delproduct", DelHandler, dict(products = products)),
        (r"/v1/getproducts", GetHandler, dict(products = products)),
        ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    
    
    
    
#http://localhost:8888/v1    (to check whether my api is working)
#http://localhost:8888/v1/addproduct?product_id="1102"&product_name="xyz"  (adding a new product)
#http://localhost:8888/v1/addproduct?product_id="1101"&product_name="abc"
#http://localhost:8888/v1/getproducts  (displays all the products)
#http://localhost:8888/v1/delproduct?product_id="1101"  (deletes the product)
