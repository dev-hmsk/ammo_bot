class Ammunition:
    def __init__(self, caliber, cpr, total_price, rounds, grains, retailer, href, timestamp=None):
        self.caliber = caliber
        self.cpr = cpr
        self.total_price = total_price
        self.rounds = rounds
        self.grains = grains
        self.retailer = retailer
        self.href = href
        self.timestamp = timestamp

    def __str__(self):
        return f"Caliber: {self.caliber}\nPrice: {self.cpr}\nTotal Price: {self.total_price}\nRounds: {self.rounds}\nGrains: {self.grains}\nRetailer: {self.retailer}\nHref: {self.href}\nTime Stamp: {self.timestamp}"
