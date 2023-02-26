class Book:
    def __init__(self, price, title, author):
        super().__init__()
        self.price = price
        self.title = title
        self.author = author 
        self._discount = 0.5
    # ''' acessing attribute'''
    # similar to the __str__ which returns a user friendly format of a string, 
    # other magic methods exist that give  user access to some specific variable in 
    # specified format. 
    
    def __str__(self):
        return f"{self.title} by {self.author}, costs{self.price}"
        
    # TODO: __getattribute__
    # """This is called to retrieve an attribute """
    # def __getattribute__(self,name):
    #     if name == "price":
    #         p = super().__getattribute__("price")
    #         d = super().__getattribute__("_discount")
    #         return p -(p*d)
    #     return super().__getattribute__(name)
    
    
    def __setattr__(self, name,value):
        if name == "price":
            if type(value) is not float:
                
                raise ValueError("The price attribute must be a float")
        return super().__setattr__(name,value)
        
    #  __getattr__ : it handles exceptions when the __getattribute__ method is not valid     
    def __getattr__(self,name):
        return (name + "is not here!")
    
    
    
b1 = Book(23.99, "The plot","Lamido sanusi")
# b1.price = 39.80
# print(b1)       
b1.price = float(20)
print(b1)     

print(b1.propsdonotexist)

# print(b)  
    
    
    
    # TODO: __setattr_
    # def 