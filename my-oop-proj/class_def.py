#creating a basic  class 
class Book:
    #creating initializer function : it runs 
    # immediately after the class declaration 
    def __init__(self, author,title,pages,year,price):
        # defining instance attributes 
        self.author = author
        self.title = title
        self.pages= pages
        self.year = year
        self.price = price
        self.__secret = "This is a hidden attr"
        
    # TODO:To create instance method 
    def get_price(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price *self._discount)
        else:
            return self.price
        # pass

    def get_discount(self,amount):
        self._discount = amount
    
    
        
#creating  class instance or instance of a class
#NB: It has to be initialized  with the other variables different from sel
# f(self is automatically initialized)
B1 = Book("Abdoulaye Konate","Abdoulaye Konate Biography", 280,2021,56.90)
# B2 = Book("ayobola kekere ekun")
print(B1)
print(B1.author)
print("price is", B1.get_price())
print("discount is true", B1.get_discount(0.25))
print("new price is", B1.get_price())
# print(B1.self)
print(B1._Book__secret)