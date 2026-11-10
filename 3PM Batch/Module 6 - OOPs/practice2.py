class Book:

    def __init__(self, title, author, price, copies):
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies

    def display_book(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Available Copies:", self.copies)
        print("-----------------------------")

    def borrow_book(self):

        if self.copies > 0:
            self.copies -= 1
            print(self.title + " borrowed successfully.")

        else:
            print("Sorry no more copies available for the mentioned title")

    def return_book(self):

        self.copies += 1
        print(self.title + " book returned successfully.")

b1 = Book("Python Programming", "Guido van Rossum", 550, 3)
b2 = Book("Data Structures", "Narasimha Karumanchi", 650, 2)

b1.display_book()
b2.display_book()

b1.borrow_book()
b1.display_book()
