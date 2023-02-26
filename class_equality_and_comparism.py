class Book:
    def __init__(self,title,author,price):
        super().__init__()
        self.title= title
        self.author = author
        self.price = price
        
#using __str__ to return a string
    def __str__(self):
        return f"{self.title}, by {self.author}, with cost {self.price}"


    #using  __repr__ to return an  obj representation and debugging
    def __repr__(self):
        return f"title = {self.title}, author= {self.author},price={self.price}"

    # using the eq function
    def __eq__(self,value):
        if not isinstance(value,Book):
            raise ValueError("Book cannot be compared to a non-book item")
        
        
        return (self.title== value.title and 
                self.author == value.author and
                self.price == value.price)
    
    # greater-than-equal-to  magic method
    def __ge__(self,value):
        if not isinstance(value,Book):
            raise ValueError("Book cannot be compared  to a non-book item")
        
        return self.price >= value.price
    
    # less-than magic method 
    def __lt__(self,value):
        if not isinstance(value, Book):
            raise valueError("Book cannot be compared to non-book item")  
        return self.price < value.price
    
    # less-than-equal-to  (le) magic method
    # greater-than (gt) magic method
    def __gt__(self,value):
        if not isinstance(value, Book):
            raise valueError("Book cannot be compared to non-book item")  
        return self.price > value.price
    
    
    
b1 = Book("Ralia the Sugar girl", "Toke Makinwa", 39.95)
b2 = Book("The Oracle","Lamido Sanmi", 29.90)
b3 = Book("The Oracle days","Lamido Sanmi",29.95)
b4 = Book("The Politician","Titilopemi Sanni", 23.50)

print("b1",b1)
print("b2", b2)
# print(str(b1))
# print(repr(b2))
# # print(b1==b4)
# # print(b2==b3)
# print(b2>=b1)
# print(b2<b1)

#To sort the book instances
books = [b1,b2,b3,b4]
books.sort()
print([book.title for book  in books])