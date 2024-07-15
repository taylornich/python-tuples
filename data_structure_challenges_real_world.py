# question 2 task 1

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_to_library(title, author):
    new_book = (title, author)

    if new_book in library:
        print("Duplicate Book")
    else:
        library.append(new_book)

book = add_to_library("1984", "George Orwell")
print(library)
