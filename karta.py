class VendingMachine:
    def __init__(self):
        self.cards = {}  # Karta ma'lumotlarini saqlash uchun bo'sh lug'at

    def rechargeCard(self, card_id, credit):
        if card_id in self.cards:
            self.cards[card_id] += credit
        else:
            self.cards[card_id] = credit

    def getCredit(self, card_id):
        if card_id in self.cards:
            return self.cards[card_id]
        else:
            return -1.0
