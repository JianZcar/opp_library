class Library:
    def __init__(self, library_name, address):
        self.library_name = library_name
        self.address = address
        self.bookshelves = []

    def add_bookshelf(self, bookshelf):
        self.bookshelves.append(bookshelf)

    def get_bookshelves(self):
        return self.bookshelves

    def remove_bookshelves(self, shelf_num: int):
        for index, bookshelf in enumerate(self.get_bookshelves()):
            if bookshelf.shelf_number == shelf_num and len(bookshelf.books) == 0:
                print(f"Bookshelf {shelf_num} removed")
                self.bookshelves.pop(index)
            elif bookshelf.shelf_number == shelf_num and len(bookshelf.books) > 0:
                print("Bookshelf is not empty")

    def search_book(self, book_name: str) -> tuple:
        for bookshelf in self.get_bookshelves():
            for book in bookshelf.get_books():
                if book_name == book:
                    return book, bookshelf.shelf_number

        print("Book not found")

    def count_total_books(self) -> int:
        total = 0
        for bookshelf in self.get_bookshelves():
            total += len(bookshelf.get_books())
        return total

    def list_all_books(self) -> list:
        all_books = []
        for bookshelf in self.get_bookshelves():
            for book in bookshelf.get_books():
                all_books.append((book, bookshelf.shelf_number))
        return all_books

    def find_bookshelf(self, shelf_number: int):
        for bookshelf in self.get_bookshelves():
            if bookshelf.shelf_number == shelf_number:
                return bookshelf


class Bookshelf:
    def __init__(self, shelf_number, capacity):
        self.shelf_number = shelf_number
        self.capacity = capacity
        self.books = []

    def add_book(self, book):
        if len(self.books) < self.capacity:
            self.books.append(book)
            return True
        else:
            print("Bookshelf is Full")
            return False

    def get_books(self):
        return self.books

    def remove_book(self, book_name: str):
        for index, book in enumerate(self.get_books()):
            if book_name == book:
                print(f"Book {book} removed")
                self.books.pop(index)

    def check_availability(self, book_name: str):
        for book in self.get_books():
            if book == book_name:
                return True
        return False

    def list_all_books(self):
        all_books = []
        for book in self.get_books():
            all_books.append((book, self.shelf_number))
        return all_books

    def calculate_remaining_capacity(self):
        num_books = len(self.get_books())
        remaining_capacity = self.capacity - num_books
        print(f"Bookshelf {self.shelf_number} Remaining Capacity: {remaining_capacity}")
        return remaining_capacity

    def get_book_count(self):
        num_books = len(self.get_books())
        return num_books

    def sort_books(self):
        self.books.sort()


def display_books(library: Library):
    bookshelves = library.get_bookshelves()
    for bookshelf in bookshelves:
        print("\n")
        print(f"Bookshelf {bookshelf.shelf_number}")
        print(f"Capacity: {bookshelf.capacity}")
        print(f"Number of Books: {bookshelf.get_book_count()}")
        print(f"Remaining Capacity: {bookshelf.calculate_remaining_capacity()}")
        [print(f"{index + 1} {book}") for index, book in enumerate(bookshelf.get_books())]
        print("\n")


def add_list_books(books: list, bookshelf) -> None:
    [bookshelf.add_book(book) for book in books]


def access_bookshelf(shelf_num: int, library) -> Bookshelf:
    for bookshelf in library.get_bookshelves():
        if bookshelf.shelf_number == shelf_num:
            return bookshelf


def main():
    library = Library("Library", "123 Main St")
    bookshelves = [Bookshelf(1, 5), Bookshelf(2, 5), Bookshelf(3, 5)]
    books = {"Book1": 1,
             "Book2": 1,
             "Book3": 1,
             "Book4": 1,
             "Book5": 1,
             "Book6": 2,
             "Book7": 2,
             "Book8": 2,
             "Book9": 2,
             "Book10": 2,
             "Book11": 3,
             "Book12": 3,
             "Book13": 3,
             "Book14": 3,
             "Book15": 3}

    for bookshelf in bookshelves:
        library.add_bookshelf(bookshelf)
    for book_name, shelf_number in books.items():
        library.find_bookshelf(shelf_number).add_book(book_name)
    while True:
        selection = ["Remove Bookshelf",
                     "Remove Book",
                     "Search Book",
                     "Count Total Books",
                     "List All Books",
                     "Display Books"
                     "Exit"]
        [print(f"{index + 1} {option}") for index, option in enumerate(selection)]
        choice = int(input("-> "))
        match choice:
            case 1:
                shelf_num = int(input("Enter Bookshelf Number: "))
                library.remove_bookshelves(shelf_num)
            case 2:
                book_name = input("Enter Book Name: ")
                book_data = library.search_book(book_name)
                library.find_bookshelf(book_data[1]).remove_book(book_data[0])
            case 3:
                book_name = input("Enter Book Name: ")
                book_data = library.search_book(book_name)
                print(f"Book {book_data[0]} found in Bookshelf {book_data[1]}")
            case 4:
                print(f"Total Books: {library.count_total_books()}")
            case 5:
                print(library.list_all_books())
            case 6:
                display_books(library)
            case 7:
                exit()


if __name__ == "__main__":
    main()
    pass
