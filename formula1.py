class Driver:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class Championship:
    def __init__(self):
        self.drivers = []

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

championship = Championship()


driver1 = championship.createDriver("Abdushukr")
driver2 = championship.createDriver("Abduqodir")
driver3 = championship.createDriver("Abdushukr1")

# Barcha haydovchilarni olish
drivers = championship.getDrivers()
for driver in drivers:
    print(driver.getName())

# Haydovchini olish
driver = championship.getDriver("Abdushukr")
print(driver.getName())
