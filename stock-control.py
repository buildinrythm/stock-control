class product:
    pass

class Goods:
    def __init__(self, prodCode, quantity):
        self.prodCode = prodCode
        self.quantity = quantity

    def welcomeMessage(): 
        print("=" * 50)
        print("Welcome to the stock control system!")
        print("=" * 50)


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

    def getReg(self):
        self.getReg = input("What is your car's registration number?" "\n")

def main():
    # Welcome User
    Goods.welcomeMessage()
    choice = input("Enter 1 for (Goods in) Enter 2 for (Goods out)" '\n')

    # Get user choice
    if choice == 1:
        print("Goods in confirmed")
    else: 
        print("Goods out confirmed")
    




# Run the program
if __name__ == "__main__":
    main()