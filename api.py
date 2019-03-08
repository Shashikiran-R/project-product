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