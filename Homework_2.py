class Book:
    book_id = 0
    
    def __init__(self, author, title, year):
        self.year = year
        self.title = title
        self.author = author
        Book.book_id += 0.5
        self.book_id = int(Book.book_id + 0.5)
    
    def __str__(self):
        return ("{}: Название книги - {}, год издания - {}, автор - {}".format(self.book_id, self.title, self.year, self.author))

class Library:
    def __init__(self):
        self.books = {}
    
    def printAll(self):
        output = []
        for item in self.books.values():
            output.append(f"{str(item[0])}")
        return str('\n'.join(map(str, output)))

    def add(self,book):
        book_id = book.book_id
        if book.title in self.books:
            self.books[book_id][1] += 1
        else:
            self.books[book_id] = [book, 1]
            
    def printAt(self, book_id):
        item = self.books.get(book_id)
        if item:
            return item[0]
        return None
    
    def removeAt(self, book_id):
        item = self.books.get(book_id)
        if item:
            item[1] -= 1
            if not item[1]:
                self.books.pop(book_id)
            return item[0]        

book1 = Book('Плохой К.', 'Вредные советы', 2000)
book2 = Book('Плохой К.', 'Вредные советы', 2000)
book3 = Book('Разводила В.', 'Как быстро заработать', 2008)
book4 = Book('Смелый Я.', 'Гаси разводил!', 2009)
book5 = Book('Разводила В.', 'Как быстро потерять деньги', 2010)
library = Library()    

library.add(book1)
library.add(book2)
library.add(book3)

print()
print(library.printAll())
print()
print(library.printAt(1))

library.add(book4)
library.add(book5)

print()
print(library.printAll())

library.removeAt(2)

print()
print(library.printAll())


    
