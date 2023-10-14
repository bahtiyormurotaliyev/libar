class SotuvMashinasi:
    def __init__(self):
        self.columns = [] 

    def refillColumn(self, column_number, drink_name, bank_count):
    
        self.columns.append((column_number, drink_name, bank_count))

    def availableCans(self, drink_name):
        
        count = 0
        for column in self.columns:
            if column[1] == drink_name:
                count += column[2]
        return count 
mashina = SotuvMashinasi()

mashina.refillColumn(1, 'Coca Cola', 1)
mashina.refillColumn(2, 'Suv', 10)
mashina.refillColumn(3, 'Pepsi', 15)
mashina.refillColumn(4, 'Suv', 20)

coca_cola_soni = mashina.availableCans('Coca Cola')
print("Coca Cola soni:", coca_cola_soni)

suv_soni = mashina.availableCans('Suv')
print("Suv soni:", suv_soni)

pepsi_soni = mashina.availableCans('Pepsi')
print("Pepsi soni:", pepsi_soni)
