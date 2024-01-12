class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Library Books:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Book Found - Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
                return
        print(f"Book with title '{title}' not found in the library.")

def main():
    my_library = Library()

    book1 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")
    book3 = Book("1984", "George Orwell", "978-0-452-28423-4")

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    my_library.display_books()

    search_title = input("Enter the title of the book to search: ")
    my_library.search_book(search_title)

if __name__ == "__main__":
    main()

