import json

class Product:

    def __init__(self):
        self.products = []

    def add_product(self, product_id, product_name):
        new_product = {}
        new_product["Product_id"] = product_id
        new_product["Product_Name"] = product_name
        self.products.append(new_product)
        print("Product: {0}".format(new_product))
        return json.dumps(new_product)

    def del_product(self, product_id):
        found = False
        for idx, product in enumerate(self.products):
            if product["Product_id"] == product_id:
                index = idx
                found = True
                del self.products[idx]
        print("books: {0}".format(json.dumps(self.products)))
        return found

    def get_all_products(self):
        return self.products

    def json_list(self):
        return json.dumps(self.products)
