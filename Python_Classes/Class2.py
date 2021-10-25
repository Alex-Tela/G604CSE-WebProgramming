productList = []

class Product:
    def __init__(self, name='', description='', price=0.0):
        self.name = name
        self.description = description
        self.price = price

    def change_name(self, newName):
        if (newName.strip() != ''):
            self.name = newName

    def change_description(self, newDesc):
        if (newDesc.strip() != ''):
            self.description = newDesc

    def change_price(self, newPrice):
        if (newPrice > 0.0):
            self.price = newPrice

    def display(self):
        return f"Product name: {self.name} \nProduct Description: {self.description}\nProduct Price: {self.price}"


# In OOP we have two choices:
# - using inheritance
# - using composition (using a class in another class)
# To make the difference, we need to ask ourselves: Is ProductList a type of Product? NO, so we don't inherit. We use it inside 

class ProductList:
    def __init__(self, products=None):
        if products is None:
            self.products = []
        else:
            self.products = products

    def add_product(self, product):
        self.products.append(product)
    
    def delete_product(self, product_name):
        product_to_delete = None
        for product in self.products:
            if product.name == product_name:
                product_to_delete = product
                break
        self.products.remove(product_to_delete)

    def display_products(self):
        if (len(self.products) == 0):
            print('List is empty')
        for product in self.products:
            print(product.display())
    

if __name__ == '__main__':
    product1 = Product('Product 1', 'prd 1', 10)
    product2 = Product('Product 2', 'prd 2', 20)

    productList = ProductList()
    productList.add_product(product1)
    productList.add_product(product2)

    productList.display_products()