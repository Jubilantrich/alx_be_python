
from book_class import Book

def main():
    the_book = Book("1984","George Orwell",1949)

    #demotrating the __str__ method
    print(the_book) # expected to use __str__

    #demonstrating the __repr__ method
    print(repr(the_book))
    del the_book

if __name__ == "__main__":
    main()