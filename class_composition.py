#using composition


class Book:
    def __init__(self,title,price,author=None):
        self.title = title 
        self.price = price
        
        self.author = author
        

        self.chapters = []
        
    def addchapter(self,chapter):
        self.chapters.append(chapter)
        
    def getbookpagecount(self):
        result = 0
        for chapt in self.chapters:
            result += chapt.pagecount 
        return pagecount
        
class Author:
    def __init__(self, firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Chapter:
    def __init__(self,name,pagecount):
        self.name = name
        self.pagecount = pagecount
        
        
auth = Author("Van", "Leffredi")
b1 = Book("Machine Learning",26.99, auth)
print(auth)
print(b1)
b1.addchapter(Chapter("Chapter 1",24))
b1.addchapter(Chapter("Chapter 2",17))
b1.addchapter(Chapter("Chapter 3",67))

print(b1.author)
print(b1.title)
# print(b1.getbookpagecount())

    
        