class Book:
    BOOK_TYPES = ("HARDCOVER","PAPERBACK","EBOOK")
    
    #double underscore variables are hidden from other class 
    __booklist = None
    #create a class method decorator 
    
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES
    
    
    
    #how to create  a static method
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
            
      #creating an instance method 
    def resetTitle(self,newtitle):
        self.title = newtitle
        
        
    def __init__(self, title,booktype):
        self.title = title
        
        if (not booktype in Book.BOOK_TYPES):
            raiseValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype
        
#To access class attribute
print("Book types:", Book.getbooktypes())      
      
  
b1 = Book("Title1", "HARDCOVER")   
b2 = Book("Title2", "EBOOK")
# print(b1) 


#How to use  static method to access a singleton object 

thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)

b3 = Book("TITLE1", "PAPERBACK")
print("b3 instance ",b3)
print("resettitle", b3.resetTitle("Milk girl") )     
print(b3)
      
      

      
        
class Newspaper:
    def __init__(self, publisher):
        self.publisher = publisher

print(b1)
print(type(b1))

n1 = Newspaper("Forbes")
print(n1)

# to check  class variable instance  type
print(isinstance(b1, Book))
print(isinstance(n1,Newspaper))