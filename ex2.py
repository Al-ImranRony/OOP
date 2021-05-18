
class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def display(self):
        print("Book title: ", self.title)
        print("International standard book number: ", self.isbn)
        print("The price is: ", self.price)
        print("Number of copies: ", self.copies)
        print('-' * 70)                       

    def in_stock(self):
        return True if self.copies > 0 else False

    def sell(self):
        if self.in_stock():
            self.copies -= 1
        else:
            print("The book is out of stock.")

    @property
    def price(self):
        return self._price

    def price(self, new_price):
        if 50 <= new_price <= 1000:
            self._price = new_price
        else:
            raise ValueError("Price can't be less than 20 or more than 800")


book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300, 5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200, 6)

books = [book1, book2, book3, book4]
for book in books:
    book.display()

jacksBooks = [book.title for book in books if book.author == 'Jack']
print(f'Books which author is Jack, are {jacksBooks}')