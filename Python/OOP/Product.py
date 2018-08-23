class Product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = 'sold'
        return self

    def addTax(self,tax):
        print (self.price + (self.price * tax))
        return self

    def returnItem(self, reason_for_return):
        if reason_for_return == 'defective':
            self.status = 'defective'
            self.price = 0.0
        elif reason_for_return == 'like new':
            self.status = 'for sale'
        elif reason_for_return == 'opened':
            self.status = 'used'
            self.price = self.price *.8
        return self
    
    def showAll(self):
        print(f'\nPrince: {self.price} \nItem Name: {self.item_name} \nWeight: {self.weight} \nBrand: {self.brand}\nStatus: {self.status}\n')
        return self

product1 = Product(50.00,'Hat','5lb','ADIDAS')

product1.showAll().sell().showAll().returnItem('opened').showAll()

