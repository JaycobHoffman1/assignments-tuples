# Task 1: Library System Enhancement

library = [('1984', 'George Orwell'), ('Brave New World', 'Aldous Huxley')]

def check_input(user_input, input_type):
    while True:
        try:
            response = input(user_input)

            if len(response) == 0 or response.count(' ') == len(response):
                raise ValueError(f'{input_type} cannot be blank.')
        except ValueError as v:
            print(v)
        else:
            return response.strip()

def insert_new_books():
    enter_title = 'Enter the title of the book you wish to insert: '
    title = check_input(enter_title, 'Book title')
    enter_author = 'Enter the book\'s author: '
    author = check_input(enter_author, 'Author')

    try:
        duplicate = None

        for book in library:
            for attribute in book:
                if attribute.lower() == title.lower():
                    duplicate = attribute
                    break

        if duplicate:
            duplicate_title = title if title == duplicate else title.lower()

            raise ValueError(f'The system contains an existing copy of "{duplicate_title}".')
    except ValueError as v:
        print(v)
    else:
        library.append((title, author))

        print(f'"{title}" by {author} has been added to the system.')

        display_books()

def display_books():
    for i, book in enumerate(library):
        title, author = book

        print(f'{i + 1}. {title} - {author}')

insert_new_books()