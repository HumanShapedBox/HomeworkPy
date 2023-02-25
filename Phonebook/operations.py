def print_book():
    book = open('phonebook.txt', 'r')
    print(book.read())
    book.close()

def find(name):
    book = open('phonebook.txt', 'r')
    find_list = list()
    for line in book:
        if name in line.split():
            find_list.append(line)
    book.close()
    return find_list

def add(data):
    book = open('phonebook.txt', 'a')
    book.write(' '.join(data) + '\n')
    book.close()