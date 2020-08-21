#Goal (supplied by codecademy): You recently began employment at “A Sorted Tale”, an independent bookshop. Every morning, the owner decides to sort the books in a new way.


    #Some of his favorite methods include:
    #By author name
    #By title
    #By number of characters in the title
    #By the reverse of the author’s name

    #Throughout the day, patrons of the bookshop remove books from the shelf. Given the strange ordering of the store, they do not always get the books placed back in exactly the correct location.

    #The owner wants you to research methods of fixing the book ordering throughout the day and sorting the books in the morning. It is currently taking too long!

import utils, sorts

#saving the books_small.csv and books_large.csv files to respective variables
bookshelf_long = utils.load_books('/Users/tbohmert/Google Drive/developmentProjects/dev_courses/Codecademy/a_sorted_tale/books_large.csv')
bookshelf_short = utils.load_books('/Users/tbohmert/Google Drive/developmentProjects/dev_courses/Codecademy/a_sorted_tale/books_small.csv')


#comparison functions that will be used to decide how the books are sorted (author unicode, title unicode, or length of title & author)
def by_title_ascending(book_a, book_b):
     return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']


def by_total_length(book_a, book_b):
    return len(book_a['author']) + len(book_a['title']) > len(book_b['author']) + len(book_b['title'])


#test print of the titles at default
for book in bookshelf_short:
    print(book['title_lower'])


#using bubble sort on slightly unsorted books using title unicode with following test print
sort_1 = sorts.bubble_sort(bookshelf_short, by_title_ascending)

for book in sort_1:
    print(book['title_lower'], book['author_lower'])


#copy of the bookshelf to then use for future sorting to not mutate original
bookshelf_v1 = bookshelf_short.copy()

#using bubble sort on new sorting method by author unicode with following test print
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

for book in sort_2:
    print(book['author'])

#additional copy of the bookshelf to then use for future sorting to not mutate original
bookshelf_v2 = bookshelf_short.copy()



for book in bookshelf_v2:
    print(book['author'])

#using quicksort on new sorting method by author unicode with following test print
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

for book in bookshelf_v2:
    print(book['author'])


#using bubble sort & quicksort on new sorting method by title and author length - bubble sort much longer runtime vs quicksort
sorts.bubble_sort(bookshelf_long, by_total_length)
sorts.quicksort(bookshelf_long, 0, len(bookshelf_long) -1, by_total_length)