
from book_class import book

def main():
    the_book = book("1994","George orwell",1949)

    #demotrating the __str__ method
    print(the_book) # expected to use __str__

    #demonstrating the __repr__ method
    print(repr(the_book))
    del the_book

if __name__ == "__main__":
    main()