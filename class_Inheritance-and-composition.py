## Inheritance and composition 

class Publication:
    def __init__(self,title,price):
        self.title = title
        self.price = price
        
class Periodical(Publication):
    def __init__(self,title, price,period, publisher,year):
        super().__init__(title,price)
        self.period = period
        self.publisher = publisher
        self.year = year
        
        
    
        
class Book(Publication):
    def __init__( self,title, author,pages, price):
        super().__init__(title,price)
        self.author = author
        self.pages  = pages 
        
class Newspaper(Periodical):
    def __init__(self, publisher, title, year, price,period):
        super().__init__(title, price,period,publisher, year)
        
class Magazine(Periodical):
    def __init__(self, title, publisher,year, price, period):
       super().__init__(title,price,period,publisher,year)
        
m1 = Magazine("Noara","Nor","1990",30.99,"daily")
n1 = Newspaper("Nora","Regents",1990,30,"monthly")
b1 = Book("Sugar Girl","50","Chinua Achebe",450)

print(m1, n1, b1)
        