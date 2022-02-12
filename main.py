class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in the library are: ")
        for book in self.books:
            print(book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            self.books.remove(bookName)
            print(f"You have been assigned with the book \"{bookName}\". Please return it in 30 days. \n")
            return True
        else:
            print(f"Sorry. The book \"{bookName}\" has already been assigned to one of our user OR it is not available.\n")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print('Thanks for returning the book!!\n')


class Student:

    def requestBook(self):
        self.books = input("Enter the books you want to borrow: ")
        return self.books

    def returnBook(self):
        self.books = input("Enter the books you want to return: ")
        return self.books


if __name__ == "__main__":
    centralLibray = Library(["A", "B", "C"])
    student = Student()
    while(True):
        welcomeMsg = '''\nHello Sir
        please choose a option 
        1. list of all books
        2. Request a book
        3. Return a book
        4. Exit\n\n'''

        print(welcomeMsg)
        option = int(input("Enter your choice: "))
        if option == 1:
            centralLibray.displayAvailableBooks()
        elif option == 2:
            centralLibray.borrowBook(student.requestBook())
        elif option == 3:
            centralLibray.returnBook(student.returnBook())
        elif option == 4:
            print("Thank you using our library. Have a nice day!")
            exit()
        else:
            print("Invalid choice. Please try again !")
        
