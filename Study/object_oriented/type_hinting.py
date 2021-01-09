from typing import List



def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


print(list_avg([23, 33]))


class Book:
    TYPES = ('hardcover', 'paperback')  # class properties

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod  # use as a factory method
    # not Book because we are in Book class
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod  # use as a factory method
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)


book = Book.hardcover("Python 101", 200)
print(book)


#print('mymodulename: ', mymoduleName)
#print(divide(10, 2))
