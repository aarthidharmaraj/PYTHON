class car:
    name="Sai"
    year="2021"
    price="100000"
    def __init__(self,name,year,price):
            self.name=name
            self.year=year
            self.price=price
    def names(self):
        print("Car owner:",self.name)
        return self.name
        #return self.name
    def years(self):
        print("Car bought year is:",self.year)
        return self.year
    def prices(self):
        print("Car bought price is:",self.price)
        return self.price
    def cal(self,advance,base_price):
        cal=advance+base_price
        print("Advance given",advance)
        print("Base price given is",base_price)
        print("Car price is:",cal)    