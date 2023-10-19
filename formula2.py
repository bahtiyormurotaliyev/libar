class Driver:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name


class Championship:
    def __init__(self):
        self.drivers = []
        self.grand_prix = None
    
    def createDriver(self, name):
        driver = Driver(name)
        self.drivers.append(driver)
        return driver
    
    def getDrivers(self):
        return self.drivers
    
    def getDriver(self, name):
        for driver in self.drivers:
            if driver.getName() == name:
                return driver
    
    def defineGrandPrix(self, name):
        grand_prix = GrandPrix(name)
        return grand_prix
    
    def getGrandPrix(self, name):
        if self.grand_prix and self.grand_prix.getName() == name:
            return self.grand_prix


class GrandPrix:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name

championship = Championship()
driver1 = championship.createDriver("Abdushukr")
driver2 = championship.createDriver("Abduqodir")
driver3 = championship.createDriver("Abdushukr1")


grand_prix = championship.defineGrandPrix("Abdushukr")

# Grand Prix nomini olish
print(grand_prix.getName())


driver = championship.getDriver("Lewis Hamilton")
print(driver.getName())


grand_prix = championship.getGrandPrix("Monaco Grand Prix")
print(grand_prix.getName())
