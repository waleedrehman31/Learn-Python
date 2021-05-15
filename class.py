class Phone:
    def __init__(self, brand, price):  # constructor
        self.brand = brand
        self.price = price

    def call(self, phoneNumber):
        print(f"{self.brand} is calling {phoneNumber}")

    def __str__(self) -> str:
        return f"Brand {self.brand}  Price {self.price}"


iphone = Phone("Iphone 7+", 300)
samsung = Phone("samsung S20", 1400)

print(iphone.brand)
print(iphone.price)
iphone.call("911")

print(samsung.brand)
print(samsung.price)
samsung.call("912")

# below two print line give error if you not write __str__function in class
print(iphone)
print(samsung)
