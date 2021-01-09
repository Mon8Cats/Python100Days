
class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookself with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(*[book, book2]) # or BookShelf(book, book2)
print(shelf)


'''
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnected(self):
        self.connected = False
        print("disconnnected")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("your printer is not connected!")
            return
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages


#printer = Device("Printer", "USB")
printer = Printer("Printer", "USB", 500)
printer.print(20)
print(printer)
printer.disconnected()
printer.print(100)



class ClassTest:
    def instance_method(self):
        print(f'called instance_method of {self}')

    @classmethod
    def class_method(cls):
        print(f"called class_method of {cls}")

    @staticmethod
    def static_method():
        print("called static_method")


myobj = ClassTest()
ClassTest.instance_method(myobj)
myobj.instance_method()
ClassTest.class_method()
ClassTest.static_method()



class Book:
    TYPES = ('hardcover', 'paperback')  # class properties

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod  # use as a factory method
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod  # use as a factory method
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


print(Book.TYPES)
book = Book("Harry Potter", "hardcover", 1500)
print(book)
book2 = Book.hardcover("Harry Potter", 1500)
print(book2)
book3 = Book.paperback("Harry Potter", 1500)
print(book3)
'''
