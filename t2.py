class VendingMachine:
    def __init__(self):
        self.cards = {}  # Kartalar lug'ati

    def rechargeCard(self, card_id, credit):
        # Karta to'ldirish
        if card_id in self.cards:
            self.cards[card_id] += credit
        else:
            self.cards[card_id] = credit

    def getCredit(self, card_id):
        # Karta kreditini olish
        if card_id in self.cards:
            return self.cards[card_id]
        else:
            return -1.0
mashina = VendingMachine()

mashina.rechargeCard(12, 12000)
mashina.rechargeCard(21, 5600)
mashina.rechargeCard(99, 15800)

card_12_krediti = mashina.getCredit(12)
print("Karta ID 12 krediti:", card_12_krediti)

card_21_krediti = mashina.getCredit(21)
print("Karta ID 21 krediti:", card_21_krediti)

card_99_krediti = mashina.getCredit(99)
print("Karta ID 99 krediti:", card_99_krediti)

non_existing_krediti = mashina.getCredit(555)
print("Mavjud bo'lmagan karta krediti:", non_existing_krediti)
