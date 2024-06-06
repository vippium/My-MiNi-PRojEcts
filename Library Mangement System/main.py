'''
Author: Vipin Prajapat 
Date:  16 September,2022
Purpose: Mini Python Project

'''



from win32com.client import Dispatch

class library:

    def __init__(self, list, name):

        self.book_list = list
        self.name = name
        self.lend_dict = {}

    def display_books(self):
        print(f"{self.name} library has: ")
        for books in self.book_list:
            print(books)

    def lend_book(self, user, book):

        if book not in self.lend_dict.keys():
            self.lend_dict.update({book: user})
            print('Database updated . you can now lend the book.')

        else:
            print(f"the book is already lend by {self.lend_dict[book]}.")

    def return_book(self, book):
        if book not in self.lend_dict.keys():
            print('Not Returnable. Check twice')
        else:
            self.lend_dict.pop(book)
            print('Book returned successfuly.\n')

    def add_book(self, book):
        self.book_list.append(book)
        print('Book added successfully.')


if __name__ == '__main__':
    print('\t\t **Welcome to Library** \t\t\n')

    obj = library([
        'Basics of Python', 'Let us C', 'C++', 'Compiler Design', 'Java', 'Web Designing'], "Vipin Prajapat's")

    while True:

        user = int(input(
            "What you want you do?\nPress 1 to display the books in the library.\nPress 2 to lend a book from library.\nPress 3 to return a book.(Return the book in given time to ignore late fine)\nPress 4 to add a book.\n"))

        if user is 1:

            obj.display_books()

        elif user is 2:
            user_name = input('Enter your name.\n')
            user_book = input('Enter the book name u want to lend.\n')
            obj.lend_book(user_name, user_book)

        elif user is 3:
            returning_book = input('Enter the book you want to return.\n')
            obj.return_book(returning_book)

        elif user is 4:
            adding_book = input('Enter the book you want to add.\n')
            obj.add_book(adding_book)

        else:
            print('Something gone wrong! Please check again.')

        user_input = int(
            input('Want something more?\nPress 1 to continue.\nPress 2 to exit.\n'))

        if user_input is 1:

            continue

        else:

            exit()
