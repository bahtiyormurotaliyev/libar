class VendingMachine:
    def __init__(self):
        self.beverages = {} 
        self.cards = {}  

    def addBeverage(self, beverage_name, price):
        self.beverages[beverage_name] = price

    def rechargeCard(self, card_id, credit):
        if card_id in self.cards:
            self.cards[card_id] += credit
        else:
            self.cards[card_id] = credit

    def getPrice(self, beverage_name):
        if beverage_name in self.beverages:
            return self.beverages[beverage_name]
        else:
            return -1.0

    def getCredit(self, card_id):
        if card_id in self.cards:
            return self.cards[card_id]
        else:
            return -1.0

    def sell(self, beverage_name, card_id):
        if beverage_name not in self.beverages or card_id not in self.cards:
            return -1.0
        elif self.beverages[beverage_name] > self.cards[card_id]:
            return -1.0
        else:
            self.cards[card_id] -= self.beverages[beverage_name]
            return self.beverages[beverage_name]
mashina = VendingMachine()
mashina.addBeverage('Coca Cola', 3200)
mashina.addBeverage('Suv', 1000)
mashina.addBeverage('Pepsi', 2500)

mashina.rechargeCard(12, 12000)
mashina.rechargeCard(21, 5600)
mashina.rechargeCard(99, 15800)

sotilgan_ustun_raqami = mashina.sell('Coca Cola', 12)
if sotilgan_ustun_raqami == -1.0:
    print("Ichimlik sotilmadi")
else:
    print("Ichimlik sotilgan ustun raqami:", sotilgan_ustun_raqami)

sotilgan_ustun_raqami = mashina.sell('Suv', 21)
if sotilgan_ustun_raqami == -1.0:
    print("Ichimlik sotilmadi")
else:
    print("Ichimlik sotilgan ustun raqami:", sotilgan_ustun_raqami)

sotilgan_ustun_raqami = mashina.sell('Non Existing', 99)
if sotilgan_ustun_raqami == -1.0:
    print("Ichimlik nomi yoki karta ID si noto'g'ri")
else:
    print("Ichimlik sotilgan ustun raqami:", sotilgan_ustun_raqami)

sotilgan_ustun_raqami = mashina.sell('Pepsi', 99)
if sotilgan_ustun_raqami == -1.0:
    print("Ichimlik sotilmadi")
else:
    print("Ichimlik sotilgan ustun raqami:", sotilgan_ustun_raqami)
