class product:
    pass

class Goods:
    def __init__(self, prodCode, quantity):
        self.prodCode = prodCode
        self.quantity = quantity

class GoodsIn(Goods): 

    chargePerProduct = 5.00
    def __init__(self, prodCode, quantity):
        super().__init__(prodCode, quantity)

    def calcStorageCharge(self):
        self.storageCharge = self.quantity * self.chargePerProduct
        return self.storageCharge

class GoodsOut(Goods):
    def __init__(self, prodCode, quantity):
        super().__init__(prodCode, quantity)

