class Product:
    pass

class Goods:
    def __init__(self, prodCode, quantity):
        self.prodCode = prodCode
        self.quantity = quantity

    @staticmethod
    def welcomeMessage(): 
        print("=" * 50)
        print("Welcome to the stock control system!")
        print("=" * 50)

    def getSummary(self):
        print(f"Product code:                 {self.prodCode}")
        print(f"quantity:                     {self.quantity}")


class GoodsIn(Goods): 

    chargePerProduct = 5.00
    def __init__(self, prodCode, quantity):
        super().__init__(prodCode, quantity)

    def calcStorageCharge(self):
        self.storageCharge = self.quantity * self.chargePerProduct
        return self.storageCharge

    def displayDetails(self):
        """Print Goods In details to screen"""
        print("\n=== GOODS IN TRANSACTION ===")
        print(f"Product Code: {self.prodCode}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Storage Charge: €{self.storageCharge:.2f}")
        print("============================\n")

class GoodsOut(Goods):
    def __init__(self, prodCode, quantity):
        super().__init__(prodCode, quantity)

    def getReg(self):
        self.vehicleReg = input("What is your car's registration number?" "\n")

    def displayDetails(self):
        """Print Goods Out details to screen"""
        print("\n=== GOODS OUT TRANSACTION ===")
        print(f"Product Code: {self.prodCode}")
        print(f"Quantity: {self.quantity}")
        print(f"Vehicle Registration: {self.vehicleReg}")
        print("=============================\n")


def main():
    # Welcome User
    Goods.welcomeMessage()
    choice = input("Enter 1 for (Goods in) Enter 2 for (Goods out)" '\n')

    # Get user choice
    if choice == "1":
        print("Goods in confirmed")
    else: 
        print("Goods out confirmed")

    #Get delivery info
    prodCode = input("Enter product code" "\n")
    quantity = int(input("Enter quantity" "\n"))
    
    # Choose to create goodsin object or not
    if choice == "1":
        product = GoodsIn(prodCode, quantity)
        product.calcStorageCharge()
    
    else:
        product = GoodsOut(prodCode, quantity)
        product.getReg()
    
    #Polymorph the display
    product.displayDetails()
    




# Run the program
if __name__ == "__main__":
    main()